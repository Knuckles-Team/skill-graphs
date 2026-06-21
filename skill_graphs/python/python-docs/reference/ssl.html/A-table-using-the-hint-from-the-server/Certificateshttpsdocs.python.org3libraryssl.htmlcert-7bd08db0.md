## Certificates[¶](https://docs.python.org/3/library/ssl.html#certificates "Link to this heading")
Certificates in general are part of a public-key / private-key system. In this system, each _principal_ , (which may be a machine, or a person, or an organization) is assigned a unique two-part encryption key. One part of the key is public, and is called the _public key_ ; the other part is kept secret, and is called the _private key_. The two parts are related, in that if you encrypt a message with one of the parts, you can decrypt it with the other part, and **only** with the other part.
A certificate contains information about two principals. It contains the name of a _subject_ , and the subject’s public key. It also contains a statement by a second principal, the _issuer_ , that the subject is who they claim to be, and that this is indeed the subject’s public key. The issuer’s statement is signed with the issuer’s private key, which only the issuer knows. However, anyone can verify the issuer’s statement by finding the issuer’s public key, decrypting the statement with it, and comparing it to the other information in the certificate. The certificate also contains information about the time period over which it is valid. This is expressed as two fields, called “notBefore” and “notAfter”.
In the Python use of certificates, a client or server can use a certificate to prove who they are. The other side of a network connection can also be required to produce a certificate, and that certificate can be validated to the satisfaction of the client or server that requires such validation. The connection attempt can be set to raise an exception if the validation fails. Validation is done automatically, by the underlying OpenSSL framework; the application need not concern itself with its mechanics. But the application does usually need to provide sets of certificates to allow this process to take place.
Python uses files to contain certificates. They should be formatted as “PEM” (see
Copy```
-----BEGIN CERTIFICATE-----
... (certificate in base64 PEM encoding) ...
-----END CERTIFICATE-----

```

### Certificate chains[¶](https://docs.python.org/3/library/ssl.html#certificate-chains "Link to this heading")
The Python files which contain certificates can contain a sequence of certificates, sometimes called a _certificate chain_. This chain should start with the specific certificate for the principal who “is” the client or server, and then the certificate for the issuer of that certificate, and then the certificate for the issuer of _that_ certificate, and so on up the chain till you get to a certificate which is _self-signed_ , that is, a certificate which has the same subject and issuer, sometimes called a _root certificate_. The certificates should just be concatenated together in the certificate file. For example, suppose we had a three certificate chain, from our server certificate to the certificate of the certification authority that signed our server certificate, to the root certificate of the agency which issued the certification authority’s certificate:
Copy```
-----BEGIN CERTIFICATE-----
... (certificate for your server)...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
... (the certificate for the CA)...
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
... (the root certificate for the CA's issuer)...
-----END CERTIFICATE-----

```

### CA certificates[¶](https://docs.python.org/3/library/ssl.html#ca-certificates "Link to this heading")
If you are going to require validation of the other side of the connection’s certificate, you need to provide a “CA certs” file, filled with the certificate chains for each issuer you are willing to trust. Again, this file just contains these chains concatenated together. For validation, Python will use the first chain it finds in the file which matches. The platform’s certificates file can be used by calling [`SSLContext.load_default_certs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs "ssl.SSLContext.load_default_certs"), this is done automatically with [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context").
### Combined key and certificate[¶](https://docs.python.org/3/library/ssl.html#combined-key-and-certificate "Link to this heading")
Often the private key is stored in the same file as the certificate; in this case, only the `certfile` parameter to [`SSLContext.load_cert_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain "ssl.SSLContext.load_cert_chain") needs to be passed. If the private key is stored with the certificate, it should come before the first certificate in the certificate chain:
Copy```
-----BEGIN RSA PRIVATE KEY-----
... (private key in base64 encoding) ...
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
... (certificate in base64 PEM encoding) ...
-----END CERTIFICATE-----

```

### Self-signed certificates[¶](https://docs.python.org/3/library/ssl.html#self-signed-certificates "Link to this heading")
If you are going to create a server that provides SSL-encrypted connection services, you will need to acquire a certificate for that service. There are many ways of acquiring appropriate certificates, such as buying one from a certification authority. Another common practice is to generate a self-signed certificate. The simplest way to do this is with the OpenSSL package, using something like the following:
Copy```
% openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
Generating a 1024 bit RSA private key
.......++++++
.............................++++++
writing new private key to 'cert.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:MyState
Locality Name (eg, city) []:Some City
Organization Name (eg, company) [Internet Widgets Pty Ltd]:My Organization, Inc.
Organizational Unit Name (eg, section) []:My Group
Common Name (eg, YOUR name) []:myserver.mygroup.myorganization.com
Email Address []:ops@myserver.mygroup.myorganization.com
%

```

The disadvantage of a self-signed certificate is that it is its own root certificate, and no one else will have it in their cache of known (and trusted) root certificates.
