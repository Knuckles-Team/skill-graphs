## Known browser bugs[](https://nextjs.org/docs/app/api-reference/components/image#known-browser-bugs)
This `next/image` component uses browser native `width`/`height` of `auto`, it is possible to cause
  *     * Use CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }`
    * Use [`loading="eager"`](https://nextjs.org/docs/app/api-reference/components/image#loading) if the image is above the fold
  *     * Enable [AVIF `formats`](https://nextjs.org/docs/app/api-reference/components/image#formats)
    * Use [`placeholder`](https://nextjs.org/docs/app/api-reference/components/image#placeholder)
