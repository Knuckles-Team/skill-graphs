## Scout
### Full-Text Improvements
Pull request by
Several improvements to full-text support were added when using the `database` engine. First up, you can now pass multiple columns to `orWhereFullText` in a single call. Secondly, when using Postgres and no other developer-provided ordering has been defined, Scout automatically adds relevance-based ordering by default to match MySQL's built-in ordering behavior.
