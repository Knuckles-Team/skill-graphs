##  [Advanced Go Usage](https://vercel.com/docs/functions/quickstart#advanced-go-usage)[](https://vercel.com/docs/functions/quickstart#advanced-go-usage)
In order to use this runtime, no configuration is needed. You only need to create a file inside the `api` directory.
The entry point of this runtime is a global matching `.go` files that export a function that implements the `http.HandlerFunc` signature.
###  [Private Packages for Go](https://vercel.com/docs/functions/quickstart#private-packages-for-go)[](https://vercel.com/docs/functions/quickstart#private-packages-for-go)
To install private packages with `go get`, add an [Environment Variable](https://vercel.com/docs/environment-variables) named `GIT_CREDENTIALS`.
The value should be the URL to the Git repo including credentials, such as `https://username:token@github.com`.
All major Git providers are supported including GitHub, GitLab, Bitbucket, as well as a self-hosted Git server.
With GitHub, you will need to
* * *
[ Previous Functions ](https://vercel.com/docs/functions)[ Next Streaming ](https://vercel.com/docs/functions/streaming-functions)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * Other frameworks


On this page
  * [Go Version](https://vercel.com/docs/functions/quickstart#go-version)
  * [Go Dependencies](https://vercel.com/docs/functions/quickstart#go-dependencies)
  * [Go Build Configuration](https://vercel.com/docs/functions/quickstart#go-build-configuration)
  * [Advanced Go Usage](https://vercel.com/docs/functions/quickstart#advanced-go-usage)
  * [Private Packages for Go](https://vercel.com/docs/functions/quickstart#private-packages-for-go)


Copy as MarkdownGive feedbackAsk AI about this page
