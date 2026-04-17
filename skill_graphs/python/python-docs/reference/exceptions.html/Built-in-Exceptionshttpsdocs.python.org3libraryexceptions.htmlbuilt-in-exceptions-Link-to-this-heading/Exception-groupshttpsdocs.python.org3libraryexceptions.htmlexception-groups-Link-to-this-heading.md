## Exception groups[¶](https://docs.python.org/3/library/exceptions.html#exception-groups "Link to this heading")
The following are used when it is necessary to raise multiple unrelated exceptions. They are part of the exception hierarchy so they can be handled with [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) like all other exceptions. In addition, they are recognised by [`except*`](https://docs.python.org/3/reference/compound_stmts.html#except-star), which matches their subgroups based on the types of the contained exceptions.

_exception_ ExceptionGroup(_msg_ , _excs_)[¶](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "Link to this definition")


_exception_ BaseExceptionGroup(_msg_ , _excs_)[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup "Link to this definition")

Both of these exception types wrap the exceptions in the sequence `excs`. The `msg` parameter must be a string. The difference between the two classes is that `BaseExceptionGroup` extends [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") and it can wrap any exception, while [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup") extends [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") and it can only wrap subclasses of `Exception`. This design is so that `except Exception` catches an `ExceptionGroup` but not `BaseExceptionGroup`.
The `BaseExceptionGroup` constructor returns an [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup") rather than a `BaseExceptionGroup` if all contained exceptions are [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") instances, so it can be used to make the selection automatic. The `ExceptionGroup` constructor, on the other hand, raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if any contained exception is not an `Exception` subclass.

message[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.message "Link to this definition")

The `msg` argument to the constructor. This is a read-only attribute.

exceptions[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.exceptions "Link to this definition")

A tuple of the exceptions in the `excs` sequence given to the constructor. This is a read-only attribute.

subgroup(_condition_)[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.subgroup "Link to this definition")

Returns an exception group that contains only the exceptions from the current group that match _condition_ , or `None` if the result is empty.
The condition can be an exception type or tuple of exception types, in which case each exception is checked for a match using the same check that is used in an `except` clause. The condition can also be a callable (other than a type object) that accepts an exception as its single argument and returns true for the exceptions that should be in the subgroup.
The nesting structure of the current exception is preserved in the result, as are the values of its [`message`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.message "BaseExceptionGroup.message"), [`__traceback__`](https://docs.python.org/3/library/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__"), [`__cause__`](https://docs.python.org/3/library/exceptions.html#BaseException.__cause__ "BaseException.__cause__"), [`__context__`](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "BaseException.__context__") and [`__notes__`](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "BaseException.__notes__") fields. Empty nested groups are omitted from the result.
The condition is checked for all exceptions in the nested exception group, including the top-level and any nested exception groups. If the condition is true for such an exception group, it is included in the result in full.
Added in version 3.13: `condition` can be any callable which is not a type object.

split(_condition_)[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.split "Link to this definition")

Like [`subgroup()`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.subgroup "BaseExceptionGroup.subgroup"), but returns the pair `(match, rest)` where `match` is `subgroup(condition)` and `rest` is the remaining non-matching part.

derive(_excs_)[¶](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.derive "Link to this definition")

Returns an exception group with the same [`message`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.message "BaseExceptionGroup.message"), but which wraps the exceptions in `excs`.
This method is used by [`subgroup()`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.subgroup "BaseExceptionGroup.subgroup") and [`split()`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.split "BaseExceptionGroup.split"), which are used in various contexts to break up an exception group. A subclass needs to override it in order to make `subgroup()` and `split()` return instances of the subclass rather than [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup").
[`subgroup()`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.subgroup "BaseExceptionGroup.subgroup") and [`split()`](https://docs.python.org/3/library/exceptions.html#BaseExceptionGroup.split "BaseExceptionGroup.split") copy the [`__traceback__`](https://docs.python.org/3/library/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__"), [`__cause__`](https://docs.python.org/3/library/exceptions.html#BaseException.__cause__ "BaseException.__cause__"), [`__context__`](https://docs.python.org/3/library/exceptions.html#BaseException.__context__ "BaseException.__context__") and [`__notes__`](https://docs.python.org/3/library/exceptions.html#BaseException.__notes__ "BaseException.__notes__") fields from the original exception group to the one returned by `derive()`, so these fields do not need to be updated by `derive()`.
Copy```
>>> class MyGroup(ExceptionGroup):
...     def derive(self, excs):
...         return MyGroup(self.message, excs)
...
>>> e = MyGroup("eg", [ValueError(1), TypeError(2)])
>>> e.add_note("a note")
>>> e.__context__ = Exception("context")
>>> e.__cause__ = Exception("cause")
>>> try:
...    raise e
... except Exception as e:
...    exc = e
...
>>> match, rest = exc.split(ValueError)
>>> exc, exc.__context__, exc.__cause__, exc.__notes__
(MyGroup('eg', [ValueError(1), TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
>>> match, match.__context__, match.__cause__, match.__notes__
(MyGroup('eg', [ValueError(1)]), Exception('context'), Exception('cause'), ['a note'])
>>> rest, rest.__context__, rest.__cause__, rest.__notes__
(MyGroup('eg', [TypeError(2)]), Exception('context'), Exception('cause'), ['a note'])
>>> exc.__traceback__ is match.__traceback__ is rest.__traceback__
True

```

Note that `BaseExceptionGroup` defines [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__"), so subclasses that need a different constructor signature need to override that rather than [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__"). For example, the following defines an exception group subclass which accepts an exit_code and constructs the group’s message from it.
Copy```
class Errors(ExceptionGroup):
   def __new__(cls, errors, exit_code):
      self = super().__new__(Errors, f"exit code: {exit_code}", errors)
      self.exit_code = exit_code
      return self

   def derive(self, excs):
      return Errors(excs, self.exit_code)

```

Like [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup"), any subclass of `BaseExceptionGroup` which is also a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") can only wrap instances of `Exception`.
Added in version 3.11.
