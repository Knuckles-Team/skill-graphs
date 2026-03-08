### Navigation
  * [index](https://flask.palletsprojects.com/en/stable/genindex/ "General Index")
  * [modules](https://flask.palletsprojects.com/en/stable/py-modindex/ "Python Module Index") |
  * [next](https://flask.palletsprojects.com/en/stable/patterns/favicon/ "Adding a favicon") |
  * [previous](https://flask.palletsprojects.com/en/stable/patterns/lazyloading/ "Lazily Loading Views") |
  * [Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/) »
  * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/) »
  * [MongoDB with MongoEngine](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/)


# MongoDB with MongoEngine[¶](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#mongodb-with-mongoengine "Link to this heading")
Using a document database like MongoDB is a common alternative to relational SQL databases. This pattern shows how to use
A running MongoDB server and
```
pip install flask-mongoengine

```

## Configuration[¶](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#configuration "Link to this heading")
Basic setup can be done by defining `MONGODB_SETTINGS` on `app.config` and creating a `MongoEngine` instance.
```
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
}
db = MongoEngine(app)

```

## Mapping Documents[¶](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#mapping-documents "Link to this heading")
To declare a model that represents a Mongo document, create a class that inherits from `Document` and declare each of the fields.
```
import mongoengine as me

class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()

```

If the document has nested fields, use `EmbeddedDocument` to defined the fields of the embedded document and `EmbeddedDocumentField` to declare it on the parent document.
```
class Imdb(me.EmbeddedDocument):
    imdb_id = me.StringField()
    rating = me.DecimalField()
    votes = me.IntField()

class Movie(me.Document):
    ...
    imdb = me.EmbeddedDocumentField(Imdb)

```

## Creating Data[¶](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#creating-data "Link to this heading")
Instantiate your document class with keyword arguments for the fields. You can also assign values to the field attributes after instantiation. Then call `doc.save()`.
```
bttf = Movie(title="Back To The Future", year=1985)
bttf.actors = [
    "Michael J. Fox",
    "Christopher Lloyd"
]
bttf.imdb = Imdb(imdb_id="tt0088763", rating=8.5)
bttf.save()

```

## Queries[¶](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#queries "Link to this heading")
Use the class `objects` attribute to make queries. A keyword argument looks for an equal value on the field.
```
bttf = Movie.objects(title="Back To The Future").get_or_404()

```

Query operators may be used by concatenating them with the field name using a double-underscore. `objects`, and queries returned by calling it, are iterable.
```
some_theron_movie = Movie.objects(actors__in=["Charlize Theron"]).first()

for recents in Movie.objects(year__gte=2017):
    print(recents.title)

```

## Documentation[¶](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#documentation "Link to this heading")
There are many more ways to define and query documents with MongoEngine. For more information, check out the
Flask-MongoEngine adds helpful utilities on top of MongoEngine. Check out their
[ ![Logo of Flask](https://flask.palletsprojects.com/en/stable/_static/flask-logo.svg) ](https://flask.palletsprojects.com/en/stable/)
### Contents
  * [MongoDB with MongoEngine](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/)
    * [Configuration](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#configuration)
    * [Mapping Documents](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#mapping-documents)
    * [Creating Data](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#creating-data)
    * [Queries](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#queries)
    * [Documentation](https://flask.palletsprojects.com/en/stable/patterns/mongoengine/#documentation)


### Navigation
  * [Overview](https://flask.palletsprojects.com/en/stable/)
    * [Patterns for Flask](https://flask.palletsprojects.com/en/stable/patterns/)
      * Previous: [Lazily Loading Views](https://flask.palletsprojects.com/en/stable/patterns/lazyloading/ "previous chapter")
      * Next: [Adding a favicon](https://flask.palletsprojects.com/en/stable/patterns/favicon/ "next chapter")


### Quick search
·
![](https://server.ethicalads.io/proxy/view/10129/019ccc1a-a6f3-7fb3-acbb-e7aba1d739fd/)
