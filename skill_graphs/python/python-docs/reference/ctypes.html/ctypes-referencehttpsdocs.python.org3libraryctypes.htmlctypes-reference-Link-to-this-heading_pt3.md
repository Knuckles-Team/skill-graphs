These are the fundamental ctypes data types:

_class_ ctypes.c_byte[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_byte "Link to this definition")

Represents the C signedchar datatype, and interprets the value as small integer. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_char[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "Link to this definition")

Represents the C char datatype, and interprets the value as a single character. The constructor accepts an optional string initializer, the length of the string must be exactly one character.

_class_ ctypes.c_char_p[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "Link to this definition")

Represents the C char* datatype when it points to a zero-terminated string. For a general character pointer that may also point to binary data, `POINTER(c_char)` must be used. The constructor accepts an integer address, or a bytes object.

_class_ ctypes.c_double[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "Link to this definition")

Represents the C double datatype. The constructor accepts an optional float initializer.

_class_ ctypes.c_longdouble[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble "Link to this definition")

Represents the C longdouble datatype. The constructor accepts an optional float initializer. On platforms where `sizeof(long double) == sizeof(double)` it is an alias to [`c_double`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "ctypes.c_double").

_class_ ctypes.c_float[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_float "Link to this definition")

Represents the C float datatype. The constructor accepts an optional float initializer.

_class_ ctypes.c_double_complex[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_double_complex "Link to this definition")

Represents the C doublecomplex datatype, if available. The constructor accepts an optional [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") initializer.
Added in version 3.14.

_class_ ctypes.c_float_complex[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_float_complex "Link to this definition")

Represents the C floatcomplex datatype, if available. The constructor accepts an optional [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") initializer.
Added in version 3.14.

_class_ ctypes.c_longdouble_complex[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble_complex "Link to this definition")

Represents the C longdoublecomplex datatype, if available. The constructor accepts an optional [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") initializer.
Added in version 3.14.

_class_ ctypes.c_int[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "Link to this definition")

Represents the C signedint datatype. The constructor accepts an optional integer initializer; no overflow checking is done. On platforms where `sizeof(int) == sizeof(long)` it is an alias to [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long").

_class_ ctypes.c_int8[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int8 "Link to this definition")

Represents the C 8-bit signedint datatype. It is an alias for [`c_byte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_byte "ctypes.c_byte").

_class_ ctypes.c_int16[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int16 "Link to this definition")

Represents the C 16-bit signedint datatype. Usually an alias for [`c_short`](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "ctypes.c_short").

_class_ ctypes.c_int32[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "Link to this definition")

Represents the C 32-bit signedint datatype. Usually an alias for [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int").

_class_ ctypes.c_int64[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "Link to this definition")

Represents the C 64-bit signedint datatype. Usually an alias for [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong").

_class_ ctypes.c_long[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "Link to this definition")

Represents the C signedlong datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_longlong[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "Link to this definition")

Represents the C signedlonglong datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_short[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "Link to this definition")

Represents the C signedshort datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_size_t[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_size_t "Link to this definition")

Represents the C `size_t` datatype.

_class_ ctypes.c_ssize_t[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ssize_t "Link to this definition")

Represents the C `ssize_t` datatype.
Added in version 3.2.

_class_ ctypes.c_time_t[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_time_t "Link to this definition")

Represents the C `time_t` datatype.
Added in version 3.12.

_class_ ctypes.c_ubyte[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "Link to this definition")

Represents the C unsignedchar datatype, it interprets the value as small integer. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_uint[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "Link to this definition")

Represents the C unsignedint datatype. The constructor accepts an optional integer initializer; no overflow checking is done. On platforms where `sizeof(int) == sizeof(long)` it is an alias for [`c_ulong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "ctypes.c_ulong").

_class_ ctypes.c_uint8[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint8 "Link to this definition")

Represents the C 8-bit unsignedint datatype. It is an alias for [`c_ubyte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "ctypes.c_ubyte").

_class_ ctypes.c_uint16[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint16 "Link to this definition")

Represents the C 16-bit unsignedint datatype. Usually an alias for [`c_ushort`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "ctypes.c_ushort").

_class_ ctypes.c_uint32[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint32 "Link to this definition")

Represents the C 32-bit unsignedint datatype. Usually an alias for [`c_uint`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "ctypes.c_uint").

_class_ ctypes.c_uint64[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint64 "Link to this definition")

Represents the C 64-bit unsignedint datatype. Usually an alias for [`c_ulonglong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "ctypes.c_ulonglong").

_class_ ctypes.c_ulong[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "Link to this definition")

Represents the C unsignedlong datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_ulonglong[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "Link to this definition")

Represents the C unsignedlonglong datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_ushort[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "Link to this definition")

Represents the C unsignedshort datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

_class_ ctypes.c_void_p[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "Link to this definition")

Represents the C void* type. The value is represented as integer. The constructor accepts an optional integer initializer.

_class_ ctypes.c_wchar[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "Link to this definition")

Represents the C `wchar_t` datatype, and interprets the value as a single character unicode string. The constructor accepts an optional string initializer, the length of the string must be exactly one character.

_class_ ctypes.c_wchar_p[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "Link to this definition")

Represents the C wchar_t* datatype, which must be a pointer to a zero-terminated wide character string. The constructor accepts an integer address, or a string.

_class_ ctypes.c_bool[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_bool "Link to this definition")

Represent the C bool datatype (more accurately, _Bool from C99). Its value can be `True` or `False`, and the constructor accepts any object that has a truth value.

_class_ ctypes.HRESULT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.HRESULT "Link to this definition")

Represents a `HRESULT` value, which contains success or error information for a function or method call.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows

_class_ ctypes.py_object[¶](https://docs.python.org/3/library/ctypes.html#ctypes.py_object "Link to this definition")

Represents the C [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")* datatype. Calling this without an argument creates a `NULL` PyObject* pointer.
Changed in version 3.14: `py_object` is now a [generic type](https://docs.python.org/3/glossary.html#term-generic-type).
The `ctypes.wintypes` module provides quite some other Windows specific data types, for example `HWND`, `WPARAM`, or `DWORD`. Some useful structures like `MSG` or `RECT` are also defined.
### Structured data types[¶](https://docs.python.org/3/library/ctypes.html#structured-data-types "Link to this heading")

_class_ ctypes.Union(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Union "Link to this definition")

Abstract base class for unions in native byte order.
Unions share common attributes and behavior with structures; see [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure") documentation for details.

_class_ ctypes.BigEndianUnion(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianUnion "Link to this definition")

Abstract base class for unions in _big endian_ byte order.
Added in version 3.11.

_class_ ctypes.LittleEndianUnion(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianUnion "Link to this definition")

Abstract base class for unions in _little endian_ byte order.
Added in version 3.11.

_class_ ctypes.BigEndianStructure(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianStructure "Link to this definition")

Abstract base class for structures in _big endian_ byte order.

_class_ ctypes.LittleEndianStructure(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianStructure "Link to this definition")

Abstract base class for structures in _little endian_ byte order.
Structures and unions with non-native byte order cannot contain pointer type fields, or any other data types containing pointer type fields.

_class_ ctypes.Structure(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "Link to this definition")

Abstract base class for structures in _native_ byte order.
Concrete structure and union types must be created by subclassing one of these types, and at least define a [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") class variable. `ctypes` will create [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)s which allow reading and writing the fields by direct attribute accesses. These are the

_fields_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "Link to this definition")

A sequence defining the structure fields. The items must be 2-tuples or 3-tuples. The first item is the name of the field, the second item specifies the type of the field; it can be any ctypes data type.
For integer type fields like [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int"), a third optional item can be given. It must be a small positive integer defining the bit width of the field.
Field names must be unique within one structure or union. This is not checked, only one field can be accessed when names are repeated.
It is possible to define the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") class variable _after_ the class statement that defines the Structure subclass, this allows creating data types that directly or indirectly reference themselves:
Copy```
class List(Structure):
    pass
List._fields_ = [("pnext", POINTER(List)),
                 ...
                ]

```

The `_fields_` class variable can only be set once. Later assignments will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError").
Additionally, the `_fields_` class variable must be defined before the structure or union type is first used: an instance or subclass is created, [`sizeof()`](https://docs.python.org/3/library/ctypes.html#ctypes.sizeof "ctypes.sizeof") is called on it, and so on. Later assignments to `_fields_` will raise an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError"). If `_fields_` has not been set before such use, the structure or union will have no own fields, as if `_fields_` was empty.
Sub-subclasses of structure types inherit the fields of the base class plus the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") defined in the sub-subclass, if any.

_pack_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "Link to this definition")

An optional small integer that allows overriding the alignment of structure fields in the instance.
This is only implemented for the MSVC-compatible memory layout (see [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")).
Setting `_pack_` to 0 is the same as not setting it at all. Otherwise, the value must be a positive power of two. The effect is equivalent to `#pragma pack(N)` in C, except `ctypes` may allow larger _n_ than what the compiler accepts.
`_pack_` must already be defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") is assigned, otherwise it will have no effect.
Deprecated since version 3.14, will be removed in version 3.19: For historical reasons, if `_pack_` is non-zero, the MSVC-compatible layout will be used by default. On non-Windows platforms, this default is deprecated and is slated to become an error in Python 3.19. If it is intended, set [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_") to `'ms'` explicitly.

_align_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._align_ "Link to this definition")

An optional small integer that allows increasing the alignment of the structure when being packed or unpacked to/from memory.
The value must not be negative. The effect is equivalent to `__attribute__((aligned(N)))` on GCC or `#pragma align(N)` on MSVC, except `ctypes` may allow values that the compiler would reject.
`_align_` can only _increase_ a structure’s alignment requirements. Setting it to 0 or 1 has no effect.
Using values that are not powers of two is discouraged and may lead to surprising behavior.
`_align_` must already be defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") is assigned, otherwise it will have no effect.
Added in version 3.13.

_layout_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "Link to this definition")

An optional string naming the struct/union layout. It can currently be set to:
  * `"ms"`: the layout used by the Microsoft compiler (MSVC). On GCC and Clang, this layout can be selected with `__attribute__((ms_struct))`.
  * `"gcc-sysv"`: the layout used by GCC with the System V or “SysV-like” data model, as used on Linux and macOS. With this layout, [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_") must be unset or zero.


If not set explicitly, `ctypes` will use a default that matches the platform conventions. This default may change in future Python releases (for example, when a new platform gains official support, or when a difference between similar platforms is found). Currently the default will be:
  * On Windows: `"ms"`
  * When [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_") is specified: `"ms"`. (This is deprecated; see `_pack_` documentation.)
  * Otherwise: `"gcc-sysv"`


`_layout_` must already be defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") is assigned, otherwise it will have no effect.
Added in version 3.14.

_anonymous_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._anonymous_ "Link to this definition")

An optional sequence that lists the names of unnamed (anonymous) fields. [`_anonymous_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._anonymous_ "ctypes.Structure._anonymous_") must be already defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") is assigned, otherwise it will have no effect.
The fields listed in this variable must be structure or union type fields. `ctypes` will create descriptors in the structure type that allows accessing the nested fields directly, without the need to create the structure or union field.
Here is an example type (Windows):
Copy```
class _U(Union):
    _fields_ = [("lptdesc", POINTER(TYPEDESC)),
                ("lpadesc", POINTER(ARRAYDESC)),
                ("hreftype", HREFTYPE)]

class TYPEDESC(Structure):
    _anonymous_ = ("u",)
    _fields_ = [("u", _U),
                ("vt", VARTYPE)]

```

The `TYPEDESC` structure describes a COM data type, the `vt` field specifies which one of the union fields is valid. Since the `u` field is defined as anonymous field, it is now possible to access the members directly off the TYPEDESC instance. `td.lptdesc` and `td.u.lptdesc` are equivalent, but the former is faster since it does not need to create a temporary union instance:
Copy```
td = TYPEDESC()
td.vt = VT_PTR
td.lptdesc = POINTER(some_type)
td.u.lptdesc = POINTER(some_type)

```

It is possible to define sub-subclasses of structures, they inherit the fields of the base class. If the subclass definition has a separate [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_") variable, the fields specified in this are appended to the fields of the base class.
Structure and union constructors accept both positional and keyword arguments. Positional arguments are used to initialize member fields in the same order as they are appear in [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_"). Keyword arguments in the constructor are interpreted as attribute assignments, so they will initialize `_fields_` with the same name, or create new attributes for names not present in `_fields_`.

_class_ ctypes.CField(_* args_, _** kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField "Link to this definition")

Descriptor for fields of a [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure") and [`Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "ctypes.Union"). For example:
Copy```
>>> class Color(Structure):
...     _fields_ = (
...         ('red', c_uint8),
...         ('green', c_uint8),
...         ('blue', c_uint8),
...         ('intense', c_bool, 1),
...         ('blinking', c_bool, 1),
...    )
...
>>> Color.red
<ctypes.CField 'red' type=c_ubyte, ofs=0, size=1>
>>> Color.green.type
<class 'ctypes.c_ubyte'>
>>> Color.blue.byte_offset
2
>>> Color.intense
<ctypes.CField 'intense' type=c_bool, ofs=3, bit_size=1, bit_offset=0>
>>> Color.blinking.bit_offset
1

```

All attributes are read-only.
`CField` objects are created via [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_"); do not instantiate the class directly.
Added in version 3.14: Previously, descriptors only had `offset` and `size` attributes and a readable string representation; the `CField` class was not available directly.

name[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.name "Link to this definition")

Name of the field, as a string.

type[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.type "Link to this definition")

Type of the field, as a [ctypes class](https://docs.python.org/3/library/ctypes.html#ctypes-data-types).

offset[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.offset "Link to this definition")


byte_offset[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_offset "Link to this definition")

Offset of the field, in bytes.
For bitfields, this is the offset of the underlying byte-aligned _storage unit_ ; see [`bit_offset`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_offset "ctypes.CField.bit_offset").

byte_size[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_size "Link to this definition")

Size of the field, in bytes.
For bitfields, this is the size of the underlying _storage unit_. Typically, it has the same size as the bitfield’s type.

size[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.size "Link to this definition")

For non-bitfields, equivalent to [`byte_size`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_size "ctypes.CField.byte_size").
For bitfields, this contains a backwards-compatible bit-packed value that combines [`bit_size`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_size "ctypes.CField.bit_size") and [`bit_offset`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_offset "ctypes.CField.bit_offset"). Prefer using the explicit attributes instead.

is_bitfield[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.is_bitfield "Link to this definition")

True if this is a bitfield.

bit_offset[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_offset "Link to this definition")


bit_size[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_size "Link to this definition")

The location of a bitfield within its _storage unit_ , that is, within [`byte_size`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_size "ctypes.CField.byte_size") bytes of memory starting at [`byte_offset`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_offset "ctypes.CField.byte_offset").
To get the field’s value, read the storage unit as an integer, [shift left](https://docs.python.org/3/reference/expressions.html#shifting) by `bit_offset` and take the `bit_size` least significant bits.
For non-bitfields, `bit_offset` is zero and `bit_size` is equal to `byte_size * 8`.

is_anonymous[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.is_anonymous "Link to this definition")

True if this field is anonymous, that is, it contains nested sub-fields that should be merged into a containing structure or union.
### Arrays and pointers[¶](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers "Link to this heading")

_class_ ctypes.Array(_* args_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array "Link to this definition")

Abstract base class for arrays.
The recommended way to create concrete array types is by multiplying any `ctypes` data type with a non-negative integer. Alternatively, you can subclass this type and define [`_length_`](https://docs.python.org/3/library/ctypes.html#ctypes.Array._length_ "ctypes.Array._length_") and [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes.Array._type_ "ctypes.Array._type_") class variables. Array elements can be read and written using standard subscript and slice accesses; for slice reads, the resulting object is _not_ itself an `Array`.

_length_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array._length_ "Link to this definition")
