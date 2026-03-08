## Streaming and Suspense[](https://nextjs.org/docs/app/guides/self-hosting#streaming-and-suspense)
The Next.js App Router supports [streaming responses](https://nextjs.org/docs/app/api-reference/file-conventions/loading) when self-hosting. If you are using nginx or a similar proxy, you will need to configure it to disable buffering to enable streaming.
For example, you can disable buffering in nginx by setting `X-Accel-Buffering` to `no`:
next.config.js
```
module.exports = {
  async headers() {
    return [
      {
        source: '/:path*{/}?',
        headers: [
          {
            key: 'X-Accel-Buffering',
            value: 'no',
          },
        ],
      },
    ]
  },
}
```
