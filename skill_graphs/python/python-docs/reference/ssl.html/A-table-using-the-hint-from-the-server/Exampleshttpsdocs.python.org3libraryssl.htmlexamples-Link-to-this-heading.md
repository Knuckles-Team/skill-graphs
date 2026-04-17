## Examples[¶](https://docs.python.org/3/library/ssl.html#examples "Link to this heading")
### Testing for SSL support[¶](https://docs.python.org/3/library/ssl.html#testing-for-ssl-support "Link to this heading")
To test for the presence of SSL support in a Python installation, user code should use the following idiom:
Copy```
try:
    import ssl
except ImportError:
    pass
else:
    ...  # do something that requires SSL support

```

### Client-side operation[¶](https://docs.python.org/3/library/ssl.html#client-side-operation "Link to this heading")
This example creates a SSL context with the recommended security settings for client sockets, including automatic certificate verification:
Copy```
>>> context = ssl.create_default_context()

```

If you prefer to tune security settings yourself, you might create a context from scratch (but beware that you might not get the settings right):
Copy```
>>> context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
>>> context.load_verify_locations("/etc/ssl/certs/ca-bundle.crt")

```

(this snippet assumes your operating system places a bundle of all CA certificates in `/etc/ssl/certs/ca-bundle.crt`; if not, you’ll get an error and have to adjust the location)
The [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") protocol configures the context for cert validation and hostname verification. [`verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode") is set to [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") and [`check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") is set to `True`. All other protocols create SSL contexts with insecure defaults.
When you use the context to connect to a server, [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") and [`check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") validate the server certificate: it ensures that the server certificate was signed with one of the CA certificates, checks the signature for correctness, and verifies other properties like validity and identity of the hostname:
Copy```
>>> conn = context.wrap_socket(socket.socket(socket.AF_INET),
...                            server_hostname="www.python.org")
>>> conn.connect(("www.python.org", 443))

```

You may then fetch the certificate:
Copy```
>>> cert = conn.getpeercert()

```

Visual inspection shows that the certificate does identify the desired service (that is, the HTTPS host `www.python.org`):
Copy```
>>> pprint.pprint(cert)
{'OCSP': ('http://ocsp.digicert.com',),
 'caIssuers': ('http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt',),
 'crlDistributionPoints': ('http://crl3.digicert.com/sha2-ev-server-g1.crl',
                           'http://crl4.digicert.com/sha2-ev-server-g1.crl'),
 'issuer': ((('countryName', 'US'),),
            (('organizationName', 'DigiCert Inc'),),
            (('organizationalUnitName', 'www.digicert.com'),),
            (('commonName', 'DigiCert SHA2 Extended Validation Server CA'),)),
 'notAfter': 'Sep  9 12:00:00 2016 GMT',
 'notBefore': 'Sep  5 00:00:00 2014 GMT',
 'serialNumber': '01BB6F00122B177F36CAB49CEA8B6B26',
 'subject': ((('businessCategory', 'Private Organization'),),
             (('1.3.6.1.4.1.311.60.2.1.3', 'US'),),
             (('1.3.6.1.4.1.311.60.2.1.2', 'Delaware'),),
             (('serialNumber', '3359300'),),
             (('streetAddress', '16 Allen Rd'),),
             (('postalCode', '03894-4801'),),
             (('countryName', 'US'),),
             (('stateOrProvinceName', 'NH'),),
             (('localityName', 'Wolfeboro'),),
             (('organizationName', 'Python Software Foundation'),),
             (('commonName', 'www.python.org'),)),
 'subjectAltName': (('DNS', 'www.python.org'),
                    ('DNS', 'python.org'),
                    ('DNS', 'pypi.org'),
                    ('DNS', 'docs.python.org'),
                    ('DNS', 'testpypi.org'),
                    ('DNS', 'bugs.python.org'),
                    ('DNS', 'wiki.python.org'),
                    ('DNS', 'hg.python.org'),
                    ('DNS', 'mail.python.org'),
                    ('DNS', 'packaging.python.org'),
                    ('DNS', 'pythonhosted.org'),
                    ('DNS', 'www.pythonhosted.org'),
                    ('DNS', 'test.pythonhosted.org'),
                    ('DNS', 'us.pycon.org'),
                    ('DNS', 'id.python.org')),
 'version': 3}

```

Now the SSL channel is established and the certificate verified, you can proceed to talk with the server:
Copy```
>>> conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
>>> pprint.pprint(conn.recv(1024).split(b"\r\n"))
[b'HTTP/1.1 200 OK',
 b'Date: Sat, 18 Oct 2014 18:27:20 GMT',
 b'Server: nginx',
 b'Content-Type: text/html; charset=utf-8',
 b'X-Frame-Options: SAMEORIGIN',
 b'Content-Length: 45679',
 b'Accept-Ranges: bytes',
 b'Via: 1.1 varnish',
 b'Age: 2188',
 b'X-Served-By: cache-lcy1134-LCY',
 b'X-Cache: HIT',
 b'X-Cache-Hits: 11',
 b'Vary: Cookie',
 b'Strict-Transport-Security: max-age=63072000; includeSubDomains',
 b'Connection: close',
 b'',
 b'']

```

See the discussion of [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) below.
### Server-side operation[¶](https://docs.python.org/3/library/ssl.html#server-side-operation "Link to this heading")
For server operation, typically you’ll need to have a server certificate, and private key, each in a file. You’ll first create a context holding the key and the certificate, so that clients can check your authenticity. Then you’ll open a socket, bind it to a port, call `listen()` on it, and start waiting for clients to connect:
Copy```
import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="mycertfile", keyfile="mykeyfile")

bindsocket = socket.socket()
bindsocket.bind(('myaddr.example.com', 10023))
bindsocket.listen(5)

```

When a client connects, you’ll call `accept()` on the socket to get the new socket from the other end, and use the context’s [`SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket") method to create a server-side SSL socket for the connection:
Copy```
while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()

```

Then you’ll read data from the `connstream` and do something with it till you are finished with the client (or the client is finished with you):
Copy```
def deal_with_client(connstream):
    data = connstream.recv(1024)
    # empty data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.recv(1024)
    # finished with client

```

And go back to listening for new client connections (of course, a real server would probably handle each client connection in a separate thread, or put the sockets in [non-blocking mode](https://docs.python.org/3/library/ssl.html#ssl-nonblocking) and use an event loop).
