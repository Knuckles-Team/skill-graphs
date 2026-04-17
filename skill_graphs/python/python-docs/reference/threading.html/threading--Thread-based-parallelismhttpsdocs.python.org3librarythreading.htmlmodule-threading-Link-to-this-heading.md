#  `threading` — Thread-based parallelism[¶](https://docs.python.org/3/library/threading.html#module-threading "Link to this heading")
**Source code:**
* * *
This module constructs higher-level threading interfaces on top of the lower level [`_thread`](https://docs.python.org/3/library/_thread.html#module-_thread "_thread: Low-level threading API.") module.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
## Introduction[¶](https://docs.python.org/3/library/threading.html#introduction "Link to this heading")
The `threading` module provides a way to run multiple
A typical use case for `threading` includes managing a pool of worker threads that can process multiple tasks concurrently. Here’s a basic example of creating and starting threads using [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread"):
Copy```
import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)  # Blocking I/O (simulating a network request)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]
