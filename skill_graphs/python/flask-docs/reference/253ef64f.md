## Message Flashing[¶](https://flask.palletsprojects.com/en/stable/api/#message-flashing "Link to this heading")

flask.flash(_message_ , _category ='message'_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.flash "Link to this definition")

Flashes a message to the next request. In order to remove the flashed message from the session and to display it to the user, the template has to call [`get_flashed_messages()`](https://flask.palletsprojects.com/en/stable/api/#flask.get_flashed_messages "flask.get_flashed_messages").
Changelog
Changed in version 0.3: `category` parameter added.

Parameters:

  * **message** (
  * **category** (`'message'` for any kind of message, `'error'` for errors, `'info'` for information messages and `'warning'` for warnings. However any kind of string can be used as category.



Return type:

None

flask.get_flashed_messages(_with_categories =False_, _category_filter =()_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.get_flashed_messages "Link to this definition")

Pulls all flashed messages from the session and returns them. Further calls in the same request to the function will return the same messages. By default just the messages are returned, but when `with_categories` is set to `True`, the return value will be a list of tuples in the form `(category, message)` instead.
Filter the flashed messages to one or more categories by providing those categories in `category_filter`. This allows rendering categories in separate html blocks. The `with_categories` and `category_filter` arguments are distinct:
  * `with_categories` controls whether categories are returned with message text (`True` gives a tuple, where `False` gives just the message text).
  * `category_filter` filters the messages down to only those matching the provided categories.


See [Message Flashing](https://flask.palletsprojects.com/en/stable/patterns/flashing/) for examples.
Changelog
Changed in version 0.9: `category_filter` parameter added.
Changed in version 0.3: `with_categories` parameter added.

Parameters:

  * **with_categories** (`True` to also receive categories.
  * **category_filter** (_[__]_) – filter of categories to limit return values. Only categories in the list will be returned.



Return type:
