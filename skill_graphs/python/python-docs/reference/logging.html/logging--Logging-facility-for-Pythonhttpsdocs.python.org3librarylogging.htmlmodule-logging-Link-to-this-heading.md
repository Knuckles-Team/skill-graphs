#  `logging` — Logging facility for Python[¶](https://docs.python.org/3/library/logging.html#module-logging "Link to this heading")
**Source code:**
Important
This page contains the API reference information. For tutorial information and discussion of more advanced topics, see
  * [Basic Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
  * [Advanced Tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
  * [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)


* * *
This module defines functions and classes which implement a flexible event logging system for applications and libraries.
The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.
Here’s a simple example of idiomatic usage:
Copy```
