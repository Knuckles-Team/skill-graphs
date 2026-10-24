# Update Release ID
Source: https://docs.postiz.com/public-api/posts/update-release-id

PUT /posts/{id}/release-id
Updates the `releaseId` of a post that currently has its release ID set to `"missing"`. This connects the post to its actual published content on the platform, enabling analytics and statistics tracking.

Typically used after calling the **Get Missing Content** endpoint to retrieve the list of available content items.
