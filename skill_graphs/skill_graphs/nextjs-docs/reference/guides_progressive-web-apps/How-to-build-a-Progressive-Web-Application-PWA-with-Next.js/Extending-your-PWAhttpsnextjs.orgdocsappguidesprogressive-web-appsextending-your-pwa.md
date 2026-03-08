## Extending your PWA[](https://nextjs.org/docs/app/guides/progressive-web-apps#extending-your-pwa)
  1. **Exploring PWA Capabilities** : PWAs can leverage various web APIs to provide advanced functionality. Consider exploring features like background sync, periodic background sync, or the File System Access API to enhance your application. For inspiration and up-to-date information on PWA capabilities, you can refer to resources like
  2. **Static Exports:** If your application requires not running a server, and instead using a static export of files, you can update the Next.js configuration to enable this change. Learn more in the [Next.js Static Export documentation](https://nextjs.org/docs/app/guides/static-exports). However, you will need to move from Server Actions to calling an external API, as well as moving your defined headers to your proxy.
  3. **Offline Support** : To provide offline functionality, one option is **Note:** this plugin currently requires webpack configuration.
  4. **Security Considerations** : Ensure that your service worker is properly secured. This includes using HTTPS, validating the source of push messages, and implementing proper error handling.
  5. **User Experience** : Consider implementing progressive enhancement techniques to ensure your app works well even when certain PWA features are not supported by the user's browser.


### [manifest.json API Reference for manifest.json file.](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
[PreviousProduction](https://nextjs.org/docs/app/guides/production-checklist)[NextPublic pages](https://nextjs.org/docs/app/guides/public-static-pages)
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
