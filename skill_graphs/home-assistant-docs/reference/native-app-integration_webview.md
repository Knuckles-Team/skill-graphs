[Skip to main content](https://developers.home-assistant.io/docs/api/native-app-integration/webview/#__docusaurus_skipToContent_fallback)
[![Home Assistant](https://developers.home-assistant.io/img/logo.svg) **Developers**](https://developers.home-assistant.io/)
[Home Assistant](https://developers.home-assistant.io/docs/api/native-app-integration/webview/)
  * [Overview](https://developers.home-assistant.io/docs/architecture_index)
  * [Core](https://developers.home-assistant.io/docs/development_index)
  * [Frontend](https://developers.home-assistant.io/docs/frontend)
  * [Supervisor](https://developers.home-assistant.io/docs/supervisor)
  * [Apps](https://developers.home-assistant.io/docs/apps)
  * [Operating System](https://developers.home-assistant.io/docs/operating-system)
  * [Voice](https://developers.home-assistant.io/docs/voice/overview)
  * [Translations](https://developers.home-assistant.io/docs/translations)
  * [Android](https://developers.home-assistant.io/docs/android)


[Misc](https://developers.home-assistant.io/docs/misc)[Blog](https://developers.home-assistant.io/blog)
`⌘``K`
  * [](https://developers.home-assistant.io/)
  * Native App Integration
  * Authenticated WebView


Your application already asked the user to authenticate. This means that your app should not ask the user to authenticate again when they open the Home Assistant UI.
To make this possible, the Home Assistant UI supports [external authentication](https://developers.home-assistant.io/docs/frontend/external-authentication). This allows your app to provide hooks so that the frontend will ask your app for access tokens.
Home Assistant also supports further integration between frontend and app via an [external bus](https://developers.home-assistant.io/docs/frontend/external-bus).
Note that this feature requires a direct connection to the instance.
[Previous Push notifications](https://developers.home-assistant.io/docs/api/native-app-integration/notifications)[Next Brands](https://developers.home-assistant.io/docs/creating_integration_brand)