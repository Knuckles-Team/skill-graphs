# Get Missing Content
Source: https://docs.postiz.com/public-api/posts/missing-content

GET /posts/{id}/missing
When a post has been published but the platform did not return a usable post ID (the `releaseId` is set to `"missing"`), this endpoint fetches recent content from the provider so you can match and connect the correct one to the post.

The provider must implement the optional `missing` method. If the provider does not support it, an empty array is returned.
