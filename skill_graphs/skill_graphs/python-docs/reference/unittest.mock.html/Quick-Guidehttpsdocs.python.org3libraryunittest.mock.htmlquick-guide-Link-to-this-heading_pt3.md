The simplest way to make a mock raise an exception when called is to make [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") an exception class or instance:
Copy```
>>> m = MagicMock(side_effect=IndexError)
>>> m(1, 2, 3)
Traceback (most recent call last):
  ...
IndexError
>>> m.mock_calls
[call(1, 2, 3)]
>>> m.side_effect = KeyError('Bang!')
>>> m('two', 'three', 'four')
Traceback (most recent call last):
  ...
KeyError: 'Bang!'
>>> m.mock_calls
[call(1, 2, 3), call('two', 'three', 'four')]

```

If [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") is a function then whatever that function returns is what calls to the mock return. The `side_effect` function is called with the same arguments as the mock. This allows you to vary the return value of the call dynamically, based on the input:
Copy```
>>> def side_effect(value):
...     return value + 1
...
>>> m = MagicMock(side_effect=side_effect)
>>> m(1)
2
>>> m(2)
3
>>> m.mock_calls
[call(1), call(2)]

```

If you want the mock to still return the default return value (a new mock), or any set return value, then there are two ways of doing this. Either return [`return_value`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value "unittest.mock.Mock.return_value") from inside [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect"), or return [`DEFAULT`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.DEFAULT "unittest.mock.DEFAULT"):
Copy```
>>> m = MagicMock()
>>> def side_effect(*args, **kwargs):
...     return m.return_value
...
>>> m.side_effect = side_effect
>>> m.return_value = 3
>>> m()
3
>>> def side_effect(*args, **kwargs):
...     return DEFAULT
...
>>> m.side_effect = side_effect
>>> m()
3

```

To remove a [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect"), and return to the default behaviour, set the `side_effect` to `None`:
Copy```
>>> m = MagicMock(return_value=6)
>>> def side_effect(*args, **kwargs):
...     return 3
...
>>> m.side_effect = side_effect
>>> m()
3
>>> m.side_effect = None
>>> m()
6

```

The [`side_effect`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect "unittest.mock.Mock.side_effect") can also be any iterable object. Repeated calls to the mock will return values from the iterable (until the iterable is exhausted and a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") is raised):
Copy```
>>> m = MagicMock(side_effect=[1, 2, 3])
>>> m()
1
>>> m()
2
>>> m()
3
>>> m()
Traceback (most recent call last):
  ...
StopIteration

```

If any members of the iterable are exceptions they will be raised instead of returned:
Copy```
>>> iterable = (33, ValueError, 66)
>>> m = MagicMock(side_effect=iterable)
>>> m()
33
>>> m()
Traceback (most recent call last):
 ...
ValueError
>>> m()
66

```

### Deleting Attributes[¶](https://docs.python.org/3/library/unittest.mock.html#deleting-attributes "Link to this heading")
Mock objects create attributes on demand. This allows them to pretend to be objects of any type.
You may want a mock object to return `False` to a [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") call, or raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") when an attribute is fetched. You can do this by providing an object as a `spec` for a mock, but that isn’t always convenient.
You “block” attributes by deleting them. Once deleted, accessing an attribute will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
Copy```
>>> mock = MagicMock()
>>> hasattr(mock, 'm')
True
>>> del mock.m
>>> hasattr(mock, 'm')
False
>>> del mock.f
>>> mock.f
Traceback (most recent call last):
    ...
AttributeError: f

```

### Mock names and the name attribute[¶](https://docs.python.org/3/library/unittest.mock.html#mock-names-and-the-name-attribute "Link to this heading")
Since “name” is an argument to the [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") constructor, if you want your mock object to have a “name” attribute you can’t just pass it in at creation time. There are two alternatives. One option is to use [`configure_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.configure_mock "unittest.mock.Mock.configure_mock"):
Copy```
>>> mock = MagicMock()
>>> mock.configure_mock(name='my_name')
>>> mock.name
'my_name'

```

A simpler option is to simply set the “name” attribute after mock creation:
Copy```
>>> mock = MagicMock()
>>> mock.name = "foo"

```

### Attaching Mocks as Attributes[¶](https://docs.python.org/3/library/unittest.mock.html#attaching-mocks-as-attributes "Link to this heading")
When you attach a mock as an attribute of another mock (or as the return value) it becomes a “child” of that mock. Calls to the child are recorded in the [`method_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.method_calls "unittest.mock.Mock.method_calls") and [`mock_calls`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.mock_calls "unittest.mock.Mock.mock_calls") attributes of the parent. This is useful for configuring child mocks and then attaching them to the parent, or for attaching mocks to a parent that records all calls to the children and allows you to make assertions about the order of calls between mocks:
Copy```
>>> parent = MagicMock()
>>> child1 = MagicMock(return_value=None)
>>> child2 = MagicMock(return_value=None)
>>> parent.child1 = child1
>>> parent.child2 = child2
>>> child1(1)
>>> child2(2)
>>> parent.mock_calls
[call.child1(1), call.child2(2)]

```

The exception to this is if the mock has a name. This allows you to prevent the “parenting” if for some reason you don’t want it to happen.
Copy```
>>> mock = MagicMock()
>>> not_a_child = MagicMock(name='not-a-child')
>>> mock.attribute = not_a_child
>>> mock.attribute()
<MagicMock name='not-a-child()' id='...'>
>>> mock.mock_calls
[]

```

Mocks created for you by [`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") are automatically given names. To attach mocks that have names to a parent you use the [`attach_mock()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.attach_mock "unittest.mock.Mock.attach_mock") method:
Copy```
>>> thing1 = object()
>>> thing2 = object()
>>> parent = MagicMock()
>>> with patch('__main__.thing1', return_value=None) as child1:
...     with patch('__main__.thing2', return_value=None) as child2:
...         parent.attach_mock(child1, 'child1')
...         parent.attach_mock(child2, 'child2')
...         child1('one')
...         child2('two')
...
>>> parent.mock_calls
[call.child1('one'), call.child2('two')]

```

[[1](https://docs.python.org/3/library/unittest.mock.html#id1)]
The only exceptions are magic methods and attributes (those that have leading and trailing double underscores). Mock doesn’t create these but instead raises an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError"). This is because the interpreter will often implicitly request these methods, and gets _very_ confused to get a new Mock object when it expects a magic method. If you need magic method support see [magic methods](https://docs.python.org/3/library/unittest.mock.html#magic-methods).
