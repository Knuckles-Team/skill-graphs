## Self-hosted videos[](https://nextjs.org/docs/app/guides/videos#self-hosted-videos)
Self-hosting videos may be preferable for several reasons:
  * **Complete control and independence** : Self-hosting gives you direct management over your video content, from playback to appearance, ensuring full ownership and control, free from external platform constraints.
  * **Customization for specific needs** : Ideal for unique requirements, like dynamic background videos, it allows for tailored customization to align with design and functional needs.
  * **Performance and scalability considerations** : Choose storage solutions that are both high-performing and scalable, to support increasing traffic and content size effectively.
  * **Cost and integration** : Balance the costs of storage and bandwidth with the need for easy integration into your Next.js framework and broader tech ecosystem.


### Using Vercel Blob for video hosting[](https://nextjs.org/docs/app/guides/videos#using-vercel-blob-for-video-hosting)
**1. Uploading a video to Vercel Blob**
In your Vercel dashboard, navigate to the "Storage" tab and select your
Alternatively, you can upload your video using a server action. For detailed instructions, refer to the Vercel documentation on
**2. Displaying the video in Next.js**
Once the video is uploaded and stored, you can display it in your Next.js application. Here's an example of how to do this using the `<video>` tag and React Suspense:
app/page.jsx
```
import { Suspense } from 'react'
import { list } from '@vercel/blob'

export default function Page() {
  return (
    <Suspense fallback={<p>Loading video...</p>}>
      <VideoComponent fileName="my-video.mp4" />
    </Suspense>
  )
}

async function VideoComponent({ fileName }) {
  const { blobs } = await list({
    prefix: fileName,
    limit: 1,
  })
  const { url } = blobs[0]

  return (
    <video controls preload="none" aria-label="Video player">
      <source src={url} type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  )
}
```

In this approach, the page uses the video's `@vercel/blob` URL to display the video using the `VideoComponent`. React Suspense is used to show a fallback until the video URL is fetched and the video is ready to be displayed.
### Adding subtitles to your video[](https://nextjs.org/docs/app/guides/videos#adding-subtitles-to-your-video)
If you have subtitles for your video, you can easily add them using the `<track>` element inside your `<video>` tag. You can fetch the subtitle file from `<VideoComponent>` to include subtitles.
app/page.jsx
```
async function VideoComponent({ fileName }) {
  const { blobs } = await list({
    prefix: fileName,
    limit: 2,
  })
  const { url } = blobs[0]
  const { url: captionsUrl } = blobs[1]

  return (
    <video controls preload="none" aria-label="Video player">
      <source src={url} type="video/mp4" />
      <track src={captionsUrl} kind="subtitles" srcLang="en" label="English" />
      Your browser does not support the video tag.
    </video>
  )
}
```

By following this approach, you can effectively self-host and integrate videos into your Next.js applications.
