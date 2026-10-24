[Skip to main content](https://developers.home-assistant.io/docs/api/native-app-integration/#__docusaurus_skipToContent_fallback)
[![Home Assistant](https://developers.home-assistant.io/img/logo.svg) **Developers**](https://developers.home-assistant.io/)
[Home Assistant](https://developers.home-assistant.io/docs/api/native-app-integration/)
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
  * [Introduction](https://developers.home-assistant.io/docs/development_index)
  * [Architecture](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Development Workflow](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Building Integrations](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Development Checklist](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Integration Quality Scale](https://developers.home-assistant.io/docs/core/integration-quality-scale/)
  * [The `hash` object](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Entities](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Areas, Devices and Entities](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Authentication](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Config entries](https://developers.home-assistant.io/docs/config_entries_index)
  * [Data entry flow](https://developers.home-assistant.io/docs/data_entry_flow_index)
  * [Creating Labs preview features](https://developers.home-assistant.io/docs/development/labs)
  * [Automations](https://developers.home-assistant.io/docs/automations)
  * [Device Automations](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Intents](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Conversation](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [LLM API](https://developers.home-assistant.io/docs/core/llm/)
  * [Native App Integration](https://developers.home-assistant.io/docs/api/native-app-integration/)
    * [Introduction](https://developers.home-assistant.io/docs/api/native-app-integration)
    * [Connecting to an instance](https://developers.home-assistant.io/docs/api/native-app-integration/setup)
    * [Sending data home](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data)
    * [Sensors](https://developers.home-assistant.io/docs/api/native-app-integration/sensors)
    * [Push notifications](https://developers.home-assistant.io/docs/api/native-app-integration/notifications)
    * [Authenticated WebView](https://developers.home-assistant.io/docs/api/native-app-integration/webview)
  * [Brands](https://developers.home-assistant.io/docs/creating_integration_brand)
  * [Application credentials](https://developers.home-assistant.io/docs/core/platform/application_credentials)
  * [Backup](https://developers.home-assistant.io/docs/core/platform/backup)
  * [Raising exceptions](https://developers.home-assistant.io/docs/core/platform/raising_exceptions)
  * [Repairs](https://developers.home-assistant.io/docs/core/platform/repairs)
  * [Reproduce state](https://developers.home-assistant.io/docs/core/platform/reproduce_state)
  * [Significant change](https://developers.home-assistant.io/docs/core/platform/significant_change)
  * [External APIs](https://developers.home-assistant.io/docs/api/native-app-integration/)
  * [Misc](https://developers.home-assistant.io/docs/api/native-app-integration/)


  * [](https://developers.home-assistant.io/)
  * Native App Integration
  * Introduction


# Native app integration
This guide describes how to build a native Home Assistant app that communicates with Home Assistant and offers a seamless integration. Below is a list of the things that we will discuss in this guide.
  * Allow the user to establish a connection and authenticate with their own Home Assistant instance.
  * Send location and device info back to Home Assistant.
  * Call service actions, fire events and render templates.
  * A view to control the house via an authenticated webview.


Last updated on **Jul 16, 2024**
[ Previous LLM API](https://developers.home-assistant.io/docs/core/llm/)[Next Connecting to an instance](https://developers.home-assistant.io/docs/api/native-app-integration/setup)
More Home Assistant
  * [Homepage](https://www.home-assistant.io)
  * [Data Science Portal](https://data.home-assistant.io)
  * [Alerts](https://alerts.home-assistant.io)
  * [System Status](https://status.home-assistant.io/)


Social
  * [Blog](https://developers.home-assistant.io/blog)
  * [Discord chat](https://www.home-assistant.io/join-chat)


Other
  * [Privacy](https://www.home-assistant.io/privacy/)
  * [Security](https://www.home-assistant.io/security/)


Thanks
[![Home Assistant](https://developers.home-assistant.io/img/logo-white.svg)](https://www.home-assistant.io)
Copyright © 2026 Home Assistant. Built with Docusaurus.
