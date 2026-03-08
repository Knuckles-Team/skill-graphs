                    test=Compare(
                        left=Name(id='a', ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=5)]),
                    body=[
                        Break()],
                    orelse=[
                        Continue()])])])

```


_class_ ast.Try(_body_ , _handlers_ , _orelse_ , _finalbody_)[¶](https://docs.python.org/3/library/ast.html#ast.Try "Link to this definition")

`try` blocks. All attributes are list of nodes to execute, except for `handlers`, which is a list of [`ExceptHandler`](https://docs.python.org/3/library/ast.html#ast.ExceptHandler "ast.ExceptHandler") nodes.
Copy```
>>> print(ast.dump(ast.parse("""
... try:
...    ...
... except Exception:
...    ...
... except OtherException as e:
...    ...
... else:
...    ...
... finally:
...    ...
... """), indent=4))
Module(
    body=[
        Try(
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            handlers=[
                ExceptHandler(
                    type=Name(id='Exception', ctx=Load()),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                ExceptHandler(
                    type=Name(id='OtherException', ctx=Load()),
                    name='e',
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])],
            orelse=[
                Expr(
                    value=Constant(value=Ellipsis))],
            finalbody=[
                Expr(
                    value=Constant(value=Ellipsis))])])

```


_class_ ast.TryStar(_body_ , _handlers_ , _orelse_ , _finalbody_)[¶](https://docs.python.org/3/library/ast.html#ast.TryStar "Link to this definition")

`try` blocks which are followed by `except*` clauses. The attributes are the same as for [`Try`](https://docs.python.org/3/library/ast.html#ast.Try "ast.Try") but the [`ExceptHandler`](https://docs.python.org/3/library/ast.html#ast.ExceptHandler "ast.ExceptHandler") nodes in `handlers` are interpreted as `except*` blocks rather then `except`.
Copy```
>>> print(ast.dump(ast.parse("""
... try:
...    ...
... except* Exception:
...    ...
... """), indent=4))
Module(
    body=[
        TryStar(
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            handlers=[
                ExceptHandler(
                    type=Name(id='Exception', ctx=Load()),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.11.

_class_ ast.ExceptHandler(_type_ , _name_ , _body_)[¶](https://docs.python.org/3/library/ast.html#ast.ExceptHandler "Link to this definition")

A single `except` clause. `type` is the exception type it will match, typically a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") node (or `None` for a catch-all `except:` clause). `name` is a raw string for the name to hold the exception, or `None` if the clause doesn’t have `as foo`. `body` is a list of nodes.
Copy```
>>> print(ast.dump(ast.parse("""\
... try:
...     a + 1
... except TypeError:
...     pass
... """), indent=4))
Module(
    body=[
        Try(
            body=[
                Expr(
                    value=BinOp(
                        left=Name(id='a', ctx=Load()),
                        op=Add(),
                        right=Constant(value=1)))],
            handlers=[
                ExceptHandler(
                    type=Name(id='TypeError', ctx=Load()),
                    body=[
                        Pass()])])])

```


_class_ ast.With(_items_ , _body_ , _type_comment_)[¶](https://docs.python.org/3/library/ast.html#ast.With "Link to this definition")

A `with` block. `items` is a list of [`withitem`](https://docs.python.org/3/library/ast.html#ast.withitem "ast.withitem") nodes representing the context managers, and `body` is the indented block inside the context.

type_comment[¶](https://docs.python.org/3/library/ast.html#ast.With.type_comment "Link to this definition")

`type_comment` is an optional string with the type annotation as a comment.

_class_ ast.withitem(_context_expr_ , _optional_vars_)[¶](https://docs.python.org/3/library/ast.html#ast.withitem "Link to this definition")

A single context manager in a `with` block. `context_expr` is the context manager, often a [`Call`](https://docs.python.org/3/library/ast.html#ast.Call "ast.Call") node. `optional_vars` is a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"), [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple") or [`List`](https://docs.python.org/3/library/ast.html#ast.List "ast.List") for the `as foo` part, or `None` if that isn’t used.
Copy```
>>> print(ast.dump(ast.parse("""\
... with a as b, c as d:
...    something(b, d)
... """), indent=4))
Module(
    body=[
        With(
            items=[
                withitem(
                    context_expr=Name(id='a', ctx=Load()),
                    optional_vars=Name(id='b', ctx=Store())),
                withitem(
                    context_expr=Name(id='c', ctx=Load()),
                    optional_vars=Name(id='d', ctx=Store()))],
            body=[
                Expr(
                    value=Call(
                        func=Name(id='something', ctx=Load()),
                        args=[
                            Name(id='b', ctx=Load()),
                            Name(id='d', ctx=Load())]))])])

```

### Pattern matching[¶](https://docs.python.org/3/library/ast.html#pattern-matching "Link to this heading")

_class_ ast.Match(_subject_ , _cases_)[¶](https://docs.python.org/3/library/ast.html#ast.Match "Link to this definition")

A `match` statement. `subject` holds the subject of the match (the object that is being matched against the cases) and `cases` contains an iterable of [`match_case`](https://docs.python.org/3/library/ast.html#ast.match_case "ast.match_case") nodes with the different cases.
Added in version 3.10.

_class_ ast.match_case(_pattern_ , _guard_ , _body_)[¶](https://docs.python.org/3/library/ast.html#ast.match_case "Link to this definition")

A single case pattern in a `match` statement. `pattern` contains the match pattern that the subject will be matched against. Note that the [`AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST") nodes produced for patterns differ from those produced for expressions, even when they share the same syntax.
The `guard` attribute contains an expression that will be evaluated if the pattern matches the subject.
`body` contains a list of nodes to execute if the pattern matches and the result of evaluating the guard expression is true.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case [x] if x>0:
...         ...
...     case tuple():
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchSequence(
                        patterns=[
                            MatchAs(name='x')]),
                    guard=Compare(
                        left=Name(id='x', ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=0)]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchClass(
                        cls=Name(id='tuple', ctx=Load())),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchValue(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchValue "Link to this definition")

A match literal or value pattern that compares by equality. `value` is an expression node. Permitted value nodes are restricted as described in the match statement documentation. This pattern succeeds if the match subject is equal to the evaluated value.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case "Relevant":
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchValue(
                        value=Constant(value='Relevant')),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchSingleton(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchSingleton "Link to this definition")

A match literal pattern that compares by identity. `value` is the singleton to be compared against: `None`, `True`, or `False`. This pattern succeeds if the match subject is the given constant.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case None:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchSingleton(value=None),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchSequence(_patterns_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchSequence "Link to this definition")

A match sequence pattern. `patterns` contains the patterns to be matched against the subject elements if the subject is a sequence. Matches a variable length sequence if one of the subpatterns is a `MatchStar` node, otherwise matches a fixed length sequence.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case [1, 2]:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchSequence(
                        patterns=[
                            MatchValue(
                                value=Constant(value=1)),
                            MatchValue(
                                value=Constant(value=2))]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchStar(_name_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchStar "Link to this definition")

Matches the rest of the sequence in a variable length match sequence pattern. If `name` is not `None`, a list containing the remaining sequence elements is bound to that name if the overall sequence pattern is successful.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case [1, 2, *rest]:
...         ...
...     case [*_]:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchSequence(
                        patterns=[
                            MatchValue(
                                value=Constant(value=1)),
                            MatchValue(
                                value=Constant(value=2)),
                            MatchStar(name='rest')]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchSequence(
                        patterns=[
                            MatchStar()]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchMapping(_keys_ , _patterns_ , _rest_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchMapping "Link to this definition")

A match mapping pattern. `keys` is a sequence of expression nodes. `patterns` is a corresponding sequence of pattern nodes. `rest` is an optional name that can be specified to capture the remaining mapping elements. Permitted key expressions are restricted as described in the match statement documentation.
This pattern succeeds if the subject is a mapping, all evaluated key expressions are present in the mapping, and the value corresponding to each key matches the corresponding subpattern. If `rest` is not `None`, a dict containing the remaining mapping elements is bound to that name if the overall mapping pattern is successful.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case {1: _, 2: _}:
...         ...
...     case {**rest}:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchMapping(
                        keys=[
                            Constant(value=1),
                            Constant(value=2)],
                        patterns=[
                            MatchAs(),
                            MatchAs()]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchMapping(rest='rest'),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchClass(_cls_ , _patterns_ , _kwd_attrs_ , _kwd_patterns_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchClass "Link to this definition")

A match class pattern. `cls` is an expression giving the nominal class to be matched. `patterns` is a sequence of pattern nodes to be matched against the class defined sequence of pattern matching attributes. `kwd_attrs` is a sequence of additional attributes to be matched (specified as keyword arguments in the class pattern), `kwd_patterns` are the corresponding patterns (specified as keyword values in the class pattern).
This pattern succeeds if the subject is an instance of the nominated class, all positional patterns match the corresponding class-defined attributes, and any specified keyword attributes match their corresponding pattern.
Note: classes may define a property that returns self in order to match a pattern node against the instance being matched. Several builtin types are also matched that way, as described in the match statement documentation.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case Point2D(0, 0):
...         ...
...     case Point3D(x=0, y=0, z=0):
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchClass(
                        cls=Name(id='Point2D', ctx=Load()),
                        patterns=[
                            MatchValue(
                                value=Constant(value=0)),
                            MatchValue(
                                value=Constant(value=0))]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchClass(
                        cls=Name(id='Point3D', ctx=Load()),
                        kwd_attrs=[
                            'x',
                            'y',
                            'z'],
                        kwd_patterns=[
                            MatchValue(
                                value=Constant(value=0)),
                            MatchValue(
                                value=Constant(value=0)),
                            MatchValue(
                                value=Constant(value=0))]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchAs(_pattern_ , _name_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchAs "Link to this definition")

A match “as-pattern”, capture pattern or wildcard pattern. `pattern` contains the match pattern that the subject will be matched against. If the pattern is `None`, the node represents a capture pattern (i.e a bare name) and will always succeed.
The `name` attribute contains the name that will be bound if the pattern is successful. If `name` is `None`, `pattern` must also be `None` and the node represents the wildcard pattern.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case [x] as y:
...         ...
...     case _:
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchAs(
                        pattern=MatchSequence(
                            patterns=[
                                MatchAs(name='x')]),
                        name='y'),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))]),
                match_case(
                    pattern=MatchAs(),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.

_class_ ast.MatchOr(_patterns_)[¶](https://docs.python.org/3/library/ast.html#ast.MatchOr "Link to this definition")

A match “or-pattern”. An or-pattern matches each of its subpatterns in turn to the subject, until one succeeds. The or-pattern is then deemed to succeed. If none of the subpatterns succeed the or-pattern fails. The `patterns` attribute contains a list of match pattern nodes that will be matched against the subject.
Copy```
>>> print(ast.dump(ast.parse("""
... match x:
...     case [x] | (y):
...         ...
... """), indent=4))
Module(
    body=[
        Match(
            subject=Name(id='x', ctx=Load()),
            cases=[
                match_case(
                    pattern=MatchOr(
                        patterns=[
                            MatchSequence(
                                patterns=[
                                    MatchAs(name='x')]),
                            MatchAs(name='y')]),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```

Added in version 3.10.
### Type annotations[¶](https://docs.python.org/3/library/ast.html#type-annotations "Link to this heading")

_class_ ast.TypeIgnore(_lineno_ , _tag_)[¶](https://docs.python.org/3/library/ast.html#ast.TypeIgnore "Link to this definition")

A `# type: ignore` comment located at _lineno_. _tag_ is the optional tag specified by the form `# type: ignore <tag>`.
Copy```
>>> print(ast.dump(ast.parse('x = 1 # type: ignore', type_comments=True), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1))],
    type_ignores=[
        TypeIgnore(lineno=1, tag='')])
>>> print(ast.dump(ast.parse('x: bool = 1 # type: ignore[assignment]', type_comments=True), indent=4))
Module(
    body=[
        AnnAssign(
            target=Name(id='x', ctx=Store()),
            annotation=Name(id='bool', ctx=Load()),
            value=Constant(value=1),
            simple=1)],
    type_ignores=[
        TypeIgnore(lineno=1, tag='[assignment]')])

```

Note
`TypeIgnore` nodes are not generated when the _type_comments_ parameter is set to `False` (default). See [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") for more details.
Added in version 3.8.
### Type parameters[¶](https://docs.python.org/3/library/ast.html#type-parameters "Link to this heading")
[Type parameters](https://docs.python.org/3/reference/compound_stmts.html#type-params) can exist on classes, functions, and type aliases.

_class_ ast.TypeVar(_name_ , _bound_ , _default_value_)[¶](https://docs.python.org/3/library/ast.html#ast.TypeVar "Link to this definition")

A [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar"). `name` is the name of the type variable. `bound` is the bound or constraints, if any. If `bound` is a [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple"), it represents constraints; otherwise it represents the bound. `default_value` is the default value; if the `TypeVar` has no default, this attribute will be set to `None`.
Copy```
>>> print(ast.dump(ast.parse("type Alias[T: int = bool] = list[T]"), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            type_params=[
                TypeVar(
                    name='T',
                    bound=Name(id='int', ctx=Load()),
                    default_value=Name(id='bool', ctx=Load()))],
            value=Subscript(
                value=Name(id='list', ctx=Load()),
                slice=Name(id='T', ctx=Load()),
                ctx=Load()))])

```

Added in version 3.12.
Changed in version 3.13: Added the _default_value_ parameter.

_class_ ast.ParamSpec(_name_ , _default_value_)[¶](https://docs.python.org/3/library/ast.html#ast.ParamSpec "Link to this definition")

A [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"). `name` is the name of the parameter specification. `default_value` is the default value; if the `ParamSpec` has no default, this attribute will be set to `None`.
Copy```
>>> print(ast.dump(ast.parse("type Alias[**P = [int, str]] = Callable[P, int]"), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            type_params=[
                ParamSpec(
                    name='P',
                    default_value=List(
                        elts=[
                            Name(id='int', ctx=Load()),
                            Name(id='str', ctx=Load())],
                        ctx=Load()))],
            value=Subscript(
                value=Name(id='Callable', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Name(id='P', ctx=Load()),
                        Name(id='int', ctx=Load())],
                    ctx=Load()),
                ctx=Load()))])

```

Added in version 3.12.
Changed in version 3.13: Added the _default_value_ parameter.

_class_ ast.TypeVarTuple(_name_ , _default_value_)[¶](https://docs.python.org/3/library/ast.html#ast.TypeVarTuple "Link to this definition")

A [`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple"). `name` is the name of the type variable tuple. `default_value` is the default value; if the `TypeVarTuple` has no default, this attribute will be set to `None`.
Copy```
>>> print(ast.dump(ast.parse("type Alias[*Ts = ()] = tuple[*Ts]"), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            type_params=[
                TypeVarTuple(
                    name='Ts',
                    default_value=Tuple(ctx=Load()))],
            value=Subscript(
                value=Name(id='tuple', ctx=Load()),
                slice=Tuple(
                    elts=[
                        Starred(
                            value=Name(id='Ts', ctx=Load()),
                            ctx=Load())],
                    ctx=Load()),
                ctx=Load()))])

```

Added in version 3.12.
Changed in version 3.13: Added the _default_value_ parameter.
### Function and class definitions[¶](https://docs.python.org/3/library/ast.html#function-and-class-definitions "Link to this heading")

_class_ ast.FunctionDef(_name_ , _args_ , _body_ , _decorator_list_ , _returns_ , _type_comment_ , _type_params_)[¶](https://docs.python.org/3/library/ast.html#ast.FunctionDef "Link to this definition")

A function definition.
  * `name` is a raw string of the function name.
  * `args` is an [`arguments`](https://docs.python.org/3/library/ast.html#ast.arguments "ast.arguments") node.
  * `body` is the list of nodes inside the function.
  * `decorator_list` is the list of decorators to be applied, stored outermost first (i.e. the first in the list will be applied last).
  * `returns` is the return annotation.
  * `type_params` is a list of [type parameters](https://docs.python.org/3/library/ast.html#ast-type-params).



type_comment[¶](https://docs.python.org/3/library/ast.html#ast.FunctionDef.type_comment "Link to this definition")

`type_comment` is an optional string with the type annotation as a comment.
Changed in version 3.12: Added `type_params`.

_class_ ast.Lambda(_args_ , _body_)[¶](https://docs.python.org/3/library/ast.html#ast.Lambda "Link to this definition")

`lambda` is a minimal function definition that can be used inside an expression. Unlike [`FunctionDef`](https://docs.python.org/3/library/ast.html#ast.FunctionDef "ast.FunctionDef"), `body` holds a single node.
Copy```
>>> print(ast.dump(ast.parse('lambda x,y: ...'), indent=4))
