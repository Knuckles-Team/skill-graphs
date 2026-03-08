### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/flashing/ "Message Flashing") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/wtforms/ "Form Validation with WTForms") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/)


# Template Inheritance[¶](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/#template-inheritance "Link to this heading")
The most powerful part of Jinja is template inheritance. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines **blocks** that child templates can override.
Sounds complicated but is very basic. It’s easiest to understand it by starting with an example.
## Base Template[¶](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/#base-template "Link to this heading")
This template, which we’ll call `layout.html`, defines a simple HTML skeleton document that you might use for a simple two-column page. It’s the job of “child” templates to fill the empty blocks with content:
```
<!doctype html>
<html>
  <head>
    {% block head %}
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
  </head>
  <body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
      {% block footer %}
      &copy; Copyright 2010 by <a href="http://domain.invalid/">you</a>.
      {% endblock %}
    </div>
  </body>
</html>

```

In this example, the `{% block %}` tags define four blocks that child templates can fill in. All the `block` tag does is tell the template engine that a child template may override those portions of the template.
## Child Template[¶](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/#child-template "Link to this heading")
A child template might look like this:
```
{% extends "layout.html" %}
{% block title %}Index{% endblock %}
{% block head %}
  {{ super() }}
  <style type="text/css">
    .important { color: #336699; }
  </style>
{% endblock %}
{% block content %}
  <h1>Index</h1>
  <p class="important">
    Welcome on my awesome homepage.
{% endblock %}

```

The `{% extends %}` tag is the key here. It tells the template engine that this template “extends” another template. When the template system evaluates this template, first it locates the parent. The extends tag must be the first tag in the template. To render the contents of a block defined in the parent template, use `{{ super() }}`.
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/)
    * [Base Template](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/#base-template)
    * [Child Template](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/#child-template)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [Form Validation with WTForms](https://flask.palletsprojects.com/en/stable/patterns/wtforms/ "previous chapter")
      * Next: [Message Flashing](https://flask.palletsprojects.com/en/stable/patterns/flashing/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10129/019ccc1c-0b55-76a1-b9a4-a9a7a7861bcc/)
