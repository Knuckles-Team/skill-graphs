## Control Flow[¶](https://go.dev/doc/faq#Control_flow)
### Why does Go not have the `?:` operator?[¶](https://go.dev/doc/faq#Does_Go_have_a_ternary_form)
There is no ternary testing operation in Go. You may use the following to achieve the same result:
```
if expr {
    n = trueVal
} else {
    n = falseVal
}

```

The reason `?:` is absent from Go is that the language’s designers had seen the operation used too often to create impenetrably complex expressions. The `if-else` form, although longer, is unquestionably clearer. A language needs only one conditional control flow construct.
