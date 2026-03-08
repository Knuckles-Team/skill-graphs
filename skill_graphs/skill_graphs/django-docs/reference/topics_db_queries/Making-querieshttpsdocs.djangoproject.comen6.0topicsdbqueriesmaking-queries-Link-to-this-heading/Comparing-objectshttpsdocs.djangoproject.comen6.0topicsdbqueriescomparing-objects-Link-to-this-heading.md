## Comparing objects[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#comparing-objects "Link to this heading")
To compare two model instances, use the standard Python comparison operator, the double equals sign: `==`. Behind the scenes, that compares the primary key values of two models.
Using the `Entry` example above, the following two statements are equivalent:
```
>>> some_entry == other_entry
>>> some_entry.id == other_entry.id

```

If a model’s primary key isn’t called `id`, no problem. Comparisons will always use the primary key, whatever it’s called. For example, if a model’s primary key field is called `name`, these two statements are equivalent:
```
>>> some_obj == other_obj
>>> some_obj.name == other_obj.name

```
