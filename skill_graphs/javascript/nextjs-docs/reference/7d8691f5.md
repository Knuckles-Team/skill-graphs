## Why This Error Occurred[](https://nextjs.org/docs/messages/url-deprecated#why-this-error-occurred)
In versions prior to 6.x the `url` property got magically injected into every `Page` component (every page inside the `pages` directory).
The reason this is going away is that we want to make things very predictable and explicit. Having a magical url property coming out of nowhere doesn't aid that goal.
> **Note** : ⚠️ In some cases using React Dev Tools may trigger this warning even if you do not reference `url` anywhere in your code. Try temporarily disabling the extension and see if the warning persists.
