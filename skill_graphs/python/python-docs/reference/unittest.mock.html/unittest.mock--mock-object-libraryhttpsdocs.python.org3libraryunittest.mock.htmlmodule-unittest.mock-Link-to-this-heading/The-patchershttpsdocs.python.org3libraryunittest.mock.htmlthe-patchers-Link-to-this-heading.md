## The patchers[¶](https://docs.python.org/3/library/unittest.mock.html#the-patchers "Link to this heading")
The patch decorators are used for patching objects only within the scope of the function they decorate. They automatically handle the unpatching for you, even if exceptions are raised. All of these functions can also be used in with statements or as class decorators.
### patch[¶](https://docs.python.org/3/library/unittest.mock.html#patch "Link to this heading")
Note
The key is to do the patching in the right namespace. See the section [where to patch](https://docs.python.org/3/library/unittest.mock.html#id6).

unittest.mock.patch(_target_ , _new =DEFAULT_, _spec =None_, _create =False_, _spec_set =None_, _autospec =None_, _new_callable =None_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "Link to this definition")

`patch()` acts as a function decorator, class decorator or a context manager. Inside the body of the function or with statement, the _target_ is patched with a _new_ object. When the function/with statement exits the patch is undone.
If _new_ is omitted, then the target is replaced with an [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock") if the patched object is an async function or a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") otherwise. If `patch()` is used as a decorator and _new_ is omitted, the created mock is passed in as an extra argument to the decorated function. If `patch()` is used as a context manager the created mock is returned by the context manager.
_target_ should be a string in the form `'package.module.ClassName'`. The _target_ is imported and the specified object replaced with the _new_ object, so the _target_ must be importable from the environment you are calling `patch()` from. The target is imported when the decorated function is executed, not at decoration time.
The _spec_ and _spec_set_ keyword arguments are passed to the [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") if patch is creating one for you.
In addition you can pass `spec=True` or `spec_set=True`, which causes patch to pass in the object being mocked as the spec/spec_set object.
_new_callable_ allows you to specify a different class, or callable object, that will be called to create the _new_ object. By default [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock") is used for async functions and [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") for the rest.
A more powerful form of _spec_ is _autospec_. If you set `autospec=True` then the mock will be created with a spec from the object being replaced. All attributes of the mock will also have the spec of the corresponding attribute of the object being replaced. Methods and functions being mocked will have their arguments checked and will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if they are called with the wrong signature. For mocks replacing a class, their return value (the ‘instance’) will have the same spec as the class. See the [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") function and [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing).
Instead of `autospec=True` you can pass `autospec=some_object` to use an arbitrary object as the spec instead of the one being replaced.
By default `patch()` will fail to replace attributes that don’t exist. If you pass in `create=True`, and the attribute doesn’t exist, patch will create the attribute for you when the patched function is called, and delete it again after the patched function has exited. This is useful for writing tests against attributes that your production code creates at runtime. It is off by default because it can be dangerous. With it switched on you can write passing tests against APIs that don’t actually exist!
Note
Changed in version 3.5: If you are patching builtins in a module then you don’t need to pass `create=True`, it will be added by default.
Patch can be used as a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") class decorator. It works by decorating each test method in the class. This reduces the boilerplate code when your test methods share a common patchings set. `patch()` finds tests by looking for method names that start with `patch.TEST_PREFIX`. By default this is `'test'`, which matches the way [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") finds tests. You can specify an alternative prefix by setting `patch.TEST_PREFIX`.
Patch can be used as a context manager, with the with statement. Here the patching applies to the indented block after the with statement. If you use “as” then the patched object will be bound to the name after the “as”; very useful if `patch()` is creating a mock object for you.
`patch()` takes arbitrary keyword arguments. These will be passed to [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock") if the patched object is asynchronous, to [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") otherwise or to _new_callable_ if specified.
`patch.dict(...)`, `patch.multiple(...)` and `patch.object(...)` are available for alternate use-cases.
[`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") as function decorator, creating the mock for you and passing it into the decorated function:
Copy```
>>> @patch('__main__.SomeClass')
... def function(normal_argument, mock_class):
...     print(mock_class is SomeClass)
...
>>> function(None)
True

```

Patching a class replaces the class with a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") _instance_. If the class is instantiated in the code under test then it will be the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") of the mock that will be used.
If the class is instantiated multiple times you could use [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") to return a new mock each time. Alternatively you can set the _return_value_ to be anything you want.
To configure return values on methods of _instances_ on the patched class you must do this on the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value"). For example:
Copy```
>>> class Class:
...     def method(self):
...         pass
...
>>> with patch('__main__.Class') as MockClass:
...     instance = MockClass.return_value
...     instance.method.return_value = 'foo'
...     assert Class() is instance
...     assert Class().method() == 'foo'
...

```

If you use _spec_ or _spec_set_ and [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") is replacing a _class_ , then the return value of the created mock will have the same spec.
Copy```
>>> Original = Class
>>> patcher = patch('__main__.Class', spec=True)
>>> MockClass = patcher.start()
>>> instance = MockClass()
>>> assert isinstance(instance, Original)
>>> patcher.stop()

```

The _new_callable_ argument is useful where you want to use an alternative class to the default [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") for the created mock. For example, if you wanted a [`NonCallableMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMock "unittest.mock.NonCallableMock") to be used:
Copy```
>>> thing = object()
>>> with patch('__main__.thing', new_callable=NonCallableMock) as mock_thing:
...     assert thing is mock_thing
...     thing()
...
Traceback (most recent call last):
  ...
TypeError: 'NonCallableMock' object is not callable

```

Another use case might be to replace an object with an [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") instance:
Copy```
>>> from io import StringIO
>>> def foo():
...     print('Something')
...
>>> @patch('sys.stdout', new_callable=StringIO)
... def test(mock_stdout):
...     foo()
...     assert mock_stdout.getvalue() == 'Something\n'
...
>>> test()

```

When [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") is creating a mock for you, it is common that the first thing you need to do is to configure the mock. Some of that configuration can be done in the call to patch. Any arbitrary keywords you pass into the call will be used to set attributes on the created mock:
Copy```
>>> patcher = patch('__main__.thing', first='one', second='two')
>>> mock_thing = patcher.start()
>>> mock_thing.first
'one'
>>> mock_thing.second
'two'

```

As well as attributes on the created mock attributes, like the [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") and [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect"), of child mocks can also be configured. These aren’t syntactically valid to pass in directly as keyword arguments, but a dictionary with these as keys can still be expanded into a [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") call using `**`:
Copy```
>>> config = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> patcher = patch('__main__.thing', **config)
>>> mock_thing = patcher.start()
>>> mock_thing.method()
3
>>> mock_thing.other()
Traceback (most recent call last):
  ...
KeyError

```

By default, attempting to patch a function in a module (or a method or an attribute in a class) that does not exist will fail with [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError"):
Copy```
>>> @patch('sys.non_existing_attribute', 42)
... def test():
...     assert sys.non_existing_attribute == 42
...
>>> test()
Traceback (most recent call last):
  ...
AttributeError: <module 'sys' (built-in)> does not have the attribute 'non_existing_attribute'

```

but adding `create=True` in the call to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") will make the previous example work as expected:
Copy```
>>> @patch('sys.non_existing_attribute', 42, create=True)
... def test(mock_stdout):
...     assert sys.non_existing_attribute == 42
...
>>> test()

```

Changed in version 3.8: [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") now returns an [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock") if the target is an async function.
### patch.object[¶](https://docs.python.org/3/library/unittest.mock.html#patch-object "Link to this heading")

patch.object(_target_ , _attribute_ , _new =DEFAULT_, _spec =None_, _create =False_, _spec_set =None_, _autospec =None_, _new_callable =None_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "Link to this definition")

patch the named member (_attribute_) on an object (_target_) with a mock object.
`patch.object()` can be used as a decorator, class decorator or a context manager. Arguments _new_ , _spec_ , _create_ , _spec_set_ , _autospec_ and _new_callable_ have the same meaning as for [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch"). Like `patch()`, `patch.object()` takes arbitrary keyword arguments for configuring the mock object it creates.
When used as a class decorator `patch.object()` honours `patch.TEST_PREFIX` for choosing which methods to wrap.
You can either call [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object") with three arguments or two arguments. The three argument form takes the object to be patched, the attribute name and the object to replace the attribute with.
When calling with the two argument form you omit the replacement object, and a mock is created for you and passed in as an extra argument to the decorated function:
Copy```
>>> @patch.object(SomeClass, 'class_method')
... def test(mock_method):
...     SomeClass.class_method(3)
...     mock_method.assert_called_with(3)
...
>>> test()

```

_spec_ , _create_ and the other arguments to [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object") have the same meaning as they do for [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch").
### patch.dict[¶](https://docs.python.org/3/library/unittest.mock.html#patch-dict "Link to this heading")

patch.dict(_in_dict_ , _values =()_, _clear =False_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "Link to this definition")

Patch a dictionary, or dictionary like object, and restore the dictionary to its original state after the test, where the restored dictionary is a copy of the dictionary as it was before the test.
_in_dict_ can be a dictionary or a mapping like container. If it is a mapping then it must at least support getting, setting and deleting items plus iterating over keys.
_in_dict_ can also be a string specifying the name of the dictionary, which will then be fetched by importing it.
_values_ can be a dictionary of values to set in the dictionary. _values_ can also be an iterable of `(key, value)` pairs.
If _clear_ is true then the dictionary will be cleared before the new values are set.
`patch.dict()` can also be called with arbitrary keyword arguments to set values in the dictionary.
Changed in version 3.8: `patch.dict()` now returns the patched dictionary when used as a context manager.
[`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") can be used as a context manager, decorator or class decorator:
Copy```
>>> foo = {}
>>> @patch.dict(foo, {'newkey': 'newvalue'})
... def test():
...     assert foo == {'newkey': 'newvalue'}
...
>>> test()
>>> assert foo == {}

```

When used as a class decorator [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") honours `patch.TEST_PREFIX` (default to `'test'`) for choosing which methods to wrap:
Copy```
>>> import os
>>> import unittest
>>> from unittest.mock import patch
>>> @patch.dict('os.environ', {'newkey': 'newvalue'})
... class TestSample(unittest.TestCase):
...     def test_sample(self):
...         self.assertEqual(os.environ['newkey'], 'newvalue')

```

If you want to use a different prefix for your test, you can inform the patchers of the different prefix by setting `patch.TEST_PREFIX`. For more details about how to change the value of see [TEST_PREFIX](https://docs.python.org/3/library/unittest.mock.html#test-prefix).
[`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") can be used to add members to a dictionary, or simply let a test change a dictionary, and ensure the dictionary is restored when the test ends.
Copy```
>>> foo = {}
>>> with patch.dict(foo, {'newkey': 'newvalue'}) as patched_foo:
...     assert foo == {'newkey': 'newvalue'}
...     assert patched_foo == {'newkey': 'newvalue'}
...     # You can add, update or delete keys of foo (or patched_foo, it's the same dict)
...     patched_foo['spam'] = 'eggs'
...
>>> assert foo == {}
>>> assert patched_foo == {}

```

Copy```
>>> import os
>>> with patch.dict('os.environ', {'newkey': 'newvalue'}):
...     print(os.environ['newkey'])
...
newvalue
>>> assert 'newkey' not in os.environ

```

Keywords can be used in the [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") call to set values in the dictionary:
Copy```
>>> mymodule = MagicMock()
>>> mymodule.function.return_value = 'fish'
>>> with patch.dict('sys.modules', mymodule=mymodule):
...     import mymodule
...     mymodule.function('some', 'args')
...
'fish'

```

[`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") can be used with dictionary like objects that aren’t actually dictionaries. At the very minimum they must support item getting, setting, deleting and either iteration or membership test. This corresponds to the magic methods [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__"), [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__"), [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__") and either [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "container.__iter__") or [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__").
Copy```
>>> class Container:
...     def __init__(self):
...         self.values = {}
...     def __getitem__(self, name):
...         return self.values[name]
...     def __setitem__(self, name, value):
...         self.values[name] = value
...     def __delitem__(self, name):
...         del self.values[name]
...     def __iter__(self):
...         return iter(self.values)
...
>>> thing = Container()
>>> thing['one'] = 1
>>> with patch.dict(thing, one=2, two=3):
...     assert thing['one'] == 2
...     assert thing['two'] == 3
...
>>> assert thing['one'] == 1
>>> assert list(thing) == ['one']

```

### patch.multiple[¶](https://docs.python.org/3/library/unittest.mock.html#patch-multiple "Link to this heading")

patch.multiple(_target_ , _spec =None_, _create =False_, _spec_set =None_, _autospec =None_, _new_callable =None_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "Link to this definition")

Perform multiple patches in a single call. It takes the object to be patched (either as an object or a string to fetch the object by importing) and keyword arguments for the patches:
Copy```
with patch.multiple(settings, FIRST_PATCH='one', SECOND_PATCH='two'):
    ...

```

Use [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT") as the value if you want `patch.multiple()` to create mocks for you. In this case the created mocks are passed into a decorated function by keyword, and a dictionary is returned when `patch.multiple()` is used as a context manager.
`patch.multiple()` can be used as a decorator, class decorator or a context manager. The arguments _spec_ , _spec_set_ , _create_ , _autospec_ and _new_callable_ have the same meaning as for [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch"). These arguments will be applied to _all_ patches done by `patch.multiple()`.
When used as a class decorator `patch.multiple()` honours `patch.TEST_PREFIX` for choosing which methods to wrap.
If you want [`patch.multiple()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "unittest.mock.patch.multiple") to create mocks for you, then you can use [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT") as the value. If you use `patch.multiple()` as a decorator then the created mocks are passed into the decorated function by keyword.
Copy```
>>> thing = object()
>>> other = object()

>>> @patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)
... def test_function(thing, other):
...     assert isinstance(thing, MagicMock)
...     assert isinstance(other, MagicMock)
...
>>> test_function()

```

[`patch.multiple()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "unittest.mock.patch.multiple") can be nested with other `patch` decorators, but put arguments passed by keyword _after_ any of the standard arguments created by [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch"):
Copy```
>>> @patch('sys.exit')
... @patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)
... def test_function(mock_exit, other, thing):
...     assert 'other' in repr(other)
...     assert 'thing' in repr(thing)
...     assert 'exit' in repr(mock_exit)
...
>>> test_function()

```

If [`patch.multiple()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.multiple "unittest.mock.patch.multiple") is used as a context manager, the value returned by the context manager is a dictionary where created mocks are keyed by name:
Copy```
>>> with patch.multiple('__main__', thing=DEFAULT, other=DEFAULT) as values:
...     assert 'other' in repr(values['other'])
...     assert 'thing' in repr(values['thing'])
...     assert values['thing'] is thing
...     assert values['other'] is other
...

```

### patch methods: start and stop[¶](https://docs.python.org/3/library/unittest.mock.html#patch-methods-start-and-stop "Link to this heading")
All the patchers have `start()` and `stop()` methods. These make it simpler to do patching in `setUp` methods or where you want to do multiple patches without nesting decorators or with statements.
To use them call [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch"), [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object") or [`patch.dict()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict "unittest.mock.patch.dict") as normal and keep a reference to the returned `patcher` object. You can then call `start()` to put the patch in place and `stop()` to undo it.
If you are using [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") to create a mock for you then it will be returned by the call to `patcher.start`.
Copy```
>>> patcher = patch('package.module.ClassName')
>>> from package import module
>>> original = module.ClassName
>>> new_mock = patcher.start()
>>> assert module.ClassName is not original
>>> assert module.ClassName is new_mock
>>> patcher.stop()
>>> assert module.ClassName is original
>>> assert module.ClassName is not new_mock

```

A typical use case for this might be for doing multiple patches in the `setUp` method of a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"):
Copy```
>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         self.patcher1 = patch('package.module.Class1')
...         self.patcher2 = patch('package.module.Class2')
...         self.MockClass1 = self.patcher1.start()
...         self.MockClass2 = self.patcher2.start()
...
...     def tearDown(self):
...         self.patcher1.stop()
...         self.patcher2.stop()
...
...     def test_something(self):
...         assert package.module.Class1 is self.MockClass1
...         assert package.module.Class2 is self.MockClass2
...
>>> MyTest('test_something').run()

```

Caution
If you use this technique you must ensure that the patching is “undone” by calling `stop`. This can be fiddlier than you might think, because if an exception is raised in the `setUp` then `tearDown` is not called. [`unittest.TestCase.addCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup") makes this easier:
Copy```
>>> class MyTest(unittest.TestCase):
...     def setUp(self):
...         patcher = patch('package.module.Class')
...         self.MockClass = patcher.start()
...         self.addCleanup(patcher.stop)
...
...     def test_something(self):
...         assert package.module.Class is self.MockClass
...

```

As an added bonus you no longer need to keep a reference to the `patcher` object.
It is also possible to stop all patches which have been started by using [`patch.stopall()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.stopall "unittest.mock.patch.stopall").

patch.stopall()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.stopall "Link to this definition")

Stop all active patches. Only stops patches started with `start`.
### patch builtins[¶](https://docs.python.org/3/library/unittest.mock.html#patch-builtins "Link to this heading")
You can patch any builtins within a module. The following example patches builtin [`ord()`](https://docs.python.org/3/library/functions.html#ord "ord"):
Copy```
>>> @patch('__main__.ord')
... def test(mock_ord):
...     mock_ord.return_value = 101
...     print(ord('c'))
...
>>> test()
101

```

### TEST_PREFIX[¶](https://docs.python.org/3/library/unittest.mock.html#test-prefix "Link to this heading")
All of the patchers can be used as class decorators. When used in this way they wrap every test method on the class. The patchers recognise methods that start with `'test'` as being test methods. This is the same way that the [`unittest.TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") finds test methods by default.
It is possible that you want to use a different prefix for your tests. You can inform the patchers of the different prefix by setting `patch.TEST_PREFIX`:
Copy```
>>> patch.TEST_PREFIX = 'foo'
>>> value = 3
>>>
>>> @patch('__main__.value', 'not three')
... class Thing:
...     def foo_one(self):
...         print(value)
...     def foo_two(self):
...         print(value)
...
>>>
>>> Thing().foo_one()
not three
>>> Thing().foo_two()
not three
>>> value
3

```

### Nesting Patch Decorators[¶](https://docs.python.org/3/library/unittest.mock.html#nesting-patch-decorators "Link to this heading")
If you want to perform multiple patches then you can simply stack up the decorators.
You can stack up multiple patch decorators using this pattern:
Copy```
>>> @patch.object(SomeClass, 'class_method')
... @patch.object(SomeClass, 'static_method')
... def test(mock1, mock2):
...     assert SomeClass.static_method is mock1
...     assert SomeClass.class_method is mock2
...     SomeClass.static_method('foo')
...     SomeClass.class_method('bar')
...     return mock1, mock2
...
>>> mock1, mock2 = test()
>>> mock1.assert_called_once_with('foo')
>>> mock2.assert_called_once_with('bar')

```

Note that the decorators are applied from the bottom upwards. This is the standard way that Python applies decorators. The order of the created mocks passed into your test function matches this order.
### Where to patch[¶](https://docs.python.org/3/library/unittest.mock.html#where-to-patch "Link to this heading")
[`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") works by (temporarily) changing the object that a _name_ points to with another one. There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.
The basic principle is that you patch where an object is _looked up_ , which is not necessarily the same place as where it is defined. A couple of examples will help to clarify this.
Imagine we have a project that we want to test with the following structure:
Copy```
a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass

```

Now we want to test `some_function` but we want to mock out `SomeClass` using [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch"). The problem is that when we import module b, which we will have to do when it imports `SomeClass` from module a. If we use `patch()` to mock out `a.SomeClass` then it will have no effect on our test; module b already has a reference to the _real_ `SomeClass` and it looks like our patching had no effect.
The key is to patch out `SomeClass` where it is used (or where it is looked up). In this case `some_function` will actually look up `SomeClass` in module b, where we have imported it. The patching should look like:
Copy```
@patch('b.SomeClass')

```

However, consider the alternative scenario where instead of `from a import SomeClass` module b does `import a` and `some_function` uses `a.SomeClass`. Both of these import forms are common. In this case the class we want to patch is being looked up in the module and so we have to patch `a.SomeClass` instead:
Copy```
@patch('a.SomeClass')

```

### Patching Descriptors and Proxy Objects[¶](https://docs.python.org/3/library/unittest.mock.html#patching-descriptors-and-proxy-objects "Link to this heading")
Both [patch](https://docs.python.org/3/library/unittest.mock.html#patch) and [patch.object](https://docs.python.org/3/library/unittest.mock.html#patch-object) correctly patch and restore descriptors: class methods, static methods and properties. You should patch these on the _class_ rather than an instance. They also work with _some_ objects that proxy attribute access, like the
## MagicMock and magic method support[¶](https://docs.python.org/3/library/unittest.mock.html#magicmock-and-magic-method-support "Link to this heading")
### Mocking Magic Methods[¶](https://docs.python.org/3/library/unittest.mock.html#mocking-magic-methods "Link to this heading")
[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") supports mocking the Python protocol methods, also known as [“magic methods”](https://docs.python.org/3/glossary.html#term-magic-method). This allows mock objects to replace containers or other objects that implement Python protocols.
Because magic methods are looked up differently from normal methods [[2]](https://docs.python.org/3/library/unittest.mock.html#id9), this support has been specially implemented. This means that only specific magic methods are supported. The supported list includes _almost_ all of them. If there are any missing that you need please let us know.
You mock magic methods by setting the method you are interested in to a function or a mock instance. If you are using a function then it _must_ take `self` as the first argument [[3]](https://docs.python.org/3/library/unittest.mock.html#id10).
Copy```
>>> def __str__(self):
...     return 'fooble'
...
>>> mock = Mock()
>>> mock.__str__ = __str__
>>> str(mock)
'fooble'

```

Copy```
>>> mock = Mock()
>>> mock.__str__ = Mock()
>>> mock.__str__.return_value = 'fooble'
>>> str(mock)
'fooble'

```

Copy```
>>> mock = Mock()
>>> mock.__iter__ = Mock(return_value=iter([]))
>>> list(mock)
[]

```

One use case for this is for mocking objects used as context managers in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement:
Copy```
>>> mock = Mock()
>>> mock.__enter__ = Mock(return_value='foo')
>>> mock.__exit__ = Mock(return_value=False)
>>> with mock as m:
...     assert m == 'foo'
...
>>> mock.__enter__.assert_called_with()
>>> mock.__exit__.assert_called_with(None, None, None)

```

Calls to magic methods do not appear in [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls"), but they are recorded in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls").
Note
If you use the _spec_ keyword argument to create a mock then attempting to set a magic method that isn’t in the spec will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
The full list of supported magic methods is:
  * `__hash__`, `__sizeof__`, `__repr__` and `__str__`
  * `__dir__`, `__format__` and `__subclasses__`
  * `__round__`, `__floor__`, `__trunc__` and `__ceil__`
  * Comparisons: `__lt__`, `__gt__`, `__le__`, `__ge__`, `__eq__` and `__ne__`
  * Container methods: `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__len__`, `__iter__`, `__reversed__` and `__missing__`
  * Context manager: `__enter__`, `__exit__`, `__aenter__` and `__aexit__`
  * Unary numeric methods: `__neg__`, `__pos__` and `__invert__`
  * The numeric methods (including right hand and in-place variants): `__add__`, `__sub__`, `__mul__`, `__matmul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__divmod__`, `__lshift__`, `__rshift__`, `__and__`, `__xor__`, `__or__`, and `__pow__`
  * Numeric conversion methods: `__complex__`, `__int__`, `__float__` and `__index__`
  * Descriptor methods: `__get__`, `__set__` and `__delete__`
  * Pickling: `__reduce__`, `__reduce_ex__`, `__getinitargs__`, `__getnewargs__`, `__getstate__` and `__setstate__`
  * File system path representation: `__fspath__`
  * Asynchronous iteration methods: `__aiter__` and `__anext__`


Changed in version 3.8: Added support for [`os.PathLike.__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__").
Changed in version 3.8: Added support for `__aenter__`, `__aexit__`, `__aiter__` and `__anext__`.
The following methods exist but are _not_ supported as they are either in use by mock, can’t be set dynamically, or can cause problems:
  * `__getattr__`, `__setattr__`, `__init__` and `__new__`
  * `__prepare__`, `__instancecheck__`, `__subclasscheck__`, `__del__`


### Magic Mock[¶](https://docs.python.org/3/library/unittest.mock.html#magic-mock "Link to this heading")
There are two `MagicMock` variants: [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") and [`NonCallableMagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMagicMock "unittest.mock.NonCallableMagicMock").

_class_ unittest.mock.MagicMock(_* args_, _** kw_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "Link to this definition")

`MagicMock` is a subclass of [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") with default implementations of most of the [magic methods](https://docs.python.org/3/glossary.html#term-magic-method). You can use `MagicMock` without having to configure the magic methods yourself.
The constructor parameters have the same meaning as for [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock").
If you use the _spec_ or _spec_set_ arguments then _only_ magic methods that exist in the spec will be created.

_class_ unittest.mock.NonCallableMagicMock(_* args_, _** kw_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.NonCallableMagicMock "Link to this definition")

A non-callable version of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock").
The constructor parameters have the same meaning as for [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock"), with the exception of _return_value_ and _side_effect_ which have no meaning on a non-callable mock.
The magic methods are setup with [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") objects, so you can configure them and use them in the usual way:
Copy```
>>> mock = MagicMock()
>>> mock[3] = 'fish'
>>> mock.__setitem__.assert_called_with(3, 'fish')
>>> mock.__getitem__.return_value = 'result'
>>> mock[2]
'result'

```

By default many of the protocol methods are required to return objects of a specific type. These methods are preconfigured with a default return value, so that they can be used without you having to do anything if you aren’t interested in the return value. You can still _set_ the return value manually if you want to change the default.
Methods and their defaults:
  * `__lt__`: [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented")
  * `__gt__`: `NotImplemented`
  * `__le__`: `NotImplemented`
  * `__ge__`: `NotImplemented`
  * `__int__`: `1`
  * `__contains__`: `False`
  * `__len__`: `0`
  * `__iter__`: `iter([])`
  * `__exit__`: `False`
  * `__aexit__`: `False`
  * `__complex__`: `1j`
  * `__float__`: `1.0`
  * `__bool__`: `True`
  * `__index__`: `1`
  * `__hash__`: default hash for the mock
  * `__str__`: default str for the mock
  * `__sizeof__`: default sizeof for the mock


For example:
Copy```
>>> mock = MagicMock()
>>> int(mock)
1
>>> len(mock)
0
>>> list(mock)
[]
>>> object() in mock
False

```

The two equality methods, `__eq__()` and `__ne__()`, are special. They do the default equality comparison on identity, using the [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") attribute, unless you change their return value to return something else:
Copy```
>>> MagicMock() == 3
False
>>> MagicMock() != 3
True
>>> mock = MagicMock()
>>> mock.__eq__.return_value = True
>>> mock == 3
True

```

The return value of `MagicMock.__iter__()` can be any iterable object and isn’t required to be an iterator:
Copy```
>>> mock = MagicMock()
>>> mock.__iter__.return_value = ['a', 'b', 'c']
>>> list(mock)
['a', 'b', 'c']
>>> list(mock)
['a', 'b', 'c']

```

If the return value _is_ an iterator, then iterating over it once will consume it and subsequent iterations will result in an empty list:
Copy```
>>> mock.__iter__.return_value = iter(['a', 'b', 'c'])
>>> list(mock)
['a', 'b', 'c']
>>> list(mock)
[]

```

`MagicMock` has all of the supported magic methods configured except for some of the obscure and obsolete ones. You can still set these up if you want.
Magic methods that are supported but not setup by default in `MagicMock` are:
  * `__subclasses__`
  * `__dir__`
  * `__format__`
  * `__get__`, `__set__` and `__delete__`
  * `__reversed__` and `__missing__`
  * `__reduce__`, `__reduce_ex__`, `__getinitargs__`, `__getnewargs__`, `__getstate__` and `__setstate__`
  * `__getformat__`

[[2](https://docs.python.org/3/library/unittest.mock.html#id7)]
Magic methods _should_ be looked up on the class rather than the instance. Different versions of Python are inconsistent about applying this rule. The supported protocol methods should work with all supported versions of Python.
[[3](https://docs.python.org/3/library/unittest.mock.html#id8)]
The function is basically hooked up to the class, but each `Mock` instance is kept isolated from the others.
