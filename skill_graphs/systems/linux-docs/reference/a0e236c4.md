#                            ^ Note whitespace before #
```

---
Comments may also follow [whitespace](https://tldp.org/LDP/abs/html/abs-guide.html#WHITESPACEREF) at the beginning of a line.
```
     # A tab precedes this comment.
```

---
Comments may even be embedded within a [pipe](https://tldp.org/LDP/abs/html/abs-guide.html#PIPEREF).
```
initial=( `cat "$startfile" | sed -e '/#/d' | tr -d '\n' |\
