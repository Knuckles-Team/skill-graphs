
Works as [`STORE_NAME`](https://docs.python.org/3/library/dis.html#opcode-STORE_NAME), but stores the name as a global.

DELETE_GLOBAL(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_GLOBAL "Link to this definition")

Works as [`DELETE_NAME`](https://docs.python.org/3/library/dis.html#opcode-DELETE_NAME), but deletes a global name.

LOAD_CONST(_consti_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_CONST "Link to this definition")

Pushes `co_consts[consti]` onto the stack.

LOAD_SMALL_INT(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_SMALL_INT "Link to this definition")

Pushes the integer `i` onto the stack. `i` must be in `range(256)`
Added in version 3.14.

LOAD_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_NAME "Link to this definition")

Pushes the value associated with `co_names[namei]` onto the stack. The name is looked up within the locals, then the globals, then the builtins.

LOAD_LOCALS[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_LOCALS "Link to this definition")

Pushes a reference to the locals dictionary onto the stack. This is used to prepare namespace dictionaries for [`LOAD_FROM_DICT_OR_DEREF`](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_DEREF) and [`LOAD_FROM_DICT_OR_GLOBALS`](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_GLOBALS).
Added in version 3.12.

LOAD_FROM_DICT_OR_GLOBALS(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_GLOBALS "Link to this definition")

Pops a mapping off the stack and looks up the value for `co_names[namei]`. If the name is not found there, looks it up in the globals and then the builtins, similar to [`LOAD_GLOBAL`](https://docs.python.org/3/library/dis.html#opcode-LOAD_GLOBAL). This is used for loading global variables in [annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes) within class bodies.
Added in version 3.12.

BUILD_TEMPLATE[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_TEMPLATE "Link to this definition")

Constructs a new [`Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template") instance from a tuple of strings and a tuple of interpolations and pushes the resulting object onto the stack:
Copy```
interpolations = STACK.pop()
strings = STACK.pop()
STACK.append(_build_template(strings, interpolations))

```

Added in version 3.14.

BUILD_INTERPOLATION(_format_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_INTERPOLATION "Link to this definition")

Constructs a new [`Interpolation`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation") instance from a value and its source expression and pushes the resulting object onto the stack.
If no conversion or format specification is present, `format` is set to `2`.
If the low bit of `format` is set, it indicates that the interpolation contains a format specification.
If `format >> 2` is non-zero, it indicates that the interpolation contains a conversion. The value of `format >> 2` is the conversion type (`0` for no conversion, `1` for `!s`, `2` for `!r`, and `3` for `!a`):
Copy```
conversion = format >> 2
if format & 1:
    format_spec = STACK.pop()
else:
    format_spec = None
expression = STACK.pop()
value = STACK.pop()
STACK.append(_build_interpolation(value, expression, conversion, format_spec))

```

Added in version 3.14.

BUILD_TUPLE(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_TUPLE "Link to this definition")

Creates a tuple consuming _count_ items from the stack, and pushes the resulting tuple onto the stack:
Copy```
if count == 0:
    value = ()
else:
    value = tuple(STACK[-count:])
    STACK = STACK[:-count]

STACK.append(value)

```


BUILD_LIST(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_LIST "Link to this definition")

Works as [`BUILD_TUPLE`](https://docs.python.org/3/library/dis.html#opcode-BUILD_TUPLE), but creates a list.

BUILD_SET(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_SET "Link to this definition")

Works as [`BUILD_TUPLE`](https://docs.python.org/3/library/dis.html#opcode-BUILD_TUPLE), but creates a set.

BUILD_MAP(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_MAP "Link to this definition")

Pushes a new dictionary object onto the stack. Pops `2 * count` items so that the dictionary holds _count_ entries: `{..., STACK[-4]: STACK[-3], STACK[-2]: STACK[-1]}`.
Changed in version 3.5: The dictionary is created from stack items instead of creating an empty dictionary pre-sized to hold _count_ items.

BUILD_STRING(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_STRING "Link to this definition")

Concatenates _count_ strings from the stack and pushes the resulting string onto the stack.
Added in version 3.6.

LIST_EXTEND(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LIST_EXTEND "Link to this definition")

Implements:
Copy```
seq = STACK.pop()
list.extend(STACK[-i], seq)

```

Used to build lists.
Added in version 3.9.

SET_UPDATE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-SET_UPDATE "Link to this definition")

Implements:
Copy```
seq = STACK.pop()
set.update(STACK[-i], seq)

```

Used to build sets.
Added in version 3.9.

DICT_UPDATE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-DICT_UPDATE "Link to this definition")

Implements:
Copy```
map = STACK.pop()
dict.update(STACK[-i], map)

```

Used to build dicts.
Added in version 3.9.

DICT_MERGE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-DICT_MERGE "Link to this definition")

Like [`DICT_UPDATE`](https://docs.python.org/3/library/dis.html#opcode-DICT_UPDATE) but raises an exception for duplicate keys.
Added in version 3.9.

LOAD_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR "Link to this definition")

If the low bit of `namei` is not set, this replaces `STACK[-1]` with `getattr(STACK[-1], co_names[namei>>1])`.
If the low bit of `namei` is set, this will attempt to load a method named `co_names[namei>>1]` from the `STACK[-1]` object. `STACK[-1]` is popped. This bytecode distinguishes two cases: if `STACK[-1]` has a method with the correct name, the bytecode pushes the unbound method and `STACK[-1]`. `STACK[-1]` will be used as the first argument (`self`) by [`CALL`](https://docs.python.org/3/library/dis.html#opcode-CALL) or [`CALL_KW`](https://docs.python.org/3/library/dis.html#opcode-CALL_KW) when calling the unbound method. Otherwise, `NULL` and the object returned by the attribute lookup are pushed.
Changed in version 3.12: If the low bit of `namei` is set, then a `NULL` or `self` is pushed to the stack before the attribute or unbound method respectively.

LOAD_SUPER_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_SUPER_ATTR "Link to this definition")

This opcode implements [`super()`](https://docs.python.org/3/library/functions.html#super "super"), both in its zero-argument and two-argument forms (e.g. `super().method()`, `super().attr` and `super(cls, self).method()`, `super(cls, self).attr`).
It pops three values from the stack (from top of stack down):
  * `self`: the first argument to the current method
  * `cls`: the class within which the current method was defined
  * the global `super`


With respect to its argument, it works similarly to [`LOAD_ATTR`](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR), except that `namei` is shifted left by 2 bits instead of 1.
The low bit of `namei` signals to attempt a method load, as with [`LOAD_ATTR`](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR), which results in pushing `NULL` and the loaded method. When it is unset a single value is pushed to the stack.
The second-low bit of `namei`, if set, means that this was a two-argument call to [`super()`](https://docs.python.org/3/library/functions.html#super "super") (unset means zero-argument).
Added in version 3.12.

COMPARE_OP(_opname_)[¶](https://docs.python.org/3/library/dis.html#opcode-COMPARE_OP "Link to this definition")

Performs a Boolean operation. The operation name can be found in `cmp_op[opname >> 5]`. If the fifth-lowest bit of `opname` is set (`opname & 16`), the result should be coerced to `bool`.
Changed in version 3.13: The fifth-lowest bit of the oparg now indicates a forced conversion to [`bool`](https://docs.python.org/3/library/functions.html#bool "bool").

IS_OP(_invert_)[¶](https://docs.python.org/3/library/dis.html#opcode-IS_OP "Link to this definition")

Performs `is` comparison, or `is not` if `invert` is 1.
Added in version 3.9.

CONTAINS_OP(_invert_)[¶](https://docs.python.org/3/library/dis.html#opcode-CONTAINS_OP "Link to this definition")

Performs `in` comparison, or `not in` if `invert` is 1.
Added in version 3.9.

IMPORT_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-IMPORT_NAME "Link to this definition")

Imports the module `co_names[namei]`. `STACK[-1]` and `STACK[-2]` are popped and provide the _fromlist_ and _level_ arguments of [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__"). The module object is pushed onto the stack. The current namespace is not affected: for a proper import statement, a subsequent [`STORE_FAST`](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST) instruction modifies the namespace.

IMPORT_FROM(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-IMPORT_FROM "Link to this definition")

Loads the attribute `co_names[namei]` from the module found in `STACK[-1]`. The resulting object is pushed onto the stack, to be subsequently stored by a [`STORE_FAST`](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST) instruction.

JUMP_FORWARD(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_FORWARD "Link to this definition")

Increments bytecode counter by _delta_.

JUMP_BACKWARD(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_BACKWARD "Link to this definition")

Decrements bytecode counter by _delta_. Checks for interrupts.
Added in version 3.11.

JUMP_BACKWARD_NO_INTERRUPT(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_BACKWARD_NO_INTERRUPT "Link to this definition")

Decrements bytecode counter by _delta_. Does not check for interrupts.
Added in version 3.11.

POP_JUMP_IF_TRUE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_TRUE "Link to this definition")

If `STACK[-1]` is true, increments the bytecode counter by _delta_. `STACK[-1]` is popped.
Changed in version 3.11: The oparg is now a relative delta rather than an absolute target. This opcode is a pseudo-instruction, replaced in final bytecode by the directed versions (forward/backward).
Changed in version 3.12: This is no longer a pseudo-instruction.
Changed in version 3.13: This instruction now requires an exact [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") operand.

POP_JUMP_IF_FALSE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_FALSE "Link to this definition")

If `STACK[-1]` is false, increments the bytecode counter by _delta_. `STACK[-1]` is popped.
Changed in version 3.11: The oparg is now a relative delta rather than an absolute target. This opcode is a pseudo-instruction, replaced in final bytecode by the directed versions (forward/backward).
Changed in version 3.12: This is no longer a pseudo-instruction.
Changed in version 3.13: This instruction now requires an exact [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") operand.

POP_JUMP_IF_NOT_NONE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_NOT_NONE "Link to this definition")

If `STACK[-1]` is not `None`, increments the bytecode counter by _delta_. `STACK[-1]` is popped.
Added in version 3.11.
Changed in version 3.12: This is no longer a pseudo-instruction.

POP_JUMP_IF_NONE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_NONE "Link to this definition")

If `STACK[-1]` is `None`, increments the bytecode counter by _delta_. `STACK[-1]` is popped.
Added in version 3.11.
Changed in version 3.12: This is no longer a pseudo-instruction.

FOR_ITER(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-FOR_ITER "Link to this definition")

`STACK[-1]` is an [iterator](https://docs.python.org/3/glossary.html#term-iterator). Call its [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method. If this yields a new value, push it on the stack (leaving the iterator below it). If the iterator indicates it is exhausted then the byte code counter is incremented by _delta_.
Changed in version 3.12: Up until 3.11 the iterator was popped when it was exhausted.

LOAD_GLOBAL(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_GLOBAL "Link to this definition")

Loads the global named `co_names[namei>>1]` onto the stack.
Changed in version 3.11: If the low bit of `namei` is set, then a `NULL` is pushed to the stack before the global variable.

LOAD_FAST(_var_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST "Link to this definition")

Pushes a reference to the local `co_varnames[var_num]` onto the stack.
Changed in version 3.12: This opcode is now only used in situations where the local variable is guaranteed to be initialized. It cannot raise [`UnboundLocalError`](https://docs.python.org/3/library/exceptions.html#UnboundLocalError "UnboundLocalError").

LOAD_FAST_BORROW(_var_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_BORROW "Link to this definition")

Pushes a borrowed reference to the local `co_varnames[var_num]` onto the stack.
Added in version 3.14.

LOAD_FAST_LOAD_FAST(_var_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_LOAD_FAST "Link to this definition")

Pushes references to `co_varnames[var_nums >> 4]` and `co_varnames[var_nums & 15]` onto the stack.
Added in version 3.13.

LOAD_FAST_BORROW_LOAD_FAST_BORROW(_var_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_BORROW_LOAD_FAST_BORROW "Link to this definition")

Pushes borrowed references to `co_varnames[var_nums >> 4]` and `co_varnames[var_nums & 15]` onto the stack.
Added in version 3.14.

LOAD_FAST_CHECK(_var_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_CHECK "Link to this definition")

Pushes a reference to the local `co_varnames[var_num]` onto the stack, raising an [`UnboundLocalError`](https://docs.python.org/3/library/exceptions.html#UnboundLocalError "UnboundLocalError") if the local variable has not been initialized.
Added in version 3.12.

LOAD_FAST_AND_CLEAR(_var_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_AND_CLEAR "Link to this definition")

Pushes a reference to the local `co_varnames[var_num]` onto the stack (or pushes `NULL` onto the stack if the local variable has not been initialized) and sets `co_varnames[var_num]` to `NULL`.
Added in version 3.12.

STORE_FAST(_var_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST "Link to this definition")

Stores `STACK.pop()` into the local `co_varnames[var_num]`.

STORE_FAST_STORE_FAST(_var_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST_STORE_FAST "Link to this definition")

Stores `STACK[-1]` into `co_varnames[var_nums >> 4]` and `STACK[-2]` into `co_varnames[var_nums & 15]`.
Added in version 3.13.

STORE_FAST_LOAD_FAST(_var_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST_LOAD_FAST "Link to this definition")

Stores `STACK.pop()` into the local `co_varnames[var_nums >> 4]` and pushes a reference to the local `co_varnames[var_nums & 15]` onto the stack.
Added in version 3.13.

DELETE_FAST(_var_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_FAST "Link to this definition")

Deletes local `co_varnames[var_num]`.

MAKE_CELL(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-MAKE_CELL "Link to this definition")

Creates a new cell in slot `i`. If that slot is nonempty then that value is stored into the new cell.
Added in version 3.11.

LOAD_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_DEREF "Link to this definition")

Loads the cell contained in slot `i` of the “fast locals” storage. Pushes a reference to the object the cell contains on the stack.
Changed in version 3.11: `i` is no longer offset by the length of [`co_varnames`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "codeobject.co_varnames").

LOAD_FROM_DICT_OR_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_DEREF "Link to this definition")

Pops a mapping off the stack and looks up the name associated with slot `i` of the “fast locals” storage in this mapping. If the name is not found there, loads it from the cell contained in slot `i`, similar to [`LOAD_DEREF`](https://docs.python.org/3/library/dis.html#opcode-LOAD_DEREF). This is used for loading [closure variables](https://docs.python.org/3/glossary.html#term-closure-variable) in class bodies (which previously used `LOAD_CLASSDEREF`) and in [annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes) within class bodies.
Added in version 3.12.

STORE_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_DEREF "Link to this definition")

Stores `STACK.pop()` into the cell contained in slot `i` of the “fast locals” storage.
Changed in version 3.11: `i` is no longer offset by the length of [`co_varnames`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "codeobject.co_varnames").

DELETE_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_DEREF "Link to this definition")

Empties the cell contained in slot `i` of the “fast locals” storage. Used by the [`del`](https://docs.python.org/3/reference/simple_stmts.html#del) statement.
Added in version 3.2.
Changed in version 3.11: `i` is no longer offset by the length of [`co_varnames`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "codeobject.co_varnames").

COPY_FREE_VARS(_n_)[¶](https://docs.python.org/3/library/dis.html#opcode-COPY_FREE_VARS "Link to this definition")

Copies the `n` [free (closure) variables](https://docs.python.org/3/glossary.html#term-closure-variable) from the closure into the frame. Removes the need for special code on the caller’s side when calling closures.
Added in version 3.11.

RAISE_VARARGS(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-RAISE_VARARGS "Link to this definition")

Raises an exception using one of the 3 forms of the `raise` statement, depending on the value of _argc_ :
  * 0: `raise` (re-raise previous exception)
  * 1: `raise STACK[-1]` (raise exception instance or type at `STACK[-1]`)
  * 2: `raise STACK[-2] from STACK[-1]` (raise exception instance or type at `STACK[-2]` with `__cause__` set to `STACK[-1]`)



CALL(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-CALL "Link to this definition")

Calls a callable object with the number of arguments specified by `argc`. On the stack are (in ascending order):
  * The callable
  * `self` or `NULL`
  * The remaining positional arguments


`argc` is the total of the positional arguments, excluding `self`.
`CALL` pops all arguments and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.
Added in version 3.11.
Changed in version 3.13: The callable now always appears at the same position on the stack.
Changed in version 3.13: Calls with keyword arguments are now handled by [`CALL_KW`](https://docs.python.org/3/library/dis.html#opcode-CALL_KW).

CALL_KW(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_KW "Link to this definition")

Calls a callable object with the number of arguments specified by `argc`, including one or more named arguments. On the stack are (in ascending order):
  * The callable
  * `self` or `NULL`
  * The remaining positional arguments
  * The named arguments
  * A [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of keyword argument names


`argc` is the total of the positional and named arguments, excluding `self`. The length of the tuple of keyword argument names is the number of named arguments.
`CALL_KW` pops all arguments, the keyword names, and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.
Added in version 3.13.

CALL_FUNCTION_EX(_flags_)[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_FUNCTION_EX "Link to this definition")

Calls a callable object with variable set of positional and keyword arguments. If the lowest bit of _flags_ is set, the top of the stack contains a mapping object containing additional keyword arguments. Before the callable is called, the mapping object and iterable object are each “unpacked” and their contents passed in as keyword and positional arguments respectively. `CALL_FUNCTION_EX` pops all arguments and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.
Added in version 3.6.

PUSH_NULL[¶](https://docs.python.org/3/library/dis.html#opcode-PUSH_NULL "Link to this definition")

Pushes a `NULL` to the stack. Used in the call sequence to match the `NULL` pushed by `LOAD_METHOD` for non-method calls.
Added in version 3.11.

MAKE_FUNCTION[¶](https://docs.python.org/3/library/dis.html#opcode-MAKE_FUNCTION "Link to this definition")

Pushes a new function object on the stack built from the code object at `STACK[-1]`.
Changed in version 3.10: Flag value `0x04` is a tuple of strings instead of dictionary
Changed in version 3.11: Qualified name at `STACK[-1]` was removed.
Changed in version 3.13: Extra function attributes on the stack, signaled by oparg flags, were removed. They now use [`SET_FUNCTION_ATTRIBUTE`](https://docs.python.org/3/library/dis.html#opcode-SET_FUNCTION_ATTRIBUTE).

SET_FUNCTION_ATTRIBUTE(_flag_)[¶](https://docs.python.org/3/library/dis.html#opcode-SET_FUNCTION_ATTRIBUTE "Link to this definition")

Sets an attribute on a function object. Expects the function at `STACK[-1]` and the attribute value to set at `STACK[-2]`; consumes both and leaves the function at `STACK[-1]`. The flag determines which attribute to set:
  * `0x01` a tuple of default values for positional-only and positional-or-keyword parameters in positional order
  * `0x02` a dictionary of keyword-only parameters’ default values
  * `0x04` a tuple of strings containing parameters’ annotations
  * `0x08` a tuple containing cells for free variables, making a closure
  * `0x10` the [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function) for the function object


Added in version 3.13.
Changed in version 3.14: Added `0x10` to indicate the annotate function for the function object.

BUILD_SLICE(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_SLICE "Link to this definition")

Pushes a slice object on the stack. _argc_ must be 2 or 3. If it is 2, implements:
Copy```
end = STACK.pop()
start = STACK.pop()
STACK.append(slice(start, end))

```

if it is 3, implements:
Copy```
step = STACK.pop()
end = STACK.pop()
start = STACK.pop()
STACK.append(slice(start, end, step))

```

See the [`slice()`](https://docs.python.org/3/library/functions.html#slice "slice") built-in function for more information.

EXTENDED_ARG(_ext_)[¶](https://docs.python.org/3/library/dis.html#opcode-EXTENDED_ARG "Link to this definition")

Prefixes any opcode which has an argument too big to fit into the default one byte. _ext_ holds an additional byte which act as higher bits in the argument. For each opcode, at most three prefixal `EXTENDED_ARG` are allowed, forming an argument from two-byte to four-byte.

CONVERT_VALUE(_oparg_)[¶](https://docs.python.org/3/library/dis.html#opcode-CONVERT_VALUE "Link to this definition")

Convert value to a string, depending on `oparg`:
Copy```
value = STACK.pop()
result = func(value)
STACK.append(result)

```

  * `oparg == 1`: call [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") on _value_
  * `oparg == 2`: call [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") on _value_
  * `oparg == 3`: call [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii") on _value_


Used for implementing formatted string literals (f-strings).
Added in version 3.13.

FORMAT_SIMPLE[¶](https://docs.python.org/3/library/dis.html#opcode-FORMAT_SIMPLE "Link to this definition")

Formats the value on top of stack:
Copy```
value = STACK.pop()
result = value.__format__("")
STACK.append(result)

```

Used for implementing formatted string literals (f-strings).
