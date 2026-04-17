##  D.9.1. HTML file names
By default, when separate HTML files are made, the SGML processor will assign arbitrary names to the resulting files. This can be confusing to readers who may bookmark a page only to have it change. Whatever your reasoning, here's how to make separate files named the way you want:
In your first `<article>` tag (which should be the only one) include an `_id_` parameter and call it "index". This will make your tag look like this:
```

`<article id="index">`
```

---
Do not modify the first `<chapter>` tag, as it's usually an introduction and you want that on the first page. For each other `<section>` tag, include the id parameter and name it. A name should include only alphanumeric characters, and it should be short enough to understand what it is.
```

	`<chapter id="tips">`

```

---
![Note](https://tldp.org/LDP/LDP-Author-Guide/images/note.gif) | **Pick section IDs intelligently**
---|---
|  We all know that
![Warning](https://tldp.org/LDP/LDP-Author-Guide/images/warning.gif) | **HTML file name generation using Jade**
---|---
|  If you are using Jade to transform your DocBook into HTML you must use the following parameter: `_-V %use-id-as-filename%_`.
* * *
