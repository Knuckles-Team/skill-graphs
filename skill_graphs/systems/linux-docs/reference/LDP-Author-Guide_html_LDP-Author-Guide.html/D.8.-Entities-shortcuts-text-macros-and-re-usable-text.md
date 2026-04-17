#  D.8. Entities (shortcuts, text macros and reusable text)
There may be some segments of text, or markup that you want to use over and over again. Instead of typing it up multiple times (and then having to edit it multiple times if you want to make a change) you can use _external entities_. Entities can give you a short cut to: reusing whole documents, text snippets, and special markup. Some common ways to use an entity would be for:
  * **text macros for markup.** An example would be a company URL. By using a parameter entity you could refer simply to &my-company-url; instead of typing out the full <ulink url="http://foo.bar">Foo.bar</ulink> each time.
  * **software license.** Such as the GNU Free Documentation License: it is long. And must be included in full in each document. By leaving the license in a separate file you can easily include it in many documents without having to redo the markup each time.
  * **repeated text.** For instance an introduction to a topic which is included both as a summary in one section and as an introduction to the full information in another. Saves on editing time if you need to make changes to both sets of text.


**Example D-12. Adding Entities**
```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN"
"http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd" [
<-- I can add comments here -->
<!ENTITY shortcut "Replace 'shortcut' with this text.">

<!ENTITY sc-to-a-file SYSTEM "anotherfile.xml">
<-- note: the square bracket on the third line is closed on the next
line--> ]>

```

---
To use these entities simply insert the name you gave the entity between a "&" (ampersand) and a ";" (semicolon). For example: "&shortcut;" would expand into "Replace 'shortcut' with this text"; "&sc-to-a-file;" would include the full contents of whatever is in `_anotherfile.xml_`.
An important feature while writing a text is the ability to check whether or not it will be presented in the final draft. It is common to have several parts of the text marked as draft, especially when updating an already existing document.
With the use of parameter entities, you can include or eliminate these drafts by altering only one line at the beginning of a document.
**Example D-13. Use of parameter entities**
```

`<!ENTITY % review "INCLUDE">` ...
`<![%review;[ <para>This paragraph will
be included on the draft when the entity "review" is defined with the
value "INCLUDE". </para> ]]>`

```

---
The entity `review` might have several texts defined, as in [Example D-13](https://tldp.org/LDP/LDP-Author-Guide/html/LDP-Author-Guide.html#ex-entity-parameters). When the changes to the text are considered final, you need only to remove parts of the text between the 3rd. and 6th. lines.
To keep the draft definitions and hide the text in the final draft, just alter the specification of the entity from `INCLUDE` to `IGNORE`.
* * *
