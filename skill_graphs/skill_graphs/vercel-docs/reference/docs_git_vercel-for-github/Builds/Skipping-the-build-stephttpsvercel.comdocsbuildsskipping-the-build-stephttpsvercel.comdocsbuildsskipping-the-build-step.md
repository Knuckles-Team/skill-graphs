##  [Skipping the build step](https://vercel.com/docs/builds#skipping-the-build-step)[](https://vercel.com/docs/builds#skipping-the-build-step)
For static websites (HTML, CSS, and client-side JavaScript only), no build step is required. In those cases:
  1. Set Framework Preset to Other.
  2. Leave the build command blank.
  3. (Optionally) override the Output Directory if you want to serve a folder other than `public` or `.`.
