##  [Header parameters](https://vercel.com/docs#header-parameters)[](https://vercel.com/docs#header-parameters)
Content-LengthnumberRequired
The artifact size in bytes
x-artifact-durationnumberOptional
The time taken to generate the uploaded artifact in milliseconds.
x-artifact-client-cistringOptional
The continuous integration or delivery environment where this artifact was generated.
x-artifact-client-interactiveintegerOptional
1 if the client is an interactive shell. Otherwise 0
x-artifact-tagstringOptional
The base64 encoded tag for this artifact. The value is sent back to clients when the artifact is downloaded as the header `x-artifact-tag`
