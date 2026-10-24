## Analysis functions[¶](https://docs.python.org/3/library/dis.html#analysis-functions "Link to this heading")
The `dis` module also defines the following analysis functions that convert the input directly to the desired output. They can be useful if only a single operation is being performed, so the intermediate analysis object isn’t useful:

dis.code_info(_x_)[¶](https://docs.python.org/3/library/dis.html#dis.code_info "Link to this definition")

Return a formatted multi-line string with detailed code object information for the supplied function, generator, asynchronous generator, coroutine, method, source code string or code object.
Note that the exact contents of code info strings are highly implementation dependent and they may change arbitrarily across Python VMs or Python releases.
Added in version 3.2.
Changed in version 3.7: This can now handle coroutine and asynchronous generator objects.

dis.show_code(_x_ , _*_ , _file =None_)[¶](https://docs.python.org/3/library/dis.html#dis.show_code "Link to this definition")

Print detailed code object information for the supplied function, method, source code string or code object to _file_ (or `sys.stdout` if _file_ is not specified).
This is a convenient shorthand for `print(code_info(x), file=file)`, intended for interactive exploration at the interpreter prompt.
Added in version 3.2.
Changed in version 3.4: Added _file_ parameter.

dis.dis(_x =None_, _*_ , _file =None_, _depth =None_, _show_caches =False_, _adaptive =False_, _show_offsets =False_, _show_positions =False_)[¶](https://docs.python.org/3/library/dis.html#dis.dis "Link to this definition")

Disassemble the _x_ object. _x_ can denote either a module, a class, a method, a function, a generator, an asynchronous generator, a coroutine, a code object, a string of source code or a byte sequence of raw bytecode. For a module, it disassembles all functions. For a class, it disassembles all methods (including class and static methods). For a code object or sequence of raw bytecode, it prints one line per bytecode instruction. It also recursively disassembles nested code objects. These can include generator expressions, nested functions, the bodies of nested classes, and the code objects used for [annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes). Strings are first compiled to code objects with the [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") built-in function before being disassembled. If no object is provided, this function disassembles the last traceback.
The disassembly is written as text to the supplied _file_ argument if provided and to `sys.stdout` otherwise.
The maximal depth of recursion is limited by _depth_ unless it is `None`. `depth=0` means no recursion.
If _show_caches_ is `True`, this function will display inline cache entries used by the interpreter to specialize the bytecode.
If _adaptive_ is `True`, this function will display specialized bytecode that may be different from the original bytecode.
Changed in version 3.4: Added _file_ parameter.
Changed in version 3.7: Implemented recursive disassembling and added _depth_ parameter.
Changed in version 3.7: This can now handle coroutine and asynchronous generator objects.
Changed in version 3.11: Added the _show_caches_ and _adaptive_ parameters.
Changed in version 3.13: Added the _show_offsets_ parameter.
Changed in version 3.14: Added the _show_positions_ parameter.

dis.distb(_tb =None_, _*_ , _file =None_, _show_caches =False_, _adaptive =False_, _show_offset =False_, _show_positions =False_)[¶](https://docs.python.org/3/library/dis.html#dis.distb "Link to this definition")

Disassemble the top-of-stack function of a traceback, using the last traceback if none was passed. The instruction causing the exception is indicated.
The disassembly is written as text to the supplied _file_ argument if provided and to `sys.stdout` otherwise.
Changed in version 3.4: Added _file_ parameter.
Changed in version 3.11: Added the _show_caches_ and _adaptive_ parameters.
Changed in version 3.13: Added the _show_offsets_ parameter.
Changed in version 3.14: Added the _show_positions_ parameter.

dis.disassemble(_code_ , _lasti =-1_, _*_ , _file =None_, _show_caches =False_, _adaptive =False_, _show_offsets =False_, _show_positions =False_)[¶](https://docs.python.org/3/library/dis.html#dis.disassemble "Link to this definition")


dis.disco(_code_ , _lasti =-1_, _*_ , _file =None_, _show_caches =False_, _adaptive =False_, _show_offsets =False_, _show_positions =False_)[¶](https://docs.python.org/3/library/dis.html#dis.disco "Link to this definition")

Disassemble a code object, indicating the last instruction if _lasti_ was provided. The output is divided in the following columns:
  1. the source code location of the instruction. Complete location information is shown if _show_positions_ is true. Otherwise (the default) only the line number is displayed.
  2. the current instruction, indicated as `-->`,
  3. a labelled instruction, indicated with `>>`,
  4. the address of the instruction,
  5. the operation code name,
  6. operation parameters, and
  7. interpretation of the parameters in parentheses.


The parameter interpretation recognizes local and global variable names, constant values, branch targets, and compare operators.
The disassembly is written as text to the supplied _file_ argument if provided and to `sys.stdout` otherwise.
Changed in version 3.4: Added _file_ parameter.
Changed in version 3.11: Added the _show_caches_ and _adaptive_ parameters.
Changed in version 3.13: Added the _show_offsets_ parameter.
Changed in version 3.14: Added the _show_positions_ parameter.

dis.get_instructions(_x_ , _*_ , _first_line =None_, _show_caches =False_, _adaptive =False_)[¶](https://docs.python.org/3/library/dis.html#dis.get_instructions "Link to this definition")

Return an iterator over the instructions in the supplied function, method, source code string or code object.
The iterator generates a series of [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction") named tuples giving the details of each operation in the supplied code.
If _first_line_ is not `None`, it indicates the line number that should be reported for the first source line in the disassembled code. Otherwise, the source line information (if any) is taken directly from the disassembled code object.
The _adaptive_ parameter works as it does in [`dis()`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.").
Added in version 3.4.
Changed in version 3.11: Added the _show_caches_ and _adaptive_ parameters.
Changed in version 3.13: The _show_caches_ parameter is deprecated and has no effect. The iterator generates the [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction") instances with the _cache_info_ field populated (regardless of the value of _show_caches_) and it no longer generates separate items for the cache entries.

dis.findlinestarts(_code_)[¶](https://docs.python.org/3/library/dis.html#dis.findlinestarts "Link to this definition")

This generator function uses the [`co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines") method of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects) _code_ to find the offsets which are starts of lines in the source code. They are generated as `(offset, lineno)` pairs.
Changed in version 3.6: Line numbers can be decreasing. Before, they were always increasing.
Changed in version 3.10: The [**PEP 626**](https://peps.python.org/pep-0626/) [`co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines") method is used instead of the [`co_firstlineno`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_firstlineno "codeobject.co_firstlineno") and [`co_lnotab`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lnotab "codeobject.co_lnotab") attributes of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects).
Changed in version 3.13: Line numbers can be `None` for bytecode that does not map to source lines.

dis.findlabels(_code_)[¶](https://docs.python.org/3/library/dis.html#dis.findlabels "Link to this definition")

Detect all offsets in the raw compiled bytecode string _code_ which are jump targets, and return a list of these offsets.

dis.stack_effect(_opcode_ , _oparg =None_, _*_ , _jump =None_)[¶](https://docs.python.org/3/library/dis.html#dis.stack_effect "Link to this definition")

Compute the stack effect of _opcode_ with argument _oparg_.
If the code has a jump target and _jump_ is `True`, `stack_effect()` will return the stack effect of jumping. If _jump_ is `False`, it will return the stack effect of not jumping. And if _jump_ is `None` (default), it will return the maximal stack effect of both cases.
Added in version 3.4.
Changed in version 3.8: Added _jump_ parameter.
Changed in version 3.13: If `oparg` is omitted (or `None`), the stack effect is now returned for `oparg=0`. Previously this was an error for opcodes that use their arg. It is also no longer an error to pass an integer `oparg` when the `opcode` does not use it; the `oparg` in this case is ignored.
