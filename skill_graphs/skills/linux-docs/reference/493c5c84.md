# Copies "file22.txt" to "file22.backup"
```

---
A command may act upon a comma-separated list of file specs within `_braces_`. [[20]](https://tldp.org/LDP/abs/html/abs-guide.html#FTN.AEN1124) Filename expansion ([globbing](https://tldp.org/LDP/abs/html/abs-guide.html#GLOBBINGREF)) applies to the file specs between the braces.
![Caution](https://tldp.org/LDP/abs/images/caution.gif) |  No spaces allowed within the braces _unless_ the spaces are quoted or escaped. `**echo {file1,file2}\ :{\ A," B",' C'}**` `file1 : A file1 : B file1 : C file2 : A file2 : B file2 : C`
---|---

{a..z}

**Extended Brace expansion.**
```
echo {a..z} # a b c d e f g h i j k l m n o p q r s t u v w x y z
