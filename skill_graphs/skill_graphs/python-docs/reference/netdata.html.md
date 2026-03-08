[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html "previous chapter")
#### Next topic
[`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Internet+Data+Handling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnetdata.html&pagesource=library%2Fnetdata.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/email.html "email — An email and MIME handling package") |
  * [previous](https://docs.python.org/3/library/mmap.html "mmap — Memory-mapped file support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
  * |
  * Theme  Auto Light Dark |


# Internet Data Handling[¶](https://docs.python.org/3/library/netdata.html#internet-data-handling "Link to this heading")
This chapter describes modules which support handling data formats commonly used on the internet.
  * [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
    * [`email.message`: Representing an email message](https://docs.python.org/3/library/email.message.html)
    * [`email.parser`: Parsing email messages](https://docs.python.org/3/library/email.parser.html)
      * [FeedParser API](https://docs.python.org/3/library/email.parser.html#feedparser-api)
      * [Parser API](https://docs.python.org/3/library/email.parser.html#parser-api)
      * [Additional notes](https://docs.python.org/3/library/email.parser.html#additional-notes)
    * [`email.generator`: Generating MIME documents](https://docs.python.org/3/library/email.generator.html)
    * [`email.policy`: Policy Objects](https://docs.python.org/3/library/email.policy.html)
    * [`email.errors`: Exception and Defect classes](https://docs.python.org/3/library/email.errors.html)
    * [`email.headerregistry`: Custom Header Objects](https://docs.python.org/3/library/email.headerregistry.html)
    * [`email.contentmanager`: Managing MIME Content](https://docs.python.org/3/library/email.contentmanager.html)
      * [Content Manager Instances](https://docs.python.org/3/library/email.contentmanager.html#content-manager-instances)
    * [`email`: Examples](https://docs.python.org/3/library/email.examples.html)
    * [`email.message.Message`: Representing an email message using the `compat32` API](https://docs.python.org/3/library/email.compat32-message.html)
    * [`email.mime`: Creating email and MIME objects from scratch](https://docs.python.org/3/library/email.mime.html)
    * [`email.header`: Internationalized headers](https://docs.python.org/3/library/email.header.html)
    * [`email.charset`: Representing character sets](https://docs.python.org/3/library/email.charset.html)
    * [`email.encoders`: Encoders](https://docs.python.org/3/library/email.encoders.html)
    * [`email.utils`: Miscellaneous utilities](https://docs.python.org/3/library/email.utils.html)
    * [`email.iterators`: Iterators](https://docs.python.org/3/library/email.iterators.html)
  * [`json` — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
    * [Basic Usage](https://docs.python.org/3/library/json.html#basic-usage)
    * [Encoders and Decoders](https://docs.python.org/3/library/json.html#encoders-and-decoders)
    * [Exceptions](https://docs.python.org/3/library/json.html#exceptions)
    * [Standard Compliance and Interoperability](https://docs.python.org/3/library/json.html#standard-compliance-and-interoperability)
      * [Character Encodings](https://docs.python.org/3/library/json.html#character-encodings)
      * [Infinite and NaN Number Values](https://docs.python.org/3/library/json.html#infinite-and-nan-number-values)
      * [Repeated Names Within an Object](https://docs.python.org/3/library/json.html#repeated-names-within-an-object)
      * [Top-level Non-Object, Non-Array Values](https://docs.python.org/3/library/json.html#top-level-non-object-non-array-values)
      * [Implementation Limitations](https://docs.python.org/3/library/json.html#implementation-limitations)
    * [Command-line interface](https://docs.python.org/3/library/json.html#module-json.tool)
      * [Command-line options](https://docs.python.org/3/library/json.html#command-line-options)
  * [`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3/library/mailbox.html)
    * [`Mailbox` objects](https://docs.python.org/3/library/mailbox.html#mailbox-objects)
      * [`Maildir` objects](https://docs.python.org/3/library/mailbox.html#maildir-objects)
      * [`mbox` objects](https://docs.python.org/3/library/mailbox.html#mbox-objects)
      * [`MH` objects](https://docs.python.org/3/library/mailbox.html#mh-objects)
      * [`Babyl` objects](https://docs.python.org/3/library/mailbox.html#babyl-objects)
      * [`MMDF` objects](https://docs.python.org/3/library/mailbox.html#mmdf-objects)
    * [`Message` objects](https://docs.python.org/3/library/mailbox.html#message-objects)
      * [`MaildirMessage` objects](https://docs.python.org/3/library/mailbox.html#maildirmessage-objects)
      * [`mboxMessage` objects](https://docs.python.org/3/library/mailbox.html#mboxmessage-objects)
      * [`MHMessage` objects](https://docs.python.org/3/library/mailbox.html#mhmessage-objects)
      * [`BabylMessage` objects](https://docs.python.org/3/library/mailbox.html#babylmessage-objects)
      * [`MMDFMessage` objects](https://docs.python.org/3/library/mailbox.html#mmdfmessage-objects)
    * [Exceptions](https://docs.python.org/3/library/mailbox.html#exceptions)
    * [Examples](https://docs.python.org/3/library/mailbox.html#examples)
  * [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html)
    * [MimeTypes objects](https://docs.python.org/3/library/mimetypes.html#mimetypes-objects)
    * [Command-line usage](https://docs.python.org/3/library/mimetypes.html#command-line-usage)
    * [Command-line example](https://docs.python.org/3/library/mimetypes.html#command-line-example)
  * [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
    * [RFC 4648 Encodings](https://docs.python.org/3/library/base64.html#rfc-4648-encodings)
    * [Base85 Encodings](https://docs.python.org/3/library/base64.html#base85-encodings)
    * [Legacy Interface](https://docs.python.org/3/library/base64.html#legacy-interface)
    * [Security Considerations](https://docs.python.org/3/library/base64.html#security-considerations)
  * [`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html)
  * [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html)


#### Previous topic
[`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html "previous chapter")
#### Next topic
[`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Internet+Data+Handling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnetdata.html&pagesource=library%2Fnetdata.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/email.html "email — An email and MIME handling package") |
  * [previous](https://docs.python.org/3/library/mmap.html "mmap — Memory-mapped file support") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
