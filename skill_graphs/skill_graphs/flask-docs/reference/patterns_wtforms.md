### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/ "Template Inheritance") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/ "View Decorators") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [Form Validation with WTForms](https://flask.palletsprojects.com/en/stable/patterns/wtforms/)


# Form Validation with WTForms[¶](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#form-validation-with-wtforms "Link to this heading")
When you have to work with form data submitted by a browser view, code quickly becomes very hard to read. There are libraries out there designed to make this process easier to manage. One of them is
When you are working with WTForms you have to define your forms as classes first. I recommend breaking up the application into multiple modules ([Large Applications as Packages](https://flask.palletsprojects.com/en/stable/patterns/packages/)) for that and adding a separate module for the forms.
Getting the most out of WTForms with an Extension
The
## The Forms[¶](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#the-forms "Link to this heading")
This is an example form for a typical registration page:
```
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

```

## In the View[¶](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#in-the-view "Link to this heading")
In the view function, the usage of this form looks like this:
```
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

```

Notice we’re implying that the view is using SQLAlchemy here ([SQLAlchemy in Flask](https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/)), but that’s not a requirement, of course. Adapt the code as necessary.
Things to remember:
  1. create the form from the request `form` value if the data is submitted via the HTTP `POST` method and `args` if the data is submitted as `GET`.
  2. to validate the data, call the `validate()` method, which will return `True` if the data validates, `False` otherwise.
  3. to access individual values from the form, access `form.<NAME>.data`.


## Forms in Templates[¶](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#forms-in-templates "Link to this heading")
Now to the template side. When you pass the form to the templates, you can easily render them there. Look at the following example template to see how easy this is. WTForms does half the form generation for us already. To make it even nicer, we can write a macro that renders a field with label and a list of errors if there are any.
Here’s an example `_formhelpers.html` template with such a macro:
```
{% macro render_field(field) %}
  <dt>{{ field.label }}
  <dd>{{ field(**kwargs)|safe }}
  {% if field.errors %}
    <ul class=errors>
    {% for error in field.errors %}
      <li>{{ error }}</li>
    {% endfor %}
    </ul>
  {% endif %}
  </dd>
{% endmacro %}

```

This macro accepts a couple of keyword arguments that are forwarded to WTForm’s field function, which renders the field for us. The keyword arguments will be inserted as HTML attributes. So, for example, you can call `render_field(form.username, class='username')` to add a class to the input element. Note that WTForms returns standard Python strings, so we have to tell Jinja that this data is already HTML-escaped with the `|safe` filter.
Here is the `register.html` template for the function we used above, which takes advantage of the `_formhelpers.html` template:
```
{% from "_formhelpers.html" import render_field %}
<form method=post>
  <dl>
    {{ render_field(form.username) }}
    {{ render_field(form.email) }}
    {{ render_field(form.password) }}
    {{ render_field(form.confirm) }}
    {{ render_field(form.accept_tos) }}
  </dl>
  <p><input type=submit value=Register>
</form>

```

For more information about WTForms, head over to the
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [Form Validation with WTForms](https://flask.palletsprojects.com/en/stable/patterns/wtforms/)
    * [The Forms](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#the-forms)
    * [In the View](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#in-the-view)
    * [Forms in Templates](https://flask.palletsprojects.com/en/stable/patterns/wtforms/#forms-in-templates)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [View Decorators](https://flask.palletsprojects.com/en/stable/patterns/viewdecorators/ "previous chapter")
      * Next: [Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10129/019ccc1c-0b55-76a1-b9a4-a9a7a7861bcc/)
