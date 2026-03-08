## Google Third-Parties[](https://nextjs.org/docs/app/guides/third-party-libraries#google-third-parties)
All supported third-party libraries from Google can be imported from `@next/third-parties/google`.
### Google Tag Manager[](https://nextjs.org/docs/app/guides/third-party-libraries#google-tag-manager)
The `GoogleTagManager` component can be used to instantiate a
To load Google Tag Manager for all routes, include the component directly in your root layout and pass in your GTM container ID:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { GoogleTagManager } from '@next/third-parties/google'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

To load Google Tag Manager for a single route, include the component in your page file:
app/page.js
```
import { GoogleTagManager } from '@next/third-parties/google'

export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```

#### Sending Events[](https://nextjs.org/docs/app/guides/third-party-libraries#sending-events)
The `sendGTMEvent` function can be used to track user interactions on your page by sending events using the `dataLayer` object. For this function to work, the `<GoogleTagManager />` component must be included in either a parent layout, page, or component, or directly in the same file.
app/page.js
```
'use client'

import { sendGTMEvent } from '@next/third-parties/google'

export function EventButton() {
  return (
    <div>
      <button
        onClick={() => sendGTMEvent({ event: 'buttonClicked', value: 'xyz' })}
      >
        Send Event
      </button>
    </div>
  )
}
```

Refer to the Tag Manager
#### Server-side Tagging[](https://nextjs.org/docs/app/guides/third-party-libraries#server-side-tagging)
If you're using a server-side tag manager and serving `gtm.js` scripts from your tagging server you can use `gtmScriptUrl` option to specify the URL of the script.
#### Options[](https://nextjs.org/docs/app/guides/third-party-libraries#options)
Options to pass to the Google Tag Manager. For a full list of options, read the
Name | Type | Description
---|---|---
`gtmId` | Required* | Your GTM container ID. Usually starts with `GTM-`.
`gtmScriptUrl` | Optional* | GTM script URL. Defaults to `https://www.googletagmanager.com/gtm.js`.
`dataLayer` | Optional | Data layer object to instantiate the container with.
`dataLayerName` | Optional | Name of the data layer. Defaults to `dataLayer`.
`auth` | Optional | Value of authentication parameter (`gtm_auth`) for environment snippets.
`preview` | Optional | Value of preview parameter (`gtm_preview`) for environment snippets.
*`gtmId` can be omitted when `gtmScriptUrl` is provided to support
### Google Analytics[](https://nextjs.org/docs/app/guides/third-party-libraries#google-analytics)
The `GoogleAnalytics` component can be used to include `gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.
> **Recommendation** : If Google Tag Manager is already included in your application, you can configure Google Analytics directly using it, rather than including Google Analytics as a separate component. Refer to the `gtag.js`.
To load Google Analytics for all routes, include the component directly in your root layout and pass in your measurement ID:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { GoogleAnalytics } from '@next/third-parties/google'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XYZ" />
    </html>
  )
}
```

To load Google Analytics for a single route, include the component in your page file:
app/page.js
```
import { GoogleAnalytics } from '@next/third-parties/google'

export default function Page() {
  return <GoogleAnalytics gaId="G-XYZ" />
}
```

#### Sending Events[](https://nextjs.org/docs/app/guides/third-party-libraries#sending-events-1)
The `sendGAEvent` function can be used to measure user interactions on your page by sending events using the `dataLayer` object. For this function to work, the `<GoogleAnalytics />` component must be included in either a parent layout, page, or component, or directly in the same file.
app/page.js
```
'use client'

import { sendGAEvent } from '@next/third-parties/google'

export function EventButton() {
  return (
    <div>
      <button
        onClick={() => sendGAEvent('event', 'buttonClicked', { value: 'xyz' })}
      >
        Send Event
      </button>
    </div>
  )
}
```

Refer to the Google Analytics
#### Tracking Pageviews[](https://nextjs.org/docs/app/guides/third-party-libraries#tracking-pageviews)
Google Analytics automatically tracks pageviews when the browser history state changes. This means that client-side navigations between Next.js routes will send pageview data without any configuration.
To ensure that client-side navigations are being measured correctly, verify that the _“Page changes based on browser history events”_ checkbox is selected.
> **Note** : If you decide to manually send pageview events, make sure to disable the default pageview measurement to avoid having duplicate data. Refer to the Google Analytics
#### Options[](https://nextjs.org/docs/app/guides/third-party-libraries#options-1)
Options to pass to the `<GoogleAnalytics>` component.
Name | Type | Description
---|---|---
`gaId` | Required | Your `G-`.
`dataLayerName` | Optional | Name of the data layer. Defaults to `dataLayer`.
`nonce` | Optional | A [nonce](https://nextjs.org/docs/app/guides/content-security-policy#nonces).
### Google Maps Embed[](https://nextjs.org/docs/app/guides/third-party-libraries#google-maps-embed)
The `GoogleMapsEmbed` component can be used to add a `loading` attribute to lazy-load the embed below the fold.
app/page.js
```
import { GoogleMapsEmbed } from '@next/third-parties/google'

export default function Page() {
  return (
    <GoogleMapsEmbed
      apiKey="XYZ"
      height={200}
      width="100%"
      mode="place"
      q="Brooklyn+Bridge,New+York,NY"
    />
  )
}
```

#### Options[](https://nextjs.org/docs/app/guides/third-party-libraries#options-2)
Options to pass to the Google Maps Embed. For a full list of options, read the
Name | Type | Description
---|---|---
`apiKey` | Required | Your api key.
`mode` | Required |
`height` | Optional | Height of the embed. Defaults to `auto`.
`width` | Optional | Width of the embed. Defaults to `auto`.
`style` | Optional | Pass styles to the iframe.
`allowfullscreen` | Optional | Property to allow certain map parts to go full screen.
`loading` | Optional | Defaults to lazy. Consider changing if you know your embed will be above the fold.
`q` | Optional | Defines map marker location. _This may be required depending on the map mode_.
`center` | Optional | Defines the center of the map view.
`zoom` | Optional | Sets initial zoom level of the map.
`maptype` | Optional | Defines type of map tiles to load.
`language` | Optional | Defines the language to use for UI elements and for the display of labels on map tiles.
`region` | Optional | Defines the appropriate borders and labels to display, based on geo-political sensitivities.
### YouTube Embed[](https://nextjs.org/docs/app/guides/third-party-libraries#youtube-embed)
The `YouTubeEmbed` component can be used to load and display a YouTube embed. This component loads faster by using
app/page.js
```
import { YouTubeEmbed } from '@next/third-parties/google'

export default function Page() {
  return <YouTubeEmbed videoid="ogfYd705cRs" height={400} params="controls=0" />
}
```

#### Options[](https://nextjs.org/docs/app/guides/third-party-libraries#options-3)
Name | Type | Description
---|---|---
`videoid` | Required | YouTube video id.
`width` | Optional | Width of the video container. Defaults to `auto`
`height` | Optional | Height of the video container. Defaults to `auto`
`playlabel` | Optional | A visually hidden label for the play button for accessibility.
`params` | Optional | The video player params defined
Params are passed as a query param string.
Eg: `params="controls=0&start=10&end=30"`
`style` | Optional | Used to apply styles to the video container.
[PreviousVitest](https://nextjs.org/docs/app/guides/testing/vitest)[NextUpgrading](https://nextjs.org/docs/app/guides/upgrading)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
