### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/celery/ "Background Tasks with Celery") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/methodoverrides/ "Adding HTTP Method Overrides") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [Request Content Checksums](https://flask.palletsprojects.com/en/stable/patterns/requestchecksum/)


# Request Content Checksums[¶](https://flask.palletsprojects.com/en/stable/patterns/requestchecksum/#request-content-checksums "Link to this heading")
Various pieces of code can consume the request data and preprocess it. For instance JSON data ends up on the request object already read and processed, form data ends up there as well but goes through a different code path. This seems inconvenient when you want to calculate the checksum of the incoming request data. This is necessary sometimes for some APIs.
Fortunately this is however very simple to change by wrapping the input stream.
The following example calculates the SHA1 checksum of the incoming data as it gets read and stores it in the WSGI environment:
```
import hashlib

class ChecksumCalcStream(object):

    def __init__(self, stream):
        self._stream = stream
        self._hash = hashlib.sha1()

    def read(self, bytes):
        rv = self._stream.read(bytes)
        self._hash.update(rv)
        return rv

    def readline(self, size_hint):
        rv = self._stream.readline(size_hint)
        self._hash.update(rv)
        return rv

def generate_checksum(request):
    env = request.environ
    stream = ChecksumCalcStream(env['wsgi.input'])
    env['wsgi.input'] = stream
    return stream._hash

```

To use this, all you need to do is to hook the calculating stream in before the request starts consuming data. (Eg: be careful accessing `request.form` or anything of that nature. `before_request_handlers` for instance should be careful not to access it).
Example usage:
```
@app.route('/special-api', methods=['POST'])
def special_api():
    hash = generate_checksum(request)
    # Accessing this parses the input stream
    files = request.files
    # At this point the hash is fully constructed.
    checksum = hash.hexdigest()
    return f"Hash was: {checksum}"

```

[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [Adding HTTP Method Overrides](https://flask.palletsprojects.com/en/stable/patterns/methodoverrides/ "previous chapter")
      * Next: [Background Tasks with Celery](https://flask.palletsprojects.com/en/stable/patterns/celery/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10129/019ccc1a-a6f3-7fb3-acbb-e7aba1d739fd/)
