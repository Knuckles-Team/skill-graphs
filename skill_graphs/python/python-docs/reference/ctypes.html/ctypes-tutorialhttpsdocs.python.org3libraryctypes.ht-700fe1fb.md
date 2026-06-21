The field type must be a `ctypes` type like [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int"), or any other derived `ctypes` type: structure, union, array, pointer.
Here is a simple example of a POINT structure, which contains two integers named _x_ and _y_ , and also shows how to initialize a structure in the constructor:
Copy```
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = [("x", c_int),
...                 ("y", c_int)]
...
>>> point = POINT(10, 20)
>>> print(point.x, point.y)
10 20
>>> point = POINT(y=5)
>>> print(point.x, point.y)
0 5
>>> POINT(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: too many initializers
>>>

```

You can, however, build much more complicated structures. A structure can itself contain other structures by using a structure as a field type.
Here is a RECT structure which contains two POINTs named _upperleft_ and _lowerright_ :
Copy```
>>> class RECT(Structure):
...     _fields_ = [("upperleft", POINT),
...                 ("lowerright", POINT)]
...
>>> rc = RECT(point)
>>> print(rc.upperleft.x, rc.upperleft.y)
0 5
>>> print(rc.lowerright.x, rc.lowerright.y)
0 0
>>>

```

Nested structures can also be initialized in the constructor in several ways:
Copy```
>>> r = RECT(POINT(1, 2), POINT(3, 4))
>>> r = RECT((1, 2), (3, 4))

```

Field [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)s can be retrieved from the _class_ , they are useful for debugging because they can provide useful information. See [`CField`](https://docs.python.org/3/library/ctypes.html#ctypes.CField "ctypes.CField"):
Copy```
>>> POINT.x
<ctypes.CField 'x' type=c_int, ofs=0, size=4>
>>> POINT.y
<ctypes.CField 'y' type=c_int, ofs=4, size=4>
>>>

```

Warning
`ctypes` does not support passing unions or structures with bit-fields to functions by value. While this may work on 32-bit x86, it’s not guaranteed by the library to work in the general case. Unions and structures with bit-fields should always be passed to functions by pointer.
### Structure/union layout, alignment and byte order[¶](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order "Link to this heading")
By default, Structure and Union fields are laid out in the same way the C compiler does it. It is possible to override this behavior entirely by specifying a [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_") class attribute in the subclass definition; see the attribute documentation for details.
It is possible to specify the maximum alignment for the fields and/or for the structure itself by setting the class attributes [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_") and/or [`_align_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._align_ "ctypes.Structure._align_"), respectively. See the attribute documentation for details.
`ctypes` uses the native byte order for Structures and Unions. To build structures with non-native byte order, you can use one of the [`BigEndianStructure`](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianStructure "ctypes.BigEndianStructure"), [`LittleEndianStructure`](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianStructure "ctypes.LittleEndianStructure"), [`BigEndianUnion`](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianUnion "ctypes.BigEndianUnion"), and [`LittleEndianUnion`](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianUnion "ctypes.LittleEndianUnion") base classes. These classes cannot contain pointer fields.
### Bit fields in structures and unions[¶](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions "Link to this heading")
It is possible to create structures and unions containing bit fields. Bit fields are only possible for integer fields, the bit width is specified as the third item in the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") tuples:
Copy```
>>> class Int(Structure):
...     _fields_ = [("first_16", c_int, 16),
...                 ("second_16", c_int, 16)]
...
>>> print(Int.first_16)
<ctypes.CField 'first_16' type=c_int, ofs=0, bit_size=16, bit_offset=0>
>>> print(Int.second_16)
<ctypes.CField 'second_16' type=c_int, ofs=0, bit_size=16, bit_offset=16>

```

It is important to note that bit field allocation and layout in memory are not defined as a C standard; their implementation is compiler-specific. By default, Python will attempt to match the behavior of a “native” compiler for the current platform. See the [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_") attribute for details on the default behavior and how to change it.
### Arrays[¶](https://docs.python.org/3/library/ctypes.html#arrays "Link to this heading")
Arrays are sequences, containing a fixed number of instances of the same type.
The recommended way to create array types is by multiplying a data type with a positive integer:
Copy```
TenPointsArrayType = POINT * 10

```

Here is an example of a somewhat artificial data type, a structure containing 4 POINTs among other stuff:
Copy```
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = ("x", c_int), ("y", c_int)
...
>>> class MyStruct(Structure):
...     _fields_ = [("a", c_int),
...                 ("b", c_float),
...                 ("point_array", POINT * 4)]
>>>
>>> print(len(MyStruct().point_array))
4
>>>

```

Instances are created in the usual way, by calling the class:
Copy```
arr = TenPointsArrayType()
for pt in arr:
    print(pt.x, pt.y)

```

The above code print a series of `0 0` lines, because the array contents is initialized to zeros.
Initializers of the correct type can also be specified:
Copy```
>>> from ctypes import *
>>> TenIntegers = c_int * 10
>>> ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> print(ii)
<c_long_Array_10 object at 0x...>
>>> for i in ii: print(i, end=" ")
...
1 2 3 4 5 6 7 8 9 10
>>>

```

### Pointers[¶](https://docs.python.org/3/library/ctypes.html#pointers "Link to this heading")
Pointer instances are created by calling the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer") function on a `ctypes` type:
Copy```
>>> from ctypes import *
>>> i = c_int(42)
>>> pi = pointer(i)
>>>

```

Pointer instances have a [`contents`](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer.contents "ctypes._Pointer.contents") attribute which returns the object to which the pointer points, the `i` object above:
Copy```
>>> pi.contents
c_long(42)
>>>

```

Note that `ctypes` does not have OOR (original object return), it constructs a new, equivalent object each time you retrieve an attribute:
Copy```
>>> pi.contents is i
False
>>> pi.contents is pi.contents
False
>>>

```

Assigning another [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") instance to the pointer’s contents attribute would cause the pointer to point to the memory location where this is stored:
Copy```
>>> i = c_int(99)
>>> pi.contents = i
>>> pi.contents
c_long(99)
>>>

```

Pointer instances can also be indexed with integers:
Copy```
>>> pi[0]
99
>>>

```

Assigning to an integer index changes the pointed to value:
Copy```
>>> print(i)
c_long(99)
>>> pi[0] = 22
>>> print(i)
c_long(22)
>>>

```

It is also possible to use indexes different from 0, but you must know what you’re doing, just as in C: You can access or change arbitrary memory locations. Generally you only use this feature if you receive a pointer from a C function, and you _know_ that the pointer actually points to an array instead of a single item.
Behind the scenes, the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer") function does more than simply create pointer instances, it has to create pointer _types_ first. This is done with the [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER") function, which accepts any `ctypes` type, and returns a new type:
Copy```
>>> PI = POINTER(c_int)
>>> PI
<class 'ctypes.LP_c_long'>
>>> PI(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected c_long instead of int
>>> PI(c_int(42))
<ctypes.LP_c_long object at 0x...>
>>>

```

Calling the pointer type without an argument creates a `NULL` pointer. `NULL` pointers have a `False` boolean value:
Copy```
>>> null_ptr = POINTER(c_int)()
>>> print(bool(null_ptr))
False
>>>

```

`ctypes` checks for `NULL` when dereferencing pointers (but dereferencing invalid non-`NULL` pointers would crash Python):
Copy```
>>> null_ptr[0]
Traceback (most recent call last):
    ....
ValueError: NULL pointer access
>>>

>>> null_ptr[0] = 1234
Traceback (most recent call last):
    ....
ValueError: NULL pointer access
>>>

```

### Thread safety without the GIL[¶](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil "Link to this heading")
From Python 3.13 onward, the [GIL](https://docs.python.org/3/glossary.html#term-GIL) can be disabled on the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build). In ctypes, reads and writes to a single object concurrently is safe, but not across multiple objects:
> Copy```
>>> number = c_int(42)
>>> pointer_a = pointer(number)
>>> pointer_b = pointer(number)

```

In the above, it’s only safe for one object to read and write to the address at once if the GIL is disabled. So, `pointer_a` can be shared and written to across multiple threads, but only if `pointer_b` is not also attempting to do the same. If this is an issue, consider using a [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") to synchronize access to memory:
> Copy```
>>> import threading
>>> lock = threading.Lock()
>>> # Thread 1
>>> with lock:
...    pointer_a.contents = 24
>>> # Thread 2
>>> with lock:
...    pointer_b.contents = 42

```

### Type conversions[¶](https://docs.python.org/3/library/ctypes.html#type-conversions "Link to this heading")
Usually, ctypes does strict type checking. This means, if you have `POINTER(c_int)` in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes") list of a function or as the type of a member field in a structure definition, only instances of exactly the same type are accepted. There are some exceptions to this rule, where ctypes accepts other objects. For example, you can pass compatible array instances instead of pointer types. So, for `POINTER(c_int)`, ctypes accepts an array of c_int:
Copy```
>>> class Bar(Structure):
...     _fields_ = [("count", c_int), ("values", POINTER(c_int))]
...
>>> bar = Bar()
>>> bar.values = (c_int * 3)(1, 2, 3)
>>> bar.count = 3
>>> for i in range(bar.count):
...     print(bar.values[i])
...
1
2
3
>>>

```

In addition, if a function argument is explicitly declared to be a pointer type (such as `POINTER(c_int)`) in [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes"), an object of the pointed type (`c_int` in this case) can be passed to the function. ctypes will apply the required [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref") conversion in this case automatically.
To set a POINTER type field to `NULL`, you can assign `None`:
Copy```
>>> bar.values = None
>>>

```

Sometimes you have instances of incompatible types. In C, you can cast one type into another type. `ctypes` provides a [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") function which can be used in the same way. The `Bar` structure defined above accepts `POINTER(c_int)` pointers or [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") arrays for its `values` field, but not instances of other types:
Copy```
>>> bar.values = (c_byte * 4)()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: incompatible types, c_byte_Array_4 instance instead of LP_c_long instance
>>>

```

For these cases, the [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") function is handy.
The [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") function can be used to cast a ctypes instance into a pointer to a different ctypes data type. `cast()` takes two parameters, a ctypes object that is or can be converted to a pointer of some kind, and a ctypes pointer type. It returns an instance of the second argument, which references the same memory block as the first argument:
Copy```
>>> a = (c_byte * 4)()
>>> cast(a, POINTER(c_int))
<ctypes.LP_c_long object at ...>
>>>

```

So, [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast") can be used to assign to the `values` field of `Bar` the structure:
Copy```
>>> bar = Bar()
>>> bar.values = cast((c_byte * 4)(), POINTER(c_int))
>>> print(bar.values[0])
0
>>>

```

### Incomplete Types[¶](https://docs.python.org/3/library/ctypes.html#incomplete-types "Link to this heading")
_Incomplete Types_ are structures, unions or arrays whose members are not yet specified. In C, they are specified by forward declarations, which are defined later:
Copy```
struct cell; /* forward declaration */

struct cell {
    char *name;
    struct cell *next;
};

```

The straightforward translation into ctypes code would be this, but it does not work:
Copy```
>>> class cell(Structure):
...     _fields_ = [("name", c_char_p),
...                 ("next", POINTER(cell))]
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in cell
NameError: name 'cell' is not defined
>>>

```

because the new `class cell` is not available in the class statement itself. In `ctypes`, we can define the `cell` class and set the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") attribute later, after the class statement:
Copy```
>>> from ctypes import *
>>> class cell(Structure):
...     pass
...
>>> cell._fields_ = [("name", c_char_p),
...                  ("next", POINTER(cell))]
>>>

```

Let’s try it. We create two instances of `cell`, and let them point to each other, and finally follow the pointer chain a few times:
Copy```
>>> c1 = cell()
>>> c1.name = b"foo"
>>> c2 = cell()
>>> c2.name = b"bar"
>>> c1.next = pointer(c2)
>>> c2.next = pointer(c1)
>>> p = c1
>>> for i in range(8):
...     print(p.name, end=" ")
...     p = p.next[0]
...
foo bar foo bar foo bar foo bar
>>>

```

### Callback functions[¶](https://docs.python.org/3/library/ctypes.html#callback-functions "Link to this heading")
`ctypes` allows creating C callable function pointers from Python callables. These are sometimes called _callback functions_.
First, you must create a class for the callback function. The class knows the calling convention, the return type, and the number and types of arguments this function will receive.
The [`CFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "ctypes.CFUNCTYPE") factory function creates types for callback functions using the `cdecl` calling convention. On Windows, the [`WINFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.WINFUNCTYPE "ctypes.WINFUNCTYPE") factory function creates types for callback functions using the `stdcall` calling convention.
Both of these factory functions are called with the result type as first argument, and the callback functions expected argument types as the remaining arguments.
I will present an example here which uses the standard C library’s `qsort()` function, that is used to sort items with the help of a callback function. `qsort()` will be used to sort an array of integers:
Copy```
>>> IntArray5 = c_int * 5
>>> ia = IntArray5(5, 1, 7, 33, 99)
>>> qsort = libc.qsort
>>> qsort.restype = None
>>>

```

`qsort()` must be called with a pointer to the data to sort, the number of items in the data array, the size of one item, and a pointer to the comparison function, the callback. The callback will then be called with two pointers to items, and it must return a negative integer if the first item is smaller than the second, a zero if they are equal, and a positive integer otherwise.
So our callback function receives pointers to integers, and must return an integer. First we create the `type` for the callback function:
Copy```
>>> CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
>>>

```

To get started, here is a simple callback that shows the values it gets passed:
Copy```
>>> def py_cmp_func(a, b):
...     print("py_cmp_func", a[0], b[0])
...     return 0
...
>>> cmp_func = CMPFUNC(py_cmp_func)
>>>

```

The result:
Copy```
>>> qsort(ia, len(ia), sizeof(c_int), cmp_func)
py_cmp_func 5 1
py_cmp_func 33 99
py_cmp_func 7 33
py_cmp_func 5 7
py_cmp_func 1 7
>>>

```

Now we can actually compare the two items and return a useful result:
Copy```
>>> def py_cmp_func(a, b):
...     print("py_cmp_func", a[0], b[0])
...     return a[0] - b[0]
...
>>>
>>> qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))
py_cmp_func 5 1
py_cmp_func 33 99
py_cmp_func 7 33
py_cmp_func 1 7
py_cmp_func 5 7
>>>

```

As we can easily check, our array is sorted now:
Copy```
>>> for i in ia: print(i, end=" ")
...
1 5 7 33 99
>>>

```

The function factories can be used as decorator factories, so we may as well write:
Copy```
>>> @CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
... def py_cmp_func(a, b):
...     print("py_cmp_func", a[0], b[0])
...     return a[0] - b[0]
...
>>> qsort(ia, len(ia), sizeof(c_int), py_cmp_func)
py_cmp_func 5 1
py_cmp_func 33 99
py_cmp_func 7 33
py_cmp_func 1 7
py_cmp_func 5 7
>>>

```

Note
Make sure you keep references to [`CFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "ctypes.CFUNCTYPE") objects as long as they are used from C code. `ctypes` doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made.
Also, note that if the callback function is called in a thread created outside of Python’s control (e.g. by the foreign code that calls the callback), ctypes creates a new dummy Python thread on every invocation. This behavior is correct for most purposes, but it means that values stored with [`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") will _not_ survive across different callbacks, even when those calls are made from the same C thread.
### Accessing values exported from dlls[¶](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls "Link to this heading")
Some shared libraries not only export functions, they also export variables. An example in the Python library itself is the [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version"), Python runtime version number encoded in a single constant integer.
`ctypes` can access values like this with the [`in_dll()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.in_dll "ctypes._CData.in_dll") class methods of the type. _pythonapi_ is a predefined symbol giving access to the Python C api:
Copy```
>>> version = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_Version")
>>> print(hex(version.value))
0x30c00a0

```

An extended example which also demonstrates the use of pointers accesses the [`PyImport_FrozenModules`](https://docs.python.org/3/c-api/import.html#c.PyImport_FrozenModules "PyImport_FrozenModules") pointer exported by Python.
Quoting the docs for that value:
> This pointer is initialized to point to an array of [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen") records, terminated by one whose members are all `NULL` or zero. When a frozen module is imported, it is searched in this table. Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.
So manipulating this pointer could even prove useful. To restrict the example size, we show only how this table can be read with `ctypes`:
Copy```
>>> from ctypes import *
>>>
>>> class struct_frozen(Structure):
...     _fields_ = [("name", c_char_p),
...                 ("code", POINTER(c_ubyte)),
...                 ("size", c_int),
...                 ("get_code", POINTER(c_ubyte)),  # Function pointer
...                ]
...
>>>

```

We have defined the [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen") data type, so we can get the pointer to the table:
Copy```
>>> FrozenTable = POINTER(struct_frozen)
>>> table = FrozenTable.in_dll(pythonapi, "_PyImport_FrozenBootstrap")
>>>

```

Since `table` is a `pointer` to the array of `struct_frozen` records, we can iterate over it, but we just have to make sure that our loop terminates, because pointers have no size. Sooner or later it would probably crash with an access violation or whatever, so it’s better to break out of the loop when we hit the `NULL` entry:
Copy```
>>> for item in table:
...     if item.name is None:
...         break
...     print(item.name.decode("ascii"), item.size)
...
_frozen_importlib 31764
_frozen_importlib_external 41499
zipimport 12345
>>>

```

The fact that standard Python has a frozen module and a frozen package (indicated by the negative `size` member) is not well known, it is only used for testing. Try it out with `import __hello__` for example.
### Surprises[¶](https://docs.python.org/3/library/ctypes.html#surprises "Link to this heading")
There are some edges in `ctypes` where you might expect something other than what actually happens.
Consider the following example:
Copy```
>>> from ctypes import *
>>> class POINT(Structure):
...     _fields_ = ("x", c_int), ("y", c_int)
...
>>> class RECT(Structure):
...     _fields_ = ("a", POINT), ("b", POINT)
...
>>> p1 = POINT(1, 2)
>>> p2 = POINT(3, 4)
>>> rc = RECT(p1, p2)
>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
1 2 3 4
>>> # now swap the two points
>>> rc.a, rc.b = rc.b, rc.a
>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
3 4 3 4
>>>

```

Hm. We certainly expected the last statement to print `3 4 1 2`. What happened? Here are the steps of the `rc.a, rc.b = rc.b, rc.a` line above:
Copy```
>>> temp0, temp1 = rc.b, rc.a
>>> rc.a = temp0
>>> rc.b = temp1
>>>

```

Note that `temp0` and `temp1` are objects still using the internal buffer of the `rc` object above. So executing `rc.a = temp0` copies the buffer contents of `temp0` into `rc` ‘s buffer. This, in turn, changes the contents of `temp1`. So, the last assignment `rc.b = temp1`, doesn’t have the expected effect.
Keep in mind that retrieving sub-objects from Structure, Unions, and Arrays doesn’t _copy_ the sub-object, instead it retrieves a wrapper object accessing the root-object’s underlying buffer.
Another example that may behave differently from what one would expect is this:
Copy```
>>> s = c_char_p()
>>> s.value = b"abc def ghi"
>>> s.value
b'abc def ghi'
>>> s.value is s.value
False
>>>

```

Note
Objects instantiated from [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") can only have their value set to bytes or integers.
Why is it printing `False`? ctypes instances are objects containing a memory block plus some [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)s accessing the contents of the memory. Storing a Python object in the memory block does not store the object itself, instead the `contents` of the object is stored. Accessing the contents again constructs a new Python object each time!
### Variable-sized data types[¶](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types "Link to this heading")
`ctypes` provides some support for variable-sized arrays and structures.
The [`resize()`](https://docs.python.org/3/library/ctypes.html#ctypes.resize "ctypes.resize") function can be used to resize the memory buffer of an existing ctypes object. The function takes the object as first argument, and the requested size in bytes as the second argument. The memory block cannot be made smaller than the natural memory block specified by the objects type, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if this is tried:
Copy```
>>> short_array = (c_short * 4)()
>>> print(sizeof(short_array))
8
>>> resize(short_array, 4)
Traceback (most recent call last):
    ...
ValueError: minimum size is 8
>>> resize(short_array, 32)
>>> sizeof(short_array)
32
>>> sizeof(type(short_array))
8
>>>

```

This is nice and fine, but how would one access the additional elements contained in this array? Since the type still only knows about 4 elements, we get errors accessing other elements:
Copy```
>>> short_array[:]
[0, 0, 0, 0]
>>> short_array[7]
Traceback (most recent call last):
    ...
IndexError: invalid index
>>>

```

Another way to use variable-sized data types with `ctypes` is to use the dynamic nature of Python, and (re-)define the data type after the required size is already known, on a case by case basis.
