## Template Rendering[¶](https://flask.palletsprojects.com/en/stable/api/#template-rendering "Link to this heading")

flask.render_template(_template_name_or_list_ , _** context_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.render_template "Link to this definition")

Render a template by name with the given context.

Parameters:

  * **template_name_or_list** (_|_[_Template_](https://jinja.palletsprojects.com/en/stable/api/#jinja2.Template "\(in Jinja v3.1.x\)") _|__[__|_[_Template_](https://jinja.palletsprojects.com/en/stable/api/#jinja2.Template "\(in Jinja v3.1.x\)") _]_) – The name of the template to render. If a list is given, the first name to exist will be rendered.
  * **context** (



Return type:


flask.render_template_string(_source_ , _** context_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.render_template_string "Link to this definition")

Render a template from the given source string with the given context.

Parameters:

  * **source** (
  * **context** (



Return type:


flask.stream_template(_template_name_or_list_ , _** context_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.stream_template "Link to this definition")

Render a template by name with the given context as a stream. This returns an iterator of strings, which can be used as a streaming response from a view.

Parameters:

  * **template_name_or_list** (_|_[_Template_](https://jinja.palletsprojects.com/en/stable/api/#jinja2.Template "\(in Jinja v3.1.x\)") _|__[__|_[_Template_](https://jinja.palletsprojects.com/en/stable/api/#jinja2.Template "\(in Jinja v3.1.x\)") _]_) – The name of the template to render. If a list is given, the first name to exist will be rendered.
  * **context** (



Return type:
Changelog
Added in version 2.2.

flask.stream_template_string(_source_ , _** context_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.stream_template_string "Link to this definition")

Render a template from the given source string with the given context as a stream. This returns an iterator of strings, which can be used as a streaming response from a view.

Parameters:

  * **source** (
  * **context** (



Return type:
Changelog
Added in version 2.2.

flask.get_template_attribute(_template_name_ , _attribute_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.get_template_attribute "Link to this definition")

Loads a macro (or variable) a template exports. This can be used to invoke a macro from within Python code. If you for example have a template named `_cider.html` with the following contents:
```
{% macro hello(name) %}Hello {{ name }}!{% endmacro %}

```

You can access this from Python code like this:
```
hello = get_template_attribute('_cider.html', 'hello')
return hello('World')

```

Changelog
Added in version 0.2.

Parameters:

  * **template_name** (
  * **attribute** (



Return type:
