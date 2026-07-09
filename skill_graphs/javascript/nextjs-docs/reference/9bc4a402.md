## Configuration as a Function[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#configuration-as-a-function)
You can also use a function:
next.config.mjs
```
// @ts-check

export default (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Async Configuration[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#async-configuration)
Since Next.js 12.1.0, you can use an async function:
next.config.js
```
// @ts-check

module.exports = async (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Phase[](https://nextjs.org/docs/pages/api-reference/config/next-config-js#phase)
`phase` is the current context in which the configuration is loaded. You can see the `next/constants`:
next.config.js
```
// @ts-check

const { PHASE_DEVELOPMENT_SERVER } = require('next/constants')

module.exports = (phase, { defaultConfig }) => {
  if (phase === PHASE_DEVELOPMENT_SERVER) {
    return {
      /* development only config options here */
    }
  }

  return {
    /* config options for all phases except development here */
  }
}
```
