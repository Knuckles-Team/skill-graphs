##  [Go Version](https://vercel.com/docs/functions/quickstart#go-version)[](https://vercel.com/docs/functions/quickstart#go-version)
The Go runtime will automatically detect the `go.mod` file at the root of your Project to determine the version of Go to use.
If `go.mod` is missing or the version is not defined, the default version 1.20 will be used.
The first time the Go version is detected, it will be automatically downloaded and cached. Subsequent deployments using the same Go version will use the cached Go version instead of downloading it again.
