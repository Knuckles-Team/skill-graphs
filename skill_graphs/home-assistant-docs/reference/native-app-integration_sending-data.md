[Skip to main content](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#__docusaurus_skipToContent_fallback)
[![Home Assistant](https://developers.home-assistant.io/img/logo.svg) **Developers**](https://developers.home-assistant.io/)
[Home Assistant](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
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
  * [Architecture](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Development Workflow](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Building Integrations](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Development Checklist](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Integration Quality Scale](https://developers.home-assistant.io/docs/core/integration-quality-scale/)
  * [The `hass` object](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Entities](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Areas, Devices and Entities](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Authentication](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Config entries](https://developers.home-assistant.io/docs/config_entries_index)
  * [Data entry flow](https://developers.home-assistant.io/docs/data_entry_flow_index)
  * [Creating Labs preview features](https://developers.home-assistant.io/docs/development/labs)
  * [Automations](https://developers.home-assistant.io/docs/automations)
  * [Device Automations](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Intents](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Conversation](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [LLM API](https://developers.home-assistant.io/docs/core/llm/)
  * [Native App Integration](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
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
  * [External APIs](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)
  * [Misc](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/)


  * [](https://developers.home-assistant.io/)
  * Native App Integration
  * Sending data home


On this page
# Sending data home
Once you have registered your app with the mobile app component, you can start interacting with Home Assistant via the provided webhook information.
## Sending webhook data via Rest API[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#sending-webhook-data-via-rest-api "Direct link to Sending webhook data via Rest API")
The first step is to turn the returned webhook ID into a full URL: `<instance_url>/api/webhook/<webhook_id>`. This will be the only url that we will need for all our interactions. The webhook endpoint will not require authenticated requests.
If you were provided a Cloudhook URL during registration, you should use that by default and only fall back to a constructed URL as described above if that request fails.
If you were provided a remote UI URL during registration, you should use that as the `instance_url` when constructing a URL and only fallback to the user provided URL if the remote UI URL fails.
To summarize, here's how requests should be made:
  1. If you have a Cloudhook URL, use that until a request fails. When a request fails, go to step 2.
  2. If you have a remote UI URL, use that to construct a webhook URL: `<remote_ui_url>/api/webhook/<webhook_id>`. When a request fails, go to step 3.
  3. Construct a webhook URL using the instance URL provided during setup: `<instance_url>/api/webhook/<webhook_id>`.


## Sending webhook data via WebSocket API[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#sending-webhook-data-via-websocket-api "Direct link to Sending webhook data via WebSocket API")
Webhooks can also be delivered via the WebSocket API by sending the `webhook/handle` command:
```
{  
  "type": "webhook/handle",  
  "id": 5,  
  "method": "GET",  
  // Below fields are optional  
  "body": "{\"hello\": \"world\"}",  
  "headers": {  
    "Content-Type": "application/json"  
  },  
  "query": "a=1&b=2",  
}  

```

The response will look as follows:
```
{  
  "type": "result",  
  "id": 5,  
  "result": {  
    "body": "{\"ok\": true}",  
    "status": 200,  
    "headers": {"Content-Type": response.content_type},  
  }  
}  

```

## Short note on instance URLs[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#short-note-on-instance-urls "Direct link to Short note on instance URLs")
Some users have configured Home Assistant to be available outside of their home network using a dynamic DNS service. There are some routers that don't support hairpinning / NAT loopback: a device sending data from inside the routers network, via the externally configured DNS service, to Home Assistant, which also resides inside the local network.
To work around this, the app should record which WiFi SSID is the users home network, and use a direct connection when connected to the home WiFi network.
## Interaction basics[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#interaction-basics "Direct link to Interaction basics")
### Request[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#request "Direct link to Request")
All interaction will be done by making HTTP POST requests to the webhook url. These requests do not need to contain authentication.
The payload format depends on the type of interaction, but it all shares a common base:
```
{  
  "type": "<type of message>",  
  "data": {}  
}  

```

If you received a `secret` during registration, you **MUST** encrypt your message and put it in the payload like this:
```
{  
  "type": "encrypted",  
  "encrypted": true,  
  "encrypted_data": "<encrypted message>"  
}  

```

### Response[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#response "Direct link to Response")
As a general rule, expect to receive a 200 response for all your requests. There are a few cases in which you will receive another code:
  * You will receive a 400 status code if your JSON is invalid. However, you will not receive this error if the encrypted JSON is invalid.
  * You will receive a 201 when creating a sensor
  * If you receive a 404, the `mobile_app` component most likely isn't loaded.
  * Receiving a 410 means the integration has been deleted. You should notify the user and most likely register again.


## Implementing encryption[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#implementing-encryption "Direct link to Implementing encryption")
`mobile_app` supports two way encrypted communication via 
Sodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more.
### Choosing a library[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#choosing-a-library "Direct link to Choosing a library")
Libraries that wrap Sodium exist for most modern programming languages and platforms. Sodium itself is written in C.
Here are the libraries we suggest using, although you should feel free to use whatever works well for you.
  * Swift/Objective-C: 


For other languages, please see the list of 
### Configuration[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#configuration "Direct link to Configuration")
We use the `sodium_base64_VARIANT_ORIGINAL` (that is, "original", no padding, not URL safe). If the payload does not contain a `data` key when unencrypted (such as with the [get_config](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data#get-config) request), an empty JSON object (`{}`) must be encrypted instead.
### Signaling encryption support[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#signaling-encryption-support "Direct link to Signaling encryption support")
There are two ways to enable encryption support:
  * **During initial registration** you set `supports_encryption` to `true`.
  * **After initial registration** you call the `enable_encryption` webhook action.


The Home Assistant instance must be able to install `libsodium` to enable encryption. Confirm that you should make all future webhook requests encrypted by the presence of the key `secret` in the initial registration or enable encryption response.
You must store this secret forever. There is no way to recover it via the Home Assistant UI and you should **not** ask users to investigate hidden storage files to re-enter the encryption key. You should create a new registration if encryption ever fails and alert the user.
A registration may not initially support encryption due to a lack of Sodium/NaCL on the Home Assistant Core side. You should always strive to encrypt communications if possible. Therefore, we politely request that from time to time you attempt to enable encryption automatically or allow the user to manually enable encryption via a button in your app. That way, they can attempt to first fix whatever error is causing Sodium/NaCL to be uninstallable and then have an encrypted registration later. Home Assistant Core will log exact details if Sodium/NaCL is uninstallable.
## Update device location[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#update-device-location "Direct link to Update device location")
This message will inform Home Assistant of new location information.
```
{  
  "type": "update_location",  
  "data": {  
    "gps": [12.34, 56.78],  
    "gps_accuracy": 120,  
    "battery": 45  
  }  
}  

```

Key | Type | Description  
---|---|---  
`location_name` | string | Name of the zone the device is in.  
`gps` | latlong | Current location as latitude and longitude.  
`gps_accuracy` | int | GPS accuracy in meters. Must be greater than 0.  
`battery` | int | Percentage of battery the device has left. Must be greater than 0.  
`speed` | int | Speed of the device in meters per second. Must be greater than 0.  
`altitude` | int | Altitude of the device in meters. Must be greater than 0.  
`course` | int | The direction in which the device is traveling, measured in degrees and relative to due north. Must be greater than 0.  
`vertical_accuracy` | int | The accuracy of the altitude value, measured in meters. Must be greater than 0.  
## Call a service action[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#call-a-service-action "Direct link to Call a service action")
Call a service action in Home Assistant.
```
{  
  "type": "call_service",  
  "data": {  
    "domain": "light",  
    "service": "turn_on",  
    "service_data": {  
      "entity_id": "light.kitchen"  
    }  
  }  
}  

```

Key | Type | Description  
---|---|---  
`domain` | string | The domain of the service action  
`service` | string | The service action name  
`service_data` | dict | The data to send to the service action  
## Fire an event[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#fire-an-event "Direct link to Fire an event")
Fire an event in Home Assistant. Please be mindful of the data structure as documented on our [Data Science portal](https://data.home-assistant.io/docs/events/#database-table).
```
{  
  "type": "fire_event",  
  "data": {  
    "event_type": "my_custom_event",  
    "event_data": {  
      "something": 50  
    }  
  }  
}  

```

Key | Type | Description  
---|---|---  
`event_type` | string | Type of the event to fire  
`event_data` | string | Data of the event to fire  
## Render templates[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#render-templates "Direct link to Render templates")
Renders one or more templates and returns the result(s).
```
{  
  "type": "render_template",  
  "data": {  
    "my_tpl": {  
      "template": "Hello {{ name }}, you are {{ states('person.paulus') }}.",  
      "variables": {  
        "name": "Paulus"  
      }  
    }  
  }  
}  

```

`data` must contain a map of `key`: `dictionary`. Results will be returned like `{"my_tpl": "Hello Paulus, you are home"}`. This allows for rendering multiple templates in a single call.
Key | Type | Description  
---|---|---  
`template` | string | The template to render  
`variables` | Dict | The extra template variables to include.  
## Update registration[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#update-registration "Direct link to Update registration")
Update your app registration. Use this if the app version changed or any of the other values.
```
{  
  "type": "update_registration",  
  "data": {  
    "app_data": {  
      "push_token": "abcd",  
      "push_url": "https://push.mycool.app/push"  
    },  
    "app_version": "2.0.0",  
    "device_name": "Robbies iPhone",  
    "manufacturer": "Apple, Inc.",  
    "model": "iPhone XR",  
    "os_version": "23.02"  
  }  
}  

```

All keys are optional.
Key | Type | Description  
---|---|---  
`app_data` | Dict | App data can be used if the app has a supporting component that extends mobile_app functionality or wishes to enable the notification platform.  
`app_version` | string | Version of the mobile app.  
`device_name` | string | Name of the device running the app.  
`manufacturer` | string | The manufacturer of the device running the app.  
`model` | string | The model of the device running the app.  
`os_version` | string | The OS version of the device running the app.  
## Get zones[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#get-zones "Direct link to Get zones")
Get all enabled zones.
```
{  
  "type": "get_zones"  
}  

```

## Get config[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#get-config "Direct link to Get config")
Returns a version of `/api/config` with values useful for configuring your app.
```
{  
  "type": "get_config"  
}  

```

## Enable encryption[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#enable-encryption "Direct link to Enable encryption")
_This requires Home Assistant 0.106 or later._
Enables encryption support for an existing registration
```
{  
  "type": "enable_encryption"  
}  

```

There are two errors you may receive:
  * `encryption_already_enabled` - Encryption is already enabled for this registration
  * `encryption_not_available` - Sodium/NaCL is unable to be installed. Cease all future attempts to enable encryption.


## Stream camera[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#stream-camera "Direct link to Stream camera")
_This requires Home Assistant 0.112 or later._
Retrieve path information on how to stream a Camera.
```
{  
  "type": "stream_camera",  
  "data": {  
    "camera_entity_id": "camera.name_here"  
  }  
}  

```

Key | Type | Description  
---|---|---  
`camera_entity_id` | string | The camera entity to retrieve streaming information about  
The response will include paths for streaming either via HLS or via MJPEG image previews.
```
{  
  "hls_path": "/api/hls/…/playlist.m3u8",  
  "mjpeg_path": "/api/camera_proxy_stream/…"  
}  

```

If HLS streaming is not available, the `hls_path` will be `null`. See notes above on instance URL for how to construct a full URL.
## Process conversation[​](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#process-conversation "Direct link to Process conversation")
_This requires Home Assistant 2023.2.0 or later._
Process a sentence with the conversation integration.
```
{  
  "type": "conversation_process",  
  "data": {  
    "text": "Turn on the lights",  
    "language": "en",  
    "conversation_id": "ABCD",  
  }  
}  

```

For available keys and response, see the [conversation API documentation](https://developers.home-assistant.io/docs/intent_conversation_api).
Last updated on **Jan 2, 2026**
[ Previous Connecting to an instance](https://developers.home-assistant.io/docs/api/native-app-integration/setup)[Next Sensors](https://developers.home-assistant.io/docs/api/native-app-integration/sensors)
  * [Sending webhook data via Rest API](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#sending-webhook-data-via-rest-api)
  * [Sending webhook data via WebSocket API](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#sending-webhook-data-via-websocket-api)
  * [Short note on instance URLs](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#short-note-on-instance-urls)
  * [Interaction basics](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#interaction-basics)
    * [Request](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#request)
    * [Response](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#response)
  * [Implementing encryption](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#implementing-encryption)
    * [Choosing a library](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#choosing-a-library)
    * [Configuration](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#configuration)
    * [Signaling encryption support](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#signaling-encryption-support)
  * [Update device location](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#update-device-location)
  * [Call a service action](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#call-a-service-action)
  * [Fire an event](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#fire-an-event)
  * [Render templates](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#render-templates)
  * [Update registration](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#update-registration)
  * [Get zones](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#get-zones)
  * [Get config](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#get-config)
  * [Enable encryption](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#enable-encryption)
  * [Stream camera](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#stream-camera)
  * [Process conversation](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data/#process-conversation)


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