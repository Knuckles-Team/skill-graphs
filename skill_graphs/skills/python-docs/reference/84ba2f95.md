
Boolean operator tokens.

_class_ ast.Compare(_left_ , _ops_ , _comparators_)[¶](https://docs.python.org/3/library/ast.html#ast.Compare "Link to this definition")

A comparison of two or more values. `left` is the first value in the comparison, `ops` the list of operators, and `comparators` the list of values after the first element in the comparison.
Copy```
>>> print(ast.dump(ast.parse('1 <= a < 10', mode='eval'), indent=4))
Expression(
    body=Compare(
        left=Constant(value=1),
        ops=[
            LtE(),
            Lt()],
        comparators=[
            Name(id='a', ctx=Load()),
            Constant(value=10)]))

```


_class_ ast.Eq[¶](https://docs.python.org/3/library/ast.html#ast.Eq "Link to this definition")


_class_ ast.NotEq[¶](https://docs.python.org/3/library/ast.html#ast.NotEq "Link to this definition")


_class_ ast.Lt[¶](https://docs.python.org/3/library/ast.html#ast.Lt "Link to this definition")


_class_ ast.LtE[¶](https://docs.python.org/3/library/ast.html#ast.LtE "Link to this definition")


_class_ ast.Gt[¶](https://docs.python.org/3/library/ast.html#ast.Gt "Link to this definition")


_class_ ast.GtE[¶](https://docs.python.org/3/library/ast.html#ast.GtE "Link to this definition")


_class_ ast.Is[¶](https://docs.python.org/3/library/ast.html#ast.Is "Link to this definition")


_class_ ast.IsNot[¶](https://docs.python.org/3/library/ast.html#ast.IsNot "Link to this definition")


_class_ ast.In[¶](https://docs.python.org/3/library/ast.html#ast.In "Link to this definition")


_class_ ast.NotIn[¶](https://docs.python.org/3/library/ast.html#ast.NotIn "Link to this definition")

Comparison operator tokens.

_class_ ast.Call(_func_ , _args_ , _keywords_)[¶](https://docs.python.org/3/library/ast.html#ast.Call "Link to this definition")

A function call. `func` is the function, which will often be a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") or [`Attribute`](https://docs.python.org/3/library/ast.html#ast.Attribute "ast.Attribute") object. Of the arguments:
  * `args` holds a list of the arguments passed by position.
  * `keywords` holds a list of [`keyword`](https://docs.python.org/3/library/ast.html#ast.keyword "ast.keyword") objects representing arguments passed by keyword.


The `args` and `keywords` arguments are optional and default to empty lists.
Copy```
>>> print(ast.dump(ast.parse('func(a, b=c, *d, **e)', mode='eval'), indent=4))
Expression(
    body=Call(
        func=Name(id='func', ctx=Load()),
        args=[
            Name(id='a', ctx=Load()),
            Starred(
                value=Name(id='d', ctx=Load()),
                ctx=Load())],
        keywords=[
            keyword(
                arg='b',
                value=Name(id='c', ctx=Load())),
            keyword(
                value=Name(id='e', ctx=Load()))]))

```


_class_ ast.keyword(_arg_ , _value_)[¶](https://docs.python.org/3/library/ast.html#ast.keyword "Link to this definition")

A keyword argument to a function call or class definition. `arg` is a raw string of the parameter name, `value` is a node to pass in.

_class_ ast.IfExp(_test_ , _body_ , _orelse_)[¶](https://docs.python.org/3/library/ast.html#ast.IfExp "Link to this definition")

An expression such as `a if b else c`. Each field holds a single node, so in the following example, all three are [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") nodes.
Copy```
>>> print(ast.dump(ast.parse('a if b else c', mode='eval'), indent=4))
Expression(
    body=IfExp(
        test=Name(id='b', ctx=Load()),
        body=Name(id='a', ctx=Load()),
        orelse=Name(id='c', ctx=Load())))

```


_class_ ast.Attribute(_value_ , _attr_ , _ctx_)[¶](https://docs.python.org/3/library/ast.html#ast.Attribute "Link to this definition")

Attribute access, e.g. `d.keys`. `value` is a node, typically a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"). `attr` is a bare string giving the name of the attribute, and `ctx` is [`Load`](https://docs.python.org/3/library/ast.html#ast.Load "ast.Load"), [`Store`](https://docs.python.org/3/library/ast.html#ast.Store "ast.Store") or [`Del`](https://docs.python.org/3/library/ast.html#ast.Del "ast.Del") according to how the attribute is acted on.
Copy```
>>> print(ast.dump(ast.parse('snake.colour', mode='eval'), indent=4))
Expression(
    body=Attribute(
        value=Name(id='snake', ctx=Load()),
        attr='colour',
        ctx=Load()))

```


_class_ ast.NamedExpr(_target_ , _value_)[¶](https://docs.python.org/3/library/ast.html#ast.NamedExpr "Link to this definition")

A named expression. This AST node is produced by the assignment expressions operator (also known as the walrus operator). As opposed to the [`Assign`](https://docs.python.org/3/library/ast.html#ast.Assign "ast.Assign") node in which the first argument can be multiple nodes, in this case both `target` and `value` must be single nodes.
Copy```
>>> print(ast.dump(ast.parse('(x := 4)', mode='eval'), indent=4))
Expression(
    body=NamedExpr(
        target=Name(id='x', ctx=Store()),
        value=Constant(value=4)))

```

Added in version 3.8.
#### Subscripting[¶](https://docs.python.org/3/library/ast.html#subscripting "Link to this heading")

_class_ ast.Subscript(_value_ , _slice_ , _ctx_)[¶](https://docs.python.org/3/library/ast.html#ast.Subscript "Link to this definition")

A subscript, such as `l[1]`. `value` is the subscripted object (usually sequence or mapping). `slice` is an index, slice or key. It can be a [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple") and contain a [`Slice`](https://docs.python.org/3/library/ast.html#ast.Slice "ast.Slice"). `ctx` is [`Load`](https://docs.python.org/3/library/ast.html#ast.Load "ast.Load"), [`Store`](https://docs.python.org/3/library/ast.html#ast.Store "ast.Store") or [`Del`](https://docs.python.org/3/library/ast.html#ast.Del "ast.Del") according to the action performed with the subscript.
Copy```
>>> print(ast.dump(ast.parse('l[1:2, 3]', mode='eval'), indent=4))
Expression(
    body=Subscript(
        value=Name(id='l', ctx=Load()),
        slice=Tuple(
            elts=[
                Slice(
                    lower=Constant(value=1),
                    upper=Constant(value=2)),
                Constant(value=3)],
            ctx=Load()),
        ctx=Load()))

```


_class_ ast.Slice(_lower_ , _upper_ , _step_)[¶](https://docs.python.org/3/library/ast.html#ast.Slice "Link to this definition")

Regular slicing (on the form `lower:upper` or `lower:upper:step`). Can occur only inside the _slice_ field of [`Subscript`](https://docs.python.org/3/library/ast.html#ast.Subscript "ast.Subscript"), either directly or as an element of [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple").
Copy```
>>> print(ast.dump(ast.parse('l[1:2]', mode='eval'), indent=4))
Expression(
    body=Subscript(
        value=Name(id='l', ctx=Load()),
        slice=Slice(
            lower=Constant(value=1),
            upper=Constant(value=2)),
        ctx=Load()))

```

#### Comprehensions[¶](https://docs.python.org/3/library/ast.html#comprehensions "Link to this heading")

_class_ ast.ListComp(_elt_ , _generators_)[¶](https://docs.python.org/3/library/ast.html#ast.ListComp "Link to this definition")


_class_ ast.SetComp(_elt_ , _generators_)[¶](https://docs.python.org/3/library/ast.html#ast.SetComp "Link to this definition")


_class_ ast.GeneratorExp(_elt_ , _generators_)[¶](https://docs.python.org/3/library/ast.html#ast.GeneratorExp "Link to this definition")


_class_ ast.DictComp(_key_ , _value_ , _generators_)[¶](https://docs.python.org/3/library/ast.html#ast.DictComp "Link to this definition")

List and set comprehensions, generator expressions, and dictionary comprehensions. `elt` (or `key` and `value`) is a single node representing the part that will be evaluated for each item.
`generators` is a list of [`comprehension`](https://docs.python.org/3/library/ast.html#ast.comprehension "ast.comprehension") nodes.
Copy```
>>> print(ast.dump(
...     ast.parse('[x for x in numbers]', mode='eval'),
...     indent=4,
... ))
Expression(
    body=ListComp(
        elt=Name(id='x', ctx=Load()),
        generators=[
            comprehension(
                target=Name(id='x', ctx=Store()),
                iter=Name(id='numbers', ctx=Load()),
                is_async=0)]))
>>> print(ast.dump(
...     ast.parse('{x: x**2 for x in numbers}', mode='eval'),
...     indent=4,
... ))
Expression(
    body=DictComp(
        key=Name(id='x', ctx=Load()),
        value=BinOp(
            left=Name(id='x', ctx=Load()),
            op=Pow(),
            right=Constant(value=2)),
        generators=[
            comprehension(
                target=Name(id='x', ctx=Store()),
                iter=Name(id='numbers', ctx=Load()),
                is_async=0)]))
>>> print(ast.dump(
...     ast.parse('{x for x in numbers}', mode='eval'),
...     indent=4,
... ))
Expression(
    body=SetComp(
        elt=Name(id='x', ctx=Load()),
        generators=[
            comprehension(
                target=Name(id='x', ctx=Store()),
                iter=Name(id='numbers', ctx=Load()),
                is_async=0)]))

```


_class_ ast.comprehension(_target_ , _iter_ , _ifs_ , _is_async_)[¶](https://docs.python.org/3/library/ast.html#ast.comprehension "Link to this definition")

One `for` clause in a comprehension. `target` is the reference to use for each element - typically a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") or [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple") node. `iter` is the object to iterate over. `ifs` is a list of test expressions: each `for` clause can have multiple `ifs`.
`is_async` indicates a comprehension is asynchronous (using an `async for` instead of `for`). The value is an integer (0 or 1).
Copy```
>>> print(ast.dump(ast.parse('[ord(c) for line in file for c in line]', mode='eval'),
...                indent=4)) # Multiple comprehensions in one.
Expression(
    body=ListComp(
        elt=Call(
            func=Name(id='ord', ctx=Load()),
            args=[
                Name(id='c', ctx=Load())]),
        generators=[
            comprehension(
                target=Name(id='line', ctx=Store()),
                iter=Name(id='file', ctx=Load()),
                is_async=0),
            comprehension(
                target=Name(id='c', ctx=Store()),
                iter=Name(id='line', ctx=Load()),
                is_async=0)]))

>>> print(ast.dump(ast.parse('(n**2 for n in it if n>5 if n<10)', mode='eval'),
...                indent=4)) # generator comprehension
Expression(
    body=GeneratorExp(
        elt=BinOp(
            left=Name(id='n', ctx=Load()),
            op=Pow(),
            right=Constant(value=2)),
        generators=[
            comprehension(
                target=Name(id='n', ctx=Store()),
                iter=Name(id='it', ctx=Load()),
                ifs=[
                    Compare(
                        left=Name(id='n', ctx=Load()),
                        ops=[
                            Gt()],
                        comparators=[
                            Constant(value=5)]),
                    Compare(
                        left=Name(id='n', ctx=Load()),
                        ops=[
                            Lt()],
                        comparators=[
                            Constant(value=10)])],
                is_async=0)]))

>>> print(ast.dump(ast.parse('[i async for i in soc]', mode='eval'),
...                indent=4)) # Async comprehension
Expression(
    body=ListComp(
        elt=Name(id='i', ctx=Load()),
        generators=[
            comprehension(
                target=Name(id='i', ctx=Store()),
                iter=Name(id='soc', ctx=Load()),
                is_async=1)]))

```

### Statements[¶](https://docs.python.org/3/library/ast.html#statements "Link to this heading")

_class_ ast.Assign(_targets_ , _value_ , _type_comment_)[¶](https://docs.python.org/3/library/ast.html#ast.Assign "Link to this definition")

An assignment. `targets` is a list of nodes, and `value` is a single node.
Multiple nodes in `targets` represents assigning the same value to each. Unpacking is represented by putting a [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple") or [`List`](https://docs.python.org/3/library/ast.html#ast.List "ast.List") within `targets`.

type_comment[¶](https://docs.python.org/3/library/ast.html#ast.Assign.type_comment "Link to this definition")

`type_comment` is an optional string with the type annotation as a comment.
Copy```
>>> print(ast.dump(ast.parse('a = b = 1'), indent=4)) # Multiple assignment
Module(
    body=[
        Assign(
            targets=[
                Name(id='a', ctx=Store()),
                Name(id='b', ctx=Store())],
            value=Constant(value=1))])

>>> print(ast.dump(ast.parse('a,b = c'), indent=4)) # Unpacking
Module(
    body=[
        Assign(
            targets=[
                Tuple(
                    elts=[
                        Name(id='a', ctx=Store()),
                        Name(id='b', ctx=Store())],
                    ctx=Store())],
            value=Name(id='c', ctx=Load()))])

```


_class_ ast.AnnAssign(_target_ , _annotation_ , _value_ , _simple_)[¶](https://docs.python.org/3/library/ast.html#ast.AnnAssign "Link to this definition")

An assignment with a type annotation. `target` is a single node and can be a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"), an [`Attribute`](https://docs.python.org/3/library/ast.html#ast.Attribute "ast.Attribute") or a [`Subscript`](https://docs.python.org/3/library/ast.html#ast.Subscript "ast.Subscript"). `annotation` is the annotation, such as a [`Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant") or `Name` node. `value` is a single optional node.
`simple` is always either 0 (indicating a “complex” target) or 1 (indicating a “simple” target). A “simple” target consists solely of a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") node that does not appear between parentheses; all other targets are considered complex. Only simple targets appear in the [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__") dictionary of modules and classes.
Copy```
>>> print(ast.dump(ast.parse('c: int'), indent=4))
Module(
    body=[
        AnnAssign(
            target=Name(id='c', ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            simple=1)])

>>> print(ast.dump(ast.parse('(a): int = 1'), indent=4)) # Annotation with parenthesis
Module(
    body=[
        AnnAssign(
            target=Name(id='a', ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            value=Constant(value=1),
            simple=0)])

>>> print(ast.dump(ast.parse('a.b: int'), indent=4)) # Attribute annotation
Module(
    body=[
        AnnAssign(
            target=Attribute(
                value=Name(id='a', ctx=Load()),
                attr='b',
                ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            simple=0)])

>>> print(ast.dump(ast.parse('a[1]: int'), indent=4)) # Subscript annotation
Module(
    body=[
        AnnAssign(
            target=Subscript(
                value=Name(id='a', ctx=Load()),
                slice=Constant(value=1),
                ctx=Store()),
            annotation=Name(id='int', ctx=Load()),
            simple=0)])

```


_class_ ast.AugAssign(_target_ , _op_ , _value_)[¶](https://docs.python.org/3/library/ast.html#ast.AugAssign "Link to this definition")

Augmented assignment, such as `a += 1`. In the following example, `target` is a [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name") node for `x` (with the [`Store`](https://docs.python.org/3/library/ast.html#ast.Store "ast.Store") context), `op` is [`Add`](https://docs.python.org/3/library/ast.html#ast.Add "ast.Add"), and `value` is a [`Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant") with value for 1.
The `target` attribute cannot be of class [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple") or [`List`](https://docs.python.org/3/library/ast.html#ast.List "ast.List"), unlike the targets of [`Assign`](https://docs.python.org/3/library/ast.html#ast.Assign "ast.Assign").
Copy```
>>> print(ast.dump(ast.parse('x += 2'), indent=4))
Module(
    body=[
        AugAssign(
            target=Name(id='x', ctx=Store()),
            op=Add(),
            value=Constant(value=2))])

```


_class_ ast.Raise(_exc_ , _cause_)[¶](https://docs.python.org/3/library/ast.html#ast.Raise "Link to this definition")

A `raise` statement. `exc` is the exception object to be raised, normally a [`Call`](https://docs.python.org/3/library/ast.html#ast.Call "ast.Call") or [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"), or `None` for a standalone `raise`. `cause` is the optional part for `y` in `raise x from y`.
Copy```
>>> print(ast.dump(ast.parse('raise x from y'), indent=4))
Module(
    body=[
        Raise(
            exc=Name(id='x', ctx=Load()),
            cause=Name(id='y', ctx=Load()))])

```


_class_ ast.Assert(_test_ , _msg_)[¶](https://docs.python.org/3/library/ast.html#ast.Assert "Link to this definition")

An assertion. `test` holds the condition, such as a [`Compare`](https://docs.python.org/3/library/ast.html#ast.Compare "ast.Compare") node. `msg` holds the failure message.
Copy```
>>> print(ast.dump(ast.parse('assert x,y'), indent=4))
Module(
    body=[
        Assert(
            test=Name(id='x', ctx=Load()),
            msg=Name(id='y', ctx=Load()))])

```


_class_ ast.Delete(_targets_)[¶](https://docs.python.org/3/library/ast.html#ast.Delete "Link to this definition")

Represents a `del` statement. `targets` is a list of nodes, such as [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"), [`Attribute`](https://docs.python.org/3/library/ast.html#ast.Attribute "ast.Attribute") or [`Subscript`](https://docs.python.org/3/library/ast.html#ast.Subscript "ast.Subscript") nodes.
Copy```
>>> print(ast.dump(ast.parse('del x,y,z'), indent=4))
Module(
    body=[
        Delete(
            targets=[
                Name(id='x', ctx=Del()),
                Name(id='y', ctx=Del()),
                Name(id='z', ctx=Del())])])

```


_class_ ast.Pass[¶](https://docs.python.org/3/library/ast.html#ast.Pass "Link to this definition")

A `pass` statement.
Copy```
>>> print(ast.dump(ast.parse('pass'), indent=4))
Module(
    body=[
        Pass()])

```


_class_ ast.TypeAlias(_name_ , _type_params_ , _value_)[¶](https://docs.python.org/3/library/ast.html#ast.TypeAlias "Link to this definition")

A [type alias](https://docs.python.org/3/library/typing.html#type-aliases) created through the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement. `name` is the name of the alias, `type_params` is a list of [type parameters](https://docs.python.org/3/library/ast.html#ast-type-params), and `value` is the value of the type alias.
Copy```
>>> print(ast.dump(ast.parse('type Alias = int'), indent=4))
Module(
    body=[
        TypeAlias(
            name=Name(id='Alias', ctx=Store()),
            value=Name(id='int', ctx=Load()))])

```

Added in version 3.12.
Other statements which are only applicable inside functions or loops are described in other sections.
#### Imports[¶](https://docs.python.org/3/library/ast.html#imports "Link to this heading")

_class_ ast.Import(_names_)[¶](https://docs.python.org/3/library/ast.html#ast.Import "Link to this definition")

An import statement. `names` is a list of [`alias`](https://docs.python.org/3/library/ast.html#ast.alias "ast.alias") nodes.
Copy```
>>> print(ast.dump(ast.parse('import x,y,z'), indent=4))
Module(
    body=[
        Import(
            names=[
                alias(name='x'),
                alias(name='y'),
                alias(name='z')])])

```


_class_ ast.ImportFrom(_module_ , _names_ , _level_)[¶](https://docs.python.org/3/library/ast.html#ast.ImportFrom "Link to this definition")

Represents `from x import y`. `module` is a raw string of the ‘from’ name, without any leading dots, or `None` for statements such as `from . import foo`. `level` is an integer holding the level of the relative import (0 means absolute import).
Copy```
>>> print(ast.dump(ast.parse('from y import x,y,z'), indent=4))
Module(
    body=[
        ImportFrom(
            module='y',
            names=[
                alias(name='x'),
                alias(name='y'),
                alias(name='z')],
            level=0)])

```


_class_ ast.alias(_name_ , _asname_)[¶](https://docs.python.org/3/library/ast.html#ast.alias "Link to this definition")

Both parameters are raw strings of the names. `asname` can be `None` if the regular name is to be used.
Copy```
>>> print(ast.dump(ast.parse('from ..foo.bar import a as b, c'), indent=4))
Module(
    body=[
        ImportFrom(
            module='foo.bar',
            names=[
                alias(name='a', asname='b'),
                alias(name='c')],
            level=2)])

```

### Control flow[¶](https://docs.python.org/3/library/ast.html#control-flow "Link to this heading")
Note
Optional clauses such as `else` are stored as an empty list if they’re not present.

_class_ ast.If(_test_ , _body_ , _orelse_)[¶](https://docs.python.org/3/library/ast.html#ast.If "Link to this definition")

An `if` statement. `test` holds a single node, such as a [`Compare`](https://docs.python.org/3/library/ast.html#ast.Compare "ast.Compare") node. `body` and `orelse` each hold a list of nodes.
`elif` clauses don’t have a special representation in the AST, but rather appear as extra `If` nodes within the `orelse` section of the previous one.
Copy```
>>> print(ast.dump(ast.parse("""
... if x:
...    ...
... elif y:
...    ...
... else:
...    ...
... """), indent=4))
Module(
    body=[
        If(
            test=Name(id='x', ctx=Load()),
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            orelse=[
                If(
                    test=Name(id='y', ctx=Load()),
                    body=[
                        Expr(
                            value=Constant(value=Ellipsis))],
                    orelse=[
                        Expr(
                            value=Constant(value=Ellipsis))])])])

```


_class_ ast.For(_target_ , _iter_ , _body_ , _orelse_ , _type_comment_)[¶](https://docs.python.org/3/library/ast.html#ast.For "Link to this definition")

A `for` loop. `target` holds the variable(s) the loop assigns to, as a single [`Name`](https://docs.python.org/3/library/ast.html#ast.Name "ast.Name"), [`Tuple`](https://docs.python.org/3/library/ast.html#ast.Tuple "ast.Tuple"), [`List`](https://docs.python.org/3/library/ast.html#ast.List "ast.List"), [`Attribute`](https://docs.python.org/3/library/ast.html#ast.Attribute "ast.Attribute") or [`Subscript`](https://docs.python.org/3/library/ast.html#ast.Subscript "ast.Subscript") node. `iter` holds the item to be looped over, again as a single node. `body` and `orelse` contain lists of nodes to execute. Those in `orelse` are executed if the loop finishes normally, rather than via a `break` statement.

type_comment[¶](https://docs.python.org/3/library/ast.html#ast.For.type_comment "Link to this definition")

`type_comment` is an optional string with the type annotation as a comment.
Copy```
>>> print(ast.dump(ast.parse("""
... for x in y:
...     ...
... else:
...     ...
... """), indent=4))
Module(
    body=[
        For(
            target=Name(id='x', ctx=Store()),
            iter=Name(id='y', ctx=Load()),
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            orelse=[
                Expr(
                    value=Constant(value=Ellipsis))])])

```


_class_ ast.While(_test_ , _body_ , _orelse_)[¶](https://docs.python.org/3/library/ast.html#ast.While "Link to this definition")

A `while` loop. `test` holds the condition, such as a [`Compare`](https://docs.python.org/3/library/ast.html#ast.Compare "ast.Compare") node.
Copy```
>>> print(ast.dump(ast.parse("""
... while x:
...    ...
... else:
...    ...
... """), indent=4))
Module(
    body=[
        While(
            test=Name(id='x', ctx=Load()),
            body=[
                Expr(
                    value=Constant(value=Ellipsis))],
            orelse=[
                Expr(
                    value=Constant(value=Ellipsis))])])

```


_class_ ast.Break[¶](https://docs.python.org/3/library/ast.html#ast.Break "Link to this definition")


_class_ ast.Continue[¶](https://docs.python.org/3/library/ast.html#ast.Continue "Link to this definition")

The `break` and `continue` statements.
Copy```
>>> print(ast.dump(ast.parse("""\
... for a in b:
...     if a > 5:
...         break
...     else:
...         continue
...
... """), indent=4))
Module(
    body=[
        For(
            target=Name(id='a', ctx=Store()),
            iter=Name(id='b', ctx=Load()),
            body=[
                If(
