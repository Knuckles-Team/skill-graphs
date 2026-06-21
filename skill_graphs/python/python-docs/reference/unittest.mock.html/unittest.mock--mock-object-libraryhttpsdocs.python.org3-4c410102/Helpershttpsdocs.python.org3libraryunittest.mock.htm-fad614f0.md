## Helpers[¶](https://docs.python.org/3/library/unittest.mock.html#helpers "Link to this heading")
### sentinel[¶](https://docs.python.org/3/library/unittest.mock.html#sentinel "Link to this heading")

unittest.mock.sentinel[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.sentinel "Link to this definition")

The `sentinel` object provides a convenient way of providing unique objects for your tests.
Attributes are created on demand when you access them by name. Accessing the same attribute will always return the same object. The objects returned have a sensible repr so that test failure messages are readable.
Changed in version 3.7: The `sentinel` attributes now preserve their identity when they are [`copied`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") or [`pickled`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.").
Sometimes when testing you need to test that a specific object is passed as an argument to another method, or returned. It can be common to create named sentinel objects to test this. [`sentinel`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.sentinel "unittest.mock.sentinel") provides a convenient way of creating and testing the identity of objects like this.
In this example we monkey patch `method` to return `sentinel.some_object`:
Copy```
>>> real = ProductionClass()
>>> real.method = Mock(name="method")
>>> real.method.return_value = sentinel.some_object
>>> result = real.method()
>>> assert result is sentinel.some_object
>>> result
sentinel.some_object

```

### DEFAULT[¶](https://docs.python.org/3/library/unittest.mock.html#default "Link to this heading")

unittest.mock.DEFAULT[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "Link to this definition")

The `DEFAULT` object is a pre-created sentinel (actually `sentinel.DEFAULT`). It can be used by [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") functions to indicate that the normal return value should be used.
### call[¶](https://docs.python.org/3/library/unittest.mock.html#call "Link to this heading")

unittest.mock.call(_* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call "Link to this definition")

`call()` is a helper object for making simpler assertions, for comparing with [`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args"), [`call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list"), [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") and [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls"). `call()` can also be used with [`assert_has_calls()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls "unittest.mock.Mock.assert_has_calls").
Copy```
>>> m = MagicMock(return_value=None)
>>> m(1, 2, a='foo', b='bar')
>>> m()
>>> m.call_args_list == [call(1, 2, a='foo', b='bar'), call()]
True

```


call.call_list()[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call.call_list "Link to this definition")

For a call object that represents multiple calls, `call_list()` returns a list of all the intermediate calls as well as the final call.
`call_list` is particularly useful for making assertions on “chained calls”. A chained call is multiple calls on a single line of code. This results in multiple entries in [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") on a mock. Manually constructing the sequence of calls can be tedious.
[`call_list()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call.call_list "unittest.mock.call.call_list") can construct the sequence of calls from the same chained call:
Copy```
>>> m = MagicMock()
>>> m(1).method(arg='foo').other('bar')(2.0)
<MagicMock name='mock().method().other()()' id='...'>
>>> kall = call(1).method(arg='foo').other('bar')(2.0)
>>> kall.call_list()
[call(1),
 call().method(arg='foo'),
 call().method().other('bar'),
 call().method().other()(2.0)]
>>> m.mock_calls == kall.call_list()
True

```

A `call` object is either a tuple of (positional args, keyword args) or (name, positional args, keyword args) depending on how it was constructed. When you construct them yourself this isn’t particularly interesting, but the `call` objects that are in the [`Mock.call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args"), [`Mock.call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list") and [`Mock.mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") attributes can be introspected to get at the individual arguments they contain.
The `call` objects in [`Mock.call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args") and [`Mock.call_args_list`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list "unittest.mock.Mock.call_args_list") are two-tuples of (positional args, keyword args) whereas the `call` objects in [`Mock.mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls"), along with ones you construct yourself, are three-tuples of (name, positional args, keyword args).
You can use their “tupleness” to pull out the individual arguments for more complex introspection and assertions. The positional arguments are a tuple (an empty tuple if there are no positional arguments) and the keyword arguments are a dictionary:
Copy```
>>> m = MagicMock(return_value=None)
>>> m(1, 2, 3, arg='one', arg2='two')
>>> kall = m.call_args
>>> kall.args
(1, 2, 3)
>>> kall.kwargs
{'arg': 'one', 'arg2': 'two'}
>>> kall.args is kall[0]
True
>>> kall.kwargs is kall[1]
True

```

Copy```
>>> m = MagicMock()
>>> m.foo(4, 5, 6, arg='two', arg2='three')
<MagicMock name='mock.foo()' id='...'>
>>> kall = m.mock_calls[0]
>>> name, args, kwargs = kall
>>> name
'foo'
>>> args
(4, 5, 6)
>>> kwargs
{'arg': 'two', 'arg2': 'three'}
>>> name is m.mock_calls[0][0]
True

```

### create_autospec[¶](https://docs.python.org/3/library/unittest.mock.html#create-autospec "Link to this heading")

unittest.mock.create_autospec(_spec_ , _spec_set =False_, _instance =False_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "Link to this definition")

Create a mock object using another object as a spec. Attributes on the mock will use the corresponding attribute on the _spec_ object as their spec.
Functions or methods being mocked will have their arguments checked to ensure that they are called with the correct signature.
If _spec_set_ is `True` then attempting to set attributes that don’t exist on the spec object will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
If a class is used as a spec then the return value of the mock (the instance of the class) will have the same spec. You can use a class as the spec for an instance object by passing `instance=True`. The returned mock will only be callable if instances of the mock are callable.
`create_autospec()` also takes arbitrary keyword arguments that are passed to the constructor of the created mock.
See [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#auto-speccing) for examples of how to use auto-speccing with [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") and the _autospec_ argument to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch").
Changed in version 3.8: [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") now returns an [`AsyncMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.AsyncMock "unittest.mock.AsyncMock") if the target is an async function.
### ANY[¶](https://docs.python.org/3/library/unittest.mock.html#any "Link to this heading")

unittest.mock.ANY[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "Link to this definition")

Sometimes you may need to make assertions about _some_ of the arguments in a call to mock, but either not care about some of the arguments or want to pull them individually out of [`call_args`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args "unittest.mock.Mock.call_args") and make more complex assertions on them.
To ignore certain arguments you can pass in objects that compare equal to _everything_. Calls to [`assert_called_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_with "unittest.mock.Mock.assert_called_with") and [`assert_called_once_with()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called_once_with "unittest.mock.Mock.assert_called_once_with") will then succeed no matter what was passed in.
Copy```
>>> mock = Mock(return_value=None)
>>> mock('foo', bar=object())
>>> mock.assert_called_once_with('foo', bar=ANY)

```

[`ANY`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "unittest.mock.ANY") can also be used in comparisons with call lists like [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls"):
Copy```
>>> m = MagicMock(return_value=None)
>>> m(1)
>>> m(1, 2)
>>> m(object())
>>> m.mock_calls == [call(1), call(1, 2), ANY]
True

```

[`ANY`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY "unittest.mock.ANY") is not limited to comparisons with call objects and so can also be used in test assertions:
Copy```
class TestStringMethods(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', ANY])

```

### FILTER_DIR[¶](https://docs.python.org/3/library/unittest.mock.html#filter-dir "Link to this heading")

unittest.mock.FILTER_DIR[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "Link to this definition")

[`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR") is a module level variable that controls the way mock objects respond to [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir"). The default is `True`, which uses the filtering described below, to only show useful members. If you dislike this filtering, or need to switch it off for diagnostic purposes, then set `mock.FILTER_DIR = False`.
With filtering on, `dir(some_mock)` shows only useful attributes and will include any dynamically created attributes that wouldn’t normally be shown. If the mock was created with a _spec_ (or _autospec_ of course) then all the attributes from the original are shown, even if they haven’t been accessed yet:
Copy```
>>> dir(Mock())
['assert_any_call',
 'assert_called',
 'assert_called_once',
 'assert_called_once_with',
 'assert_called_with',
 'assert_has_calls',
 'assert_not_called',
 'attach_mock',
 ...
>>> from urllib import request
>>> dir(Mock(spec=request))
['AbstractBasicAuthHandler',
 'AbstractDigestAuthHandler',
 'AbstractHTTPHandler',
 'BaseHandler',
 ...

```

Many of the not-very-useful (private to [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") rather than the thing being mocked) underscore and double underscore prefixed attributes have been filtered from the result of calling [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") on a `Mock`. If you dislike this behaviour you can switch it off by setting the module level switch [`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR"):
Copy```
>>> from unittest import mock
>>> mock.FILTER_DIR = False
>>> dir(mock.Mock())
['_NonCallableMock__get_return_value',
 '_NonCallableMock__get_side_effect',
 '_NonCallableMock__return_value_doc',
 '_NonCallableMock__set_return_value',
 '_NonCallableMock__set_side_effect',
 '__call__',
 '__class__',
 ...

```

Alternatively you can just use `vars(my_mock)` (instance members) and `dir(type(my_mock))` (type members) to bypass the filtering irrespective of [`FILTER_DIR`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.FILTER_DIR "unittest.mock.FILTER_DIR").
### mock_open[¶](https://docs.python.org/3/library/unittest.mock.html#mock-open "Link to this heading")

unittest.mock.mock_open(_mock =None_, _read_data =None_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.mock_open "Link to this definition")

A helper function to create a mock to replace the use of [`open()`](https://docs.python.org/3/library/functions.html#open "open"). It works for `open()` called directly or used as a context manager.
The _mock_ argument is the mock object to configure. If `None` (the default) then a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") will be created for you, with the API limited to methods or attributes available on standard file handles.
_read_data_ is a string for the [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read"), [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline"), and [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") methods of the file handle to return. Calls to those methods will take data from _read_data_ until it is depleted. The mock of these methods is pretty simplistic: every time the _mock_ is called, the _read_data_ is rewound to the start. If you need more control over the data that you are feeding to the tested code you will need to customize this mock for yourself. When that is insufficient, one of the in-memory filesystem packages on
Changed in version 3.4: Added [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") and [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines "io.IOBase.readlines") support. The mock of [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") changed to consume _read_data_ rather than returning it on each call.
Changed in version 3.5: _read_data_ is now reset on each call to the _mock_.
Changed in version 3.8: Added [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "container.__iter__") to implementation so that iteration (such as in for loops) correctly consumes _read_data_.
Using [`open()`](https://docs.python.org/3/library/functions.html#open "open") as a context manager is a great way to ensure your file handles are closed properly and is becoming common:
Copy```
with open('/some/path', 'w') as f:
    f.write('something')

```

The issue is that even if you mock out the call to [`open()`](https://docs.python.org/3/library/functions.html#open "open") it is the _returned object_ that is used as a context manager (and has [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") called).
Mocking context managers with a [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") is common enough and fiddly enough that a helper function is useful.
Copy```
>>> m = mock_open()
>>> with patch('__main__.open', m):
...     with open('foo', 'w') as h:
...         h.write('some stuff')
...
>>> m.mock_calls
[call('foo', 'w'),
 call().__enter__(),
 call().write('some stuff'),
 call().__exit__(None, None, None)]
>>> m.assert_called_once_with('foo', 'w')
>>> handle = m()
>>> handle.write.assert_called_once_with('some stuff')

```

And for reading files:
Copy```
>>> with patch('__main__.open', mock_open(read_data='bibble')) as m:
...     with open('foo') as h:
...         result = h.read()
...
>>> m.assert_called_once_with('foo')
>>> assert result == 'bibble'

```

### Autospeccing[¶](https://docs.python.org/3/library/unittest.mock.html#autospeccing "Link to this heading")
Autospeccing is based on the existing `spec` feature of mock. It limits the api of mocks to the api of an original object (the spec), but it is recursive (implemented lazily) so that attributes of mocks only have the same api as the attributes of the spec. In addition mocked functions / methods have the same call signature as the original so they raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if they are called incorrectly.
Before I explain how auto-speccing works, here’s why it is needed.
[`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") is a very powerful and flexible object, but it suffers from a flaw which is general to mocking. If you refactor some of your code, rename members and so on, any tests for code that is still using the _old api_ but uses mocks instead of the real objects will still pass. This means your tests can all pass even though your code is broken.
Changed in version 3.5: Before 3.5, tests with a typo in the word assert would silently pass when they should raise an error. You can still achieve this behavior by passing `unsafe=True` to Mock.
Note that this is another reason why you need integration tests as well as unit tests. Testing everything in isolation is all fine and dandy, but if you don’t test how your units are “wired together” there is still lots of room for bugs that tests might have caught.
`unittest.mock` already provides a feature to help with this, called speccing. If you use a class or instance as the `spec` for a mock then you can only access attributes on the mock that exist on the real class:
Copy```
>>> from urllib import request
>>> mock = Mock(spec=request.Request)
>>> mock.assret_called_with  # Intentional typo!
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'assret_called_with'

```

The spec only applies to the mock itself, so we still have the same issue with any methods on the mock:
Copy```
>>> mock.header_items()
<mock.Mock object at 0x...>
>>> mock.header_items.assret_called_with()  # Intentional typo!

```

Auto-speccing solves this problem. You can either pass `autospec=True` to [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") / [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.object "unittest.mock.patch.object") or use the [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") function to create a mock with a spec. If you use the `autospec=True` argument to `patch()` then the object that is being replaced will be used as the spec object. Because the speccing is done “lazily” (the spec is created as attributes on the mock are accessed) you can use it with very complex or deeply nested objects (like modules that import modules that import modules) without a big performance hit.
Here’s an example of it in use:
Copy```
>>> from urllib import request
>>> patcher = patch('__main__.request', autospec=True)
>>> mock_request = patcher.start()
>>> request is mock_request
True
>>> mock_request.Request
<MagicMock name='request.Request' spec='Request' id='...'>

```

You can see that `request.Request` has a spec. `request.Request` takes two arguments in the constructor (one of which is _self_). Here’s what happens if we try to call it incorrectly:
Copy```
>>> req = request.Request()
Traceback (most recent call last):
 ...
TypeError: <lambda>() takes at least 2 arguments (1 given)

```

The spec also applies to instantiated classes (i.e. the return value of specced mocks):
Copy```
>>> req = request.Request('foo')
>>> req
<NonCallableMagicMock name='request.Request()' spec='Request' id='...'>

```

`Request` objects are not callable, so the return value of instantiating our mocked out `request.Request` is a non-callable mock. With the spec in place any typos in our asserts will raise the correct error:
Copy```
>>> req.add_header('spam', 'eggs')
<MagicMock name='request.Request().add_header()' id='...'>
>>> req.add_header.assret_called_with  # Intentional typo!
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'assret_called_with'
>>> req.add_header.assert_called_with('spam', 'eggs')

```

In many cases you will just be able to add `autospec=True` to your existing [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") calls and then be protected against bugs due to typos and api changes.
As well as using _autospec_ through [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") there is a [`create_autospec()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec "unittest.mock.create_autospec") for creating autospecced mocks directly:
Copy```
>>> from urllib import request
>>> mock_request = create_autospec(request)
>>> mock_request.Request('foo', 'bar')
<NonCallableMagicMock name='mock.Request()' spec='Request' id='...'>

```

This isn’t without caveats and limitations however, which is why it is not the default behaviour. In order to know what attributes are available on the spec object, autospec has to introspect (access attributes) the spec. As you traverse attributes on the mock a corresponding traversal of the original object is happening under the hood. If any of your specced objects have properties or descriptors that can trigger code execution then you may not be able to use autospec. On the other hand it is much better to design your objects so that introspection is safe [[4]](https://docs.python.org/3/library/unittest.mock.html#id12).
A more serious problem is that it is common for instance attributes to be created in the [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") method and not to exist on the class at all. _autospec_ can’t know about any dynamically created attributes and restricts the api to visible attributes.
Copy```
>>> class Something:
...   def __init__(self):
...     self.a = 33
...
>>> with patch('__main__.Something', autospec=True):
...   thing = Something()
...   thing.a
...
Traceback (most recent call last):
  ...
AttributeError: Mock object has no attribute 'a'

```

There are a few different ways of resolving this problem. The easiest, but not necessarily the least annoying, way is to simply set the required attributes on the mock after creation. Just because _autospec_ doesn’t allow you to fetch attributes that don’t exist on the spec it doesn’t prevent you setting them:
Copy```
>>> with patch('__main__.Something', autospec=True):
...   thing = Something()
...   thing.a = 33
...

```

There is a more aggressive version of both _spec_ and _autospec_ that _does_ prevent you setting non-existent attributes. This is useful if you want to ensure your code only _sets_ valid attributes too, but obviously it prevents this particular scenario:
Copy```
>>> with patch('__main__.Something', autospec=True, spec_set=True):
...   thing = Something()
...   thing.a = 33
...
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'a'

```

Probably the best way of solving the problem is to add class attributes as default values for instance members initialised in [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__"). Note that if you are only setting default attributes in `__init__()` then providing them via class attributes (shared between instances of course) is faster too. e.g.
Copy```
class Something:
    a = 33

```

This brings up another issue. It is relatively common to provide a default value of `None` for members that will later be an object of a different type. `None` would be useless as a spec because it wouldn’t let you access _any_ attributes or methods on it. As `None` is _never_ going to be useful as a spec, and probably indicates a member that will normally of some other type, autospec doesn’t use a spec for members that are set to `None`. These will just be ordinary mocks (well - MagicMocks):
Copy```
>>> class Something:
...     member = None
...
>>> mock = create_autospec(Something)
>>> mock.member.foo.bar.baz()
<MagicMock name='mock.member.foo.bar.baz()' id='...'>

```

If modifying your production classes to add defaults isn’t to your liking then there are more options. One of these is simply to use an instance as the spec rather than the class. The other is to create a subclass of the production class and add the defaults to the subclass without affecting the production class. Both of these require you to use an alternative object as the spec. Thankfully [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") supports this - you can simply pass the alternative object as the _autospec_ argument:
Copy```
>>> class Something:
...   def __init__(self):
...     self.a = 33
...
>>> class SomethingForTest(Something):
...   a = 33
...
>>> p = patch('__main__.Something', autospec=SomethingForTest)
>>> mock = p.start()
>>> mock.a
<NonCallableMagicMock name='Something.a' spec='int' id='...'>

```

[[4](https://docs.python.org/3/library/unittest.mock.html#id11)]
This only applies to classes or already instantiated objects. Calling a mocked class to create a mock instance _does not_ create a real instance. It is only attribute lookups - along with calls to [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") - that are done.
### Sealing mocks[¶](https://docs.python.org/3/library/unittest.mock.html#sealing-mocks "Link to this heading")

unittest.mock.seal(_mock_)[¶](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.seal "Link to this definition")

Seal will disable the automatic creation of mocks when accessing an attribute of the mock being sealed or any of its attributes that are already mocks recursively.
If a mock instance with a name or a spec is assigned to an attribute it won’t be considered in the sealing chain. This allows one to prevent seal from fixing part of the mock object.
Copy```
>>> mock = Mock()
>>> mock.submock.attribute1 = 2
>>> mock.not_submock = mock.Mock(name="sample_name")
>>> seal(mock)
>>> mock.new_attribute  # This will raise AttributeError.
>>> mock.submock.attribute2  # This will raise AttributeError.
>>> mock.not_submock.attribute2  # This won't raise.

```

Added in version 3.7.
## Order of precedence of `side_effect`, `return_value` and _wraps_[¶](https://docs.python.org/3/library/unittest.mock.html#order-of-precedence-of-side-effect-return-value-and-wraps "Link to this heading")
The order of their precedence is:
  1. [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect")
  2. [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value")
  3. _wraps_


If all three are set, mock will return the value from [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect"), ignoring [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") and the wrapped object altogether. If any two are set, the one with the higher precedence will return the value. Regardless of the order of which was set first, the order of precedence remains unchanged.
Copy```
>>> from unittest.mock import Mock
>>> class Order:
...     @staticmethod
...     def get_value():
...         return "third"
...
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.get_value.side_effect = ["first"]
>>> order_mock.get_value.return_value = "second"
>>> order_mock.get_value()
'first'

```

As `None` is the default value of [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect"), if you reassign its value back to `None`, the order of precedence will be checked between [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") and the wrapped object, ignoring `side_effect`.
Copy```
>>> order_mock.get_value.side_effect = None
>>> order_mock.get_value()
'second'

```

If the value being returned by [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") is [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT"), it is ignored and the order of precedence moves to the successor to obtain the value to return.
Copy```
>>> from unittest.mock import DEFAULT
>>> order_mock.get_value.side_effect = [DEFAULT]
>>> order_mock.get_value()
'second'

```

When [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") wraps an object, the default value of [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") will be [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT").
Copy```
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.return_value
sentinel.DEFAULT
>>> order_mock.get_value.return_value
sentinel.DEFAULT

```

The order of precedence will ignore this value and it will move to the last successor which is the wrapped object.
As the real call is being made to the wrapped object, creating an instance of this mock will return the real instance of the class. The positional arguments, if any, required by the wrapped object must be passed.
Copy```
>>> order_mock_instance = order_mock()
>>> isinstance(order_mock_instance, Order)
True
>>> order_mock_instance.get_value()
'third'

```

Copy```
>>> order_mock.get_value.return_value = DEFAULT
>>> order_mock.get_value()
'third'

```

Copy```
>>> order_mock.get_value.return_value = "second"
>>> order_mock.get_value()
'second'

```

But if you assign `None` to it, this will not be ignored as it is an explicit assignment. So, the order of precedence will not move to the wrapped object.
Copy```
>>> order_mock.get_value.return_value = None
>>> order_mock.get_value() is None
True

```

Even if you set all three at once when initializing the mock, the order of precedence remains the same:
Copy```
>>> order_mock = Mock(spec=Order, wraps=Order,
...                   **{"get_value.side_effect": ["first"],
...                      "get_value.return_value": "second"}
...                   )
...
>>> order_mock.get_value()
'first'
>>> order_mock.get_value.side_effect = None
>>> order_mock.get_value()
'second'
>>> order_mock.get_value.return_value = DEFAULT
>>> order_mock.get_value()
'third'

```

If [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") is exhausted, the order of precedence will not cause a value to be obtained from the successors. Instead, `StopIteration` exception is raised.
Copy```
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.get_value.side_effect = ["first side effect value",
...                                     "another side effect value"]
>>> order_mock.get_value.return_value = "second"

```

Copy```
>>> order_mock.get_value()
'first side effect value'
>>> order_mock.get_value()
'another side effect value'

```

Copy```
>>> order_mock.get_value()
Traceback (most recent call last):
 ...
StopIteration

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
    * [Quick Guide](https://docs.python.org/3/library/unittest.mock.html#quick-guide)
    * [The Mock Class](https://docs.python.org/3/library/unittest.mock.html#the-mock-class)
      * [Calling](https://docs.python.org/3/library/unittest.mock.html#calling)
      * [Deleting Attributes](https://docs.python.org/3/library/unittest.mock.html#deleting-attributes)
      * [Mock names and the name attribute](https://docs.python.org/3/library/unittest.mock.html#mock-names-and-the-name-attribute)
      * [Attaching Mocks as Attributes](https://docs.python.org/3/library/unittest.mock.html#attaching-mocks-as-attributes)
    * [The patchers](https://docs.python.org/3/library/unittest.mock.html#the-patchers)
      * [patch](https://docs.python.org/3/library/unittest.mock.html#patch)
      * [patch.object](https://docs.python.org/3/library/unittest.mock.html#patch-object)
      * [patch.dict](https://docs.python.org/3/library/unittest.mock.html#patch-dict)
      * [patch.multiple](https://docs.python.org/3/library/unittest.mock.html#patch-multiple)
      * [patch methods: start and stop](https://docs.python.org/3/library/unittest.mock.html#patch-methods-start-and-stop)
      * [patch builtins](https://docs.python.org/3/library/unittest.mock.html#patch-builtins)
      * [TEST_PREFIX](https://docs.python.org/3/library/unittest.mock.html#test-prefix)
      * [Nesting Patch Decorators](https://docs.python.org/3/library/unittest.mock.html#nesting-patch-decorators)
      * [Where to patch](https://docs.python.org/3/library/unittest.mock.html#where-to-patch)
      * [Patching Descriptors and Proxy Objects](https://docs.python.org/3/library/unittest.mock.html#patching-descriptors-and-proxy-objects)
    * [MagicMock and magic method support](https://docs.python.org/3/library/unittest.mock.html#magicmock-and-magic-method-support)
      * [Mocking Magic Methods](https://docs.python.org/3/library/unittest.mock.html#mocking-magic-methods)
      * [Magic Mock](https://docs.python.org/3/library/unittest.mock.html#magic-mock)
    * [Helpers](https://docs.python.org/3/library/unittest.mock.html#helpers)
      * [sentinel](https://docs.python.org/3/library/unittest.mock.html#sentinel)
      * [DEFAULT](https://docs.python.org/3/library/unittest.mock.html#default)
      * [call](https://docs.python.org/3/library/unittest.mock.html#call)
      * [create_autospec](https://docs.python.org/3/library/unittest.mock.html#create-autospec)
      * [ANY](https://docs.python.org/3/library/unittest.mock.html#any)
      * [FILTER_DIR](https://docs.python.org/3/library/unittest.mock.html#filter-dir)
      * [mock_open](https://docs.python.org/3/library/unittest.mock.html#mock-open)
      * [Autospeccing](https://docs.python.org/3/library/unittest.mock.html#autospeccing)
      * [Sealing mocks](https://docs.python.org/3/library/unittest.mock.html#sealing-mocks)
    * [Order of precedence of `side_effect`, `return_value` and _wraps_](https://docs.python.org/3/library/unittest.mock.html#order-of-precedence-of-side-effect-return-value-and-wraps)


#### Previous topic
[`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html "previous chapter")
#### Next topic
[`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=unittest.mock+%E2%80%94+mock+object+library&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.mock.html&pagesource=library%2Funittest.mock.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/unittest.mock-examples.html "unittest.mock — getting started") |
  * [previous](https://docs.python.org/3/library/unittest.html "unittest — Unit testing framework") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Development Tools](https://docs.python.org/3/library/development.html) »
  * [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
