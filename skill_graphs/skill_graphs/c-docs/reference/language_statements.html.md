##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flanguage%2Fstatements&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flanguage%2Fstatements "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/language/statements.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/language/statements.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/language/statements.html)
##### Views
  * [View](https://en.cppreference.com/w/c/language/statements.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/language/statements.html)
![ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611897;dc_trk_aid=613858979;dc_trk_cid=235700574;ord=177295381;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
# Statements
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [language](https://en.cppreference.com/w/c/language.html "c/language")
[ C](https://en.cppreference.com/w/c.html "c")
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
---
[Language](https://en.cppreference.com/w/c/language.html "c/language")
[Headers](https://en.cppreference.com/w/c/header.html "c/header")
[Type support](https://en.cppreference.com/w/c/types.html "c/types")
[Program utilities](https://en.cppreference.com/w/c/program.html "c/program")
[Variadic function support](https://en.cppreference.com/w/c/variadic.html "c/variadic")
[Error handling](https://en.cppreference.com/w/c/error.html "c/error")
[Dynamic memory management](https://en.cppreference.com/w/c/memory.html "c/memory")
[Strings library](https://en.cppreference.com/w/c/string.html "c/string")
[Algorithms](https://en.cppreference.com/w/c/algorithm.html "c/algorithm")
[Numerics](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[Date and time utilities](https://en.cppreference.com/w/c/chrono.html "c/chrono")
[Input/output support](https://en.cppreference.com/w/c/io.html "c/io")
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
[ C language](https://en.cppreference.com/w/c/language.html "c/language")
[Basic concepts](https://en.cppreference.com/w/c/language/basic_concepts.html "c/language/basic concepts")
---
[ Keywords](https://en.cppreference.com/w/c/keyword.html "c/keyword")
[ Preprocessor](https://en.cppreference.com/w/c/preprocessor.html "c/preprocessor")
**Statements**
[ Expressions](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions")
[ Initialization](https://en.cppreference.com/w/c/language/initialization.html "c/language/initialization")
[ Declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations")
[ Functions](https://en.cppreference.com/w/c/language/functions.html "c/language/functions")
Miscellaneous
[ History of C](https://en.cppreference.com/w/c/language/history.html "c/language/history")
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/navbar_content&action=edit)
**Statements**
Labels
---
[label : statement](https://en.cppreference.com/w/c/language/statements.html#Labels "c/language/statements")
Expression statements
[expression ;](https://en.cppreference.com/w/c/language/statements.html#Expression_statements "c/language/statements")
Compound statements
[{ statement... }](https://en.cppreference.com/w/c/language/statements.html#Compound_statements "c/language/statements")
Selection statements
[if](https://en.cppreference.com/w/c/language/if.html "c/language/if")
[switch](https://en.cppreference.com/w/c/language/switch.html "c/language/switch")
Iteration statements
[while](https://en.cppreference.com/w/c/language/while.html "c/language/while")
[do-while](https://en.cppreference.com/w/c/language/do.html "c/language/do")
[for](https://en.cppreference.com/w/c/language/for.html "c/language/for")
Jump statements
[break](https://en.cppreference.com/w/c/language/break.html "c/language/break")
[continue](https://en.cppreference.com/w/c/language/continue.html "c/language/continue")
[return](https://en.cppreference.com/w/c/language/return.html "c/language/return")
[goto](https://en.cppreference.com/w/c/language/goto.html "c/language/goto")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/statements/navbar_content&action=edit)
Statements are fragments of the C program that are executed in sequence. The body of any function is a compound statement, which, in turn is a sequence of statements and declarations:
```
int main(void)
{ // start of a compound statement
    int n = 1; // declaration (not a statement)
    n = n+1; // expression statement
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("n = %d\n", n); // expression statement
    return 0; // return statement
} // end of compound statement, end of function body
```


There are five types of statements:
1) [compound statements](https://en.cppreference.com/w/c/language/statements.html#Compound_statements)
2) [expression statements](https://en.cppreference.com/w/c/language/statements.html#Expression_statements)
3) [selection statements](https://en.cppreference.com/w/c/language/statements.html#Selection_statements)
4) [iteration statements](https://en.cppreference.com/w/c/language/statements.html#Iteration_statements)
5) [jump statements](https://en.cppreference.com/w/c/language/statements.html#Jump_statements)
An [attribute specifier sequence](https://en.cppreference.com/w/c/language/attributes.html "c/language/attributes") (attr-spec-seq) can be applied to an unlabeled statement, in which case (except for an expression statement) the attributes are applied to the respective statement.  | (since C23)
---|---
## Contents
  * [1 Labels](https://en.cppreference.com/w/c/language/statements.html#Labels)
  * [2 Compound statements](https://en.cppreference.com/w/c/language/statements.html#Compound_statements)
  * [3 Expression statements](https://en.cppreference.com/w/c/language/statements.html#Expression_statements)
  * [4 Selection statements](https://en.cppreference.com/w/c/language/statements.html#Selection_statements)
  * [5 Iteration statements](https://en.cppreference.com/w/c/language/statements.html#Iteration_statements)
  * [6 Jump statements](https://en.cppreference.com/w/c/language/statements.html#Jump_statements)
  * [7 References](https://en.cppreference.com/w/c/language/statements.html#References)
  * [8 See also](https://en.cppreference.com/w/c/language/statements.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=1 "Edit section: Labels")] Labels
Any statement can be _labeled_ , by providing a name followed by a colon before the statement itself.
---
attr-spec-seq(optional)(since C23) identifier `**:**` |  (1)  |
attr-spec-seq(optional)(since C23) `**case**` constant-expression `**:**` |  (2)  |
attr-spec-seq(optional)(since C23) `**default**``**:**` |  (3)  |
1) Target for [goto](https://en.cppreference.com/w/c/language/goto.html "c/language/goto").
2) Case label in a [switch](https://en.cppreference.com/w/c/language/switch.html "c/language/switch") statement.
3) Default label in a [switch](https://en.cppreference.com/w/c/language/switch.html "c/language/switch") statement.
Any statement (but not a declaration) may be preceded by any number of _labels_ , each of which declares identifier to be a label name, which must be unique within the enclosing function (in other words, label names have [function scope](https://en.cppreference.com/w/c/language/scope.html "c/language/scope")).
Label declaration has no effect on its own, does not alter the flow of control, or modify the behavior of the statement that follows in any way.
A label shall be followed by a statement.  | (until C23)
---|---
A label can appear without its following statement. If a label appears alone in a block, it behaves as if it is followed by a [null statement](https://en.cppreference.com/w/c/language/statements.html#Expression_statements).  The optional [attr-spec-seq](https://en.cppreference.com/w/c/language/attributes.html "c/language/attributes") is applied to the label.  | (since C23)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=2 "Edit section: Compound statements")] Compound statements
A compound statement, or _block_ , is a brace-enclosed sequence of statements and declarations.
---
`**{**` statement `|` declaration...(optional) `**} **` |  |  (until C23)
attr-spec-seq(optional) `**{**` unlabeled-statement `|` label `|` declaration...(optional) `**} **` |  |  (since C23)
The compound statement allows a set of declarations and statements to be grouped into one unit that can be used anywhere a single statement is expected (for example, in an [if](https://en.cppreference.com/w/c/language/if.html "c/language/if") statement or an iteration statement):
```
if (expr) // start of if-statement
{ // start of block
  int n = 1; // declaration
  [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%d\n", n); // expression statement
} // end of block, end of if-statement
```

Each compound statement introduces its own [block scope](https://en.cppreference.com/w/c/language/scope.html "c/language/scope").
The initializers of the variables with automatic [storage duration](https://en.cppreference.com/w/c/language/storage_class_specifiers.html "c/language/storage duration") declared inside a block and the VLA declarators are executed when flow of control passes over these declarations in order, as if they were statements:
```
int main(void)
{ // start of block
  { // start of block
       [puts](https://en.cppreference.com/w/c/io/puts.html)("hello"); // expression statement
       int n = [printf](https://en.cppreference.com/w/c/io/fprintf.html)("abc\n"); // declaration, prints "abc", stores 4 in n
       int a[n*[printf](https://en.cppreference.com/w/c/io/fprintf.html)("1\n")]; // declaration, prints "1", allocates 8*sizeof(int)
       [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%zu\n", sizeof(a)); // expression statement
  } // end of block, scope of n and a ends
  int n = 7; // n can be reused
}
```

###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=3 "Edit section: Expression statements")] Expression statements
An expression followed by a semicolon is a statement.
---
expression(optional) `**;**` |  (1)  |
attr-spec-seq expression `**;**` |  (2)  |  (since C23)
Most statements in a typical C program are expression statements, such as assignments or function calls.
An expression statement without an expression is called a _null statement_. It is often used to provide an empty body to a [for](https://en.cppreference.com/w/c/language/for.html "c/language/for") or [while](https://en.cppreference.com/w/c/language/while.html "c/language/while") loop. It can also be used to carry a label in the end of a compound statement or before a declaration:
```
[puts](https://en.cppreference.com/w/c/io/puts.html)("hello"); // expression statement
char *s;
while (*s++ != '\0')
    ; // null statement
```

The optional [attr-spec-seq](https://en.cppreference.com/w/c/language/attributes.html "c/language/attributes") is applied to the expression.  An attr-spec-seq followed by `**;**`does not form an expression statement. It forms an[attribute declaration](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations") instead.  | (since C23)
---|---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=4 "Edit section: Selection statements")] Selection statements
The selection statements choose between one of several statements depending on the value of an expression.
---
attr-spec-seq(optional)(since C23) `**if**``**(**` expression `**)**` statement |  (1)  |
attr-spec-seq(optional)(since C23) `**if**``**(**` expression `**)**` statement `**else**` statement |  (2)  |
attr-spec-seq(optional)(since C23) `**switch**``**(**` expression `**)**` statement |  (3)  |
1) [if](https://en.cppreference.com/w/c/language/if.html "c/language/if") statement
2) [if](https://en.cppreference.com/w/c/language/if.html "c/language/if") statement with an else clause
3) [switch](https://en.cppreference.com/w/c/language/switch.html "c/language/switch") statement
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=5 "Edit section: Iteration statements")] Iteration statements
The iteration statements repeatedly execute a statement.
---
attr-spec-seq(optional)(since C23) `**while**``**(**` expression `**)**` statement |  (1)  |
attr-spec-seq(optional)(since C23) `**do**` statement `**while**``**(**` expression `**)**``**;**` |  (2)  |
attr-spec-seq(optional)(since C23) `**for**``**(**` init-clause `**;**` expression(optional) `**;**` expression(optional) `**)**` statement |  (3)  |
1) [while](https://en.cppreference.com/w/c/language/while.html "c/language/while") loop
2) [do-while](https://en.cppreference.com/w/c/language/do.html "c/language/do") loop
3) [for](https://en.cppreference.com/w/c/language/for.html "c/language/for") loop
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=6 "Edit section: Jump statements")] Jump statements
The jump statements unconditionally transfer flow control.
---
attr-spec-seq(optional)(since C23) `**break**``**;**` |  (1)  |
attr-spec-seq(optional)(since C23) `**continue**``**;**` |  (2)  |
attr-spec-seq(optional)(since C23) `**return**` expression(optional) `**;**` |  (3)  |
attr-spec-seq(optional)(since C23) `**goto**` identifier `**;**` |  (4)  |
1) [break](https://en.cppreference.com/w/c/language/break.html "c/language/break") statement
2) [continue](https://en.cppreference.com/w/c/language/continue.html "c/language/continue") statement
3) [return](https://en.cppreference.com/w/c/language/return.html "c/language/return") statement with an optional expression
4) [goto](https://en.cppreference.com/w/c/language/goto.html "c/language/goto") statement
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=7 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 6.8 Statements and blocks (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 6.8 Statements and blocks (p: 106-112)


  * C11 standard (ISO/IEC 9899:2011):


  * 6.8 Statements and blocks (p: 146-154)


  * C99 standard (ISO/IEC 9899:1999):


  * 6.8 Statements and blocks (p: 131-139)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 3.6 STATEMENTS


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=edit&section=8 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/language/statements.html "cpp/language/statements") for Statements
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/language/statements&oldid=179343](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&oldid=179343)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/language/statements.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/language/statements "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/language/statements "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&oldid=179343 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/language/statements&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/language/statements "c/language/statements")
  * [Česky](http://cs.cppreference.com/w/c/language/statements "c/language/statements")
  * [Deutsch](http://de.cppreference.com/w/c/language/statements "c/language/statements")
  * [Español](http://es.cppreference.com/w/c/language/statements "c/language/statements")
  * [Français](http://fr.cppreference.com/w/c/language/statements "c/language/statements")
  * [Italiano](http://it.cppreference.com/w/c/language/statements "c/language/statements")
  * [日本語](http://ja.cppreference.com/w/c/language/statements "c/language/statements")
  * [한국어](http://ko.cppreference.com/w/c/language/statements "c/language/statements")
  * [Polski](http://pl.cppreference.com/w/c/language/statements "c/language/statements")
  * [Português](http://pt.cppreference.com/w/c/language/statements "c/language/statements")
  * [Русский](http://ru.cppreference.com/w/c/language/statements "c/language/statements")
  * [Türkçe](http://tr.cppreference.com/w/c/language/statements "c/language/statements")
  * [中文](http://zh.cppreference.com/w/c/language/statements "c/language/statements")


  * This page was last modified on 8 January 2025, at 00:07.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
