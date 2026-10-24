Added in version 3.13.

FORMAT_WITH_SPEC[¶](https://docs.python.org/3/library/dis.html#opcode-FORMAT_WITH_SPEC "Link to this definition")

Formats the given value with the given format spec:
Copy```
spec = STACK.pop()
value = STACK.pop()
result = value.__format__(spec)
STACK.append(result)

```

Used for implementing formatted string literals (f-strings).
Added in version 3.13.

MATCH_CLASS(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_CLASS "Link to this definition")

`STACK[-1]` is a tuple of keyword attribute names, `STACK[-2]` is the class being matched against, and `STACK[-3]` is the match subject. _count_ is the number of positional sub-patterns.
Pop `STACK[-1]`, `STACK[-2]`, and `STACK[-3]`. If `STACK[-3]` is an instance of `STACK[-2]` and has the positional and keyword attributes required by _count_ and `STACK[-1]`, push a tuple of extracted attributes. Otherwise, push `None`.
Added in version 3.10.
Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating success (`True`) or failure (`False`).

RESUME(_context_)[¶](https://docs.python.org/3/library/dis.html#opcode-RESUME "Link to this definition")

A no-op. Performs internal tracing, debugging and optimization checks.
The `context` operand consists of two parts. The lowest two bits indicate where the `RESUME` occurs:
  * `0` The start of a function, which is neither a generator, coroutine nor an async generator
  * `1` After a `yield` expression
  * `2` After a `yield from` expression
  * `3` After an `await` expression


The next bit is `1` if the RESUME is at except-depth `1`, and `0` otherwise.
Added in version 3.11.
Changed in version 3.13: The oparg value changed to include information about except-depth

RETURN_GENERATOR[¶](https://docs.python.org/3/library/dis.html#opcode-RETURN_GENERATOR "Link to this definition")

Create a generator, coroutine, or async generator from the current frame. Used as first opcode of in code object for the above mentioned callables. Clear the current frame and return the newly created generator.
Added in version 3.11.

SEND(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-SEND "Link to this definition")

Equivalent to `STACK[-1] = STACK[-2].send(STACK[-1])`. Used in `yield from` and `await` statements.
If the call raises [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration"), pop the top value from the stack, push the exception’s `value` attribute, and increment the bytecode counter by _delta_.
Added in version 3.11.

HAVE_ARGUMENT[¶](https://docs.python.org/3/library/dis.html#opcode-HAVE_ARGUMENT "Link to this definition")

This is not really an opcode. It identifies the dividing line between opcodes in the range [0,255] which don’t use their argument and those that do (`< HAVE_ARGUMENT` and `>= HAVE_ARGUMENT`, respectively).
If your application uses pseudo instructions or specialized instructions, use the [`hasarg`](https://docs.python.org/3/library/dis.html#dis.hasarg "dis.hasarg") collection instead.
Changed in version 3.6: Now every instruction has an argument, but opcodes `< HAVE_ARGUMENT` ignore it. Before, only opcodes `>= HAVE_ARGUMENT` had an argument.
Changed in version 3.12: Pseudo instructions were added to the `dis` module, and for them it is not true that comparison with `HAVE_ARGUMENT` indicates whether they use their arg.
Deprecated since version 3.13: Use [`hasarg`](https://docs.python.org/3/library/dis.html#dis.hasarg "dis.hasarg") instead.

CALL_INTRINSIC_1[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_INTRINSIC_1 "Link to this definition")

Calls an intrinsic function with one argument. Passes `STACK[-1]` as the argument and sets `STACK[-1]` to the result. Used to implement functionality that is not performance critical.
The operand determines which intrinsic function is called:
Operand | Description
---|---
`INTRINSIC_1_INVALID` | Not valid
`INTRINSIC_PRINT` | Prints the argument to standard out. Used in the REPL.
`INTRINSIC_IMPORT_STAR` | Performs `import *` for the named module.
`INTRINSIC_STOPITERATION_ERROR` | Extracts the return value from a `StopIteration` exception.
`INTRINSIC_ASYNC_GEN_WRAP` | Wraps an async generator value
`INTRINSIC_UNARY_POSITIVE` | Performs the unary `+` operation
`INTRINSIC_LIST_TO_TUPLE` | Converts a list to a tuple
`INTRINSIC_TYPEVAR` | Creates a [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")
`INTRINSIC_PARAMSPEC` | Creates a [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec")
`INTRINSIC_TYPEVARTUPLE` | Creates a [`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")
`INTRINSIC_SUBSCRIPT_GENERIC` | Returns [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic") subscripted with the argument
`INTRINSIC_TYPEALIAS` | Creates a [`typing.TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType"); used in the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement. The argument is a tuple of the type alias’s name, type parameters, and value.
Added in version 3.12.

CALL_INTRINSIC_2[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_INTRINSIC_2 "Link to this definition")

Calls an intrinsic function with two arguments. Used to implement functionality that is not performance critical:
Copy```
arg2 = STACK.pop()
arg1 = STACK.pop()
result = intrinsic2(arg1, arg2)
STACK.append(result)

```

The operand determines which intrinsic function is called:
Operand | Description
---|---
`INTRINSIC_2_INVALID` | Not valid
`INTRINSIC_PREP_RERAISE_STAR` | Calculates the [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup") to raise from a `try-except*`.
`INTRINSIC_TYPEVAR_WITH_BOUND` | Creates a [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") with a bound.
`INTRINSIC_TYPEVAR_WITH_CONSTRAINTS` | Creates a [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") with constraints.
`INTRINSIC_SET_FUNCTION_TYPE_PARAMS` | Sets the `__type_params__` attribute of a function.
Added in version 3.12.

LOAD_SPECIAL[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_SPECIAL "Link to this definition")

Performs special method lookup on `STACK[-1]`. If `type(STACK[-1]).__xxx__` is a method, leave `type(STACK[-1]).__xxx__; STACK[-1]` on the stack. If `type(STACK[-1]).__xxx__` is not a method, leave `STACK[-1].__xxx__; NULL` on the stack.
Added in version 3.14.
**Pseudo-instructions**
These opcodes do not appear in Python bytecode. They are used by the compiler but are replaced by real opcodes or removed before bytecode is generated.

SETUP_FINALLY(_target_)[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_FINALLY "Link to this definition")

Set up an exception handler for the following code block. If an exception occurs, the value stack level is restored to its current state and control is transferred to the exception handler at `target`.

SETUP_CLEANUP(_target_)[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_CLEANUP "Link to this definition")

Like `SETUP_FINALLY`, but in case of an exception also pushes the last instruction (`lasti`) to the stack so that `RERAISE` can restore it. If an exception occurs, the value stack level and the last instruction on the frame are restored to their current state, and control is transferred to the exception handler at `target`.

SETUP_WITH(_target_)[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_WITH "Link to this definition")

Like `SETUP_CLEANUP`, but in case of an exception one more item is popped from the stack before control is transferred to the exception handler at `target`.
This variant is used in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) and [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with) constructs, which push the return value of the context manager’s [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") or [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__") to the stack.

POP_BLOCK[¶](https://docs.python.org/3/library/dis.html#opcode-POP_BLOCK "Link to this definition")

Marks the end of the code block associated with the last `SETUP_FINALLY`, `SETUP_CLEANUP` or `SETUP_WITH`.

LOAD_CONST_IMMORTAL(_consti_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_CONST_IMMORTAL "Link to this definition")

Works as [`LOAD_CONST`](https://docs.python.org/3/library/dis.html#opcode-LOAD_CONST), but is more efficient for immortal objects.

JUMP[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP "Link to this definition")


JUMP_NO_INTERRUPT[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_NO_INTERRUPT "Link to this definition")

Undirected relative jump instructions which are replaced by their directed (forward/backward) counterparts by the assembler.

JUMP_IF_TRUE[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_IF_TRUE "Link to this definition")


JUMP_IF_FALSE[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_IF_FALSE "Link to this definition")

Conditional jumps which do not impact the stack. Replaced by the sequence `COPY 1`, `TO_BOOL`, `POP_JUMP_IF_TRUE/FALSE`.

LOAD_CLOSURE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_CLOSURE "Link to this definition")

Pushes a reference to the cell contained in slot `i` of the “fast locals” storage.
Note that `LOAD_CLOSURE` is replaced with `LOAD_FAST` in the assembler.
Changed in version 3.13: This opcode is now a pseudo-instruction.
