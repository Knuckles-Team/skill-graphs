## Default list[](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#default-list)
Next.js includes a default list of HTML limited bots, including:
  * Google crawlers (e.g. Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
  * Bingbot
  * Twitterbot
  * Slackbot


See the full list
Specifying a `htmlLimitedBots` config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.
next.config.ts
TypeScript
JavaScript TypeScript
```
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}

export default config
```
