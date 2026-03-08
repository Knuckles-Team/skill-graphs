## Reference[](https://nextjs.org/docs/app/api-reference/functions/image-response#reference)
### Parameters[](https://nextjs.org/docs/app/api-reference/functions/image-response#parameters)
The following parameters are available for `ImageResponse`:
```
import { ImageResponse } from 'next/og'

new ImageResponse(
  element: ReactElement,
  options: {
    width?: number = 1200
    height?: number = 630
    emoji?: 'twemoji' | 'blobmoji' | 'noto' | 'openmoji' = 'twemoji',
    fonts?: {
      name: string,
      data: ArrayBuffer,
      weight: number,
      style: 'normal' | 'italic'
    }[]
    debug?: boolean = false

    // Options that will be passed to the HTTP response
    status?: number = 200
    statusText?: string
    headers?: Record<string, string>
  },
)
```

> Examples are available in the
### Supported HTML and CSS features[](https://nextjs.org/docs/app/api-reference/functions/image-response#supported-html-and-css-features)
`ImageResponse` supports common CSS properties including flexbox and absolute positioning, custom fonts, text wrapping, centering, and nested images.
Please refer to
