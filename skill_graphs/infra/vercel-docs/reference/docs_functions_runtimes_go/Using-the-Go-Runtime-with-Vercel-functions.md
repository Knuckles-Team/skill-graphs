# Using the Go Runtime with Vercel functions
Last updated January 13, 2026
The Go runtime is available in [Beta](https://vercel.com/docs/release-phases#beta) on [all plans](https://vercel.com/docs/plans)
The Go runtime is used by Vercel to compile Go Vercel functions that expose a single HTTP handler, from a `.go` file within an `/api` directory at your project's root.
For example, define an `index.go` file inside an `/api` directory as follows:
/api/index.go
```
package handler

import (
  "fmt"
  "net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "<h1>Hello from Go!</h1>")
}
```

An example `index.go` file inside an `/api` directory.
For advanced usage, such as using private packages with your Go projects, see the [Advanced Go Usage section](https://vercel.com/docs/functions/quickstart#advanced-go-usage).
The exported function needs to include the
