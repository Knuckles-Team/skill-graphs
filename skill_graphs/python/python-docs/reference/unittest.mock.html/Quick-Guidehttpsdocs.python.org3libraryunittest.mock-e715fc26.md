## Quick Guide[¶](https://docs.python.org/3/library/unittest.mock.html#quick-guide "Link to this heading")
[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") and [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") objects create all attributes and methods as you access them and store details of how they have been used. You can configure them, to specify return values or limit what attributes are available, and then make assertions about how they have been used:
Copy```
>>> from unittest.mock import MagicMock
>>> thing = ProductionClass()
>>> thing.method = MagicMock(return_value=3)
>>> thing.method(3, 4, 5, key='value')
3
>>> thing.method.assert_called_with(3, 4, 5, key='value')

```

[`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") allows you to perform side effects, including raising an exception when a mock is called:
Copy```
>>> from unittest.mock import Mock
>>> mock = Mock(side_effect=KeyError('foo'))
>>> mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'

```

Copy```
>>> values = {'a': 1, 'b': 2, 'c': 3}
>>> def side_effect(arg):
...     return values[arg]
...
>>> mock.side_effect = side_effect
>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)
>>> mock.side_effect = [5, 4, 3, 2, 1]
>>> mock(), mock(), mock()
(5, 4, 3)

```

Mock has many other ways you can configure it and control its behaviour. For example the _spec_ argument configures the mock to take its specification from another object. Attempting to access attributes or methods on the mock that don’t exist on the spec will fail with an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
The [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") decorator / context manager makes it easy to mock classes or objects in a module under test. The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends:
Copy```
>>> from unittest.mock import patch
>>> @patch('module.ClassName2')
... @patch('module.ClassName1')
... def test(MockClass1, MockClass2):
...     module.ClassName1()
...     module.ClassName2()
...     assert MockClass1 is module.ClassName1
...     assert MockClass2 is module.ClassName2
...     assert MockClass1.called
...     assert MockClass2.called
...
>>> test()

```

Note
When you nest patch decorators the mocks are passed in to the decorated function in the same order they applied (the normal _Python_ order that decorators are applied). This means from the bottom up, so in the example above the mock for `module.ClassName1` is passed in first.
With [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") it matters that you patch objects in the namespace where they are looked up. This is normally straightforward, but for a quick guide read [where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch).
As well as a decorator [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") can be used as a context manager in a with statement:
Copy```
>>> with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
...     thing = ProductionClass()
...     thing.method(1, 2, 3)
...
>>> mock_method.assert_called_once_with(1, 2, 3)

```

There is also [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") for setting values in a dictionary just during a scope and restoring the dictionary to its original state when the test ends:
Copy```
>>> foo = {'key': 'value'}
>>> original = foo.copy()
>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
...     assert foo == {'newkey': 'newvalue'}
...
>>> assert foo == original

```

Mock supports the mocking of Python [magic methods](https://docs.python.org/3/library/unittest.mock.html#magic-methods). The easiest way of using magic methods is with the [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") class. It allows you to do things like:
Copy```
>>> mock = MagicMock()
>>> mock.__str__.return_value = 'foobarbaz'
>>> str(mock)
'foobarbaz'
>>> mock.__str__.assert_called_with()

```

Mock allows you to assign functions (or other Mock instances) to magic methods and they will be called appropriately. The [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") class is just a Mock variant that has all of the magic methods pre-created for you (well, all the useful ones anyway).
The following is an example of using magic methods with the ordinary Mock class:
Copy```
>>> mock = Mock()
>>> mock.__str__ = Mock(return_value='wheeeeee')
>>> str(mock)
'wheeeeee'

```

For ensuring that the mock objects in your tests have the same api as the objects they are replacing, you can use [auto-speccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing). Auto-speccing can be done through the _autospec_ argument to patch, or the [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") function. Auto-speccing creates mock objects that have the same attributes and methods as the objects they are replacing, and any functions and methods (including constructors) have the same call signature as the real object.
This ensures that your mocks will fail in the same way as your production code if they are used incorrectly:
Copy```
>>> from unittest.mock import create_autospec
>>> def function(a, b, c):
...     pass
...
>>> mock_function = create_autospec(function, return_value='fishy')
>>> mock_function(1, 2, 3)
'fishy'
>>> mock_function.assert_called_once_with(1, 2, 3)
>>> mock_function('wrong arguments')
Traceback (most recent call last):
 ...
TypeError: missing a required argument: 'b'

```

[`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") can also be used on classes, where it copies the signature of the `__init__` method, and on callable objects where it copies the signature of the `__call__` method.
## The Mock Class[¶](https://docs.python.org/3/library/unittest.mock.html#the-mock-class "Link to this heading")
[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") is a flexible mock object intended to replace the use of stubs and test doubles throughout your code. Mocks are callable and create attributes as new mocks when you access them [[1]](https://docs.python.org/3/library/unittest.mock.html#id3). Accessing the same attribute will always return the same mock. Mocks record how you use them, allowing you to make assertions about what your code has done to them.
[`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") is a subclass of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") with all the magic methods pre-created and ready to use. There are also non-callable variants, useful when you are mocking out objects that aren’t callable: [`NonCallableMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMock "unittest.mock.NonCallableMock") and [`NonCallableMagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMagicMock "unittest.mock.NonCallableMagicMock")
The [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") decorators makes it easy to temporarily replace classes in a particular module with a [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") object. By default `patch()` will create a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") for you. You can specify an alternative class of `Mock` using the _new_callable_ argument to `patch()`.

_class_ unittest.mock.Mock(_spec =None_, _side_effect =None_, _return_value =DEFAULT_, _wraps =None_, _name =None_, _spec_set =None_, _unsafe =False_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "Link to this definition")

Create a new `Mock` object. `Mock` takes several optional arguments that specify the behaviour of the Mock object:
  * _spec_ : This can be either a list of strings or an existing object (a class or instance) that acts as the specification for the mock object. If you pass in an object then a list of strings is formed by calling dir on the object (excluding unsupported magic attributes and methods). Accessing any attribute not in this list will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
If _spec_ is an object (rather than a list of strings) then [`__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__") returns the class of the spec object. This allows mocks to pass [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") tests.
  * _spec_set_ : A stricter variant of _spec_. If used, attempting to _set_ or get an attribute on the mock that isn’t on the object passed as _spec_set_ will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
  * _side_effect_ : A function to be called whenever the Mock is called. See the [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") attribute. Useful for raising exceptions or dynamically changing return values. The function is called with the same arguments as the mock, and unless it returns [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT"), the return value of this function is used as the return value.
Alternatively _side_effect_ can be an exception class or instance. In this case the exception will be raised when the mock is called.
If _side_effect_ is an iterable then each call to the mock will return the next value from the iterable.
A _side_effect_ can be cleared by setting it to `None`.
  * _return_value_ : The value returned when the mock is called. By default this is a new Mock (created on first access). See the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") attribute.
  * _unsafe_ : By default, accessing any attribute whose name starts with _assert_ , _assret_ , _asert_ , _aseert_ or _assrt_ will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError"). Passing `unsafe=True` will allow access to these attributes.
Added in version 3.5.
  * _wraps_ : Item for the mock object to wrap. If _wraps_ is not `None` then calling the Mock will pass the call through to the wrapped object (returning the real result). Attribute access on the mock will return a Mock object that wraps the corresponding attribute of the wrapped object (so attempting to access an attribute that doesn’t exist will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError")).
If the mock has an explicit _return_value_ set then calls are not passed to the wrapped object and the _return_value_ is returned instead.
  * _name_ : If the mock has a name then it will be used in the repr of the mock. This can be useful for debugging. The name is propagated to child mocks.


Mocks can also be called with arbitrary keyword arguments. These will be used to set attributes on the mock after it is created. See the [`configure_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "unittest.mock.Mock.configure_mock") method for details.

assert_called()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called "Link to this definition")

Assert that the mock was called at least once.
Copy```
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called()

```

Added in version 3.6.

assert_called_once()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once "Link to this definition")

Assert that the mock was called exactly once.
Copy```
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_once()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_once()
Traceback (most recent call last):
...
AssertionError: Expected 'method' to have been called once. Called 2 times.
Calls: [call(), call()].

```

Added in version 3.6.

assert_called_with(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "Link to this definition")

This method is a convenient way of asserting that the last call has been made in a particular way:
Copy```
>>> mock = Mock()
>>> mock.method(1, 2, 3, test='wow')
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_with(1, 2, 3, test='wow')

```


assert_called_once_with(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "Link to this definition")

Assert that the mock was called exactly once and that call was with the specified arguments.
Copy```
>>> mock = Mock(return_value=None)
>>> mock('foo', bar='baz')
>>> mock.assert_called_once_with('foo', bar='baz')
>>> mock('other', bar='values')
>>> mock.assert_called_once_with('other', bar='values')
Traceback (most recent call last):
  ...
AssertionError: Expected 'mock' to be called once. Called 2 times.
Calls: [call('foo', bar='baz'), call('other', bar='values')].

```


assert_any_call(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_any_call "Link to this definition")

assert the mock has been called with the specified arguments.
The assert passes if the mock has _ever_ been called, unlike [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with") and [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with") that only pass if the call is the most recent one, and in the case of `assert_called_once_with()` it must also be the only call.
Copy```
>>> mock = Mock(return_value=None)
>>> mock(1, 2, arg='thing')
>>> mock('some', 'thing', 'else')
>>> mock.assert_any_call(1, 2, arg='thing')

```


assert_has_calls(_calls_ , _any_order =False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "Link to this definition")

assert the mock has been called with the specified calls. The [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") list is checked for the calls.
If _any_order_ is false then the calls must be sequential. There can be extra calls before or after the specified calls.
If _any_order_ is true then the calls can be in any order, but they must all appear in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls").
Copy```
>>> mock = Mock(return_value=None)
>>> mock(1)
>>> mock(2)
>>> mock(3)
>>> mock(4)
>>> calls = [call(2), call(3)]
>>> mock.assert_has_calls(calls)
>>> calls = [call(4), call(2), call(3)]
>>> mock.assert_has_calls(calls, any_order=True)

```


assert_not_called()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_not_called "Link to this definition")

Assert the mock was never called.
Copy```
>>> m = Mock()
>>> m.hello.assert_not_called()
>>> obj = m.hello()
>>> m.hello.assert_not_called()
Traceback (most recent call last):
  ...
AssertionError: Expected 'hello' to not have been called. Called 1 times.
Calls: [call()].

```

Added in version 3.5.

reset_mock(_*_ , _return_value =False_, _side_effect =False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.reset_mock "Link to this definition")

The reset_mock method resets all the call attributes on a mock object:
Copy```
>>> mock = Mock(return_value=None)
>>> mock('hello')
>>> mock.called
True
>>> mock.reset_mock()
>>> mock.called
False

```

This can be useful where you want to make a series of assertions that reuse the same object.
_return_value_ parameter when set to `True` resets [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value"):
Copy```
>>> mock = Mock(return_value=5)
>>> mock('hello')
5
>>> mock.reset_mock(return_value=True)
>>> mock('hello')
<Mock name='mock()' id='...'>

```

_side_effect_ parameter when set to `True` resets [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect"):
Copy```
>>> mock = Mock(side_effect=ValueError)
>>> mock('hello')
Traceback (most recent call last):
  ...
ValueError
>>> mock.reset_mock(side_effect=True)
>>> mock('hello')
<Mock name='mock()' id='...'>

```

Note that `reset_mock()` _doesn’t_ clear the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value"), [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") or any child attributes you have set using normal assignment by default.
Child mocks are reset as well.
Changed in version 3.6: Added two keyword-only arguments to the reset_mock function.

mock_add_spec(_spec_ , _spec_set =False_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_add_spec "Link to this definition")

Add a spec to a mock. _spec_ can either be an object or a list of strings. Only attributes on the _spec_ can be fetched as attributes from the mock.
If _spec_set_ is true then only attributes on the spec can be set.

attach_mock(_mock_ , _attribute_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.attach_mock "Link to this definition")

Attach a mock as an attribute of this one, replacing its name and parent. Calls to the attached mock will be recorded in the [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls") and [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") attributes of this one.

configure_mock(_** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "Link to this definition")

Set attributes on the mock through keyword arguments.
Attributes plus return values and side effects can be set on child mocks using standard dot notation and unpacking a dictionary in the method call:
Copy```
>>> mock = Mock()
>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock.configure_mock(**attrs)
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

```

The same thing can be achieved in the constructor call to mocks:
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

`configure_mock()` exists to make it easier to do configuration after the mock has been created.

__dir__()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.__dir__ "Link to this definition")

`Mock` objects limit the results of `dir(some_mock)` to useful results. For mocks with a _spec_ this includes all the permitted attributes for the mock.
See [`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR") for what this filtering does, and how to switch it off.

_get_child_mock(_** kw_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock._get_child_mock "Link to this definition")

Create the child mocks for attributes and return value. By default child mocks will be the same type as the parent. Subclasses of Mock may want to override this to customize the way child mocks are made.
For non-callable mocks the callable variant will be used (rather than any custom subclass).

called[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.called "Link to this definition")

A boolean representing whether or not the mock object has been called:
Copy```
>>> mock = Mock(return_value=None)
>>> mock.called
False
>>> mock()
>>> mock.called
True

```


call_count[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_count "Link to this definition")

An integer telling you how many times the mock object has been called:
Copy```
>>> mock = Mock(return_value=None)
>>> mock.call_count
0
>>> mock()
>>> mock()
>>> mock.call_count
2

```


return_value[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "Link to this definition")

Set this to configure the value returned by calling the mock:
Copy```
>>> mock = Mock()
>>> mock.return_value = 'fish'
>>> mock()
'fish'

```

The default return value is a mock object and you can configure it in the normal way:
Copy```
>>> mock = Mock()
>>> mock.return_value.attribute = sentinel.Attribute
>>> mock.return_value()
<Mock name='mock()()' id='...'>
>>> mock.return_value.assert_called_with()

```

[`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") can also be set in the constructor:
Copy```
>>> mock = Mock(return_value=3)
>>> mock.return_value
3
>>> mock()
3

```


side_effect[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "Link to this definition")

This can either be a function to be called when the mock is called, an iterable or an exception (class or instance) to be raised.
If you pass in a function it will be called with same arguments as the mock and unless the function returns the [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT") singleton the call to the mock will then return whatever the function returns. If the function returns `DEFAULT` then the mock will return its normal value (from the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")).
If you pass in an iterable, it is used to retrieve an iterator which must yield a value on every call. This value can either be an exception instance to be raised, or a value to be returned from the call to the mock ([`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT") handling is identical to the function case).
An example of a mock that raises an exception (to test exception handling of an API):
Copy```
>>> mock = Mock()
>>> mock.side_effect = Exception('Boom!')
>>> mock()
Traceback (most recent call last):
  ...
Exception: Boom!

```

Using [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") to return a sequence of values:
Copy```
>>> mock = Mock()
>>> mock.side_effect = [3, 2, 1]
>>> mock(), mock(), mock()
(3, 2, 1)

```

Using a callable:
Copy```
>>> mock = Mock(return_value=3)
>>> def side_effect(*args, **kwargs):
...     return DEFAULT
...
>>> mock.side_effect = side_effect
>>> mock()
3

```

[`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") can be set in the constructor. Here’s an example that adds one to the value the mock is called with and returns it:
Copy```
>>> side_effect = lambda value: value + 1
>>> mock = Mock(side_effect=side_effect)
>>> mock(3)
4
>>> mock(-8)
-7

```

Setting [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") to `None` clears it:
Copy```
>>> m = Mock(side_effect=KeyError, return_value=3)
>>> m()
Traceback (most recent call last):
 ...
KeyError
>>> m.side_effect = None
>>> m()
3

```


call_args[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "Link to this definition")

This is either `None` (if the mock hasn’t been called), or the arguments that the mock was last called with. This will be in the form of a tuple: the first member, which can also be accessed through the `args` property, is any positional arguments the mock was called with (or an empty tuple) and the second member, which can also be accessed through the `kwargs` property, is any keyword arguments (or an empty dictionary).
