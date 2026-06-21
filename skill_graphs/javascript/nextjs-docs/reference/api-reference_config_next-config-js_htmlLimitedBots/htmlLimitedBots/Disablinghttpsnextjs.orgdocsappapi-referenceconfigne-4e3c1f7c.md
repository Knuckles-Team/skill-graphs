## Disabling[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#disabling)
To fully disable streaming metadata:
next.config.ts
```
import type { NextConfig } from 'next'

const config: NextConfig = {
  htmlLimitedBots: /.*/,
}

export default config
```
