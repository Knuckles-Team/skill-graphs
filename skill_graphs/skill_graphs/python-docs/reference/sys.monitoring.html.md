[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html)
    * [Tool identifiers](https://docs.python.org/3/library/sys.monitoring.html#tool-identifiers)
      * [Registering and using tools](https://docs.python.org/3/library/sys.monitoring.html#registering-and-using-tools)
    * [Events](https://docs.python.org/3/library/sys.monitoring.html#events)
      * [Local events](https://docs.python.org/3/library/sys.monitoring.html#local-events)
      * [Deprecated event](https://docs.python.org/3/library/sys.monitoring.html#deprecated-event)
      * [Ancillary events](https://docs.python.org/3/library/sys.monitoring.html#ancillary-events)
      * [Other events](https://docs.python.org/3/library/sys.monitoring.html#other-events)
      * [The STOP_ITERATION event](https://docs.python.org/3/library/sys.monitoring.html#the-stop-iteration-event)
    * [Turning events on and off](https://docs.python.org/3/library/sys.monitoring.html#turning-events-on-and-off)
      * [Setting events globally](https://docs.python.org/3/library/sys.monitoring.html#setting-events-globally)
      * [Per code object events](https://docs.python.org/3/library/sys.monitoring.html#per-code-object-events)
      * [Disabling events](https://docs.python.org/3/library/sys.monitoring.html#disabling-events)
    * [Registering callback functions](https://docs.python.org/3/library/sys.monitoring.html#registering-callback-functions)
      * [Callback function arguments](https://docs.python.org/3/library/sys.monitoring.html#callback-function-arguments)


#### Previous topic
[`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html "previous chapter")
#### Next topic
[`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sys.monitoring+%E2%80%94+Execution+event+monitoring&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys.monitoring.html&pagesource=library%2Fsys.monitoring.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sysconfig.html "sysconfig — Provide access to Python’s configuration information") |
  * [previous](https://docs.python.org/3/library/sys.html "sys — System-specific parameters and functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html)
  * |
  * Theme  Auto Light Dark |


#  `sys.monitoring` — Execution event monitoring[¶](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "Link to this heading")
Added in version 3.12.
* * *
Note
`sys.monitoring` is a namespace within the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") module, not an independent module, so there is no need to `import sys.monitoring`, simply `import sys` and then use `sys.monitoring`.
This namespace provides access to the functions and constants necessary to activate and control event monitoring.
As programs execute, events occur that might be of interest to tools that monitor execution. The `sys.monitoring` namespace provides means to receive callbacks when events of interest occur.
The monitoring API consists of three components:
  * [Tool identifiers](https://docs.python.org/3/library/sys.monitoring.html#tool-identifiers)
  * [Events](https://docs.python.org/3/library/sys.monitoring.html#events)
  * [Callbacks](https://docs.python.org/3/library/sys.monitoring.html#callbacks)


## Tool identifiers[¶](https://docs.python.org/3/library/sys.monitoring.html#tool-identifiers "Link to this heading")
A tool identifier is an integer and the associated name. Tool identifiers are used to discourage tools from interfering with each other and to allow multiple tools to operate at the same time. Currently tools are completely independent and cannot be used to monitor each other. This restriction may be lifted in the future.
Before registering or activating events, a tool should choose an identifier. Identifiers are integers in the range 0 to 5 inclusive.
### Registering and using tools[¶](https://docs.python.org/3/library/sys.monitoring.html#registering-and-using-tools "Link to this heading")

sys.monitoring.use_tool_id(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _name :[str](https://docs.python.org/3/library/stdtypes.html#str "str")_, _/_) → [None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.use_tool_id "Link to this definition")

Must be called before _tool_id_ can be used. _tool_id_ must be in the range 0 to 5 inclusive. Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _tool_id_ is in use.

sys.monitoring.clear_tool_id(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _/_) → [None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.clear_tool_id "Link to this definition")

Unregister all events and callback functions associated with _tool_id_.

sys.monitoring.free_tool_id(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _/_) → [None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.free_tool_id "Link to this definition")

Should be called once a tool no longer requires _tool_id_. Will call [`clear_tool_id()`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.clear_tool_id "sys.monitoring.clear_tool_id") before releasing _tool_id_.

sys.monitoring.get_tool(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _/_) → [str](https://docs.python.org/3/library/stdtypes.html#str "str")|[None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.get_tool "Link to this definition")

Returns the name of the tool if _tool_id_ is in use, otherwise it returns `None`. _tool_id_ must be in the range 0 to 5 inclusive.
All IDs are treated the same by the VM with regard to events, but the following IDs are pre-defined to make co-operation of tools easier:
Copy```
sys.monitoring.DEBUGGER_ID = 0
sys.monitoring.COVERAGE_ID = 1
sys.monitoring.PROFILER_ID = 2
sys.monitoring.OPTIMIZER_ID = 5

```

## Events[¶](https://docs.python.org/3/library/sys.monitoring.html#events "Link to this heading")
The following events are supported:

sys.monitoring.events.BRANCH_LEFT[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT "Link to this definition")

A conditional branch goes left.
It is up to the tool to determine how to present “left” and “right” branches. There is no guarantee which branch is “left” and which is “right”, except that it will be consistent for the duration of the program.

sys.monitoring.events.BRANCH_RIGHT[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT "Link to this definition")

A conditional branch goes right.

sys.monitoring.events.CALL[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-CALL "Link to this definition")

A call in Python code (event occurs before the call).

sys.monitoring.events.C_RAISE[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RAISE "Link to this definition")

An exception raised from any callable, except for Python functions (event occurs after the exit).

sys.monitoring.events.C_RETURN[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RETURN "Link to this definition")

Return from any callable, except for Python functions (event occurs after the return).

sys.monitoring.events.EXCEPTION_HANDLED[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-EXCEPTION_HANDLED "Link to this definition")

An exception is handled.

sys.monitoring.events.INSTRUCTION[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-INSTRUCTION "Link to this definition")

A VM instruction is about to be executed.

sys.monitoring.events.JUMP[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-JUMP "Link to this definition")

An unconditional jump in the control flow graph is made.

sys.monitoring.events.LINE[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-LINE "Link to this definition")

An instruction is about to be executed that has a different line number from the preceding instruction.

sys.monitoring.events.PY_RESUME[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RESUME "Link to this definition")

Resumption of a Python function (for generator and coroutine functions), except for `throw()` calls.

sys.monitoring.events.PY_RETURN[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RETURN "Link to this definition")

Return from a Python function (occurs immediately before the return, the callee’s frame will be on the stack).

sys.monitoring.events.PY_START[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_START "Link to this definition")

Start of a Python function (occurs immediately after the call, the callee’s frame will be on the stack)

sys.monitoring.events.PY_THROW[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_THROW "Link to this definition")

A Python function is resumed by a `throw()` call.

sys.monitoring.events.PY_UNWIND[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_UNWIND "Link to this definition")

Exit from a Python function during exception unwinding. This includes exceptions raised directly within the function and that are allowed to continue to propagate.

sys.monitoring.events.PY_YIELD[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_YIELD "Link to this definition")

Yield from a Python function (occurs immediately before the yield, the callee’s frame will be on the stack).

sys.monitoring.events.RAISE[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE "Link to this definition")

An exception is raised, except those that cause a [`STOP_ITERATION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION) event.

sys.monitoring.events.RERAISE[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RERAISE "Link to this definition")

An exception is re-raised, for example at the end of a [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) block.

sys.monitoring.events.STOP_ITERATION[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION "Link to this definition")

An artificial [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") is raised; see [the STOP_ITERATION event](https://docs.python.org/3/library/sys.monitoring.html#the-stop-iteration-event).
More events may be added in the future.
These events are attributes of the `sys.monitoring.events` namespace. Each event is represented as a power-of-2 integer constant. To define a set of events, simply bitwise OR the individual events together. For example, to specify both [`PY_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RETURN) and [`PY_START`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_START) events, use the expression `PY_RETURN | PY_START`.

sys.monitoring.events.NO_EVENTS[¶](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-NO_EVENTS "Link to this definition")

An alias for `0` so users can do explicit comparisons like:
Copy```
if get_events(DEBUGGER_ID) == NO_EVENTS:
    ...

```

Setting this event deactivates all events.
### Local events[¶](https://docs.python.org/3/library/sys.monitoring.html#local-events "Link to this heading")
Local events are associated with normal execution of the program and happen at clearly defined locations. All local events can be disabled. The local events are:
  * [`PY_START`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_START)
  * [`PY_RESUME`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RESUME)
  * [`PY_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RETURN)
  * [`PY_YIELD`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_YIELD)
  * [`CALL`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-CALL)
  * [`LINE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-LINE)
  * [`INSTRUCTION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-INSTRUCTION)
  * [`JUMP`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-JUMP)
  * [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT)
  * [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT)
  * [`STOP_ITERATION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION)


### Deprecated event[¶](https://docs.python.org/3/library/sys.monitoring.html#deprecated-event "Link to this heading")
  * `BRANCH`


The `BRANCH` event is deprecated in 3.14. Using [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT) and [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) events will give much better performance as they can be disabled independently.
### Ancillary events[¶](https://docs.python.org/3/library/sys.monitoring.html#ancillary-events "Link to this heading")
Ancillary events can be monitored like other events, but are controlled by another event:
  * [`C_RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RAISE)
  * [`C_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RETURN)


The [`C_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RETURN) and [`C_RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RAISE) events are controlled by the [`CALL`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-CALL) event. `C_RETURN` and `C_RAISE` events will only be seen if the corresponding `CALL` event is being monitored.
### Other events[¶](https://docs.python.org/3/library/sys.monitoring.html#other-events "Link to this heading")
Other events are not necessarily tied to a specific location in the program and cannot be individually disabled via [`DISABLE`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "sys.monitoring.DISABLE").
The other events that can be monitored are:
  * [`PY_THROW`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_THROW)
  * [`PY_UNWIND`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_UNWIND)
  * [`RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE)
  * [`EXCEPTION_HANDLED`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-EXCEPTION_HANDLED)


### The STOP_ITERATION event[¶](https://docs.python.org/3/library/sys.monitoring.html#the-stop-iteration-event "Link to this heading")
[**PEP 380**](https://peps.python.org/pep-0380/#use-of-stopiteration-to-return-values) specifies that a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") exception is raised when returning a value from a generator or coroutine. However, this is a very inefficient way to return a value, so some Python implementations, notably CPython 3.12+, do not raise an exception unless it would be visible to other code.
To allow tools to monitor for real exceptions without slowing down generators and coroutines, the [`STOP_ITERATION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION) event is provided. `STOP_ITERATION` can be locally disabled, unlike [`RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE).
Note that the [`STOP_ITERATION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION) event and the [`RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE) event for a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") exception are equivalent, and are treated as interchangeable when generating events. Implementations will favor `STOP_ITERATION` for performance reasons, but may generate a `RAISE` event with a `StopIteration`.
## Turning events on and off[¶](https://docs.python.org/3/library/sys.monitoring.html#turning-events-on-and-off "Link to this heading")
In order to monitor an event, it must be turned on and a corresponding callback must be registered. Events can be turned on or off by setting the events either globally and/or for a particular code object. An event will trigger only once, even if it is turned on both globally and locally.
### Setting events globally[¶](https://docs.python.org/3/library/sys.monitoring.html#setting-events-globally "Link to this heading")
Events can be controlled globally by modifying the set of events being monitored.

sys.monitoring.get_events(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _/_) → [int](https://docs.python.org/3/library/functions.html#int "int")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.get_events "Link to this definition")

Returns the `int` representing all the active events.

sys.monitoring.set_events(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _event_set :[int](https://docs.python.org/3/library/functions.html#int "int")_, _/_) → [None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.set_events "Link to this definition")

Activates all events which are set in _event_set_. Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _tool_id_ is not in use.
No events are active by default.
### Per code object events[¶](https://docs.python.org/3/library/sys.monitoring.html#per-code-object-events "Link to this heading")
Events can also be controlled on a per code object basis. The functions defined below which accept a [`types.CodeType`](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType") should be prepared to accept a look-alike object from functions which are not defined in Python (see [Monitoring C API](https://docs.python.org/3/c-api/monitoring.html#c-api-monitoring)).

sys.monitoring.get_local_events(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _code :[CodeType](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType")_, _/_) → [int](https://docs.python.org/3/library/functions.html#int "int")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.get_local_events "Link to this definition")

Returns all the [local events](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-local) for _code_

sys.monitoring.set_local_events(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _code :[CodeType](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType")_, _event_set :[int](https://docs.python.org/3/library/functions.html#int "int")_, _/_) → [None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.set_local_events "Link to this definition")

Activates all the [local events](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-local) for _code_ which are set in _event_set_. Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _tool_id_ is not in use.
### Disabling events[¶](https://docs.python.org/3/library/sys.monitoring.html#disabling-events "Link to this heading")

sys.monitoring.DISABLE[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "Link to this definition")

A special value that can be returned from a callback function to disable events for the current code location.
[Local events](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-local) can be disabled for a specific code location by returning [`sys.monitoring.DISABLE`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "sys.monitoring.DISABLE") from a callback function. This does not change which events are set, or any other code locations for the same event.
Disabling events for specific locations is very important for high performance monitoring. For example, a program can be run under a debugger with no overhead if the debugger disables all monitoring except for a few breakpoints.
If [`DISABLE`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "sys.monitoring.DISABLE") is returned by a callback for a [global event](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-global), [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised by the interpreter in a non-specific location (that is, no traceback will be provided).

sys.monitoring.restart_events() → [None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.restart_events "Link to this definition")

Enable all the events that were disabled by [`sys.monitoring.DISABLE`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "sys.monitoring.DISABLE") for all tools.
## Registering callback functions[¶](https://docs.python.org/3/library/sys.monitoring.html#registering-callback-functions "Link to this heading")

sys.monitoring.register_callback(_tool_id :[int](https://docs.python.org/3/library/functions.html#int "int")_, _event :[int](https://docs.python.org/3/library/functions.html#int "int")_, _func :[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")|[None](https://docs.python.org/3/library/constants.html#None "None")_, _/_) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable")|[None](https://docs.python.org/3/library/constants.html#None "None")[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.register_callback "Link to this definition")

Registers the callable _func_ for the _event_ with the given _tool_id_
If another callback was registered for the given _tool_id_ and _event_ , it is unregistered and returned. Otherwise `register_callback()` returns `None`.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `sys.monitoring.register_callback` with argument `func`.
Functions can be unregistered by calling `sys.monitoring.register_callback(tool_id, event, None)`.
Callback functions can be registered and unregistered at any time.
Callbacks are called only once regardless if the event is turned on both globally and locally. As such, if an event could be turned on for both global and local events by your code then the callback needs to be written to handle either trigger.
### Callback function arguments[¶](https://docs.python.org/3/library/sys.monitoring.html#callback-function-arguments "Link to this heading")

sys.monitoring.MISSING[¶](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.MISSING "Link to this definition")

A special value that is passed to a callback function to indicate that there are no arguments to the call.
When an active event occurs, the registered callback function is called. Callback functions returning an object other than [`DISABLE`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "sys.monitoring.DISABLE") will have no effect. Different events will provide the callback function with different arguments, as follows:
  * [`PY_START`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_START) and [`PY_RESUME`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RESUME):
Copy```
func(code: CodeType, instruction_offset: int) -> object

```

  * [`PY_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RETURN) and [`PY_YIELD`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_YIELD):
Copy```
func(code: CodeType, instruction_offset: int, retval: object) -> object

```

  * [`CALL`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-CALL), [`C_RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RAISE) and [`C_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RETURN) (_arg0_ can be [`MISSING`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.MISSING "sys.monitoring.MISSING") specifically):
Copy```
func(code: CodeType, instruction_offset: int, callable: object, arg0: object) -> object

```

_code_ represents the code object where the call is being made, while _callable_ is the object that is about to be called (and thus triggered the event). If there are no arguments, _arg0_ is set to [`sys.monitoring.MISSING`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.MISSING "sys.monitoring.MISSING").
For instance methods, _callable_ will be the function object as found on the class with _arg0_ set to the instance (i.e. the `self` argument to the method).
  * [`RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE), [`RERAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RERAISE), [`EXCEPTION_HANDLED`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-EXCEPTION_HANDLED), [`PY_UNWIND`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_UNWIND), [`PY_THROW`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_THROW) and [`STOP_ITERATION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION):
Copy```
func(code: CodeType, instruction_offset: int, exception: BaseException) -> object

```

  * [`LINE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-LINE):
Copy```
func(code: CodeType, line_number: int) -> object

```

  * [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT), [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) and [`JUMP`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-JUMP):
Copy```
func(code: CodeType, instruction_offset: int, destination_offset: int) -> object

```

Note that the _destination_offset_ is where the code will next execute.
  * [`INSTRUCTION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-INSTRUCTION):
Copy```
func(code: CodeType, instruction_offset: int) -> object

```



### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html)
    * [Tool identifiers](https://docs.python.org/3/library/sys.monitoring.html#tool-identifiers)
      * [Registering and using tools](https://docs.python.org/3/library/sys.monitoring.html#registering-and-using-tools)
    * [Events](https://docs.python.org/3/library/sys.monitoring.html#events)
      * [Local events](https://docs.python.org/3/library/sys.monitoring.html#local-events)
      * [Deprecated event](https://docs.python.org/3/library/sys.monitoring.html#deprecated-event)
      * [Ancillary events](https://docs.python.org/3/library/sys.monitoring.html#ancillary-events)
      * [Other events](https://docs.python.org/3/library/sys.monitoring.html#other-events)
      * [The STOP_ITERATION event](https://docs.python.org/3/library/sys.monitoring.html#the-stop-iteration-event)
    * [Turning events on and off](https://docs.python.org/3/library/sys.monitoring.html#turning-events-on-and-off)
      * [Setting events globally](https://docs.python.org/3/library/sys.monitoring.html#setting-events-globally)
      * [Per code object events](https://docs.python.org/3/library/sys.monitoring.html#per-code-object-events)
      * [Disabling events](https://docs.python.org/3/library/sys.monitoring.html#disabling-events)
    * [Registering callback functions](https://docs.python.org/3/library/sys.monitoring.html#registering-callback-functions)
      * [Callback function arguments](https://docs.python.org/3/library/sys.monitoring.html#callback-function-arguments)


#### Previous topic
[`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html "previous chapter")
#### Next topic
[`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sys.monitoring+%E2%80%94+Execution+event+monitoring&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys.monitoring.html&pagesource=library%2Fsys.monitoring.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/sysconfig.html "sysconfig — Provide access to Python’s configuration information") |
  * [previous](https://docs.python.org/3/library/sys.html "sys — System-specific parameters and functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
