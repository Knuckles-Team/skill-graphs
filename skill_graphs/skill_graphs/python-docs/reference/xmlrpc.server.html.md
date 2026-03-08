[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html)
    * [SimpleXMLRPCServer Objects](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-objects)
      * [SimpleXMLRPCServer Example](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example)
    * [CGIXMLRPCRequestHandler](https://docs.python.org/3/library/xmlrpc.server.html#cgixmlrpcrequesthandler)
    * [Documenting XMLRPC server](https://docs.python.org/3/library/xmlrpc.server.html#documenting-xmlrpc-server)
    * [DocXMLRPCServer Objects](https://docs.python.org/3/library/xmlrpc.server.html#docxmlrpcserver-objects)
    * [DocCGIXMLRPCRequestHandler](https://docs.python.org/3/library/xmlrpc.server.html#doccgixmlrpcrequesthandler)


#### Previous topic
[`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html "previous chapter")
#### Next topic
[`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xmlrpc.server+%E2%80%94+Basic+XML-RPC+servers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxmlrpc.server.html&pagesource=library%2Fxmlrpc.server.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ipaddress.html "ipaddress — IPv4/IPv6 manipulation library") |
  * [previous](https://docs.python.org/3/library/xmlrpc.client.html "xmlrpc.client — XML-RPC client access") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html)
  * |
  * Theme  Auto Light Dark |


#  `xmlrpc.server` — Basic XML-RPC servers[¶](https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server "Link to this heading")
**Source code:**
* * *
The `xmlrpc.server` module provides a basic server framework for XML-RPC servers written in Python. Servers can either be free standing, using [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer"), or embedded in a CGI environment, using [`CGIXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler "xmlrpc.server.CGIXMLRPCRequestHandler").
Warning
The `xmlrpc.server` module is not secure against maliciously constructed data. If you need to parse untrusted or unauthenticated data, see [XML security](https://docs.python.org/3/library/xml.html#xml-security).
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

_class_ xmlrpc.server.SimpleXMLRPCServer(_addr_ , _requestHandler =SimpleXMLRPCRequestHandler_, _logRequests =True_, _allow_none =False_, _encoding =None_, _bind_and_activate =True_, _use_builtin_types =False_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "Link to this definition")

Create a new server instance. This class provides methods for registration of functions that can be called by the XML-RPC protocol. The _requestHandler_ parameter should be a factory for request handler instances; it defaults to [`SimpleXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCRequestHandler "xmlrpc.server.SimpleXMLRPCRequestHandler"). The _addr_ and _requestHandler_ parameters are passed to the [`socketserver.TCPServer`](https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer "socketserver.TCPServer") constructor. If _logRequests_ is true (the default), requests will be logged; setting this parameter to false will turn off logging. The _allow_none_ and _encoding_ parameters are passed on to [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.") and control the XML-RPC responses that will be returned from the server. The _bind_and_activate_ parameter controls whether `server_bind()` and `server_activate()` are called immediately by the constructor; it defaults to true. Setting it to false allows code to manipulate the _allow_reuse_address_ class variable before the address is bound. The _use_builtin_types_ parameter is passed to the [`loads()`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.loads "xmlrpc.client.loads") function and controls which types are processed when date/times values or binary data are received; it defaults to false.
Changed in version 3.3: The _use_builtin_types_ flag was added.

_class_ xmlrpc.server.CGIXMLRPCRequestHandler(_allow_none =False_, _encoding =None_, _use_builtin_types =False_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler "Link to this definition")

Create a new instance to handle XML-RPC requests in a CGI environment. The _allow_none_ and _encoding_ parameters are passed on to [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.") and control the XML-RPC responses that will be returned from the server. The _use_builtin_types_ parameter is passed to the [`loads()`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.loads "xmlrpc.client.loads") function and controls which types are processed when date/times values or binary data are received; it defaults to false.
Changed in version 3.3: The _use_builtin_types_ flag was added.

_class_ xmlrpc.server.SimpleXMLRPCRequestHandler[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCRequestHandler "Link to this definition")

Create a new request handler instance. This request handler supports `POST` requests and modifies logging so that the _logRequests_ parameter to the [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer") constructor parameter is honored.
## SimpleXMLRPCServer Objects[¶](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-objects "Link to this heading")
The [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer") class is based on [`socketserver.TCPServer`](https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer "socketserver.TCPServer") and provides a means of creating simple, stand alone XML-RPC servers.

SimpleXMLRPCServer.register_function(_function =None_, _name =None_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer.register_function "Link to this definition")

Register a function that can respond to XML-RPC requests. If _name_ is given, it will be the method name associated with _function_ , otherwise [`function.__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__") will be used. _name_ is a string, and may contain characters not legal in Python identifiers, including the period character.
This method can also be used as a decorator. When used as a decorator, _name_ can only be given as a keyword argument to register _function_ under _name_. If no _name_ is given, [`function.__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__") will be used.
Changed in version 3.7: `register_function()` can be used as a decorator.

SimpleXMLRPCServer.register_instance(_instance_ , _allow_dotted_names =False_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer.register_instance "Link to this definition")

Register an object which is used to expose method names which have not been registered using [`register_function()`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer.register_function "xmlrpc.server.SimpleXMLRPCServer.register_function"). If _instance_ contains a `_dispatch()` method, it is called with the requested method name and the parameters from the request. Its API is `def _dispatch(self, method, params)` (note that _params_ does not represent a variable argument list). If it calls an underlying function to perform its task, that function is called as `func(*params)`, expanding the parameter list. The return value from `_dispatch()` is returned to the client as the result. If _instance_ does not have a `_dispatch()` method, it is searched for an attribute matching the name of the requested method.
If the optional _allow_dotted_names_ argument is true and the instance does not have a `_dispatch()` method, then if the requested method name contains periods, each component of the method name is searched for individually, with the effect that a simple hierarchical search is performed. The value found from this search is then called with the parameters from the request, and the return value is passed back to the client.
Warning
Enabling the _allow_dotted_names_ option allows intruders to access your module’s global variables and may allow intruders to execute arbitrary code on your machine. Only use this option on a secure, closed network.

SimpleXMLRPCServer.register_introspection_functions()[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer.register_introspection_functions "Link to this definition")

Registers the XML-RPC introspection functions `system.listMethods`, `system.methodHelp` and `system.methodSignature`.

SimpleXMLRPCServer.register_multicall_functions()[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer.register_multicall_functions "Link to this definition")

Registers the XML-RPC multicall function system.multicall.

SimpleXMLRPCRequestHandler.rpc_paths[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCRequestHandler.rpc_paths "Link to this definition")

An attribute value that must be a tuple listing valid path portions of the URL for receiving XML-RPC requests. Requests posted to other paths will result in a 404 “no such page” HTTP error. If this tuple is empty, all paths will be considered valid. The default value is `('/', '/RPC2')`.
### SimpleXMLRPCServer Example[¶](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example "Link to this heading")
Server code:
Copy```
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()

```

The following client code will call the methods made available by the preceding server:
Copy```
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.pow(2,3))  # Returns 2**3 = 8
print(s.add(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods
print(s.system.listMethods())

```

`register_function()` can also be used as a decorator. The previous server example can register functions in a decorator way:
Copy```
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name, using
    # register_function as a decorator. *name* can only be given
    # as a keyword argument.
    @server.register_function(name='add')
    def adder_function(x, y):
        return x + y

    # Register a function under function.__name__.
    @server.register_function
    def mul(x, y):
        return x * y

    server.serve_forever()

```

The following example included in the `Lib/xmlrpc/server.py` module shows a server allowing dotted names and registering a multicall function.
Warning
Enabling the _allow_dotted_names_ option allows intruders to access your module’s global variables and may allow intruders to execute arbitrary code on your machine. Only use this example within a secure, closed network.
Copy```
import datetime

class ExampleService:
    def getData(self):
        return '42'

    class currentTime:
        @staticmethod
        def getCurrentTime():
            return datetime.datetime.now()

with SimpleXMLRPCServer(("localhost", 8000)) as server:
    server.register_function(pow)
    server.register_function(lambda x,y: x+y, 'add')
    server.register_instance(ExampleService(), allow_dotted_names=True)
    server.register_multicall_functions()
    print('Serving XML-RPC on localhost port 8000')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)

```

This ExampleService demo can be invoked from the command line:
Copy```
python -m xmlrpc.server

```

The client that interacts with the above server is included in `Lib/xmlrpc/client.py`:
Copy```
server = ServerProxy("http://localhost:8000")

try:
    print(server.currentTime.getCurrentTime())
except Error as v:
    print("ERROR", v)

multi = MultiCall(server)
multi.getData()
multi.pow(2,9)
multi.add(1,2)
try:
    for response in multi():
        print(response)
except Error as v:
    print("ERROR", v)

```

This client which interacts with the demo XMLRPC server can be invoked as:
Copy```
python -m xmlrpc.client

```

## CGIXMLRPCRequestHandler[¶](https://docs.python.org/3/library/xmlrpc.server.html#cgixmlrpcrequesthandler "Link to this heading")
The [`CGIXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler "xmlrpc.server.CGIXMLRPCRequestHandler") class can be used to handle XML-RPC requests sent to Python CGI scripts.

CGIXMLRPCRequestHandler.register_function(_function =None_, _name =None_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler.register_function "Link to this definition")

Register a function that can respond to XML-RPC requests. If _name_ is given, it will be the method name associated with _function_ , otherwise [`function.__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__") will be used. _name_ is a string, and may contain characters not legal in Python identifiers, including the period character.
This method can also be used as a decorator. When used as a decorator, _name_ can only be given as a keyword argument to register _function_ under _name_. If no _name_ is given, [`function.__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__") will be used.
Changed in version 3.7: `register_function()` can be used as a decorator.

CGIXMLRPCRequestHandler.register_instance(_instance_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler.register_instance "Link to this definition")

Register an object which is used to expose method names which have not been registered using [`register_function()`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler.register_function "xmlrpc.server.CGIXMLRPCRequestHandler.register_function"). If instance contains a `_dispatch()` method, it is called with the requested method name and the parameters from the request; the return value is returned to the client as the result. If instance does not have a `_dispatch()` method, it is searched for an attribute matching the name of the requested method; if the requested method name contains periods, each component of the method name is searched for individually, with the effect that a simple hierarchical search is performed. The value found from this search is then called with the parameters from the request, and the return value is passed back to the client.

CGIXMLRPCRequestHandler.register_introspection_functions()[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler.register_introspection_functions "Link to this definition")

Register the XML-RPC introspection functions `system.listMethods`, `system.methodHelp` and `system.methodSignature`.

CGIXMLRPCRequestHandler.register_multicall_functions()[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler.register_multicall_functions "Link to this definition")

Register the XML-RPC multicall function `system.multicall`.

CGIXMLRPCRequestHandler.handle_request(_request_text =None_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler.handle_request "Link to this definition")

Handle an XML-RPC request. If _request_text_ is given, it should be the POST data provided by the HTTP server, otherwise the contents of stdin will be used.
Example:
Copy```
class MyFuncs:
    def mul(self, x, y):
        return x * y


handler = CGIXMLRPCRequestHandler()
handler.register_function(pow)
handler.register_function(lambda x,y: x+y, 'add')
handler.register_introspection_functions()
handler.register_instance(MyFuncs())
handler.handle_request()

```

## Documenting XMLRPC server[¶](https://docs.python.org/3/library/xmlrpc.server.html#documenting-xmlrpc-server "Link to this heading")
These classes extend the above classes to serve HTML documentation in response to HTTP GET requests. Servers can either be free standing, using [`DocXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer "xmlrpc.server.DocXMLRPCServer"), or embedded in a CGI environment, using [`DocCGIXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocCGIXMLRPCRequestHandler "xmlrpc.server.DocCGIXMLRPCRequestHandler").

_class_ xmlrpc.server.DocXMLRPCServer(_addr_ , _requestHandler =DocXMLRPCRequestHandler_, _logRequests =True_, _allow_none =False_, _encoding =None_, _bind_and_activate =True_, _use_builtin_types =True_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer "Link to this definition")

Create a new server instance. All parameters have the same meaning as for [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer"); _requestHandler_ defaults to [`DocXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCRequestHandler "xmlrpc.server.DocXMLRPCRequestHandler").
Changed in version 3.3: The _use_builtin_types_ flag was added.

_class_ xmlrpc.server.DocCGIXMLRPCRequestHandler[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocCGIXMLRPCRequestHandler "Link to this definition")

Create a new instance to handle XML-RPC requests in a CGI environment.

_class_ xmlrpc.server.DocXMLRPCRequestHandler[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCRequestHandler "Link to this definition")

Create a new request handler instance. This request handler supports XML-RPC POST requests, documentation GET requests, and modifies logging so that the _logRequests_ parameter to the [`DocXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer "xmlrpc.server.DocXMLRPCServer") constructor parameter is honored.
## DocXMLRPCServer Objects[¶](https://docs.python.org/3/library/xmlrpc.server.html#docxmlrpcserver-objects "Link to this heading")
The [`DocXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer "xmlrpc.server.DocXMLRPCServer") class is derived from [`SimpleXMLRPCServer`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCServer "xmlrpc.server.SimpleXMLRPCServer") and provides a means of creating self-documenting, stand alone XML-RPC servers. HTTP POST requests are handled as XML-RPC method calls. HTTP GET requests are handled by generating pydoc-style HTML documentation. This allows a server to provide its own web-based documentation.

DocXMLRPCServer.set_server_title(_server_title_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer.set_server_title "Link to this definition")

Set the title used in the generated HTML documentation. This title will be used inside the HTML “title” element.

DocXMLRPCServer.set_server_name(_server_name_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer.set_server_name "Link to this definition")

Set the name used in the generated HTML documentation. This name will appear at the top of the generated documentation inside a “h1” element.

DocXMLRPCServer.set_server_documentation(_server_documentation_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocXMLRPCServer.set_server_documentation "Link to this definition")

Set the description used in the generated HTML documentation. This description will appear as a paragraph, below the server name, in the documentation.
## DocCGIXMLRPCRequestHandler[¶](https://docs.python.org/3/library/xmlrpc.server.html#doccgixmlrpcrequesthandler "Link to this heading")
The [`DocCGIXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocCGIXMLRPCRequestHandler "xmlrpc.server.DocCGIXMLRPCRequestHandler") class is derived from [`CGIXMLRPCRequestHandler`](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.CGIXMLRPCRequestHandler "xmlrpc.server.CGIXMLRPCRequestHandler") and provides a means of creating self-documenting, XML-RPC CGI scripts. HTTP POST requests are handled as XML-RPC method calls. HTTP GET requests are handled by generating pydoc-style HTML documentation. This allows a server to provide its own web-based documentation.

DocCGIXMLRPCRequestHandler.set_server_title(_server_title_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocCGIXMLRPCRequestHandler.set_server_title "Link to this definition")

Set the title used in the generated HTML documentation. This title will be used inside the HTML “title” element.

DocCGIXMLRPCRequestHandler.set_server_name(_server_name_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocCGIXMLRPCRequestHandler.set_server_name "Link to this definition")

Set the name used in the generated HTML documentation. This name will appear at the top of the generated documentation inside a “h1” element.

DocCGIXMLRPCRequestHandler.set_server_documentation(_server_documentation_)[¶](https://docs.python.org/3/library/xmlrpc.server.html#xmlrpc.server.DocCGIXMLRPCRequestHandler.set_server_documentation "Link to this definition")

Set the description used in the generated HTML documentation. This description will appear as a paragraph, below the server name, in the documentation.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html)
    * [SimpleXMLRPCServer Objects](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-objects)
      * [SimpleXMLRPCServer Example](https://docs.python.org/3/library/xmlrpc.server.html#simplexmlrpcserver-example)
    * [CGIXMLRPCRequestHandler](https://docs.python.org/3/library/xmlrpc.server.html#cgixmlrpcrequesthandler)
    * [Documenting XMLRPC server](https://docs.python.org/3/library/xmlrpc.server.html#documenting-xmlrpc-server)
    * [DocXMLRPCServer Objects](https://docs.python.org/3/library/xmlrpc.server.html#docxmlrpcserver-objects)
    * [DocCGIXMLRPCRequestHandler](https://docs.python.org/3/library/xmlrpc.server.html#doccgixmlrpcrequesthandler)


#### Previous topic
[`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html "previous chapter")
#### Next topic
[`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=xmlrpc.server+%E2%80%94+Basic+XML-RPC+servers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fxmlrpc.server.html&pagesource=library%2Fxmlrpc.server.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ipaddress.html "ipaddress — IPv4/IPv6 manipulation library") |
  * [previous](https://docs.python.org/3/library/xmlrpc.client.html "xmlrpc.client — XML-RPC client access") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
