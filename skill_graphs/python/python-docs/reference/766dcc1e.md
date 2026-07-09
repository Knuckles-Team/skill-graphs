## FileHandler Objects[¶](https://docs.python.org/3/library/urllib.request.html#filehandler-objects "Link to this heading")

FileHandler.file_open(_req_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.FileHandler.file_open "Link to this definition")

Open the file locally, if there is no host name, or the host name is `'localhost'`.
Changed in version 3.2: This method is applicable only for local hostnames. When a remote hostname is given, a [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError") is raised.
