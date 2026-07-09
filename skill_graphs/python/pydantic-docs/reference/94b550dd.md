                    # depth 2 gets you above this __class_getitem__ call.
                    # Note that we explicitly provide the parent ns, otherwise
                    # `model_rebuild` will use the parent ns no matter if it is the ns of a module.
                    # We don't want this here, as this has unexpected effects when a model
                    # is being parametrized during a forward annotation evaluation.
                    parent_ns = _typing_extra.parent_frame_namespace(parent_depth=2) or {}
                    origin.model_rebuild(_types_namespace=parent_ns)
                except PydanticUndefinedAnnotation:
                    # It's okay if it fails, it just means there are still undefined types
                    # that could be evaluated later.
                    pass

                submodel = _generics.create_generic_submodel(model_name, origin, args, params)

                _generics.set_cached_generic_type(cls, typevar_values, submodel, origin, args)

        return submodel

    def __copy__(self) -> Self:
        """Returns a shallow copy of the model."""
        cls = type(self)
        m = cls.__new__(cls)
        _object_setattr(m, '__dict__', copy(self.__dict__))
        _object_setattr(m, '__pydantic_extra__', copy(self.__pydantic_extra__))
        _object_setattr(m, '__pydantic_fields_set__', copy(self.__pydantic_fields_set__))

        if not hasattr(self, '__pydantic_private__') or self.__pydantic_private__ is None:
            _object_setattr(m, '__pydantic_private__', None)
        else:
            _object_setattr(
                m,
                '__pydantic_private__',
                {k: v for k, v in self.__pydantic_private__.items() if v is not PydanticUndefined},
            )

        return m

    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Self:
        """Returns a deep copy of the model."""
        cls = type(self)
        m = cls.__new__(cls)
        _object_setattr(m, '__dict__', deepcopy(self.__dict__, memo=memo))
        _object_setattr(m, '__pydantic_extra__', deepcopy(self.__pydantic_extra__, memo=memo))
        # This next line doesn't need a deepcopy because __pydantic_fields_set__ is a set[str],
        # and attempting a deepcopy would be marginally slower.
        _object_setattr(m, '__pydantic_fields_set__', copy(self.__pydantic_fields_set__))

        if not hasattr(self, '__pydantic_private__') or self.__pydantic_private__ is None:
            _object_setattr(m, '__pydantic_private__', None)
        else:
            _object_setattr(
                m,
                '__pydantic_private__',
                deepcopy({k: v for k, v in self.__pydantic_private__.items() if v is not PydanticUndefined}, memo=memo),
            )

        return m

    if not TYPE_CHECKING:
        # We put `__getattr__` in a non-TYPE_CHECKING block because otherwise, mypy allows arbitrary attribute access
        # The same goes for __setattr__ and __delattr__, see: https://github.com/pydantic/pydantic/issues/8643

        def __getattr__(self, item: str) -> Any:
            private_attributes = object.__getattribute__(self, '__private_attributes__')
            if item in private_attributes:
                attribute = private_attributes[item]
                if hasattr(attribute, '__get__'):
                    return attribute.__get__(self, type(self))  # type: ignore

                try:
                    # Note: self.__pydantic_private__ cannot be None if self.__private_attributes__ has items
                    return self.__pydantic_private__[item]  # type: ignore
                except KeyError as exc:
                    raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}') from exc
            else:
                # `__pydantic_extra__` can fail to be set if the model is not yet fully initialized.
                # See `BaseModel.__repr_args__` for more details
                try:
                    pydantic_extra = object.__getattribute__(self, '__pydantic_extra__')
                except AttributeError:
                    pydantic_extra = None

                if pydantic_extra and item in pydantic_extra:
                    return pydantic_extra[item]
                else:
                    if hasattr(self.__class__, item):
                        return super().__getattribute__(item)  # Raises AttributeError if appropriate
                    else:
                        # this is the current error
                        raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}')

        def __setattr__(self, name: str, value: Any) -> None:
            if (setattr_handler := self.__pydantic_setattr_handlers__.get(name)) is not None:
                setattr_handler(self, name, value)
            # if None is returned from _setattr_handler, the attribute was set directly
            elif (setattr_handler := self._setattr_handler(name, value)) is not None:
                setattr_handler(self, name, value)  # call here to not memo on possibly unknown fields
                self.__pydantic_setattr_handlers__[name] = setattr_handler  # memoize the handler for faster access

        def _setattr_handler(self, name: str, value: Any) -> Callable[[BaseModel, str, Any], None] | None:
            """Get a handler for setting an attribute on the model instance.

            Returns:
                A handler for setting an attribute on the model instance. Used for memoization of the handler.
                Memoizing the handlers leads to a dramatic performance improvement in `__setattr__`
                Returns `None` when memoization is not safe, then the attribute is set directly.
            """
            cls = self.__class__
            if name in cls.__class_vars__:
                raise AttributeError(
                    f'{name!r} is a ClassVar of `{cls.__name__}` and cannot be set on an instance. '
                    f'If you want to set a value on the class, use `{cls.__name__}.{name} = value`.'
                )
            elif not _fields.is_valid_field_name(name):
                if (attribute := cls.__private_attributes__.get(name)) is not None:
                    if hasattr(attribute, '__set__'):
                        return lambda model, _name, val: attribute.__set__(model, val)
                    else:
                        return _SIMPLE_SETATTR_HANDLERS['private']
                else:
                    _object_setattr(self, name, value)
                    return None  # Can not return memoized handler with possibly freeform attr names

            attr = getattr(cls, name, None)
            # NOTE: We currently special case properties and `cached_property`, but we might need
            # to generalize this to all data/non-data descriptors at some point. For non-data descriptors
            # (such as `cached_property`), it isn't obvious though. `cached_property` caches the value
            # to the instance's `__dict__`, but other non-data descriptors might do things differently.
            if isinstance(attr, cached_property):
                return _SIMPLE_SETATTR_HANDLERS['cached_property']

            _check_frozen(cls, name, value)

            # We allow properties to be set only on non frozen models for now (to match dataclasses).
            # This can be changed if it ever gets requested.
            if isinstance(attr, property):
                return lambda model, _name, val: attr.__set__(model, val)
            elif cls.model_config.get('validate_assignment'):
                return _SIMPLE_SETATTR_HANDLERS['validate_assignment']
            elif name not in cls.__pydantic_fields__:
                if cls.model_config.get('extra') != 'allow':
                    # TODO - matching error
                    raise ValueError(f'"{cls.__name__}" object has no field "{name}"')
                elif attr is None:
                    # attribute does not exist, so put it in extra
                    self.__pydantic_extra__[name] = value
                    return None  # Can not return memoized handler with possibly freeform attr names
                else:
                    # attribute _does_ exist, and was not in extra, so update it
                    return _SIMPLE_SETATTR_HANDLERS['extra_known']
            else:
                return _SIMPLE_SETATTR_HANDLERS['model_field']

        def __delattr__(self, item: str) -> Any:
            cls = self.__class__

            if item in self.__private_attributes__:
                attribute = self.__private_attributes__[item]
                if hasattr(attribute, '__delete__'):
                    attribute.__delete__(self)  # type: ignore
                    return

                try:
                    # Note: self.__pydantic_private__ cannot be None if self.__private_attributes__ has items
                    del self.__pydantic_private__[item]  # type: ignore
                    return
                except KeyError as exc:
                    raise AttributeError(f'{cls.__name__!r} object has no attribute {item!r}') from exc

            # Allow cached properties to be deleted (even if the class is frozen):
            attr = getattr(cls, item, None)
            if isinstance(attr, cached_property):
                return object.__delattr__(self, item)

            _check_frozen(cls, name=item, value=None)

            if item in self.__pydantic_fields__:
                object.__delattr__(self, item)
            elif self.__pydantic_extra__ is not None and item in self.__pydantic_extra__:
                del self.__pydantic_extra__[item]
            else:
                try:
                    object.__delattr__(self, item)
                except AttributeError:
                    raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}')

        # Because we make use of `@dataclass_transform()`, `__replace__` is already synthesized by
        # type checkers, so we define the implementation in this `if not TYPE_CHECKING:` block:
        def __replace__(self, **changes: Any) -> Self:
            return self.model_copy(update=changes)

    def __getstate__(self) -> dict[Any, Any]:
        private = self.__pydantic_private__
        if private:
            private = {k: v for k, v in private.items() if v is not PydanticUndefined}
        return {
            '__dict__': self.__dict__,
            '__pydantic_extra__': self.__pydantic_extra__,
            '__pydantic_fields_set__': self.__pydantic_fields_set__,
            '__pydantic_private__': private,
        }

    def __setstate__(self, state: dict[Any, Any]) -> None:
        _object_setattr(self, '__pydantic_fields_set__', state.get('__pydantic_fields_set__', {}))
        _object_setattr(self, '__pydantic_extra__', state.get('__pydantic_extra__', {}))
        _object_setattr(self, '__pydantic_private__', state.get('__pydantic_private__', {}))
        _object_setattr(self, '__dict__', state.get('__dict__', {}))

    if not TYPE_CHECKING:

        def __eq__(self, other: Any) -> bool:
            if isinstance(other, BaseModel):
                # When comparing instances of generic types for equality, as long as all field values are equal,
                # only require their generic origin types to be equal, rather than exact type equality.
                # This prevents headaches like MyGeneric(x=1) != MyGeneric[Any](x=1).
                self_type = self.__pydantic_generic_metadata__['origin'] or self.__class__
                other_type = other.__pydantic_generic_metadata__['origin'] or other.__class__

                # Perform common checks first
                if not (
                    self_type == other_type
                    and getattr(self, '__pydantic_private__', None) == getattr(other, '__pydantic_private__', None)
                    and self.__pydantic_extra__ == other.__pydantic_extra__
                ):
                    return False

                # We only want to compare pydantic fields but ignoring fields is costly.
                # We'll perform a fast check first, and fallback only when needed
                # See GH-7444 and GH-7825 for rationale and a performance benchmark

                # First, do the fast (and sometimes faulty) __dict__ comparison
                if self.__dict__ == other.__dict__:
                    # If the check above passes, then pydantic fields are equal, we can return early
                    return True

                # We don't want to trigger unnecessary costly filtering of __dict__ on all unequal objects, so we return
                # early if there are no keys to ignore (we would just return False later on anyway)
                model_fields = type(self).__pydantic_fields__.keys()
                if self.__dict__.keys() <= model_fields and other.__dict__.keys() <= model_fields:
                    return False

                # If we reach here, there are non-pydantic-fields keys, mapped to unequal values, that we need to ignore
                # Resort to costly filtering of the __dict__ objects
                # We use operator.itemgetter because it is much faster than dict comprehensions
                # NOTE: Contrary to standard python class and instances, when the Model class has a default value for an
                # attribute and the model instance doesn't have a corresponding attribute, accessing the missing attribute
                # raises an error in BaseModel.__getattr__ instead of returning the class attribute
                # So we can use operator.itemgetter() instead of operator.attrgetter()
                getter = operator.itemgetter(*model_fields) if model_fields else lambda _: _utils._SENTINEL
                try:
                    return getter(self.__dict__) == getter(other.__dict__)
                except KeyError:
                    # In rare cases (such as when using the deprecated BaseModel.copy() method),
                    # the __dict__ may not contain all model fields, which is how we can get here.
                    # getter(self.__dict__) is much faster than any 'safe' method that accounts
                    # for missing keys, and wrapping it in a `try` doesn't slow things down much
                    # in the common case.
                    self_fields_proxy = _utils.SafeGetItemProxy(self.__dict__)
                    other_fields_proxy = _utils.SafeGetItemProxy(other.__dict__)
                    return getter(self_fields_proxy) == getter(other_fields_proxy)

            # other instance is not a BaseModel
            else:
                return NotImplemented  # delegate to the other item in the comparison

    if TYPE_CHECKING:
        # We put `__init_subclass__` in a TYPE_CHECKING block because, even though we want the type-checking benefits
        # described in the signature of `__init_subclass__` below, we don't want to modify the default behavior of
        # subclass initialization.

        def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
            """This signature is included purely to help type-checkers check arguments to class declaration, which
            provides a way to conveniently set model_config key/value pairs.

        ```python
            from pydantic import BaseModel

            class MyModel(BaseModel, extra='allow'): ...
        ```

            However, this may be deceiving, since the _actual_ calls to `__init_subclass__` will not receive any
            of the config arguments, and will only receive any keyword arguments passed during class initialization
            that are _not_ expected keys in ConfigDict. (This is due to the way `ModelMetaclass.__new__` works.)

            Args:
                **kwargs: Keyword arguments passed to the class definition, which set model_config

            Note:
                You may want to override `__pydantic_init_subclass__` instead, which behaves similarly but is called
                *after* the class is fully initialized.
            """

    def __iter__(self) -> TupleGenerator:
        """So `dict(model)` works."""
        yield from [(k, v) for (k, v) in self.__dict__.items() if not k.startswith('_')]
        extra = self.__pydantic_extra__
        if extra:
            yield from extra.items()

    def __repr__(self) -> str:
        return f'{self.__repr_name__()}({self.__repr_str__(", ")})'

    def __repr_args__(self) -> _repr.ReprArgs:
        # Eagerly create the repr of computed fields, as this may trigger access of cached properties and as such
        # modify the instance's `__dict__`. If we don't do it now, it could happen when iterating over the `__dict__`
        # below if the instance happens to be referenced in a field, and would modify the `__dict__` size *during* iteration.
        computed_fields_repr_args = [
            (k, getattr(self, k)) for k, v in self.__pydantic_computed_fields__.items() if v.repr
        ]

        for k, v in self.__dict__.items():
            field = self.__pydantic_fields__.get(k)
            if field and field.repr:
                if v is not self:
                    yield k, v
                else:
                    yield k, self.__repr_recursion__(v)
        # `__pydantic_extra__` can fail to be set if the model is not yet fully initialized.
        # This can happen if a `ValidationError` is raised during initialization and the instance's
        # repr is generated as part of the exception handling. Therefore, we use `getattr` here
        # with a fallback, even though the type hints indicate the attribute will always be present.
        try:
            pydantic_extra = object.__getattribute__(self, '__pydantic_extra__')
        except AttributeError:
            pydantic_extra = None

        if pydantic_extra is not None:
            yield from ((k, v) for k, v in pydantic_extra.items())
        yield from computed_fields_repr_args

    # take logic from `_repr.Representation` without the side effects of inheritance, see #5740
    __repr_name__ = _repr.Representation.__repr_name__
    __repr_recursion__ = _repr.Representation.__repr_recursion__
    __repr_str__ = _repr.Representation.__repr_str__
    __pretty__ = _repr.Representation.__pretty__
    __rich_repr__ = _repr.Representation.__rich_repr__

    def __str__(self) -> str:
        return self.__repr_str__(' ')

    # ##### Deprecated methods from v1 #####
    @property
    @typing_extensions.deprecated(
        'The `__fields__` attribute is deprecated, use the `model_fields` class property instead.', category=None
    )
    def __fields__(self) -> dict[str, FieldInfo]:
        warnings.warn(
            'The `__fields__` attribute is deprecated, use the `model_fields` class property instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return getattr(type(self), '__pydantic_fields__', {})

    @property
    @typing_extensions.deprecated(
        'The `__fields_set__` attribute is deprecated, use `model_fields_set` instead.',
        category=None,
    )
    def __fields_set__(self) -> set[str]:
        warnings.warn(
            'The `__fields_set__` attribute is deprecated, use `model_fields_set` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return self.__pydantic_fields_set__

    @typing_extensions.deprecated('The `dict` method is deprecated; use `model_dump` instead.', category=None)
    def dict(  # noqa: D102
        self,
        *,
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> Dict[str, Any]:  # noqa UP006
        warnings.warn(
            'The `dict` method is deprecated; use `model_dump` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return self.model_dump(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )

    @typing_extensions.deprecated('The `json` method is deprecated; use `model_dump_json` instead.', category=None)
    def json(  # noqa: D102
        self,
        *,
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        encoder: Callable[[Any], Any] | None = PydanticUndefined,  # type: ignore[assignment]
        models_as_dict: bool = PydanticUndefined,  # type: ignore[assignment]
        **dumps_kwargs: Any,
    ) -> str:
        warnings.warn(
            'The `json` method is deprecated; use `model_dump_json` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        if encoder is not PydanticUndefined:
            raise TypeError('The `encoder` argument is no longer supported; use field serializers instead.')
        if models_as_dict is not PydanticUndefined:
            raise TypeError('The `models_as_dict` argument is no longer supported; use a model serializer instead.')
        if dumps_kwargs:
            raise TypeError('`dumps_kwargs` keyword arguments are no longer supported.')
        return self.model_dump_json(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )

    @classmethod
    @typing_extensions.deprecated('The `parse_obj` method is deprecated; use `model_validate` instead.', category=None)
    def parse_obj(cls, obj: Any) -> Self:  # noqa: D102
        warnings.warn(
            'The `parse_obj` method is deprecated; use `model_validate` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        return cls.model_validate(obj)

    @classmethod
    @typing_extensions.deprecated(
        'The `parse_raw` method is deprecated; if your data is JSON use `model_validate_json`, '
        'otherwise load the data then use `model_validate` instead.',
        category=None,
    )
    def parse_raw(  # noqa: D102
        cls,
        b: str | bytes,
        *,
        content_type: str | None = None,
        encoding: str = 'utf8',
        proto: DeprecatedParseProtocol | None = None,
        allow_pickle: bool = False,
    ) -> Self:  # pragma: no cover
        warnings.warn(
            'The `parse_raw` method is deprecated; if your data is JSON use `model_validate_json`, '
            'otherwise load the data then use `model_validate` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import parse

        try:
            obj = parse.load_str_bytes(
                b,
                proto=proto,
                content_type=content_type,
                encoding=encoding,
                allow_pickle=allow_pickle,
            )
        except (ValueError, TypeError) as exc:
            import json

            # try to match V1
            if isinstance(exc, UnicodeDecodeError):
                type_str = 'value_error.unicodedecode'
            elif isinstance(exc, json.JSONDecodeError):
                type_str = 'value_error.jsondecode'
            elif isinstance(exc, ValueError):
                type_str = 'value_error'
            else:
                type_str = 'type_error'

            # ctx is missing here, but since we've added `input` to the error, we're not pretending it's the same
            error: pydantic_core.InitErrorDetails = {
                # The type: ignore on the next line is to ignore the requirement of LiteralString
                'type': pydantic_core.PydanticCustomError(type_str, str(exc)),  # type: ignore
                'loc': ('__root__',),
                'input': b,
            }
            raise pydantic_core.ValidationError.from_exception_data(cls.__name__, [error])
        return cls.model_validate(obj)

    @classmethod
    @typing_extensions.deprecated(
        'The `parse_file` method is deprecated; load the data from file, then if your data is JSON '
        'use `model_validate_json`, otherwise `model_validate` instead.',
        category=None,
    )
    def parse_file(  # noqa: D102
        cls,
        path: str | Path,
        *,
        content_type: str | None = None,
        encoding: str = 'utf8',
        proto: DeprecatedParseProtocol | None = None,
        allow_pickle: bool = False,
    ) -> Self:
        warnings.warn(
            'The `parse_file` method is deprecated; load the data from file, then if your data is JSON '
            'use `model_validate_json`, otherwise `model_validate` instead.',
            category=PydanticDeprecatedSince20,
            stacklevel=2,
        )
        from .deprecated import parse

        obj = parse.load_file(
            path,
            proto=proto,
            content_type=content_type,
            encoding=encoding,
            allow_pickle=allow_pickle,
        )
        return cls.parse_obj(obj)

    @classmethod
    @typing_extensions.deprecated(
        'The `from_orm` method is deprecated; set '
        "`model_config['from_attributes']=True` and use `model_validate` instead.",
        category=None,
    )
