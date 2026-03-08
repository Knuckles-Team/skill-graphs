Copy```
>>> mock = Mock(return_value=None)
>>> print(mock.call_args)
None
>>> mock()
>>> mock.call_args
call()
>>> mock.call_args == ()
True
>>> mock(3, 4)
>>> mock.call_args
call(3, 4)
>>> mock.call_args == ((3, 4),)
True
>>> mock.call_args.args
(3, 4)
>>> mock.call_args.kwargs
{}
>>> mock(3, 4, 5, key='fish', next='w00t!')
>>> mock.call_args
call(3, 4, 5, key='fish', next='w00t!')
>>> mock.call_args.args
(3, 4, 5)
>>> mock.call_args.kwargs
{'key': 'fish', 'next': 'w00t!'}

```

[`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args"), along with members of the lists [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list"), [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls") and [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call") objects. These are tuples, so they can be unpacked to get at the individual arguments and make more complex assertions. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples).
Changed in version 3.8: Added `args` and `kwargs` properties.

call_args_list[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "Link to this definition")

This is a list of all the calls made to the mock object in sequence (so the length of the list is the number of times it has been called). Before any calls have been made it is an empty list. The [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call") object can be used for conveniently constructing lists of calls to compare with [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list").
Copy```
>>> mock = Mock(return_value=None)
>>> mock()
>>> mock(3, 4)
>>> mock(key='fish', next='w00t!')
>>> mock.call_args_list
[call(), call(3, 4), call(key='fish', next='w00t!')]
>>> expected = [(), ((3, 4),), ({'key': 'fish', 'next': 'w00t!'},)]
>>> mock.call_args_list == expected
True

```

Members of [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list") are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call") objects. These can be unpacked as tuples to get at the individual arguments. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples).

method_calls[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "Link to this definition")

As well as tracking calls to themselves, mocks also track calls to methods and attributes, and _their_ methods and attributes:
Copy```
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.property.method.attribute()
<Mock name='mock.property.method.attribute()' id='...'>
>>> mock.method_calls
[call.method(), call.property.method.attribute()]

```

Members of [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls") are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call") objects. These can be unpacked as tuples to get at the individual arguments. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples).

mock_calls[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "Link to this definition")

[`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") records _all_ calls to the mock object, its methods, magic methods _and_ return value mocks.
Copy```
>>> mock = MagicMock()
>>> result = mock(1, 2, 3)
>>> mock.first(a=3)
<MagicMock name='mock.first()' id='...'>
>>> mock.second()
<MagicMock name='mock.second()' id='...'>
>>> int(mock)
1
>>> result(1)
<MagicMock name='mock()()' id='...'>
>>> expected = [call(1, 2, 3), call.first(a=3), call.second(),
... call.__int__(), call()(1)]
>>> mock.mock_calls == expected
True

```

Members of [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") are [`call`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "unittest.mock.call") objects. These can be unpacked as tuples to get at the individual arguments. See [calls as tuples](https://docs.python.org/3/library/unittest.mock.html#calls-as-tuples).
Note
The way [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") are recorded means that where nested calls are made, the parameters of ancestor calls are not recorded and so will always compare equal:
Copy```
>>> mock = MagicMock()
>>> mock.top(a=3).bottom()
<MagicMock name='mock.top().bottom()' id='...'>
>>> mock.mock_calls
[call.top(a=3), call.top().bottom()]
>>> mock.mock_calls[-1] == call.top(a=-1).bottom()
True

```


__class__[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.__class__ "Link to this definition")

Normally the `__class__` attribute of an object will return its type. For a mock object with a `spec`, `__class__` returns the spec class instead. This allows mock objects to pass [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") tests for the object they are replacing / masquerading as:
Copy```
>>> mock = Mock(spec=3)
>>> isinstance(mock, int)
True

```

`__class__` is assignable to, this allows a mock to pass an [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") check without forcing you to use a spec:
Copy```
>>> mock = Mock()
>>> mock.__class__ = dict
>>> isinstance(mock, dict)
True

```


_class_ unittest.mock.NonCallableMock(_spec =None_, _wraps =None_, _name =None_, _spec_set =None_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMock "Link to this definition")

A non-callable version of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock"). The constructor parameters have the same meaning of `Mock`, with the exception of _return_value_ and _side_effect_ which have no meaning on a non-callable mock.
Mock objects that use a class or an instance as a `spec` or `spec_set` are able to pass [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") tests:
Copy```
>>> mock = Mock(spec=SomeClass)
>>> isinstance(mock, SomeClass)
True
>>> mock = Mock(spec_set=SomeClass())
>>> isinstance(mock, SomeClass)
True

```

The [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") classes have support for mocking magic methods. See [magic methods](https://docs.python.org/3/library/unittest.mock.html#magic-methods) for the full details.
The mock classes and the [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") decorators all take arbitrary keyword arguments for configuration. For the `patch()` decorators the keywords are passed to the constructor of the mock being created. The keyword arguments are for configuring attributes of the mock:
Copy```
>>> m = MagicMock(attribute=3, other='fish')
>>> m.attribute
3
>>> m.other
'fish'

```

The return value and side effect of child mocks can be set in the same way, using dotted notation. As you can’t use dotted names directly in a call you have to create a dictionary and unpack it using `**`:
Copy```
>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock = Mock(some_attribute='eggs', **attrs)
>>> mock.some_attribute
'eggs'
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

```

A callable mock which was created with a _spec_ (or a _spec_set_) will introspect the specification object’s signature when matching calls to the mock. Therefore, it can match the actual call’s arguments regardless of whether they were passed positionally or by name:
Copy```
>>> def f(a, b, c): pass
...
>>> mock = Mock(spec=f)
>>> mock(1, 2, c=3)
<Mock name='mock()' id='140161580456576'>
>>> mock.assert_called_with(1, 2, 3)
>>> mock.assert_called_with(a=1, b=2, c=3)

```

This applies to [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with"), [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with"), [`assert_has_calls()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "unittest.mock.Mock.assert_has_calls") and [`assert_any_call()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_any_call "unittest.mock.Mock.assert_any_call"). When [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing), it will also apply to method calls on the mock object.
Changed in version 3.4: Added signature introspection on specced and autospecced mock objects.

_class_ unittest.mock.PropertyMock(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock "Link to this definition")

A mock intended to be used as a [`property`](https://docs.python.org/3/library/functions.html#property "property"), or other [descriptor](https://docs.python.org/3/glossary.html#term-descriptor), on a class. `PropertyMock` provides [`__get__()`](https://docs.python.org/3/reference/datamodel.html#object.__get__ "object.__get__") and [`__set__()`](https://docs.python.org/3/reference/datamodel.html#object.__set__ "object.__set__") methods so you can specify a return value when it is fetched.
Fetching a `PropertyMock` instance from an object calls the mock, with no args. Setting it calls the mock with the value being set.
Copy```
>>> class Foo:
...     @property
...     def foo(self):
...         return 'something'
...     @foo.setter
...     def foo(self, value):
...         pass
...
>>> with patch('__main__.Foo.foo', new_callable=PropertyMock) as mock_foo:
...     mock_foo.return_value = 'mockity-mock'
...     this_foo = Foo()
...     print(this_foo.foo)
...     this_foo.foo = 6
...
mockity-mock
>>> mock_foo.mock_calls
[call(), call(6)]

```

Because of the way mock attributes are stored you can’t directly attach a [`PropertyMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock "unittest.mock.PropertyMock") to a mock object. Instead you can attach it to the mock type object:
Copy```
>>> m = MagicMock()
>>> p = PropertyMock(return_value=3)
>>> type(m).foo = p
>>> m.foo
3
>>> p.assert_called_once_with()

```

Caution
If an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") is raised by [`PropertyMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock "unittest.mock.PropertyMock"), it will be interpreted as a missing descriptor and [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") will be called on the parent mock:
Copy```
>>> m = MagicMock()
>>> no_attribute = PropertyMock(side_effect=AttributeError)
>>> type(m).my_property = no_attribute
>>> m.my_property
<MagicMock name='mock.my_property' id='140165240345424'>

```

See [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") for details.

_class_ unittest.mock.AsyncMock(_spec =None_, _side_effect =None_, _return_value =DEFAULT_, _wraps =None_, _name =None_, _spec_set =None_, _unsafe =False_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "Link to this definition")

An asynchronous version of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock"). The `AsyncMock` object will behave so the object is recognized as an async function, and the result of a call is an awaitable.
Copy```
>>> mock = AsyncMock()
>>> inspect.iscoroutinefunction(mock)
True
>>> inspect.isawaitable(mock())
True

```

The result of `mock()` is an async function which will have the outcome of `side_effect` or `return_value` after it has been awaited:
  * if `side_effect` is a function, the async function will return the result of that function,
  * if `side_effect` is an exception, the async function will raise the exception,
  * if `side_effect` is an iterable, the async function will return the next value of the iterable, however, if the sequence of result is exhausted, `StopAsyncIteration` is raised immediately,
  * if `side_effect` is not defined, the async function will return the value defined by `return_value`, hence, by default, the async function returns a new `AsyncMock` object.


Setting the _spec_ of a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") or [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") to an async function will result in a coroutine object being returned after calling.
Copy```
>>> async def async_func(): pass
...
>>> mock = MagicMock(async_func)
>>> mock
<MagicMock spec='function' id='...'>
>>> mock()
<coroutine object AsyncMockMixin._mock_call at ...>

```

Setting the _spec_ of a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock"), [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock"), or `AsyncMock` to a class with asynchronous and synchronous functions will automatically detect the synchronous functions and set them as `MagicMock` (if the parent mock is `AsyncMock` or `MagicMock`) or `Mock` (if the parent mock is `Mock`). All asynchronous functions will be `AsyncMock`.
Copy```
>>> class ExampleClass:
...     def sync_foo():
...         pass
...     async def async_foo():
...         pass
...
>>> a_mock = AsyncMock(ExampleClass)
>>> a_mock.sync_foo
<MagicMock name='mock.sync_foo' id='...'>
>>> a_mock.async_foo
<AsyncMock name='mock.async_foo' id='...'>
>>> mock = Mock(ExampleClass)
>>> mock.sync_foo
<Mock name='mock.sync_foo' id='...'>
>>> mock.async_foo
<AsyncMock name='mock.async_foo' id='...'>

```

Added in version 3.8.

assert_awaited()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited "Link to this definition")

Assert that the mock was awaited at least once. Note that this is separate from the object having been called, the `await` keyword must be used:
Copy```
>>> mock = AsyncMock()
>>> async def main(coroutine_mock):
...     await coroutine_mock
...
>>> coroutine_mock = mock()
>>> mock.called
True
>>> mock.assert_awaited()
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited.
>>> asyncio.run(main(coroutine_mock))
>>> mock.assert_awaited()

```


assert_awaited_once()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited_once "Link to this definition")

Assert that the mock was awaited exactly once.
Copy```
>>> mock = AsyncMock()
>>> async def main():
...     await mock()
...
>>> asyncio.run(main())
>>> mock.assert_awaited_once()
>>> asyncio.run(main())
>>> mock.assert_awaited_once()
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited once. Awaited 2 times.

```


assert_awaited_with(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited_with "Link to this definition")

Assert that the last await was with the specified arguments.
Copy```
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> asyncio.run(main('foo', bar='bar'))
>>> mock.assert_awaited_with('foo', bar='bar')
>>> mock.assert_awaited_with('other')
Traceback (most recent call last):
...
AssertionError: expected await not found.
Expected: mock('other')
Actual: mock('foo', bar='bar')

```


assert_awaited_once_with(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_awaited_once_with "Link to this definition")

Assert that the mock was awaited exactly once and with the specified arguments.
Copy```
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> asyncio.run(main('foo', bar='bar'))
>>> mock.assert_awaited_once_with('foo', bar='bar')
>>> asyncio.run(main('foo', bar='bar'))
>>> mock.assert_awaited_once_with('foo', bar='bar')
Traceback (most recent call last):
...
AssertionError: Expected mock to have been awaited once. Awaited 2 times.

```


assert_any_await(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_any_await "Link to this definition")

Assert the mock has ever been awaited with the specified arguments.
Copy```
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> asyncio.run(main('foo', bar='bar'))
>>> asyncio.run(main('hello'))
>>> mock.assert_any_await('foo', bar='bar')
>>> mock.assert_any_await('other')
Traceback (most recent call last):
...
AssertionError: mock('other') await not found

```


assert_has_awaits(_calls_ , _any_order =False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_has_awaits "Link to this definition")

Assert the mock has been awaited with the specified calls. The [`await_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "unittest.mock.AsyncMock.await_args_list") list is checked for the awaits.
If _any_order_ is false then the awaits must be sequential. There can be extra calls before or after the specified awaits.
If _any_order_ is true then the awaits can be in any order, but they must all appear in [`await_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "unittest.mock.AsyncMock.await_args_list").
Copy```
>>> mock = AsyncMock()
>>> async def main(*args, **kwargs):
...     await mock(*args, **kwargs)
...
>>> calls = [call("foo"), call("bar")]
>>> mock.assert_has_awaits(calls)
Traceback (most recent call last):
...
AssertionError: Awaits not found.
Expected: [call('foo'), call('bar')]
Actual: []
>>> asyncio.run(main('foo'))
>>> asyncio.run(main('bar'))
>>> mock.assert_has_awaits(calls)

```


assert_not_awaited()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.assert_not_awaited "Link to this definition")

Assert that the mock was never awaited.
Copy```
>>> mock = AsyncMock()
>>> mock.assert_not_awaited()

```


reset_mock(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.reset_mock "Link to this definition")

See [`Mock.reset_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.reset_mock "unittest.mock.Mock.reset_mock"). Also sets [`await_count`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_count "unittest.mock.AsyncMock.await_count") to 0, [`await_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args "unittest.mock.AsyncMock.await_args") to None, and clears the [`await_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "unittest.mock.AsyncMock.await_args_list").

await_count[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_count "Link to this definition")

An integer keeping track of how many times the mock object has been awaited.
Copy```
>>> mock = AsyncMock()
>>> async def main():
...     await mock()
...
>>> asyncio.run(main())
>>> mock.await_count
1
>>> asyncio.run(main())
>>> mock.await_count
2

```


await_args[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args "Link to this definition")

This is either `None` (if the mock hasn’t been awaited), or the arguments that the mock was last awaited with. Functions the same as [`Mock.call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args").
Copy```
>>> mock = AsyncMock()
>>> async def main(*args):
...     await mock(*args)
...
>>> mock.await_args
>>> asyncio.run(main('foo'))
>>> mock.await_args
call('foo')
>>> asyncio.run(main('bar'))
>>> mock.await_args
call('bar')

```


await_args_list[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock.await_args_list "Link to this definition")

This is a list of all the awaits made to the mock object in sequence (so the length of the list is the number of times it has been awaited). Before any awaits have been made it is an empty list.
Copy```
>>> mock = AsyncMock()
>>> async def main(*args):
...     await mock(*args)
...
>>> mock.await_args_list
[]
>>> asyncio.run(main('foo'))
>>> mock.await_args_list
[call('foo')]
>>> asyncio.run(main('bar'))
>>> mock.await_args_list
[call('foo'), call('bar')]

```


_class_ unittest.mock.ThreadingMock(_spec =None_, _side_effect =None_, _return_value =DEFAULT_, _wraps =None_, _name =None_, _spec_set =None_, _unsafe =False_, _*_ , _timeout =UNSET_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock "Link to this definition")

A version of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") for multithreading tests. The `ThreadingMock` object provides extra methods to wait for a call to be invoked, rather than assert on it immediately.
The default timeout is specified by the `timeout` argument, or if unset by the [`ThreadingMock.DEFAULT_TIMEOUT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.DEFAULT_TIMEOUT "unittest.mock.ThreadingMock.DEFAULT_TIMEOUT") attribute, which defaults to blocking (`None`).
You can configure the global default timeout by setting [`ThreadingMock.DEFAULT_TIMEOUT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.DEFAULT_TIMEOUT "unittest.mock.ThreadingMock.DEFAULT_TIMEOUT").

wait_until_called(_*_ , _timeout =UNSET_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.wait_until_called "Link to this definition")

Waits until the mock is called.
If a timeout was passed at the creation of the mock or if a timeout argument is passed to this function, the function raises an [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") if the call is not performed in time.
Copy```
>>> mock = ThreadingMock()
>>> thread = threading.Thread(target=mock)
>>> thread.start()
>>> mock.wait_until_called(timeout=1)
>>> thread.join()

```


wait_until_any_call_with(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.wait_until_any_call_with "Link to this definition")

Waits until the mock is called with the specified arguments.
If a timeout was passed at the creation of the mock the function raises an [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") if the call is not performed in time.
Copy```
>>> mock = ThreadingMock()
>>> thread = threading.Thread(target=mock, args=("arg1", "arg2",), kwargs={"arg": "thing"})
>>> thread.start()
>>> mock.wait_until_any_call_with("arg1", "arg2", arg="thing")
>>> thread.join()

```


DEFAULT_TIMEOUT[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ThreadingMock.DEFAULT_TIMEOUT "Link to this definition")

Global default timeout in seconds to create instances of `ThreadingMock`.
Added in version 3.13.
### Calling[¶](https://docs.python.org/3/library/unittest.mock.html#calling "Link to this heading")
Mock objects are callable. The call will return the value set as the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") attribute. The default return value is a new Mock object; it is created the first time the return value is accessed (either explicitly or by calling the Mock) - but it is stored and the same one returned each time.
Calls made to the object will be recorded in the attributes like [`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args") and [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list").
If [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") is set then it will be called after the call has been recorded, so if `side_effect` raises an exception the call is still recorded.
