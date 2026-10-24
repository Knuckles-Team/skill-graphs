## Python Bytecode Instructions[¶](https://docs.python.org/3/library/dis.html#python-bytecode-instructions "Link to this heading")
The [`get_instructions()`](https://docs.python.org/3/library/dis.html#dis.get_instructions "dis.get_instructions") function and [`Bytecode`](https://docs.python.org/3/library/dis.html#dis.Bytecode "dis.Bytecode") class provide details of bytecode instructions as [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction") instances:

_class_ dis.Instruction[¶](https://docs.python.org/3/library/dis.html#dis.Instruction "Link to this definition")

Details for a bytecode operation

opcode[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.opcode "Link to this definition")

numeric code for operation, corresponding to the opcode values listed below and the bytecode values in the [Opcode collections](https://docs.python.org/3/library/dis.html#opcode-collections).

opname[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.opname "Link to this definition")

human readable name for operation

baseopcode[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.baseopcode "Link to this definition")

numeric code for the base operation if operation is specialized; otherwise equal to [`opcode`](https://docs.python.org/3/library/dis.html#dis.Instruction.opcode "dis.Instruction.opcode")

baseopname[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.baseopname "Link to this definition")

human readable name for the base operation if operation is specialized; otherwise equal to [`opname`](https://docs.python.org/3/library/dis.html#dis.opname "dis.opname")

arg[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.arg "Link to this definition")

numeric argument to operation (if any), otherwise `None`

oparg[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.oparg "Link to this definition")

alias for [`arg`](https://docs.python.org/3/library/dis.html#dis.Instruction.arg "dis.Instruction.arg")

argval[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.argval "Link to this definition")

resolved arg value (if any), otherwise `None`

argrepr[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.argrepr "Link to this definition")

human readable description of operation argument (if any), otherwise an empty string.

offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.offset "Link to this definition")

start index of operation within bytecode sequence

start_offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.start_offset "Link to this definition")

start index of operation within bytecode sequence, including prefixed `EXTENDED_ARG` operations if present; otherwise equal to [`offset`](https://docs.python.org/3/library/dis.html#dis.Instruction.offset "dis.Instruction.offset")

cache_offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.cache_offset "Link to this definition")

start index of the cache entries following the operation

end_offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.end_offset "Link to this definition")

end index of the cache entries following the operation

starts_line[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.starts_line "Link to this definition")

`True` if this opcode starts a source line, otherwise `False`

line_number[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.line_number "Link to this definition")

source line number associated with this opcode (if any), otherwise `None`

is_jump_target[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.is_jump_target "Link to this definition")

`True` if other code jumps to here, otherwise `False`

jump_target[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.jump_target "Link to this definition")

bytecode index of the jump target if this is a jump operation, otherwise `None`

positions[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.positions "Link to this definition")

[`dis.Positions`](https://docs.python.org/3/library/dis.html#dis.Positions "dis.Positions") object holding the start and end locations that are covered by this instruction.

cache_info[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.cache_info "Link to this definition")

Information about the cache entries of this instruction, as triplets of the form `(name, size, data)`, where the `name` and `size` describe the cache format and data is the contents of the cache. `cache_info` is `None` if the instruction does not have caches.
Added in version 3.4.
Changed in version 3.11: Field `positions` is added.
Changed in version 3.13: Changed field `starts_line`.
Added fields `start_offset`, `cache_offset`, `end_offset`, `baseopname`, `baseopcode`, `jump_target`, `oparg`, `line_number` and `cache_info`.

_class_ dis.Positions[¶](https://docs.python.org/3/library/dis.html#dis.Positions "Link to this definition")

In case the information is not available, some fields might be `None`.

lineno[¶](https://docs.python.org/3/library/dis.html#dis.Positions.lineno "Link to this definition")


end_lineno[¶](https://docs.python.org/3/library/dis.html#dis.Positions.end_lineno "Link to this definition")


col_offset[¶](https://docs.python.org/3/library/dis.html#dis.Positions.col_offset "Link to this definition")


end_col_offset[¶](https://docs.python.org/3/library/dis.html#dis.Positions.end_col_offset "Link to this definition")

Added in version 3.11.
The Python compiler currently generates the following bytecode instructions.
**General instructions**
In the following, We will refer to the interpreter stack as `STACK` and describe operations on it as if it was a Python list. The top of the stack corresponds to `STACK[-1]` in this language.

NOP[¶](https://docs.python.org/3/library/dis.html#opcode-NOP "Link to this definition")

Do nothing code. Used as a placeholder by the bytecode optimizer, and to generate line tracing events.

NOT_TAKEN[¶](https://docs.python.org/3/library/dis.html#opcode-NOT_TAKEN "Link to this definition")

Do nothing code. Used by the interpreter to record [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT) and [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) events for [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring").
Added in version 3.14.

POP_ITER[¶](https://docs.python.org/3/library/dis.html#opcode-POP_ITER "Link to this definition")

Removes the iterator from the top of the stack.
Added in version 3.14.

POP_TOP[¶](https://docs.python.org/3/library/dis.html#opcode-POP_TOP "Link to this definition")

Removes the top-of-stack item:
Copy```
STACK.pop()

```


END_FOR[¶](https://docs.python.org/3/library/dis.html#opcode-END_FOR "Link to this definition")

Removes the top-of-stack item. Equivalent to `POP_TOP`. Used to clean up at the end of loops, hence the name.
Added in version 3.12.

END_SEND[¶](https://docs.python.org/3/library/dis.html#opcode-END_SEND "Link to this definition")

Implements `del STACK[-2]`. Used to clean up when a generator exits.
Added in version 3.12.

COPY(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-COPY "Link to this definition")

Push the i-th item to the top of the stack without removing it from its original location:
Copy```
assert i > 0
STACK.append(STACK[-i])

```

Added in version 3.11.

SWAP(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-SWAP "Link to this definition")

Swap the top of the stack with the i-th element:
Copy```
STACK[-i], STACK[-1] = STACK[-1], STACK[-i]

```

Added in version 3.11.

CACHE[¶](https://docs.python.org/3/library/dis.html#opcode-CACHE "Link to this definition")

Rather than being an actual instruction, this opcode is used to mark extra space for the interpreter to cache useful data directly in the bytecode itself. It is automatically hidden by all `dis` utilities, but can be viewed with `show_caches=True`.
Logically, this space is part of the preceding instruction. Many opcodes expect to be followed by an exact number of caches, and will instruct the interpreter to skip over them at runtime.
Populated caches can look like arbitrary instructions, so great care should be taken when reading or modifying raw, adaptive bytecode containing quickened data.
Added in version 3.11.
**Unary operations**
Unary operations take the top of the stack, apply the operation, and push the result back on the stack.

UNARY_NEGATIVE[¶](https://docs.python.org/3/library/dis.html#opcode-UNARY_NEGATIVE "Link to this definition")

Implements `STACK[-1] = -STACK[-1]`.

UNARY_NOT[¶](https://docs.python.org/3/library/dis.html#opcode-UNARY_NOT "Link to this definition")

Implements `STACK[-1] = not STACK[-1]`.
Changed in version 3.13: This instruction now requires an exact [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") operand.

UNARY_INVERT[¶](https://docs.python.org/3/library/dis.html#opcode-UNARY_INVERT "Link to this definition")

Implements `STACK[-1] = ~STACK[-1]`.

GET_ITER[¶](https://docs.python.org/3/library/dis.html#opcode-GET_ITER "Link to this definition")

Implements `STACK[-1] = iter(STACK[-1])`.

GET_YIELD_FROM_ITER[¶](https://docs.python.org/3/library/dis.html#opcode-GET_YIELD_FROM_ITER "Link to this definition")

If `STACK[-1]` is a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator) or [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) object it is left as is. Otherwise, implements `STACK[-1] = iter(STACK[-1])`.
Added in version 3.5.

TO_BOOL[¶](https://docs.python.org/3/library/dis.html#opcode-TO_BOOL "Link to this definition")

Implements `STACK[-1] = bool(STACK[-1])`.
Added in version 3.13.
**Binary and in-place operations**
Binary operations remove the top two items from the stack (`STACK[-1]` and `STACK[-2]`). They perform the operation, then put the result back on the stack.
In-place operations are like binary operations, but the operation is done in-place when `STACK[-2]` supports it, and the resulting `STACK[-1]` may be (but does not have to be) the original `STACK[-2]`.

BINARY_OP(_op_)[¶](https://docs.python.org/3/library/dis.html#opcode-BINARY_OP "Link to this definition")

Implements the binary and in-place operators (depending on the value of _op_):
Copy```
rhs = STACK.pop()
lhs = STACK.pop()
STACK.append(lhs op rhs)

```

Added in version 3.11.
Changed in version 3.14: With oparg :`NB_SUBSCR`, implements binary subscript (replaces opcode `BINARY_SUBSCR`)

STORE_SUBSCR[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_SUBSCR "Link to this definition")

Implements:
Copy```
key = STACK.pop()
container = STACK.pop()
value = STACK.pop()
container[key] = value

```


DELETE_SUBSCR[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_SUBSCR "Link to this definition")

Implements:
Copy```
key = STACK.pop()
container = STACK.pop()
del container[key]

```


BINARY_SLICE[¶](https://docs.python.org/3/library/dis.html#opcode-BINARY_SLICE "Link to this definition")

Implements:
Copy```
end = STACK.pop()
start = STACK.pop()
container = STACK.pop()
STACK.append(container[start:end])

```

Added in version 3.12.

STORE_SLICE[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_SLICE "Link to this definition")

Implements:
Copy```
end = STACK.pop()
start = STACK.pop()
container = STACK.pop()
value = STACK.pop()
container[start:end] = value

```

Added in version 3.12.
**Coroutine opcodes**

GET_AWAITABLE(_where_)[¶](https://docs.python.org/3/library/dis.html#opcode-GET_AWAITABLE "Link to this definition")

Implements `STACK[-1] = get_awaitable(STACK[-1])`, where `get_awaitable(o)` returns `o` if `o` is a coroutine object or a generator object with the [`CO_ITERABLE_COROUTINE`](https://docs.python.org/3/library/inspect.html#inspect.CO_ITERABLE_COROUTINE "inspect.CO_ITERABLE_COROUTINE") flag, or resolves `o.__await__`.
> If the `where` operand is nonzero, it indicates where the instruction occurs:
>   * `1`: After a call to `__aenter__`
>   * `2`: After a call to `__aexit__`
>

Added in version 3.5.
Changed in version 3.11: Previously, this instruction did not have an oparg.

GET_AITER[¶](https://docs.python.org/3/library/dis.html#opcode-GET_AITER "Link to this definition")

Implements `STACK[-1] = STACK[-1].__aiter__()`.
Added in version 3.5.
Changed in version 3.7: Returning awaitable objects from `__aiter__` is no longer supported.

GET_ANEXT[¶](https://docs.python.org/3/library/dis.html#opcode-GET_ANEXT "Link to this definition")

Implement `STACK.append(get_awaitable(STACK[-1].__anext__()))` to the stack. See `GET_AWAITABLE` for details about `get_awaitable`.
Added in version 3.5.

END_ASYNC_FOR[¶](https://docs.python.org/3/library/dis.html#opcode-END_ASYNC_FOR "Link to this definition")

Terminates an [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for) loop. Handles an exception raised when awaiting a next item. The stack contains the async iterable in `STACK[-2]` and the raised exception in `STACK[-1]`. Both are popped. If the exception is not [`StopAsyncIteration`](https://docs.python.org/3/library/exceptions.html#StopAsyncIteration "StopAsyncIteration"), it is re-raised.
Added in version 3.8.
Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

CLEANUP_THROW[¶](https://docs.python.org/3/library/dis.html#opcode-CLEANUP_THROW "Link to this definition")

Handles an exception raised during a [`throw()`](https://docs.python.org/3/reference/expressions.html#generator.throw "generator.throw") or [`close()`](https://docs.python.org/3/reference/expressions.html#generator.close "generator.close") call through the current frame. If `STACK[-1]` is an instance of [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration"), pop three values from the stack and push its `value` member. Otherwise, re-raise `STACK[-1]`.
Added in version 3.12.
**Miscellaneous opcodes**

SET_ADD(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-SET_ADD "Link to this definition")

Implements:
Copy```
item = STACK.pop()
set.add(STACK[-i], item)

```

Used to implement set comprehensions.

LIST_APPEND(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LIST_APPEND "Link to this definition")

Implements:
Copy```
item = STACK.pop()
list.append(STACK[-i], item)

```

Used to implement list comprehensions.

MAP_ADD(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-MAP_ADD "Link to this definition")

Implements:
Copy```
value = STACK.pop()
key = STACK.pop()
dict.__setitem__(STACK[-i], key, value)

```

Used to implement dict comprehensions.
Added in version 3.1.
Changed in version 3.8: Map value is `STACK[-1]` and map key is `STACK[-2]`. Before, those were reversed.
For all of the [`SET_ADD`](https://docs.python.org/3/library/dis.html#opcode-SET_ADD), [`LIST_APPEND`](https://docs.python.org/3/library/dis.html#opcode-LIST_APPEND) and [`MAP_ADD`](https://docs.python.org/3/library/dis.html#opcode-MAP_ADD) instructions, while the added value or key/value pair is popped off, the container object remains on the stack so that it is available for further iterations of the loop.

RETURN_VALUE[¶](https://docs.python.org/3/library/dis.html#opcode-RETURN_VALUE "Link to this definition")

Returns with `STACK[-1]` to the caller of the function.

YIELD_VALUE[¶](https://docs.python.org/3/library/dis.html#opcode-YIELD_VALUE "Link to this definition")

Yields `STACK.pop()` from a [generator](https://docs.python.org/3/glossary.html#term-generator).
Changed in version 3.11: oparg set to be the stack depth.
Changed in version 3.12: oparg set to be the exception block depth, for efficient closing of generators.
Changed in version 3.13: oparg is `1` if this instruction is part of a yield-from or await, and `0` otherwise.

SETUP_ANNOTATIONS[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_ANNOTATIONS "Link to this definition")

Checks whether `__annotations__` is defined in `locals()`, if not it is set up to an empty `dict`. This opcode is only emitted if a class or module body contains [variable annotations](https://docs.python.org/3/glossary.html#term-variable-annotation) statically.
Added in version 3.6.

POP_EXCEPT[¶](https://docs.python.org/3/library/dis.html#opcode-POP_EXCEPT "Link to this definition")

Pops a value from the stack, which is used to restore the exception state.
Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

RERAISE[¶](https://docs.python.org/3/library/dis.html#opcode-RERAISE "Link to this definition")

Re-raises the exception currently on top of the stack. If oparg is non-zero, pops an additional value from the stack which is used to set [`f_lasti`](https://docs.python.org/3/reference/datamodel.html#frame.f_lasti "frame.f_lasti") of the current frame.
Added in version 3.9.
Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

PUSH_EXC_INFO[¶](https://docs.python.org/3/library/dis.html#opcode-PUSH_EXC_INFO "Link to this definition")

Pops a value from the stack. Pushes the current exception to the top of the stack. Pushes the value originally popped back to the stack. Used in exception handlers.
Added in version 3.11.

CHECK_EXC_MATCH[¶](https://docs.python.org/3/library/dis.html#opcode-CHECK_EXC_MATCH "Link to this definition")

Performs exception matching for `except`. Tests whether the `STACK[-2]` is an exception matching `STACK[-1]`. Pops `STACK[-1]` and pushes the boolean result of the test.
Added in version 3.11.

CHECK_EG_MATCH[¶](https://docs.python.org/3/library/dis.html#opcode-CHECK_EG_MATCH "Link to this definition")

Performs exception matching for `except*`. Applies `split(STACK[-1])` on the exception group representing `STACK[-2]`.
In case of a match, pops two items from the stack and pushes the non-matching subgroup (`None` in case of full match) followed by the matching subgroup. When there is no match, pops one item (the match type) and pushes `None`.
Added in version 3.11.

WITH_EXCEPT_START[¶](https://docs.python.org/3/library/dis.html#opcode-WITH_EXCEPT_START "Link to this definition")

Calls the function in position 4 on the stack with arguments (type, val, tb) representing the exception at the top of the stack. Used to implement the call `context_manager.__exit__(*exc_info())` when an exception has occurred in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement.
Added in version 3.9.
Changed in version 3.11: The `__exit__` function is in position 4 of the stack rather than 7. Exception representation on the stack now consist of one, not three, items.

LOAD_COMMON_CONSTANT[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_COMMON_CONSTANT "Link to this definition")

Pushes a common constant onto the stack. The interpreter contains a hardcoded list of constants supported by this instruction. Used by the [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement to load [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError").
Added in version 3.14.

LOAD_BUILD_CLASS[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_BUILD_CLASS "Link to this definition")

Pushes `builtins.__build_class__()` onto the stack. It is later called to construct a class.

GET_LEN[¶](https://docs.python.org/3/library/dis.html#opcode-GET_LEN "Link to this definition")

Perform `STACK.append(len(STACK[-1]))`. Used in [`match`](https://docs.python.org/3/reference/compound_stmts.html#match) statements where comparison with structure of pattern is needed.
Added in version 3.10.

MATCH_MAPPING[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_MAPPING "Link to this definition")

If `STACK[-1]` is an instance of [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") (or, more technically: if it has the [`Py_TPFLAGS_MAPPING`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING "Py_TPFLAGS_MAPPING") flag set in its [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")), push `True` onto the stack. Otherwise, push `False`.
Added in version 3.10.

MATCH_SEQUENCE[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_SEQUENCE "Link to this definition")

If `STACK[-1]` is an instance of [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") and is _not_ an instance of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str")/[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")/[`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") (or, more technically: if it has the [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE "Py_TPFLAGS_SEQUENCE") flag set in its [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")), push `True` onto the stack. Otherwise, push `False`.
Added in version 3.10.

MATCH_KEYS[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_KEYS "Link to this definition")

`STACK[-1]` is a tuple of mapping keys, and `STACK[-2]` is the match subject. If `STACK[-2]` contains all of the keys in `STACK[-1]`, push a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") containing the corresponding values. Otherwise, push `None`.
Added in version 3.10.
Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating success (`True`) or failure (`False`).

STORE_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_NAME "Link to this definition")

Implements `name = STACK.pop()`. _namei_ is the index of _name_ in the attribute [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names") of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects). The compiler tries to use [`STORE_FAST`](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST) or [`STORE_GLOBAL`](https://docs.python.org/3/library/dis.html#opcode-STORE_GLOBAL) if possible.

DELETE_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_NAME "Link to this definition")

Implements `del name`, where _namei_ is the index into [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names") attribute of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects).

UNPACK_SEQUENCE(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-UNPACK_SEQUENCE "Link to this definition")

Unpacks `STACK[-1]` into _count_ individual values, which are put onto the stack right-to-left. Require there to be exactly _count_ values.:
Copy```
assert(len(STACK[-1]) == count)
STACK.extend(STACK.pop()[:-count-1:-1])

```


UNPACK_EX(_counts_)[¶](https://docs.python.org/3/library/dis.html#opcode-UNPACK_EX "Link to this definition")

Implements assignment with a starred target: Unpacks an iterable in `STACK[-1]` into individual values, where the total number of values can be smaller than the number of items in the iterable: one of the new values will be a list of all leftover items.
The number of values before and after the list value is limited to 255.
The number of values before the list value is encoded in the argument of the opcode. The number of values after the list if any is encoded using an `EXTENDED_ARG`. As a consequence, the argument can be seen as a two bytes values where the low byte of _counts_ is the number of values before the list value, the high byte of _counts_ the number of values after it.
The extracted values are put onto the stack right-to-left, i.e. `a, *b, c = d` will be stored after execution as `STACK.extend((a, b, c))`.

STORE_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_ATTR "Link to this definition")

Implements:
Copy```
obj = STACK.pop()
value = STACK.pop()
obj.name = value

```

where _namei_ is the index of name in [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names") of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects).

DELETE_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_ATTR "Link to this definition")

Implements:
Copy```
obj = STACK.pop()
del obj.name

```

where _namei_ is the index of name into [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names") of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects).

STORE_GLOBAL(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_GLOBAL "Link to this definition")
