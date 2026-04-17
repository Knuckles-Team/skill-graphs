#  `dis` — Disassembler for Python bytecode[¶](https://docs.python.org/3/library/dis.html#module-dis "Link to this heading")
**Source code:**
* * *
The `dis` module supports the analysis of CPython [bytecode](https://docs.python.org/3/glossary.html#term-bytecode) by disassembling it. The CPython bytecode which this module takes as an input is defined in the file `Include/opcode.h` and used by the compiler and the interpreter.
**CPython implementation detail:** Bytecode is an implementation detail of the CPython interpreter. No guarantees are made that bytecode will not be added, removed, or changed between versions of Python. Use of this module should not be considered to work across Python VMs or Python releases.
Changed in version 3.6: Use 2 bytes for each instruction. Previously the number of bytes varied by instruction.
Changed in version 3.10: The argument of jump, exception handling and loop instructions is now the instruction offset rather than the byte offset.
Changed in version 3.11: Some instructions are accompanied by one or more inline cache entries, which take the form of [`CACHE`](https://docs.python.org/3/library/dis.html#opcode-CACHE) instructions. These instructions are hidden by default, but can be shown by passing `show_caches=True` to any `dis` utility. Furthermore, the interpreter now adapts the bytecode to specialize it for different runtime conditions. The adaptive bytecode can be shown by passing `adaptive=True`.
Changed in version 3.12: The argument of a jump is the offset of the target instruction relative to the instruction that appears immediately after the jump instruction’s [`CACHE`](https://docs.python.org/3/library/dis.html#opcode-CACHE) entries.
As a consequence, the presence of the [`CACHE`](https://docs.python.org/3/library/dis.html#opcode-CACHE) instructions is transparent for forward jumps but needs to be taken into account when reasoning about backward jumps.
Changed in version 3.13: The output shows logical labels rather than instruction offsets for jump targets and exception handlers. The `-O` command line option and the `show_offsets` argument were added.
Changed in version 3.14: The [`-P`](https://docs.python.org/3/library/dis.html#cmdoption-dis-P) command-line option and the `show_positions` argument were added.
The [`-S`](https://docs.python.org/3/library/dis.html#cmdoption-dis-S) command-line option is added.
Example: Given the function `myfunc()`:
Copy```
def myfunc(alist):
    return len(alist)

```

the following command can be used to display the disassembly of `myfunc()`:
Copy```
>>> dis.dis(myfunc)
  2           RESUME                   0

  3           LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (alist)
              CALL                     1
              RETURN_VALUE

```

(The “2” is a line number).
