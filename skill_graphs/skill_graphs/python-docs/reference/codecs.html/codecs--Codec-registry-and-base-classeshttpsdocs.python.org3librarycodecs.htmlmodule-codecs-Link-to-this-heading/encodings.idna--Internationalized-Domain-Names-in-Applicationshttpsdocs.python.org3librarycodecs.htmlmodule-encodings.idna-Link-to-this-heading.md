##  `encodings.idna` — Internationalized Domain Names in Applications[¶](https://docs.python.org/3/library/codecs.html#module-encodings.idna "Link to this heading")
This module implements `punycode` encoding and [`stringprep`](https://docs.python.org/3/library/stringprep.html#module-stringprep "stringprep: String preparation, as per RFC 3453").
If you need the IDNA 2008 standard from
These RFCs together define a protocol to support non-ASCII characters in domain names. A domain name containing non-ASCII characters (such as `www.Alliancefrançaise.nu`) is converted into an ASCII-compatible encoding (ACE, such as `www.xn--alliancefranaise-npb.nu`). The ACE form of the domain name is then used in all places where arbitrary characters are not allowed by the protocol, such as DNS queries, HTTP _Host_ fields, and so on. This conversion is carried out in the application; if possible invisible to the user: The application should transparently convert Unicode domain labels to IDNA on the wire, and convert back ACE labels to Unicode before presenting them to the user.
Python supports this conversion in several ways: the `idna` codec performs conversion between Unicode and ACE, separating an input string into labels based on the separator characters defined in `.` separator and converting any ACE labels found into unicode. Furthermore, the [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module transparently converts Unicode host names to ACE, so that applications need not be concerned about converting host names themselves when they pass them to the socket module. On top of that, modules that have host names as function parameters, such as [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client \(requires sockets\).") and [`ftplib`](https://docs.python.org/3/library/ftplib.html#module-ftplib "ftplib: FTP protocol client \(requires sockets\)."), accept Unicode host names (`http.client` then also transparently sends an IDNA hostname in the _Host_ field if it sends that field at all).
When receiving host names from the wire (such as in reverse name lookup), no automatic conversion to Unicode is performed: applications wishing to present such host names to the user should decode them to Unicode.
The module `encodings.idna` also implements the nameprep procedure, which performs certain normalizations on host names, to achieve case-insensitivity of international domain names, and to unify similar characters. The nameprep functions can be used directly if desired.

encodings.idna.nameprep(_label_)[¶](https://docs.python.org/3/library/codecs.html#encodings.idna.nameprep "Link to this definition")

Return the nameprepped version of _label_. The implementation currently assumes query strings, so `AllowUnassigned` is true.

encodings.idna.ToASCII(_label_)[¶](https://docs.python.org/3/library/codecs.html#encodings.idna.ToASCII "Link to this definition")

Convert a label to ASCII, as specified in `UseSTD3ASCIIRules` is assumed to be false.

encodings.idna.ToUnicode(_label_)[¶](https://docs.python.org/3/library/codecs.html#encodings.idna.ToUnicode "Link to this definition")

Convert a label to Unicode, as specified in
