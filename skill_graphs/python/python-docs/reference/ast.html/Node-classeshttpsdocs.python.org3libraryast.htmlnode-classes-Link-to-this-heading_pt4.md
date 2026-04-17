Module(
    body=[
        Expr(
            value=Lambda(
                args=arguments(
                    args=[
                        arg(arg='x'),
                        arg(arg='y')]),
                body=Constant(value=Ellipsis)))])

```


_class_ ast.arguments(_posonlyargs_ , _args_ , _vararg_ , _kwonlyargs_ , _kw_defaults_ , _kwarg_ , _defaults_)[¶](https://docs.python.org/3/library/ast.html#ast.arguments "Link to this definition")

The arguments for a function.
  * `posonlyargs`, `args` and `kwonlyargs` are lists of [`arg`](https://docs.python.org/3/library/ast.html#ast.arg "ast.arg") nodes.
  * `vararg` and `kwarg` are single [`arg`](https://docs.python.org/3/library/ast.html#ast.arg "ast.arg") nodes, referring to the `*args, **kwargs` parameters.
  * `kw_defaults` is a list of default values for keyword-only arguments. If one is `None`, the corresponding argument is required.
  * `defaults` is a list of default values for arguments that can be passed positionally. If there are fewer defaults, they correspond to the last n arguments.



_class_ ast.arg(_arg_ , _annotation_ , _type_comment_)[¶](https://docs.python.org/3/library/ast.html#ast.arg "Link to this definition")

A single argument in a list. `arg` is a raw string of the argument name; `annotation` is its annotation, such as a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") node.

type_comment[¶](https://docs.python.org/3/library/ast.html#ast.arg.type_comment "Link to this definition")

`type_comment` is an optional string with the type annotation as a comment
Copy```
>>> print(ast.dump(ast.parse("""\
... @decorator1
... @decorator2
... def f(a: 'annotation', b=1, c=2, *d, e, f=3, **g) -> 'return annotation':
...     pass
... """), indent=4))
Module(
    body=[
        FunctionDef(
            name='f',
            args=arguments(
                args=[
                    arg(
                        arg='a',
                        annotation=Constant(value='annotation')),
                    arg(arg='b'),
                    arg(arg='c')],
                vararg=arg(arg='d'),
                kwonlyargs=[
                    arg(arg='e'),
                    arg(arg='f')],
                kw_defaults=[
                    None,
                    Constant(value=3)],
                kwarg=arg(arg='g'),
                defaults=[
                    Constant(value=1),
                    Constant(value=2)]),
            body=[
                Pass()],
            decorator_list=[
                Name(id='decorator1', ctx=Load()),
                Name(id='decorator2', ctx=Load())],
            returns=Constant(value='return annotation'))])

```


_class_ ast.Return(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.Return "Link to this definition")

A `return` statement.
Copy```
>>> print(ast.dump(ast.parse('return 4'), indent=4))
Module(
    body=[
        Return(
            value=Constant(value=4))])

```


_class_ ast.Yield(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.Yield "Link to this definition")


_class_ ast.YieldFrom(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.YieldFrom "Link to this definition")

A `yield` or `yield from` expression. Because these are expressions, they must be wrapped in an [`Expr`](https://docs.python.org/3/library/ast.html#ast.Expr "ast.Expr") node if the value sent back is not used.
Copy```
>>> print(ast.dump(ast.parse('yield x'), indent=4))
Module(
    body=[
        Expr(
            value=Yield(
                value=Name(id='x', ctx=Load())))])

>>> print(ast.dump(ast.parse('yield from x'), indent=4))
Module(
    body=[
        Expr(
            value=YieldFrom(
                value=Name(id='x', ctx=Load())))])

```


_class_ ast.Global(_names_)[¶](https://docs.python.org/3/library/ast.html#ast.Global "Link to this definition")


_class_ ast.Nonlocal(_names_)[¶](https://docs.python.org/3/library/ast.html#ast.Nonlocal "Link to this definition")

`global` and `nonlocal` statements. `names` is a list of raw strings.
Copy```
>>> print(ast.dump(ast.parse('global x,y,z'), indent=4))
Module(
    body=[
        Global(
            names=[
                'x',
                'y',
                'z'])])

>>> print(ast.dump(ast.parse('nonlocal x,y,z'), indent=4))
Module(
    body=[
        Nonlocal(
            names=[
                'x',
                'y',
                'z'])])

```


_class_ ast.ClassDef(_name_ , _bases_ , _keywords_ , _body_ , _decorator_list_ , _type_params_)[¶](https://docs.python.org/3/library/ast.html#ast.ClassDef "Link to this definition")

A class definition.
  * `name` is a raw string for the class name
  * `bases` is a list of nodes for explicitly specified base classes.
  * `keywords` is a list of [`keyword`](https://docs.python.org/3/library/ast.html#ast.keyword "ast.keyword") nodes, principally for ‘metaclass’. Other keywords will be passed to the metaclass, as per [**PEP 3115**](https://peps.python.org/pep-3115/).
  * `body` is a list of nodes representing the code within the class definition.
  * `decorator_list` is a list of nodes, as in [`FunctionDef`](https://docs.python.org/3/library/ast.html#ast.FunctionDef "ast.FunctionDef").
  * `type_params` is a list of [type parameters](https://docs.python.org/3/library/ast.html#ast-type-params).


Copy```
>>> print(ast.dump(ast.parse("""\
... @decorator1
... @decorator2
... class Foo(base1, base2, metaclass=meta):
...     pass
... """), indent=4))
Module(
    body=[
        ClassDef(
            name='Foo',
            bases=[
                Name(id='base1', ctx=Load()),
                Name(id='base2', ctx=Load())],
            keywords=[
                keyword(
                    arg='metaclass',
                    value=Name(id='meta', ctx=Load()))],
            body=[
                Pass()],
            decorator_list=[
                Name(id='decorator1', ctx=Load()),
                Name(id='decorator2', ctx=Load())])])

```

Changed in version 3.12: Added `type_params`.
### Async and await[¶](https://docs.python.org/3/library/ast.html#async-and-await "Link to this heading")

_class_ ast.AsyncFunctionDef(_name_ , _args_ , _body_ , _decorator_list_ , _returns_ , _type_comment_ , _type_params_)[¶](https://docs.python.org/3/library/ast.html#ast.AsyncFunctionDef "Link to this definition")

An `async def` function definition. Has the same fields as [`FunctionDef`](https://docs.python.org/3/library/ast.html#ast.FunctionDef "ast.FunctionDef").
Changed in version 3.12: Added `type_params`.

_class_ ast.Await(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.Await "Link to this definition")

An `await` expression. `value` is what it waits for. Only valid in the body of an [`AsyncFunctionDef`](https://docs.python.org/3/library/ast.html#ast.AsyncFunctionDef "ast.AsyncFunctionDef").
Copy```
>>> print(ast.dump(ast.parse("""\
... async def f():
...     await other_func()
... """), indent=4))
Module(
    body=[
        AsyncFunctionDef(
            name='f',
            args=arguments(),
            body=[
                Expr(
                    value=Await(
                        value=Call(
                            func=Name(id='other_func', ctx=Load()))))])])

```


_class_ ast.AsyncFor(_target_ , _iter_ , _body_ , _orelse_ , _type_comment_)[¶](https://docs.python.org/3/library/ast.html#ast.AsyncFor "Link to this definition")


_class_ ast.AsyncWith(_items_ , _body_ , _type_comment_)[¶](https://docs.python.org/3/library/ast.html#ast.AsyncWith "Link to this definition")

`async for` loops and `async with` context managers. They have the same fields as [`For`](https://docs.python.org/3/library/ast.html#ast.For "ast.For") and [`With`](https://docs.python.org/3/library/ast.html#ast.With "ast.With"), respectively. Only valid in the body of an [`AsyncFunctionDef`](https://docs.python.org/3/library/ast.html#ast.AsyncFunctionDef "ast.AsyncFunctionDef").
Note
When a string is parsed by [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse"), operator nodes (subclasses of `ast.operator`, `ast.unaryop`, `ast.cmpop`, `ast.boolop` and `ast.expr_context`) on the returned tree will be singletons. Changes to one will be reflected in all other occurrences of the same value (for example, [`ast.Add`](https://docs.python.org/3/library/ast.html#ast.Add "ast.Add")).
##  `ast` helpers[¶](https://docs.python.org/3/library/ast.html#ast-helpers "Link to this heading")
Apart from the node classes, the `ast` module defines these utility functions and classes for traversing abstract syntax trees:

ast.parse(_source_ , _filename ='<unknown>'_, _mode ='exec'_, _*_ , _type_comments =False_, _feature_version =None_, _optimize =-1_)[¶](https://docs.python.org/3/library/ast.html#ast.parse "Link to this definition")

Parse the source into an AST node. Equivalent to `compile(source, filename, mode, flags=FLAGS_VALUE, optimize=optimize)`, where `FLAGS_VALUE` is `ast.PyCF_ONLY_AST` if `optimize <= 0` and `ast.PyCF_OPTIMIZED_AST` otherwise.
If `type_comments=True` is given, the parser is modified to check and return type comments as specified by [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 526**](https://peps.python.org/pep-0526/). This is equivalent to adding [`ast.PyCF_TYPE_COMMENTS`](https://docs.python.org/3/library/ast.html#ast.PyCF_TYPE_COMMENTS "ast.PyCF_TYPE_COMMENTS") to the flags passed to [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile"). This will report syntax errors for misplaced type comments. Without this flag, type comments will be ignored, and the `type_comment` field on selected AST nodes will always be `None`. In addition, the locations of `# type: ignore` comments will be returned as the `type_ignores` attribute of [`Module`](https://docs.python.org/3/library/ast.html#ast.Module "ast.Module") (otherwise it is always an empty list).
In addition, if `mode` is `'func_type'`, the input syntax is modified to correspond to [**PEP 484**](https://peps.python.org/pep-0484/) “signature type comments”, e.g. `(str, int) -> List[str]`.
Setting `feature_version` to a tuple `(major, minor)` will result in a “best-effort” attempt to parse using that Python version’s grammar. For example, setting `feature_version=(3, 9)` will attempt to disallow parsing of [`match`](https://docs.python.org/3/reference/compound_stmts.html#match) statements. Currently `major` must equal to `3`. The lowest supported version is `(3, 7)` (and this may increase in future Python versions); the highest is `sys.version_info[0:2]`. “Best-effort” attempt means there is no guarantee that the parse (or success of the parse) is the same as when run on the Python version corresponding to `feature_version`.
If source contains a null character (`\0`), [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Warning
Note that successfully parsing source code into an AST object doesn’t guarantee that the source code provided is valid Python code that can be executed as the compilation step can raise further [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") exceptions. For instance, the source `return 42` generates a valid AST node for a return statement, but it cannot be compiled alone (it needs to be inside a function node).
In particular, [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") won’t do any scoping checks, which the compilation step does.
Warning
It is possible to crash the Python interpreter with a sufficiently large/complex string due to stack depth limitations in Python’s AST compiler.
Changed in version 3.8: Added `type_comments`, `mode='func_type'` and `feature_version`.
Changed in version 3.13: The minimum supported version for `feature_version` is now `(3, 7)`. The `optimize` argument was added.

ast.unparse(_ast_obj_)[¶](https://docs.python.org/3/library/ast.html#ast.unparse "Link to this definition")

Unparse an [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST") object and generate a string with code that would produce an equivalent `ast.AST` object if parsed back with [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse").
Warning
The produced code string will not necessarily be equal to the original code that generated the [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST") object (without any compiler optimizations, such as constant tuples/frozensets).
Warning
Trying to unparse a highly complex expression would result with [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError").
Added in version 3.9.

ast.literal_eval(_node_or_string_)[¶](https://docs.python.org/3/library/ast.html#ast.literal_eval "Link to this definition")

Evaluate an expression node or a string containing only a Python literal or container display. The string or node provided may only consist of the following Python literal structures: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, `None` and `Ellipsis`.
This can be used for evaluating strings containing Python values without the need to parse the values oneself. It is not capable of evaluating arbitrarily complex expressions, for example involving operators or indexing.
This function had been documented as “safe” in the past without defining what that meant. That was misleading. This is specifically designed not to execute Python code, unlike the more general [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"). There is no namespace, no name lookups, or ability to call out. But it is not free from attack: A relatively small input can lead to memory exhaustion or to C stack exhaustion, crashing the process. There is also the possibility for excessive CPU consumption denial of service on some inputs. Calling it on untrusted data is thus not recommended.
Warning
It is possible to crash the Python interpreter due to stack depth limitations in Python’s AST compiler.
It can raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"), [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError"), [`MemoryError`](https://docs.python.org/3/library/exceptions.html#MemoryError "MemoryError") and [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError") depending on the malformed input.
Changed in version 3.2: Now allows bytes and set literals.
Changed in version 3.9: Now supports creating empty sets with `'set()'`.
Changed in version 3.10: For string inputs, leading spaces and tabs are now stripped.

ast.get_docstring(_node_ , _clean =True_)[¶](https://docs.python.org/3/library/ast.html#ast.get_docstring "Link to this definition")

Return the docstring of the given _node_ (which must be a [`FunctionDef`](https://docs.python.org/3/library/ast.html#ast.FunctionDef "ast.FunctionDef"), [`AsyncFunctionDef`](https://docs.python.org/3/library/ast.html#ast.AsyncFunctionDef "ast.AsyncFunctionDef"), [`ClassDef`](https://docs.python.org/3/library/ast.html#ast.ClassDef "ast.ClassDef"), or [`Module`](https://docs.python.org/3/library/ast.html#ast.Module "ast.Module") node), or `None` if it has no docstring. If _clean_ is true, clean up the docstring’s indentation with [`inspect.cleandoc()`](https://docs.python.org/3/library/inspect.html#inspect.cleandoc "inspect.cleandoc").
Changed in version 3.5: [`AsyncFunctionDef`](https://docs.python.org/3/library/ast.html#ast.AsyncFunctionDef "ast.AsyncFunctionDef") is now supported.

ast.get_source_segment(_source_ , _node_ , _*_ , _padded =False_)[¶](https://docs.python.org/3/library/ast.html#ast.get_source_segment "Link to this definition")

Get source code segment of the _source_ that generated _node_. If some location information ([`lineno`](https://docs.python.org/3/library/ast.html#ast.AST.lineno "ast.AST.lineno"), [`end_lineno`](https://docs.python.org/3/library/ast.html#ast.AST.end_lineno "ast.AST.end_lineno"), [`col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.col_offset "ast.AST.col_offset"), or [`end_col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.end_col_offset "ast.AST.end_col_offset")) is missing, return `None`.
If _padded_ is `True`, the first line of a multi-line statement will be padded with spaces to match its original position.
Added in version 3.8.

ast.fix_missing_locations(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.fix_missing_locations "Link to this definition")

When you compile a node tree with [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile"), the compiler expects [`lineno`](https://docs.python.org/3/library/ast.html#ast.AST.lineno "ast.AST.lineno") and [`col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.col_offset "ast.AST.col_offset") attributes for every node that supports them. This is rather tedious to fill in for generated nodes, so this helper adds these attributes recursively where not already set, by setting them to the values of the parent node. It works recursively starting at _node_.

ast.increment_lineno(_node_ , _n =1_)[¶](https://docs.python.org/3/library/ast.html#ast.increment_lineno "Link to this definition")

Increment the line number and end line number of each node in the tree starting at _node_ by _n_. This is useful to “move code” to a different location in a file.

ast.copy_location(_new_node_ , _old_node_)[¶](https://docs.python.org/3/library/ast.html#ast.copy_location "Link to this definition")

Copy source location ([`lineno`](https://docs.python.org/3/library/ast.html#ast.AST.lineno "ast.AST.lineno"), [`col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.col_offset "ast.AST.col_offset"), [`end_lineno`](https://docs.python.org/3/library/ast.html#ast.AST.end_lineno "ast.AST.end_lineno"), and [`end_col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.end_col_offset "ast.AST.end_col_offset")) from _old_node_ to _new_node_ if possible, and return _new_node_.

ast.iter_fields(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.iter_fields "Link to this definition")

Yield a tuple of `(fieldname, value)` for each field in `node._fields` that is present on _node_.

ast.iter_child_nodes(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.iter_child_nodes "Link to this definition")

Yield all direct child nodes of _node_ , that is, all fields that are nodes and all items of fields that are lists of nodes.

ast.walk(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.walk "Link to this definition")

Recursively yield all descendant nodes in the tree starting at _node_ (including _node_ itself), in no specified order. This is useful if you only want to modify nodes in place and don’t care about the context.

_class_ ast.NodeVisitor[¶](https://docs.python.org/3/library/ast.html#ast.NodeVisitor "Link to this definition")

A node visitor base class that walks the abstract syntax tree and calls a visitor function for every node found. This function may return a value which is forwarded by the [`visit()`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.visit "ast.NodeVisitor.visit") method.
This class is meant to be subclassed, with the subclass adding visitor methods.

visit(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.visit "Link to this definition")

Visit a node. The default implementation calls the method called `self.visit__classname_`where _classname_ is the name of the node class, or [`generic_visit()`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.generic_visit "ast.NodeVisitor.generic_visit") if that method doesn’t exist.

generic_visit(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.generic_visit "Link to this definition")

This visitor calls [`visit()`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.visit "ast.NodeVisitor.visit") on all children of the node.
Note that child nodes of nodes that have a custom visitor method won’t be visited unless the visitor calls `generic_visit()` or visits them itself.

visit_Constant(_node_)[¶](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.visit_Constant "Link to this definition")

Handles all constant nodes.
Don’t use the `NodeVisitor` if you want to apply changes to nodes during traversal. For this a special visitor exists ([`NodeTransformer`](https://docs.python.org/3/library/ast.html#ast.NodeTransformer "ast.NodeTransformer")) that allows modifications.
Deprecated since version 3.8, removed in version 3.14: Methods `visit_Num()`, `visit_Str()`, `visit_Bytes()`, `visit_NameConstant()` and `visit_Ellipsis()` will not be called in Python 3.14+. Add the [`visit_Constant()`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.visit_Constant "ast.NodeVisitor.visit_Constant") method instead to handle all constant nodes.

_class_ ast.NodeTransformer[¶](https://docs.python.org/3/library/ast.html#ast.NodeTransformer "Link to this definition")

A [`NodeVisitor`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor "ast.NodeVisitor") subclass that walks the abstract syntax tree and allows modification of nodes.
The `NodeTransformer` will walk the AST and use the return value of the visitor methods to replace or remove the old node. If the return value of the visitor method is `None`, the node will be removed from its location, otherwise it is replaced with the return value. The return value may be the original node in which case no replacement takes place.
Here is an example transformer that rewrites all occurrences of name lookups (`foo`) to `data['foo']`:
Copy```
class RewriteName(NodeTransformer):

    def visit_Name(self, node):
        return Subscript(
            value=Name(id='data', ctx=Load()),
            slice=Constant(value=node.id),
            ctx=node.ctx
        )

```

Keep in mind that if the node you’re operating on has child nodes you must either transform the child nodes yourself or call the [`generic_visit()`](https://docs.python.org/3/library/ast.html#ast.NodeVisitor.generic_visit "ast.NodeVisitor.generic_visit") method for the node first.
For nodes that were part of a collection of statements (that applies to all statement nodes), the visitor may also return a list of nodes rather than just a single node.
If `NodeTransformer` introduces new nodes (that weren’t part of original tree) without giving them location information (such as [`lineno`](https://docs.python.org/3/library/ast.html#ast.AST.lineno "ast.AST.lineno")), [`fix_missing_locations()`](https://docs.python.org/3/library/ast.html#ast.fix_missing_locations "ast.fix_missing_locations") should be called with the new sub-tree to recalculate the location information:
Copy```
tree = ast.parse('foo', mode='eval')
new_tree = fix_missing_locations(RewriteName().visit(tree))

```

Usually you use the transformer like this:
Copy```
node = YourTransformer().visit(node)

```


ast.dump(_node_ , _annotate_fields =True_, _include_attributes =False_, _*_ , _indent =None_, _show_empty =False_)[¶](https://docs.python.org/3/library/ast.html#ast.dump "Link to this definition")

Return a formatted dump of the tree in _node_. This is mainly useful for debugging purposes. If _annotate_fields_ is true (by default), the returned string will show the names and the values for fields. If _annotate_fields_ is false, the result string will be more compact by omitting unambiguous field names. Attributes such as line numbers and column offsets are not dumped by default. If this is wanted, _include_attributes_ can be set to true.
If _indent_ is a non-negative integer or string, then the tree will be pretty-printed with that indent level. An indent level of 0, negative, or `""` will only insert newlines. `None` (the default) selects the single line representation. Using a positive integer indent indents that many spaces per level. If _indent_ is a string (such as `"\t"`), that string is used to indent each level.
If _show_empty_ is false (the default), optional empty lists will be omitted from the output. Optional `None` values are always omitted.
Changed in version 3.9: Added the _indent_ option.
Changed in version 3.13: Added the _show_empty_ option.
Copy```
>>> print(ast.dump(ast.parse("""\
... async def f():
...     await other_func()
... """), indent=4, show_empty=True))
Module(
    body=[
        AsyncFunctionDef(
            name='f',
            args=arguments(
                posonlyargs=[],
                args=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Expr(
                    value=Await(
                        value=Call(
                            func=Name(id='other_func', ctx=Load()),
                            args=[],
                            keywords=[])))],
            decorator_list=[],
            type_params=[])],
    type_ignores=[])

```

## Compiler flags[¶](https://docs.python.org/3/library/ast.html#compiler-flags "Link to this heading")
The following flags may be passed to [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") in order to change effects on the compilation of a program:
