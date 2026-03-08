## Session IDs in URLs[¶](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#session-ids-in-urls "Link to this heading")
The Django sessions framework is entirely, and solely, cookie-based. It does not fall back to putting session IDs in URLs as a last resort, as PHP does. This is an intentional design decision. Not only does that behavior make URLs ugly, it makes your site vulnerable to session-ID theft via the “Referer” header.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/http/middleware/)
[Working with forms ](https://docs.djangoproject.com/en/5.0/topics/forms/)
[](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#top)
