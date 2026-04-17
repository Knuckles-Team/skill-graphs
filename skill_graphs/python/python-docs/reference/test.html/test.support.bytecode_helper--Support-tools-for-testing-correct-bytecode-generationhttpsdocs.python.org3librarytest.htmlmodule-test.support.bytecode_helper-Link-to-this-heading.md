#  `test.support.bytecode_helper` — Support tools for testing correct bytecode generation[¶](https://docs.python.org/3/library/test.html#module-test.support.bytecode_helper "Link to this heading")
The `test.support.bytecode_helper` module provides support for testing and inspecting bytecode generation.
Added in version 3.9.
The module defines the following class:

_class_ test.support.bytecode_helper.BytecodeTestCase(_unittest.TestCase_)[¶](https://docs.python.org/3/library/test.html#test.support.bytecode_helper.BytecodeTestCase "Link to this definition")

This class has custom assertion methods for inspecting bytecode.

BytecodeTestCase.get_disassembly_as_string(_co_)[¶](https://docs.python.org/3/library/test.html#test.support.bytecode_helper.BytecodeTestCase.get_disassembly_as_string "Link to this definition")

Return the disassembly of _co_ as string.

BytecodeTestCase.assertInBytecode(_x_ , _opname_ , _argval =_UNSPECIFIED_)[¶](https://docs.python.org/3/library/test.html#test.support.bytecode_helper.BytecodeTestCase.assertInBytecode "Link to this definition")

Return instr if _opname_ is found, otherwise throws [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError").

BytecodeTestCase.assertNotInBytecode(_x_ , _opname_ , _argval =_UNSPECIFIED_)[¶](https://docs.python.org/3/library/test.html#test.support.bytecode_helper.BytecodeTestCase.assertNotInBytecode "Link to this definition")

Throws [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") if _opname_ is found.
