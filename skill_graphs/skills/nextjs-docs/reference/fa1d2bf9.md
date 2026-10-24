## Using `<video>` and `<iframe>`[](https://nextjs.org/docs/app/guides/videos#using-video-and-iframe)
Videos can be embedded on the page using the HTML **`<video>`**tag for direct video files and**`<iframe>`**for external platform-hosted videos.
###  `<video>`[](https://nextjs.org/docs/app/guides/videos#video)
The HTML
app/ui/video.jsx
```
export function Video() {
  return (
    <video width="320" height="240" controls preload="none">
      <source src="/path/to/video.mp4" type="video/mp4" />
      <track
        src="/path/to/captions.vtt"
        kind="subtitles"
        srcLang="en"
        label="English"
      />
      Your browser does not support the video tag.
    </video>
  )
}
```

### Common `<video>` tag attributes[](https://nextjs.org/docs/app/guides/videos#common-video-tag-attributes)
Attribute | Description | Example Value
---|---|---
`src` | Specifies the source of the video file. | `<video src="/path/to/video.mp4" />`
`width` | Sets the width of the video player. | `<video width="320" />`
`height` | Sets the height of the video player. | `<video height="240" />`
`controls` | If present, it displays the default set of playback controls. | `<video controls />`
`autoPlay` | Automatically starts playing the video when the page loads. Note: Autoplay policies vary across browsers. | `<video autoPlay />`
`loop` | Loops the video playback. | `<video loop />`
`muted` | Mutes the audio by default. Often used with `autoPlay`. | `<video muted />`
`preload` | Specifies how the video is preloaded. Values: `none`, `metadata`, `auto`. | `<video preload="none" />`
`playsInline` | Enables inline playback on iOS devices, often necessary for autoplay to work on iOS Safari. | `<video playsInline />`
> **Good to know** : When using the `autoPlay` attribute, it is important to also include the `muted` attribute to ensure the video plays automatically in most browsers and the `playsInline` attribute for compatibility with iOS devices.
For a comprehensive list of video attributes, refer to the
### Video best practices[](https://nextjs.org/docs/app/guides/videos#video-best-practices)
  * **Fallback Content:** When using the `<video>` tag, include fallback content inside the tag for browsers that do not support video playback.
  * **Subtitles or Captions:** Include subtitles or captions for users who are deaf or hard of hearing. Utilize the `<video>` elements to specify caption file sources.
  * **Accessible Controls:** Standard HTML5 video controls are recommended for keyboard navigation and screen reader compatibility. For advanced needs, consider third-party players like


###  `<iframe>`[](https://nextjs.org/docs/app/guides/videos#iframe)
The HTML `<iframe>` tag allows you to embed videos from external platforms like YouTube or Vimeo.
app/page.jsx
```
export default function Page() {
  return (
    <iframe src="https://www.youtube.com/embed/19g66ezsKAg" allowFullScreen />
  )
}
```

### Common `<iframe>` tag attributes[](https://nextjs.org/docs/app/guides/videos#common-iframe-tag-attributes)
Attribute | Description | Example Value
---|---|---
`src` | The URL of the page to embed. | `<iframe src="https://example.com" />`
`width` | Sets the width of the iframe. | `<iframe width="500" />`
`height` | Sets the height of the iframe. | `<iframe height="300" />`
`allowFullScreen` | Allows the iframe content to be displayed in full-screen mode. | `<iframe allowFullScreen />`
`sandbox` | Enables an extra set of restrictions on the content within the iframe. | `<iframe sandbox />`
`loading` | Optimize loading behavior (e.g., lazy loading). | `<iframe loading="lazy" />`
`title` | Provides a title for the iframe to support accessibility. | `<iframe title="Description" />`
For a comprehensive list of iframe attributes, refer to the
### Choosing a video embedding method[](https://nextjs.org/docs/app/guides/videos#choosing-a-video-embedding-method)
There are two ways you can embed videos in your Next.js application:
  * **Self-hosted or direct video files:** Embed self-hosted videos using the `<video>` tag for scenarios requiring detailed control over the player's functionality and appearance. This integration method within Next.js allows for customization and control of your video content.
  * **Using video hosting services (YouTube, Vimeo, etc.):** For video hosting services like YouTube or Vimeo, you'll embed their iframe-based players using the `<iframe>` tag. While this method limits some control over the player, it offers ease of use and features provided by these platforms.


Choose the embedding method that aligns with your application's requirements and the user experience you aim to deliver.
### Embedding externally hosted videos[](https://nextjs.org/docs/app/guides/videos#embedding-externally-hosted-videos)
To embed videos from external platforms, you can use Next.js to fetch the video information and React Suspense to handle the fallback state while loading.
**1. Create a Server Component for video embedding**
The first step is to create a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) that generates the appropriate iframe for embedding the video. This component will fetch the source URL for the video and render the iframe.
app/ui/video-component.jsx
```
export default async function VideoComponent() {
  const src = await getVideoSrc()

  return <iframe src={src} allowFullScreen />
}
```

**2. Stream the video component using React Suspense**
After creating the Server Component to embed the video, the next step is to [stream](https://nextjs.org/docs/app/api-reference/file-conventions/loading) the component using
app/page.jsx
```
import { Suspense } from 'react'
import VideoComponent from '../ui/VideoComponent.jsx'

export default function Page() {
  return (
    <section>
      <Suspense fallback={<p>Loading video...</p>}>
        <VideoComponent />
      </Suspense>
      {/* Other content of the page */}
    </section>
  )
}
```

> **Good to know** : When embedding videos from external platforms, consider the following best practices:
>   * Ensure the video embeds are responsive. Use CSS to make the iframe or video player adapt to different screen sizes.
>   * Implement
>

This approach results in a better user experience as it prevents the page from blocking, meaning the user can interact with the page while the video component streams in.
For a more engaging and informative loading experience, consider using a loading skeleton as the fallback UI. So instead of showing a simple loading message, you can show a skeleton that resembles the video player like this:
app/page.jsx
```
import { Suspense } from 'react'
import VideoComponent from '../ui/VideoComponent.jsx'
import VideoSkeleton from '../ui/VideoSkeleton.jsx'

export default function Page() {
  return (
    <section>
      <Suspense fallback={<VideoSkeleton />}>
        <VideoComponent />
      </Suspense>
      {/* Other content of the page */}
    </section>
  )
}
```
