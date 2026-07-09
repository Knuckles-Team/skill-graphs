## Node classes[¶](https://docs.python.org/3/library/ast.html#node-classes "Link to this heading")

_class_ ast.AST[¶](https://docs.python.org/3/library/ast.html#ast.AST "Link to this definition")

This is the base of all AST node classes. The actual node classes are derived from the `Parser/Python.asdl` file, which is reproduced [above](https://docs.python.org/3/library/ast.html#abstract-grammar). They are defined in the `_ast` C module and re-exported in `ast`.
There is one class defined for each left-hand side symbol in the abstract grammar (for example, `ast.stmt` or `ast.expr`). In addition, there is one class defined for each constructor on the right-hand side; these classes inherit from the classes for the left-hand side trees. For example, [`ast.BinOp`](https://docs.python.org/3/library/ast.html#ast.BinOp "ast.BinOp") inherits from `ast.expr`. For production rules with alternatives (aka “sums”), the left-hand side class is abstract: only instances of specific constructor nodes are ever created.

_fields[¶](https://docs.python.org/3/library/ast.html#ast.AST._fields "Link to this definition")

Each concrete class has an attribute `_fields` which gives the names of all child nodes.
Each instance of a concrete class has one attribute for each child node, of the type as defined in the grammar. For example, [`ast.BinOp`](https://docs.python.org/3/library/ast.html#ast.BinOp "ast.BinOp") instances have an attribute `left` of type `ast.expr`.
If these attributes are marked as optional in the grammar (using a question mark), the value might be `None`. If the attributes can have zero-or-more values (marked with an asterisk), the values are represented as Python lists. All possible attributes must be present and have valid values when compiling an AST with [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile").

_field_types[¶](https://docs.python.org/3/library/ast.html#ast.AST._field_types "Link to this definition")

The `_field_types` attribute on each concrete class is a dictionary mapping field names (as also listed in [`_fields`](https://docs.python.org/3/library/ast.html#ast.AST._fields "ast.AST._fields")) to their types.
Copy```
>>> ast.TypeVar._field_types
{'name': <class 'str'>, 'bound': ast.expr | None, 'default_value': ast.expr | None}

```

Added in version 3.13.

lineno[¶](https://docs.python.org/3/library/ast.html#ast.AST.lineno "Link to this definition")


col_offset[¶](https://docs.python.org/3/library/ast.html#ast.AST.col_offset "Link to this definition")


end_lineno[¶](https://docs.python.org/3/library/ast.html#ast.AST.end_lineno "Link to this definition")


end_col_offset[¶](https://docs.python.org/3/library/ast.html#ast.AST.end_col_offset "Link to this definition")

Instances of `ast.expr` and `ast.stmt` subclasses have [`lineno`](https://docs.python.org/3/library/ast.html#ast.AST.lineno "ast.AST.lineno"), [`col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.col_offset "ast.AST.col_offset"), [`end_lineno`](https://docs.python.org/3/library/ast.html#ast.AST.end_lineno "ast.AST.end_lineno"), and [`end_col_offset`](https://docs.python.org/3/library/ast.html#ast.AST.end_col_offset "ast.AST.end_col_offset") attributes. The `lineno` and `end_lineno` are the first and last line numbers of source text span (1-indexed so the first line is line 1) and the `col_offset` and `end_col_offset` are the corresponding UTF-8 byte offsets of the first and last tokens that generated the node. The UTF-8 offset is recorded because the parser uses UTF-8 internally.
Note that the end positions are not required by the compiler and are therefore optional. The end offset is _after_ the last symbol, for example one can get the source segment of a one-line expression node using `source_line[node.col_offset : node.end_col_offset]`.
The constructor of a class `ast.T` parses its arguments as follows:
  * If there are positional arguments, there must be as many as there are items in `T._fields`; they will be assigned as attributes of these names.
  * If there are keyword arguments, they will set the attributes of the same names to the given values.


For example, to create and populate an [`ast.UnaryOp`](https://docs.python.org/3/library/ast.html#ast.UnaryOp "ast.UnaryOp") node, you could use
Copy```
node = ast.UnaryOp(ast.USub(), ast.Constant(5, lineno=0, col_offset=0),
                   lineno=0, col_offset=0)

```

If a field that is optional in the grammar is omitted from the constructor, it defaults to `None`. If a list field is omitted, it defaults to the empty list. If a field of type `ast.expr_context` is omitted, it defaults to [`Load()`](https://docs.python.org/3/library/ast.html#ast.Load "ast.Load"). If any other field is omitted, a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") is raised and the AST node will not have this field. In Python 3.15, this condition will raise an error.
Changed in version 3.8: Class [`ast.Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant") is now used for all constants.
Changed in version 3.9: Simple indices are represented by their value, extended slices are represented as tuples.
Changed in version 3.14: The [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__") output of [`AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST") nodes includes the values of the node fields.
Deprecated since version 3.8, removed in version 3.14: Previous versions of Python provided the AST classes `ast.Num`, `ast.Str`, `ast.Bytes`, `ast.NameConstant` and `ast.Ellipsis`, which were deprecated in Python 3.8. These classes were removed in Python 3.14, and their functionality has been replaced with [`ast.Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant").
Deprecated since version 3.9: Old classes `ast.Index` and `ast.ExtSlice` are still available, but they will be removed in future Python releases. In the meantime, instantiating them will return an instance of a different class.
Deprecated since version 3.13, will be removed in version 3.15: Previous versions of Python allowed the creation of AST nodes that were missing required fields. Similarly, AST node constructors allowed arbitrary keyword arguments that were set as attributes of the AST node, even if they did not match any of the fields of the AST node. This behavior is deprecated and will be removed in Python 3.15.
Note
The descriptions of the specific node classes displayed here were initially adapted from the fantastic
### Root nodes[¶](https://docs.python.org/3/library/ast.html#root-nodes "Link to this heading")

_class_ ast.Module(_body_ , _type_ignores_)[¶](https://docs.python.org/3/library/ast.html#ast.Module "Link to this definition")

A Python module, as with [file input](https://docs.python.org/3/reference/toplevel_components.html#file-input). Node type generated by [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") in the default `"exec"` _mode_.
`body` is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of the module’s [Statements](https://docs.python.org/3/library/ast.html#ast-statements).
`type_ignores` is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of the module’s type ignore comments; see [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") for more details.
Copy```
>>> print(ast.dump(ast.parse('x = 1'), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1))])

```


_class_ ast.Expression(_body_)[¶](https://docs.python.org/3/library/ast.html#ast.Expression "Link to this definition")

A single Python [expression input](https://docs.python.org/3/reference/toplevel_components.html#expression-input). Node type generated by [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") when _mode_ is `"eval"`.
`body` is a single node, one of the [expression types](https://docs.python.org/3/library/ast.html#ast-expressions).
Copy```
>>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
Expression(
    body=Constant(value=123))

```


_class_ ast.Interactive(_body_)[¶](https://docs.python.org/3/library/ast.html#ast.Interactive "Link to this definition")

A single [interactive input](https://docs.python.org/3/reference/toplevel_components.html#interactive), like in [Interactive Mode](https://docs.python.org/3/tutorial/appendix.html#tut-interac). Node type generated by [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") when _mode_ is `"single"`.
`body` is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of [statement nodes](https://docs.python.org/3/library/ast.html#ast-statements).
Copy```
>>> print(ast.dump(ast.parse('x = 1; y = 2', mode='single'), indent=4))
Interactive(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1)),
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=Constant(value=2))])

```


_class_ ast.FunctionType(_argtypes_ , _returns_)[¶](https://docs.python.org/3/library/ast.html#ast.FunctionType "Link to this definition")

A representation of an old-style type comments for functions, as Python versions prior to 3.5 didn’t support [**PEP 484**](https://peps.python.org/pep-0484/) annotations. Node type generated by [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") when _mode_ is `"func_type"`.
Such type comments would look like this:
Copy```
def sum_two_number(a, b):
    # type: (int, int) -> int
    return a + b

```

`argtypes` is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of [expression nodes](https://docs.python.org/3/library/ast.html#ast-expressions).
`returns` is a single [expression node](https://docs.python.org/3/library/ast.html#ast-expressions).
Copy```
>>> print(ast.dump(ast.parse('(int, str) -> List[int]', mode='func_type'), indent=4))
FunctionType(
    argtypes=[
        Name(id='int', ctx=Load()),
        Name(id='str', ctx=Load())],
    returns=Subscript(
        value=Name(id='List', ctx=Load()),
        slice=Name(id='int', ctx=Load()),
        ctx=Load()))

```

Added in version 3.8.
### Literals[¶](https://docs.python.org/3/library/ast.html#literals "Link to this heading")

_class_ ast.Constant(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.Constant "Link to this definition")

A constant value. The `value` attribute of the `Constant` literal contains the Python object it represents. The values represented can be instances of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`complex`](https://docs.python.org/3/library/functions.html#complex "complex"), and [`bool`](https://docs.python.org/3/library/functions.html#bool "bool"), and the constants [`None`](https://docs.python.org/3/library/constants.html#None "None") and [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "Ellipsis").
Copy```
>>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
Expression(
    body=Constant(value=123))

```


_class_ ast.FormattedValue(_value_ , _conversion_ , _format_spec_)[¶](https://docs.python.org/3/library/ast.html#ast.FormattedValue "Link to this definition")

Node representing a single formatting field in an f-string. If the string contains a single formatting field and nothing else the node can be isolated otherwise it appears in [`JoinedStr`](https://docs.python.org/3/library/ast.html#ast.JoinedStr "ast.JoinedStr").
  * `value` is any expression node (such as a literal, a variable, or a function call).
  * `conversion` is an integer:
    * -1: no formatting
    * 97 (`ord('a')`): `!a` [`ASCII`](https://docs.python.org/3/library/functions.html#ascii "ascii") formatting
    * 114 (`ord('r')`): `!r` [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") formatting
    * 115 (`ord('s')`): `!s` [`string`](https://docs.python.org/3/library/stdtypes.html#str "str") formatting
  * `format_spec` is a [`JoinedStr`](https://docs.python.org/3/library/ast.html#ast.JoinedStr "ast.JoinedStr") node representing the formatting of the value, or `None` if no format was specified. Both `conversion` and `format_spec` can be set at the same time.



_class_ ast.JoinedStr(_values_)[¶](https://docs.python.org/3/library/ast.html#ast.JoinedStr "Link to this definition")

An f-string, comprising a series of [`FormattedValue`](https://docs.python.org/3/library/ast.html#ast.FormattedValue "ast.FormattedValue") and [`Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant") nodes.
Copy```
>>> print(ast.dump(ast.parse('f"sin({a}) is {sin(a):.3}"', mode='eval'), indent=4))
Expression(
    body=JoinedStr(
        values=[
            Constant(value='sin('),
            FormattedValue(
                value=Name(id='a', ctx=Load()),
                conversion=-1),
            Constant(value=') is '),
            FormattedValue(
                value=Call(
                    func=Name(id='sin', ctx=Load()),
                    args=[
                        Name(id='a', ctx=Load())]),
                conversion=-1,
                format_spec=JoinedStr(
                    values=[
                        Constant(value='.3')]))]))

```


_class_ ast.TemplateStr(_values_ , _/_)[¶](https://docs.python.org/3/library/ast.html#ast.TemplateStr "Link to this definition")

Added in version 3.14.
Node representing a template string literal, comprising a series of [`Interpolation`](https://docs.python.org/3/library/ast.html#ast.Interpolation "ast.Interpolation") and [`Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant") nodes. These nodes may be any order, and do not need to be interleaved.
Copy```
>>> expr = ast.parse('t"{name} finished {place:ordinal}"', mode='eval')
>>> print(ast.dump(expr, indent=4))
Expression(
    body=TemplateStr(
        values=[
            Interpolation(
                value=Name(id='name', ctx=Load()),
                str='name',
                conversion=-1),
            Constant(value=' finished '),
            Interpolation(
                value=Name(id='place', ctx=Load()),
                str='place',
                conversion=-1,
                format_spec=JoinedStr(
                    values=[
                        Constant(value='ordinal')]))]))

```


_class_ ast.Interpolation(_value_ , _str_ , _conversion_ , _format_spec =None_)[¶](https://docs.python.org/3/library/ast.html#ast.Interpolation "Link to this definition")

Added in version 3.14.
Node representing a single interpolation field in a template string literal.
  * `value` is any expression node (such as a literal, a variable, or a function call). This has the same meaning as `FormattedValue.value`.
  * `str` is a constant containing the text of the interpolation expression.
If `str` is set to `None`, then `value` is used to generate code when calling [`ast.unparse()`](https://docs.python.org/3/library/ast.html#ast.unparse "ast.unparse"). This no longer guarantees that the generated code is identical to the original and is intended for code generation.
  * `conversion` is an integer:
    * -1: no conversion
    * 97 (`ord('a')`): `!a` [`ASCII`](https://docs.python.org/3/library/functions.html#ascii "ascii") conversion
    * 114 (`ord('r')`): `!r` [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") conversion
    * 115 (`ord('s')`): `!s` [`string`](https://docs.python.org/3/library/stdtypes.html#str "str") conversion
This has the same meaning as `FormattedValue.conversion`.
  * `format_spec` is a [`JoinedStr`](https://docs.python.org/3/library/ast.html#ast.JoinedStr "ast.JoinedStr") node representing the formatting of the value, or `None` if no format was specified. Both `conversion` and `format_spec` can be set at the same time. This has the same meaning as `FormattedValue.format_spec`.



_class_ ast.List(_elts_ , _ctx_)[¶](https://docs.python.org/3/library/ast.html#ast.List "Link to this definition")


_class_ ast.Tuple(_elts_ , _ctx_)[¶](https://docs.python.org/3/library/ast.html#ast.Tuple "Link to this definition")

A list or tuple. `elts` holds a list of nodes representing the elements. `ctx` is [`Store`](https://docs.python.org/3/library/ast.html#ast.Store "ast.Store") if the container is an assignment target (i.e. `(x,y)=something`), and [`Load`](https://docs.python.org/3/library/ast.html#ast.Load "ast.Load") otherwise.
Copy```
>>> print(ast.dump(ast.parse('[1, 2, 3]', mode='eval'), indent=4))
Expression(
    body=List(
        elts=[
            Constant(value=1),
            Constant(value=2),
            Constant(value=3)],
        ctx=Load()))
>>> print(ast.dump(ast.parse('(1, 2, 3)', mode='eval'), indent=4))
Expression(
    body=Tuple(
        elts=[
            Constant(value=1),
            Constant(value=2),
            Constant(value=3)],
        ctx=Load()))

```


_class_ ast.Set(_elts_)[¶](https://docs.python.org/3/library/ast.html#ast.Set "Link to this definition")

A set. `elts` holds a list of nodes representing the set’s elements.
Copy```
>>> print(ast.dump(ast.parse('{1, 2, 3}', mode='eval'), indent=4))
Expression(
    body=Set(
        elts=[
            Constant(value=1),
            Constant(value=2),
            Constant(value=3)]))

```


_class_ ast.Dict(_keys_ , _values_)[¶](https://docs.python.org/3/library/ast.html#ast.Dict "Link to this definition")

A dictionary. `keys` and `values` hold lists of nodes representing the keys and the values respectively, in matching order (what would be returned when calling `dictionary.keys()` and `dictionary.values()`).
When doing dictionary unpacking using dictionary literals the expression to be expanded goes in the `values` list, with a `None` at the corresponding position in `keys`.
Copy```
>>> print(ast.dump(ast.parse('{"a":1, **d}', mode='eval'), indent=4))
Expression(
    body=Dict(
        keys=[
            Constant(value='a'),
            None],
        values=[
            Constant(value=1),
            Name(id='d', ctx=Load())]))

```

### Variables[¶](https://docs.python.org/3/library/ast.html#variables "Link to this heading")

_class_ ast.Name(_id_ , _ctx_)[¶](https://docs.python.org/3/library/ast.html#ast.Name "Link to this definition")

A variable name. `id` holds the name as a string, and `ctx` is one of the following types.

_class_ ast.Load[¶](https://docs.python.org/3/library/ast.html#ast.Load "Link to this definition")


_class_ ast.Store[¶](https://docs.python.org/3/library/ast.html#ast.Store "Link to this definition")


_class_ ast.Del[¶](https://docs.python.org/3/library/ast.html#ast.Del "Link to this definition")

Variable references can be used to load the value of a variable, to assign a new value to it, or to delete it. Variable references are given a context to distinguish these cases.
Copy```
>>> print(ast.dump(ast.parse('a'), indent=4))
Module(
    body=[
        Expr(
            value=Name(id='a', ctx=Load()))])

>>> print(ast.dump(ast.parse('a = 1'), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Name(id='a', ctx=Store())],
            value=Constant(value=1))])

>>> print(ast.dump(ast.parse('del a'), indent=4))
Module(
    body=[
        Delete(
            targets=[
                Name(id='a', ctx=Del())])])

```


_class_ ast.Starred(_value_ , _ctx_)[¶](https://docs.python.org/3/library/ast.html#ast.Starred "Link to this definition")

A `*var` variable reference. `value` holds the variable, typically a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") node. This type must be used when building a [`Call`](https://docs.python.org/3/library/ast.html#ast.Call "ast.Call") node with `*args`.
Copy```
>>> print(ast.dump(ast.parse('a, *b = it'), indent=4))
Module(
    body=[
        Assign(
            targets=[
                Tuple(
                    elts=[
                        Name(id='a', ctx=Store()),
                        Starred(
                            value=Name(id='b', ctx=Store()),
                            ctx=Store())],
                    ctx=Store())],
            value=Name(id='it', ctx=Load()))])

```

### Expressions[¶](https://docs.python.org/3/library/ast.html#expressions "Link to this heading")

_class_ ast.Expr(_value_)[¶](https://docs.python.org/3/library/ast.html#ast.Expr "Link to this definition")

When an expression, such as a function call, appears as a statement by itself with its return value not used or stored, it is wrapped in this container. `value` holds one of the other nodes in this section, a [`Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant"), a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"), a [`Lambda`](https://docs.python.org/3/library/ast.html#ast.Lambda "ast.Lambda"), a [`Yield`](https://docs.python.org/3/library/ast.html#ast.Yield "ast.Yield") or [`YieldFrom`](https://docs.python.org/3/library/ast.html#ast.YieldFrom "ast.YieldFrom") node.
Copy```
>>> print(ast.dump(ast.parse('-a'), indent=4))
Module(
    body=[
        Expr(
            value=UnaryOp(
                op=USub(),
                operand=Name(id='a', ctx=Load())))])

```


_class_ ast.UnaryOp(_op_ , _operand_)[¶](https://docs.python.org/3/library/ast.html#ast.UnaryOp "Link to this definition")

A unary operation. `op` is the operator, and `operand` any expression node.

_class_ ast.UAdd[¶](https://docs.python.org/3/library/ast.html#ast.UAdd "Link to this definition")


_class_ ast.USub[¶](https://docs.python.org/3/library/ast.html#ast.USub "Link to this definition")


_class_ ast.Not[¶](https://docs.python.org/3/library/ast.html#ast.Not "Link to this definition")


_class_ ast.Invert[¶](https://docs.python.org/3/library/ast.html#ast.Invert "Link to this definition")

Unary operator tokens. `Not` is the `not` keyword, `Invert` is the `~` operator.
Copy```
>>> print(ast.dump(ast.parse('not x', mode='eval'), indent=4))
Expression(
    body=UnaryOp(
        op=Not(),
        operand=Name(id='x', ctx=Load())))

```


_class_ ast.BinOp(_left_ , _op_ , _right_)[¶](https://docs.python.org/3/library/ast.html#ast.BinOp "Link to this definition")

A binary operation (like addition or division). `op` is the operator, and `left` and `right` are any expression nodes.
Copy```
>>> print(ast.dump(ast.parse('x + y', mode='eval'), indent=4))
Expression(
    body=BinOp(
        left=Name(id='x', ctx=Load()),
        op=Add(),
        right=Name(id='y', ctx=Load())))

```


_class_ ast.Add[¶](https://docs.python.org/3/library/ast.html#ast.Add "Link to this definition")


_class_ ast.Sub[¶](https://docs.python.org/3/library/ast.html#ast.Sub "Link to this definition")


_class_ ast.Mult[¶](https://docs.python.org/3/library/ast.html#ast.Mult "Link to this definition")


_class_ ast.Div[¶](https://docs.python.org/3/library/ast.html#ast.Div "Link to this definition")


_class_ ast.FloorDiv[¶](https://docs.python.org/3/library/ast.html#ast.FloorDiv "Link to this definition")


_class_ ast.Mod[¶](https://docs.python.org/3/library/ast.html#ast.Mod "Link to this definition")


_class_ ast.Pow[¶](https://docs.python.org/3/library/ast.html#ast.Pow "Link to this definition")


_class_ ast.LShift[¶](https://docs.python.org/3/library/ast.html#ast.LShift "Link to this definition")


_class_ ast.RShift[¶](https://docs.python.org/3/library/ast.html#ast.RShift "Link to this definition")


_class_ ast.BitOr[¶](https://docs.python.org/3/library/ast.html#ast.BitOr "Link to this definition")


_class_ ast.BitXor[¶](https://docs.python.org/3/library/ast.html#ast.BitXor "Link to this definition")


_class_ ast.BitAnd[¶](https://docs.python.org/3/library/ast.html#ast.BitAnd "Link to this definition")


_class_ ast.MatMult[¶](https://docs.python.org/3/library/ast.html#ast.MatMult "Link to this definition")

Binary operator tokens.

_class_ ast.BoolOp(_op_ , _values_)[¶](https://docs.python.org/3/library/ast.html#ast.BoolOp "Link to this definition")

A boolean operation, ‘or’ or ‘and’. `op` is [`Or`](https://docs.python.org/3/library/ast.html#ast.Or "ast.Or") or [`And`](https://docs.python.org/3/library/ast.html#ast.And "ast.And"). `values` are the values involved. Consecutive operations with the same operator, such as `a or b or c`, are collapsed into one node with several values.
This doesn’t include `not`, which is a [`UnaryOp`](https://docs.python.org/3/library/ast.html#ast.UnaryOp "ast.UnaryOp").
Copy```
>>> print(ast.dump(ast.parse('x or y', mode='eval'), indent=4))
Expression(
    body=BoolOp(
        op=Or(),
        values=[
            Name(id='x', ctx=Load()),
            Name(id='y', ctx=Load())]))

```


_class_ ast.And[¶](https://docs.python.org/3/library/ast.html#ast.And "Link to this definition")


_class_ ast.Or[¶](https://docs.python.org/3/library/ast.html#ast.Or "Link to this definition")
