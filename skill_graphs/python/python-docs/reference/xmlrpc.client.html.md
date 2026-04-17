[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html)
    * [ServerProxy Objects](https://docs.python.org/3/library/xmlrpc.client.html#serverproxy-objects)
    * [DateTime Objects](https://docs.python.org/3/library/xmlrpc.client.html#datetime-objects)
    * [Binary Objects](https://docs.python.org/3/library/xmlrpc.client.html#binary-objects)
    * [Fault Objects](https://docs.python.org/3/library/xmlrpc.client.html#fault-objects)
    * [ProtocolError Objects](https://docs.python.org/3/library/xmlrpc.client.html#protocolerror-objects)
    * [MultiCall Objects](https://docs.python.org/3/library/xmlrpc.client.html#multicall-objects)
    * [Convenience Functions](https://docs.python.org/3/library/xmlrpc.client.html#convenience-functions)
    * [Example of Client Usage](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-usage)
    * [Example of Client and Server Usage](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-and-server-usage)


#### Previous topic
[`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html "previous chapter")
#### Next topic
[`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xmlrpc.client+%E2%80%94+XML-RPC+client+access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxmlrpc.client.html&pagesource=library%2Fxmlrpc.client.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xmlrpc.server.html "xmlrpc.server — Basic XML-RPC servers") |
  * [previous](https://docs.python.org/3/library/xmlrpc.html "xmlrpc — XMLRPC server and client modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html)
  * |
  * Theme  Auto Light Dark |


#  `xmlrpc.client` — XML-RPC client access[¶](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "Link to this heading")
**Source code:**
* * *
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data. This module supports writing XML-RPC client code; it handles all the details of translating between conformable Python objects and XML on the wire.
Warning
The `xmlrpc.client` module is not secure against maliciously constructed data. If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security).
Changed in version 3.5: For HTTPS URIs, `xmlrpc.client` now performs all the necessary certificate and hostname checks by default.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

_class_ xmlrpc.client.ServerProxy(_uri_ , _transport =None_, _encoding =None_, _verbose =False_, _allow_none =False_, _use_datetime =False_, _use_builtin_types =False_, _*_ , _headers =()_, _context =None_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy "Link to this definition")

A `ServerProxy` instance is an object that manages communication with a remote XML-RPC server. The required first argument is a URI (Uniform Resource Indicator), and will normally be the URL of the server. The optional second argument is a transport factory instance; by default it is an internal `SafeTransport` instance for https: URLs and an internal HTTP `Transport` instance otherwise. The optional third argument is an encoding, by default UTF-8. The optional fourth argument is a debugging flag.
The following parameters govern the use of the returned proxy instance. If _allow_none_ is true, the Python constant `None` will be translated into XML; the default behaviour is for `None` to raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). This is a commonly used extension to the XML-RPC specification, but isn’t supported by all clients and servers; see _use_builtin_types_ flag can be used to cause date/time values to be presented as [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects and binary data to be presented as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects; this flag is false by default. `datetime.datetime`, `bytes` and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") objects may be passed to calls. The _headers_ parameter is an optional sequence of HTTP headers to send with each request, expressed as a sequence of 2-tuples representing the header name and value. (e.g. `[('Header-Name', 'value')]`). If an HTTPS URL is provided, _context_ may be [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") and configures the SSL settings of the underlying HTTPS connection. The obsolete _use_datetime_ flag is similar to _use_builtin_types_ but it applies only to date/time values.
Changed in version 3.3: The _use_builtin_types_ flag was added.
Changed in version 3.8: The _headers_ parameter was added.
Both the HTTP and HTTPS transports support the URL syntax extension for HTTP Basic Authentication: `http://user:pass@host:port/path`. The `user:pass` portion will be base64-encoded as an HTTP ‘Authorization’ header, and sent to the remote server as part of the connection process when invoking an XML-RPC method. You only need to use this if the remote server requires a Basic Authentication user and password.
The returned instance is a proxy object with methods that can be used to invoke corresponding RPC calls on the remote server. If the remote server supports the introspection API, the proxy can also be used to query the remote server for the methods it supports (service discovery) and fetch other server-associated metadata.
Types that are conformable (e.g. that can be marshalled through XML), include the following (and except where noted, they are unmarshalled as the same Python type):
XML-RPC type | Python type
---|---
`boolean` | [`bool`](https://docs.python.org/3/library/functions.html#bool "bool")
`int`, `i1`, `i2`, `i4`, `i8` or `biginteger` | [`int`](https://docs.python.org/3/library/functions.html#int "int") in range from -2147483648 to 2147483647. Values get the `<int>` tag.
`double` or `float` | [`float`](https://docs.python.org/3/library/functions.html#float "float"). Values get the `<double>` tag.
`string` | [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")
`array` | [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") containing conformable elements. Arrays are returned as `lists`.
`struct` | [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). Keys must be strings, values may be any conformable type. Objects of user-defined classes can be passed in; only their [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute is transmitted.
`dateTime.iso8601` | [`DateTime`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.DateTime "xmlrpc.client.DateTime") or [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"). Returned type depends on values of _use_builtin_types_ and _use_datetime_ flags.
`base64` | [`Binary`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Binary "xmlrpc.client.Binary"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"). Returned type depends on the value of the _use_builtin_types_ flag.
`nil` | The `None` constant. Passing is allowed only if _allow_none_ is true.
`bigdecimal` | [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"). Returned type only.
This is the full set of data types supported by XML-RPC. Method calls may also raise a special [`Fault`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault "xmlrpc.client.Fault") instance, used to signal XML-RPC server errors, or [`ProtocolError`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError "xmlrpc.client.ProtocolError") used to signal an error in the HTTP/HTTPS transport layer. Both `Fault` and `ProtocolError` derive from a base class called `Error`. Note that the xmlrpc client module currently does not marshal instances of subclasses of built-in types.
When passing strings, characters special to XML such as `<`, `>`, and `&` will be automatically escaped. However, it’s the caller’s responsibility to ensure that the string is free of characters that aren’t allowed in XML, such as the control characters with ASCII values between 0 and 31 (except, of course, tab, newline and carriage return); failing to do this will result in an XML-RPC request that isn’t well-formed XML. If you have to pass arbitrary bytes via XML-RPC, use [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") classes or the [`Binary`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Binary "xmlrpc.client.Binary") wrapper class described below.
`Server` is retained as an alias for `ServerProxy` for backwards compatibility. New code should use `ServerProxy`.
Changed in version 3.5: Added the _context_ argument.
Changed in version 3.6: Added support of type tags with prefixes (e.g. `ex:nil`). Added support of unmarshalling additional types used by Apache XML-RPC implementation for numerics: `i1`, `i2`, `i8`, `biginteger`, `float` and `bigdecimal`. See
See also
A good description of XML-RPC operation and client software in several languages. Contains pretty much everything an XML-RPC client developer needs to know.
Describes the XML-RPC protocol extension for introspection.
The official specification.
## ServerProxy Objects[¶](https://docs.python.org/3/library/xmlrpc.client.html#serverproxy-objects "Link to this heading")
A [`ServerProxy`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy "xmlrpc.client.ServerProxy") instance has a method corresponding to each remote procedure call accepted by the XML-RPC server. Calling the method performs an RPC, dispatched by both name and argument signature (e.g. the same method name can be overloaded with multiple argument signatures). The RPC finishes by returning a value, which may be either returned data in a conformant type or a [`Fault`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault "xmlrpc.client.Fault") or [`ProtocolError`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError "xmlrpc.client.ProtocolError") object indicating an error.
Servers that support the XML introspection API support some common methods grouped under the reserved `system` attribute:

ServerProxy.system.listMethods()[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy.system.listMethods "Link to this definition")

This method returns a list of strings, one for each (non-system) method supported by the XML-RPC server.

ServerProxy.system.methodSignature(_name_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy.system.methodSignature "Link to this definition")

This method takes one parameter, the name of a method implemented by the XML-RPC server. It returns an array of possible signatures for this method. A signature is an array of types. The first of these types is the return type of the method, the rest are parameters.
Because multiple signatures (ie. overloading) is permitted, this method returns a list of signatures rather than a singleton.
Signatures themselves are restricted to the top level parameters expected by a method. For instance if a method expects one array of structs as a parameter, and it returns a string, its signature is simply “string, array”. If it expects three integers and returns a string, its signature is “string, int, int, int”.
If no signature is defined for the method, a non-array value is returned. In Python this means that the type of the returned value will be something other than list.

ServerProxy.system.methodHelp(_name_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy.system.methodHelp "Link to this definition")

This method takes one parameter, the name of a method implemented by the XML-RPC server. It returns a documentation string describing the use of that method. If no such string is available, an empty string is returned. The documentation string may contain HTML markup.
Changed in version 3.5: Instances of [`ServerProxy`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy "xmlrpc.client.ServerProxy") support the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol for closing the underlying transport.
A working example follows. The server code:
Copy```
from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n % 2 == 0

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()

```

The client code for the preceding server:
Copy```
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))

```

## DateTime Objects[¶](https://docs.python.org/3/library/xmlrpc.client.html#datetime-objects "Link to this heading")

_class_ xmlrpc.client.DateTime[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.DateTime "Link to this definition")

This class may be initialized with seconds since the epoch, a time tuple, an ISO 8601 time/date string, or a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance. It has the following methods, supported mainly for internal use by the marshalling/unmarshalling code:

decode(_string_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.DateTime.decode "Link to this definition")

Accept a string as the instance’s new time value.

encode(_out_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.DateTime.encode "Link to this definition")

Write the XML-RPC encoding of this `DateTime` item to the _out_ stream object.
It also supports certain of Python’s built-in operators through [`rich comparison`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__") and [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__") methods.
A working example follows. The server code:
Copy```
import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(today, "today")
server.serve_forever()

```

The client code for the preceding server:
Copy```
import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

today = proxy.today()
# convert the ISO8601 string to a datetime object
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))

```

## Binary Objects[¶](https://docs.python.org/3/library/xmlrpc.client.html#binary-objects "Link to this heading")

_class_ xmlrpc.client.Binary[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Binary "Link to this definition")

This class may be initialized from bytes data (which may include NULs). The primary access to the content of a `Binary` object is provided by an attribute:

data[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Binary.data "Link to this definition")

The binary data encapsulated by the `Binary` instance. The data is provided as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.
`Binary` objects have the following methods, supported mainly for internal use by the marshalling/unmarshalling code:

decode(_bytes_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Binary.decode "Link to this definition")

Accept a base64 [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object and decode it as the instance’s new data.

encode(_out_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Binary.encode "Link to this definition")

Write the XML-RPC base 64 encoding of this binary item to the _out_ stream object.
The encoded data will have newlines every 76 characters as per
It also supports certain of Python’s built-in operators through [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__") and [`__ne__()`](https://docs.python.org/3/reference/datamodel.html#object.__ne__ "object.__ne__") methods.
Example usage of the binary objects. We’re going to transfer an image over XMLRPC:
Copy```
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def python_logo():
    with open("python_logo.jpg", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(python_logo, 'python_logo')

server.serve_forever()

```

The client gets the image and saves it to a file:
Copy```
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
with open("fetched_python_logo.jpg", "wb") as handle:
    handle.write(proxy.python_logo().data)

```

## Fault Objects[¶](https://docs.python.org/3/library/xmlrpc.client.html#fault-objects "Link to this heading")

_class_ xmlrpc.client.Fault[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault "Link to this definition")

A `Fault` object encapsulates the content of an XML-RPC fault tag. Fault objects have the following attributes:

faultCode[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault.faultCode "Link to this definition")

An int indicating the fault type.

faultString[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault.faultString "Link to this definition")

A string containing a diagnostic message associated with the fault.
In the following example we’re going to intentionally cause a [`Fault`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault "xmlrpc.client.Fault") by returning a complex type object. The server code:
Copy```
from xmlrpc.server import SimpleXMLRPCServer

# A marshalling error is going to occur because we're returning a
# complex number
def add(x, y):
    return x+y+0j

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(add, 'add')

server.serve_forever()

```

The client code for the preceding server:
Copy```
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
try:
    proxy.add(2, 5)
except xmlrpc.client.Fault as err:
    print("A fault occurred")
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)

```

## ProtocolError Objects[¶](https://docs.python.org/3/library/xmlrpc.client.html#protocolerror-objects "Link to this heading")

_class_ xmlrpc.client.ProtocolError[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError "Link to this definition")

A `ProtocolError` object describes a protocol error in the underlying transport layer (such as a 404 ‘not found’ error if the server named by the URI does not exist). It has the following attributes:

url[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError.url "Link to this definition")

The URI or URL that triggered the error.

errcode[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError.errcode "Link to this definition")

The error code.

errmsg[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError.errmsg "Link to this definition")

The error message or diagnostic string.

headers[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError.headers "Link to this definition")

A dict containing the headers of the HTTP/HTTPS request that triggered the error.
In the following example we’re going to intentionally cause a [`ProtocolError`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ProtocolError "xmlrpc.client.ProtocolError") by providing an invalid URI:
Copy```
import xmlrpc.client

# create a ServerProxy with a URI that doesn't respond to XMLRPC requests
proxy = xmlrpc.client.ServerProxy("http://google.com/")

try:
    proxy.some_method()
except xmlrpc.client.ProtocolError as err:
    print("A protocol error occurred")
    print("URL: %s" % err.url)
    print("HTTP/HTTPS headers: %s" % err.headers)
    print("Error code: %d" % err.errcode)
    print("Error message: %s" % err.errmsg)

```

## MultiCall Objects[¶](https://docs.python.org/3/library/xmlrpc.client.html#multicall-objects "Link to this heading")
The [`MultiCall`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.MultiCall "xmlrpc.client.MultiCall") object provides a way to encapsulate multiple calls to a remote server into a single request [[1]](https://docs.python.org/3/library/xmlrpc.client.html#id6).

_class_ xmlrpc.client.MultiCall(_server_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.MultiCall "Link to this definition")

Create an object used to boxcar method calls. _server_ is the eventual target of the call. Calls can be made to the result object, but they will immediately return `None`, and only store the call name and parameters in the `MultiCall` object. Calling the object itself causes all stored calls to be transmitted as a single `system.multicall` request. The result of this call is a [generator](https://docs.python.org/3/glossary.html#term-generator); iterating over this generator yields the individual results.
A usage example of this class follows. The server code:
Copy```
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

# A simple server with simple arithmetic functions
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')
server.serve_forever()

```

The client code for the preceding server:
Copy```
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall = xmlrpc.client.MultiCall(proxy)
multicall.add(7, 3)
multicall.subtract(7, 3)
multicall.multiply(7, 3)
multicall.divide(7, 3)
result = multicall()

print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))

```

## Convenience Functions[¶](https://docs.python.org/3/library/xmlrpc.client.html#convenience-functions "Link to this heading")

xmlrpc.client.dumps(_params_ , _methodname =None_, _methodresponse =None_, _encoding =None_, _allow_none =False_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.dumps "Link to this definition")

Convert _params_ into an XML-RPC request, or into a response if _methodresponse_ is true. _params_ can be either a tuple of arguments or an instance of the [`Fault`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault "xmlrpc.client.Fault") exception class. If _methodresponse_ is true, only a single value can be returned, meaning that _params_ must be of length 1. _encoding_ , if supplied, is the encoding to use in the generated XML; the default is UTF-8. Python’s [`None`](https://docs.python.org/3/library/constants.html#None "None") value cannot be used in standard XML-RPC; to allow using it via an extension, provide a true value for _allow_none_.

xmlrpc.client.loads(_data_ , _use_datetime =False_, _use_builtin_types =False_)[¶](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.loads "Link to this definition")

Convert an XML-RPC request or response into Python objects, a `(params, methodname)`. _params_ is a tuple of argument; _methodname_ is a string, or `None` if no method name is present in the packet. If the XML-RPC packet represents a fault condition, this function will raise a [`Fault`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.Fault "xmlrpc.client.Fault") exception. The _use_builtin_types_ flag can be used to cause date/time values to be presented as [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects and binary data to be presented as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects; this flag is false by default.
The obsolete _use_datetime_ flag is similar to _use_builtin_types_ but it applies only to date/time values.
Changed in version 3.3: The _use_builtin_types_ flag was added.
## Example of Client Usage[¶](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-usage "Link to this heading")
Copy```
# simple test program (from the XML-RPC specification)
from xmlrpc.client import ServerProxy, Error

# server = ServerProxy("http://localhost:8000") # local server
with ServerProxy("http://betty.userland.com") as proxy:

    print(proxy)

    try:
        print(proxy.examples.getStateName(41))
    except Error as v:
        print("ERROR", v)

```

To access an XML-RPC server through a HTTP proxy, you need to define a custom transport. The following example shows how:
Copy```
import http.client
import xmlrpc.client

class ProxiedTransport(xmlrpc.client.Transport):

    def set_proxy(self, host, port=None, headers=None):
        self.proxy = host, port
        self.proxy_headers = headers

    def make_connection(self, host):
        connection = http.client.HTTPConnection(*self.proxy)
        connection.set_tunnel(host, headers=self.proxy_headers)
        self._connection = host, connection
        return connection

transport = ProxiedTransport()
transport.set_proxy('proxy-server', 8080)
server = xmlrpc.client.ServerProxy('http://betty.userland.com', transport=transport)
print(server.examples.getStateName(41))

```

## Example of Client and Server Usage[¶](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-and-server-usage "Link to this heading")
See [SimpleXMLRPCServer Example](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example).
Footnotes
[[1](https://docs.python.org/3/library/xmlrpc.client.html#id5)]
This approach has been first presented in
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html)
    * [ServerProxy Objects](https://docs.python.org/3/library/xmlrpc.client.html#serverproxy-objects)
    * [DateTime Objects](https://docs.python.org/3/library/xmlrpc.client.html#datetime-objects)
    * [Binary Objects](https://docs.python.org/3/library/xmlrpc.client.html#binary-objects)
    * [Fault Objects](https://docs.python.org/3/library/xmlrpc.client.html#fault-objects)
    * [ProtocolError Objects](https://docs.python.org/3/library/xmlrpc.client.html#protocolerror-objects)
    * [MultiCall Objects](https://docs.python.org/3/library/xmlrpc.client.html#multicall-objects)
    * [Convenience Functions](https://docs.python.org/3/library/xmlrpc.client.html#convenience-functions)
    * [Example of Client Usage](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-usage)
    * [Example of Client and Server Usage](https://docs.python.org/3/library/xmlrpc.client.html#example-of-client-and-server-usage)


#### Previous topic
[`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html "previous chapter")
#### Next topic
[`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xmlrpc.client+%E2%80%94+XML-RPC+client+access&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxmlrpc.client.html&pagesource=library%2Fxmlrpc.client.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xmlrpc.server.html "xmlrpc.server — Basic XML-RPC servers") |
  * [previous](https://docs.python.org/3/library/xmlrpc.html "xmlrpc — XMLRPC server and client modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html)
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
