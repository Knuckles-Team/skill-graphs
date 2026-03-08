##  `django.utils.feedgenerator`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.feedgenerator "Link to this heading")
Sample usage:
```
>>> from django.utils import feedgenerator
>>> feed = feedgenerator.Rss201rev2Feed(
...     title="Poynter E-Media Tidbits",
...     link="http://www.poynter.org/column.asp?id=31",
...     description="A group blog by the sharpest minds in online media/journalism/publishing.",
...     language="en",
... )
>>> feed.add_item(
...     title="Hello",
...     link="http://www.holovaty.com/test/",
...     description="Testing.",
... )
>>> with open("test.rss", "w") as fp:
...     feed.write(fp, "utf-8")
...

```

For simplifying the selection of a generator use `feedgenerator.DefaultFeed` which is currently `Rss201rev2Feed`
For definitions of the different versions of RSS, see:

get_tag_uri(_url_ , _date_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#get_tag_uri)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.get_tag_uri "Link to this definition")

Creates a TagURI.
See
###  `SyndicationFeed`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#syndicationfeed "Link to this heading")

_class_ SyndicationFeed[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed "Link to this definition")

Base class for all syndication feeds. Subclasses should provide `write()`.

__init__(_title_ , _link_ , _description_ , _language =None_, _author_email =None_, _author_name =None_, _author_link =None_, _subtitle =None_, _categories =None_, _feed_url =None_, _feed_copyright =None_, _feed_guid =None_, _ttl =None_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.__init__)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.__init__ "Link to this definition")

Initialize the feed with the given dictionary of metadata, which applies to the entire feed.
Any extra keyword arguments you pass to `__init__` will be stored in `self.feed`.
All parameters should be strings, except `categories`, which should be a sequence of strings.

add_item(_title_ , _link_ , _description_ , _author_email =None_, _author_name =None_, _author_link =None_, _pubdate =None_, _comments =None_, _unique_id =None_, _categories =()_, _item_copyright =None_, _ttl =None_, _updateddate =None_, _enclosures =None_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.add_item)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.add_item "Link to this definition")

Adds an item to the feed. All args are expected to be strings except `pubdate` and `updateddate`, which are `datetime.datetime` objects, and `enclosures`, which is a list of `Enclosure` instances.

num_items()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.num_items)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.num_items "Link to this definition")


root_attributes()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.root_attributes)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.root_attributes "Link to this definition")

Return extra attributes to place on the root (i.e. feed/channel) element. Called from `write()`.

add_root_elements(_handler_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.add_root_elements)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.add_root_elements "Link to this definition")

Add elements in the root (i.e. feed/channel) element. Called from `write()`.

item_attributes(_item_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.item_attributes)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.item_attributes "Link to this definition")

Return extra attributes to place on each item (i.e. item/entry) element.

add_item_elements(_handler_ , _item_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.add_item_elements)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.add_item_elements "Link to this definition")

Add elements on each item (i.e. item/entry) element.

write(_outfile_ , _encoding_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.write)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.write "Link to this definition")

Outputs the feed in the given encoding to `outfile`, which is a file-like object. Subclasses should override this.

writeString(_encoding_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.writeString)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.writeString "Link to this definition")

Returns the feed in the given encoding as a string.

latest_post_date()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#SyndicationFeed.latest_post_date)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.SyndicationFeed.latest_post_date "Link to this definition")

Returns the latest `pubdate` or `updateddate` for all items in the feed. If no items have either of these attributes this returns the current UTC date/time.
###  `Enclosure`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#enclosure "Link to this heading")

_class_ Enclosure[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#Enclosure)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.Enclosure "Link to this definition")

Represents an RSS enclosure
###  `RssFeed`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#rssfeed "Link to this heading")

_class_ RssFeed(_SyndicationFeed_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#RssFeed)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.RssFeed "Link to this definition")

###  `Rss201rev2Feed`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#rss201rev2feed "Link to this heading")

_class_ Rss201rev2Feed(_RssFeed_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#Rss201rev2Feed)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.Rss201rev2Feed "Link to this definition")

Spec:
###  `RssUserland091Feed`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#rssuserland091feed "Link to this heading")

_class_ RssUserland091Feed(_RssFeed_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#RssUserland091Feed)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.RssUserland091Feed "Link to this definition")

Spec:
###  `Atom1Feed`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#atom1feed "Link to this heading")

_class_ Atom1Feed(_SyndicationFeed_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/feedgenerator/#Atom1Feed)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.feedgenerator.Atom1Feed "Link to this definition")

Spec:
