This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/signals/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/signals/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/signals/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/signals/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/signals/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/signals/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/signals/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/signals/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/signals/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/signals/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/signals/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/signals/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/signals/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/signals/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/signals/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/signals/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/signals/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/signals/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/signals/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/signals/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/signals/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/signals/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/signals/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/signals/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/signals/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/signals/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/signals/)


  * [](https://docs.djangoproject.com/en/5.0/topics/signals/#top)


# Signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#module-django.dispatch "Link to this heading")
Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework. In a nutshell, signals allow certain _senders_ to notify a set of _receivers_ that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events.
For example, a third-party app can register to be notified of settings changes:
```
from django.apps import AppConfig
from django.core.signals import setting_changed


def my_callback(sender, **kwargs):
    print("Setting changed!")


class MyAppConfig(AppConfig):
    ...

    def ready(self):
        setting_changed.connect(my_callback)

```

Django’s [built-in signals](https://docs.djangoproject.com/en/5.0/ref/signals/) let user code get notified of certain actions.
You can also define and send your own custom signals. See [Defining and sending signals](https://docs.djangoproject.com/en/5.0/topics/signals/#defining-and-sending-signals) below.
Warning
Signals give the appearance of loose coupling, but they can quickly lead to code that is hard to understand, adjust and debug.
Where possible you should opt for directly calling the handling code, rather than dispatching via a signal.
## Listening to signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#listening-to-signals "Link to this heading")
To receive a signal, register a _receiver_ function using the [`Signal.connect()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.connect "django.dispatch.Signal.connect") method. The receiver function is called when the signal is sent. All of the signal’s receiver functions are called one at a time, in the order they were registered.

Signal.connect(_receiver_ , _sender =None_, _weak =True_, _dispatch_uid =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal.connect)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.connect "Link to this definition")


Parameters:

  * **receiver** – The callback function which will be connected to this signal. See [Receiver functions](https://docs.djangoproject.com/en/5.0/topics/signals/#receiver-functions) for more information.
  * **sender** – Specifies a particular sender to receive signals from. See [Connecting to signals sent by specific senders](https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-to-specific-signals) for more information.
  * **weak** – Django stores signal handlers as weak references by default. Thus, if your receiver is a local function, it may be garbage collected. To prevent this, pass `weak=False` when you call the signal’s `connect()` method.
  * **dispatch_uid** – A unique identifier for a signal receiver in cases where duplicate signals may be sent. See [Preventing duplicate signals](https://docs.djangoproject.com/en/5.0/topics/signals/#preventing-duplicate-signals) for more information.


Let’s see how this works by registering a signal that gets called after each HTTP request is finished. We’ll be connecting to the [`request_finished`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.core.signals.request_finished "django.core.signals.request_finished") signal.
### Receiver functions[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#receiver-functions "Link to this heading")
First, we need to define a receiver function. A receiver can be any Python function or method:
```
def my_callback(sender, **kwargs):
    print("Request finished!")

```

Notice that the function takes a `sender` argument, along with wildcard keyword arguments (`**kwargs`); all signal handlers must take these arguments.
We’ll look at senders [a bit later](https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-to-specific-signals), but right now look at the `**kwargs` argument. All signals send keyword arguments, and may change those keyword arguments at any time. In the case of [`request_finished`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.core.signals.request_finished "django.core.signals.request_finished"), it’s documented as sending no arguments, which means we might be tempted to write our signal handling as `my_callback(sender)`.
This would be wrong – in fact, Django will throw an error if you do so. That’s because at any point arguments could get added to the signal and your receiver must be able to handle those new arguments.
Receivers may also be asynchronous functions, with the same signature but declared using `async def`:
```
async def my_callback(sender, **kwargs):
    await asyncio.sleep(5)
    print("Request finished!")

```

Signals can be sent either synchronously or asynchronously, and receivers will automatically be adapted to the correct call-style. See [sending signals](https://docs.djangoproject.com/en/5.0/topics/signals/#sending-signals) for more information.
Changed in Django 5.0:
Support for asynchronous receivers was added.
### Connecting receiver functions[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-receiver-functions "Link to this heading")
There are two ways you can connect a receiver to a signal. You can take the manual connect route:
```
from django.core.signals import request_finished

request_finished.connect(my_callback)

```

Alternatively, you can use a [`receiver()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.receiver "django.dispatch.receiver") decorator:

receiver(_signal_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#receiver)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.receiver "Link to this definition")


Parameters:

  * **signal** – A signal or a list of signals to connect a function to.
  * **kwargs** – Wildcard keyword arguments to pass to a [function](https://docs.djangoproject.com/en/5.0/topics/signals/#receiver-functions).


Here’s how you connect with the decorator:
```
from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

```

Now, our `my_callback` function will be called each time a request finishes.
Where should this code live?
Strictly speaking, signal handling and registration code can live anywhere you like, although it’s recommended to avoid the application’s root module and its `models` module to minimize side-effects of importing code.
In practice, signal handlers are usually defined in a `signals` submodule of the application they relate to. Signal receivers are connected in the [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method of your application [configuration class](https://docs.djangoproject.com/en/5.0/ref/applications/#configuring-applications-ref). If you’re using the [`receiver()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.receiver "django.dispatch.receiver") decorator, import the `signals` submodule inside [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready"), this will implicitly connect signal handlers:
```
from django.apps import AppConfig
from django.core.signals import request_finished


class MyAppConfig(AppConfig):
    ...

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals

        # Explicitly connect a signal handler.
        request_finished.connect(signals.my_callback)

```

Note
The [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method may be executed more than once during testing, so you may want to [guard your signals from duplication](https://docs.djangoproject.com/en/5.0/topics/signals/#preventing-duplicate-signals), especially if you’re planning to send them within tests.
### Connecting to signals sent by specific senders[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-to-signals-sent-by-specific-senders "Link to this heading")
Some signals get sent many times, but you’ll only be interested in receiving a certain subset of those signals. For example, consider the [`django.db.models.signals.pre_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_save "django.db.models.signals.pre_save") signal sent before a model gets saved. Most of the time, you don’t need to know when _any_ model gets saved – just when one _specific_ model is saved.
In these cases, you can register to receive signals sent only by particular senders. In the case of [`django.db.models.signals.pre_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_save "django.db.models.signals.pre_save"), the sender will be the model class being saved, so you can indicate that you only want signals sent by some model:
```
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel


@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs): ...

```

The `my_handler` function will only be called when an instance of `MyModel` is saved.
Different signals use different objects as their senders; you’ll need to consult the [built-in signal documentation](https://docs.djangoproject.com/en/5.0/ref/signals/) for details of each particular signal.
### Preventing duplicate signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#preventing-duplicate-signals "Link to this heading")
In some circumstances, the code connecting receivers to signals may run multiple times. This can cause your receiver function to be registered more than once, and thus called as many times for a signal event. For example, the [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method may be executed more than once during testing. More generally, this occurs everywhere your project imports the module where you define the signals, because signal registration runs as many times as it is imported.
If this behavior is problematic (such as when using signals to send an email whenever a model is saved), pass a unique identifier as the `dispatch_uid` argument to identify your receiver function. This identifier will usually be a string, although any hashable object will suffice. The end result is that your receiver function will only be bound to the signal once for each unique `dispatch_uid` value:
```
from django.core.signals import request_finished

request_finished.connect(my_callback, dispatch_uid="my_unique_identifier")

```

## Defining and sending signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#defining-and-sending-signals "Link to this heading")
Your applications can take advantage of the signal infrastructure and provide its own signals.
When to use custom signals
Signals are implicit function calls which make debugging harder. If the sender and receiver of your custom signal are both within your project, you’re better off using an explicit function call.
### Defining signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#defining-signals "Link to this heading")

_class_ Signal[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal "Link to this definition")

All signals are [`django.dispatch.Signal`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal "django.dispatch.Signal") instances.
For example:
```
import django.dispatch

pizza_done = django.dispatch.Signal()

```

This declares a `pizza_done` signal.
### Sending signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#sending-signals "Link to this heading")
There are two ways to send signals synchronously in Django.

Signal.send(_sender_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal.send)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.send "Link to this definition")


Signal.send_robust(_sender_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal.send_robust)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.send_robust "Link to this definition")

Signals may also be sent asynchronously.

Signal.asend(_sender_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal.asend)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.asend "Link to this definition")


Signal.asend_robust(_sender_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal.asend_robust)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.asend_robust "Link to this definition")

To send a signal, call either [`Signal.send()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.send "django.dispatch.Signal.send"), [`Signal.send_robust()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.send_robust "django.dispatch.Signal.send_robust"), [`await Signal.asend()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.asend "django.dispatch.Signal.asend"), or [`await Signal.asend_robust()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.asend_robust "django.dispatch.Signal.asend_robust"). You must provide the `sender` argument (which is a class most of the time) and may provide as many other keyword arguments as you like.
For example, here’s how sending our `pizza_done` signal might look:
```
class PizzaStore:
    ...

    def send_pizza(self, toppings, size):
        pizza_done.send(sender=self.__class__, toppings=toppings, size=size)
        ...

```

All four methods return a list of tuple pairs `[(receiver, response), ...]`, representing the list of called receiver functions and their response values.
`send()` differs from `send_robust()` in how exceptions raised by receiver functions are handled. `send()` does _not_ catch any exceptions raised by receivers; it simply allows errors to propagate. Thus not all receivers may be notified of a signal in the face of an error.
`send_robust()` catches all errors derived from Python’s `Exception` class, and ensures all receivers are notified of the signal. If an error occurs, the error instance is returned in the tuple pair for the receiver that raised the error.
The tracebacks are present on the `__traceback__` attribute of the errors returned when calling `send_robust()`.
`asend()` is similar to `send()`, but it is a coroutine that must be awaited:
```
async def asend_pizza(self, toppings, size):
    await pizza_done.asend(sender=self.__class__, toppings=toppings, size=size)
    ...

```

Whether synchronous or asynchronous, receivers will be correctly adapted to whether `send()` or `asend()` is used. Synchronous receivers will be called using [`sync_to_async()`](https://docs.djangoproject.com/en/5.0/topics/async/#asgiref.sync.sync_to_async "asgiref.sync.sync_to_async") when invoked via `asend()`. Asynchronous receivers will be called using [`async_to_sync()`](https://docs.djangoproject.com/en/5.0/topics/async/#asgiref.sync.async_to_sync "asgiref.sync.async_to_sync") when invoked via `sync()`. Similar to the [case for middleware](https://docs.djangoproject.com/en/5.0/topics/async/#async-performance), there is a small performance cost to adapting receivers in this way. Note that in order to reduce the number of sync/async calling-style switches within a `send()` or `asend()` call, the receivers are grouped by whether or not they are async before being called. This means that an asynchronous receiver registered before a synchronous receiver may be executed after the synchronous receiver. In addition, async receivers are executed concurrently using `asyncio.gather()`.
All built-in signals, except those in the async request-response cycle, are dispatched using [`Signal.send()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.send "django.dispatch.Signal.send").
Changed in Django 5.0:
Support for asynchronous signals was added.
## Disconnecting signals[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#disconnecting-signals "Link to this heading")

Signal.disconnect(_receiver =None_, _sender =None_, _dispatch_uid =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/dispatch/dispatcher/#Signal.disconnect)[¶](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.disconnect "Link to this definition")

To disconnect a receiver from a signal, call [`Signal.disconnect()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.disconnect "django.dispatch.Signal.disconnect"). The arguments are as described in [`Signal.connect()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.connect "django.dispatch.Signal.connect"). The method returns `True` if a receiver was disconnected and `False` if not. When `sender` is passed as a lazy reference to `<app label>.<model>`, this method always returns `None`.
The `receiver` argument indicates the registered receiver to disconnect. It may be `None` if `dispatch_uid` is used to identify the receiver.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/settings/)
[System check framework ](https://docs.djangoproject.com/en/5.0/topics/checks/)
[](https://docs.djangoproject.com/en/5.0/topics/signals/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Jannis Leidel donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Signals](https://docs.djangoproject.com/en/5.0/topics/signals/)
    * [Listening to signals](https://docs.djangoproject.com/en/5.0/topics/signals/#listening-to-signals)
      * [Receiver functions](https://docs.djangoproject.com/en/5.0/topics/signals/#receiver-functions)
      * [Connecting receiver functions](https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-receiver-functions)
      * [Connecting to signals sent by specific senders](https://docs.djangoproject.com/en/5.0/topics/signals/#connecting-to-signals-sent-by-specific-senders)
      * [Preventing duplicate signals](https://docs.djangoproject.com/en/5.0/topics/signals/#preventing-duplicate-signals)
    * [Defining and sending signals](https://docs.djangoproject.com/en/5.0/topics/signals/#defining-and-sending-signals)
      * [Defining signals](https://docs.djangoproject.com/en/5.0/topics/signals/#defining-signals)
      * [Sending signals](https://docs.djangoproject.com/en/5.0/topics/signals/#sending-signals)
    * [Disconnecting signals](https://docs.djangoproject.com/en/5.0/topics/signals/#disconnecting-signals)


### Browse
  * Prev: [Django settings](https://docs.djangoproject.com/en/5.0/topics/settings/)
  * Next: [System check framework](https://docs.djangoproject.com/en/5.0/topics/checks/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Signals


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
