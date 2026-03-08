# From vladz's "base64.sh" example script.
```

---
The _{a..z}_ [extended brace expansion](https://tldp.org/LDP/abs/html/abs-guide.html#BRACEEXPREF3) construction is a feature introduced in [version 3](https://tldp.org/LDP/abs/html/abs-guide.html#BASH3REF) of _Bash_.

{}

**Block of code [curly brackets].** Also referred to as an _inline group_ , this construct, in effect, creates an _anonymous function_ (a function without a name). However, unlike in a "standard" [function](https://tldp.org/LDP/abs/html/abs-guide.html#FUNCTIONREF), the variables inside a code block remain visible to the remainder of the script.
```
`bash$ ``**{ local a;
	      a=123; }**`
`bash: local: can only be used in a
function`

```

---
```
a=123
{ a=321; }
echo "a = $a"   # a = 321   (value inside code block)
