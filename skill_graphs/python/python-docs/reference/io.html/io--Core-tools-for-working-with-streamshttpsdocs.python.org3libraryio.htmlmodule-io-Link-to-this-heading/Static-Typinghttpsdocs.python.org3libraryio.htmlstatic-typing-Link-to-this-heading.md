## Static Typing[¶](https://docs.python.org/3/library/io.html#static-typing "Link to this heading")
The following protocols can be used for annotating function and method arguments for simple stream reading or writing operations. They are decorated with [`@typing.runtime_checkable`](https://docs.python.org/3/library/typing.html#typing.runtime_checkable "typing.runtime_checkable").

_class_ io.Reader[_T_][¶](https://docs.python.org/3/library/io.html#io.Reader "Link to this definition")

Generic protocol for reading from a file or other input stream. `T` will usually be [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), but can be any type that is read from the stream.
Added in version 3.14.

read()[¶](https://docs.python.org/3/library/io.html#io.Reader.read "Link to this definition")


read(_size_ , _/_)

Read data from the input stream and return it. If _size_ is specified, it should be an integer, and at most _size_ items (bytes/characters) will be read.
For example:
Copy```
def read_it(reader: Reader[str]):
    data = reader.read(11)
    assert isinstance(data, str)

```


_class_ io.Writer[_T_][¶](https://docs.python.org/3/library/io.html#io.Writer "Link to this definition")

Generic protocol for writing to a file or other output stream. `T` will usually be [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), but can be any type that can be written to the stream.
Added in version 3.14.

write(_data_ , _/_)[¶](https://docs.python.org/3/library/io.html#io.Writer.write "Link to this definition")

Write _data_ to the output stream and return the number of items (bytes/characters) written.
For example:
Copy```
def write_binary(writer: Writer[bytes]):
    writer.write(b"Hello world!\n")

```

See [ABCs and Protocols for working with I/O](https://docs.python.org/3/library/typing.html#typing-io) for other I/O related protocols and classes that can be used for static type checking.
