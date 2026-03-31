[Skip to main content](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#__docusaurus_skipToContent_fallback)
[![Home Assistant](https://developers.home-assistant.io/img/logo.svg) **Developers**](https://developers.home-assistant.io/)
[Home Assistant](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
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
  * [Architecture](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Development Workflow](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Building Integrations](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Development Checklist](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Integration Quality Scale](https://developers.home-assistant.io/docs/core/integration-quality-scale/)
  * [The `hass` object](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Entities](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Areas, Devices and Entities](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Authentication](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Config entries](https://developers.home-assistant.io/docs/config_entries_index)
  * [Data entry flow](https://developers.home-assistant.io/docs/data_entry_flow_index)
  * [Creating Labs preview features](https://developers.home-assistant.io/docs/development/labs)
  * [Automations](https://developers.home-assistant.io/docs/automations)
  * [Device Automations](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Intents](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Conversation](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [LLM API](https://developers.home-assistant.io/docs/core/llm/)
  * [Native App Integration](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
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
  * [External APIs](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)
  * [Misc](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/)


  * [](https://developers.home-assistant.io/)
  * Native App Integration
  * Sensors


On this page
# Sensors
The `mobile_app` integration supports exposing custom sensors that can be managed entirely via your app.
## Registering a sensor[​](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#registering-a-sensor "Direct link to Registering a sensor")
All sensors must be registered before they can get updated. You can only register one sensor at a time, unlike updating sensors.
To register a sensor, make a request to the webhook like this:
```
{  
  "data": {  
    "attributes": {  
      "foo": "bar"  
    },  
    "device_class": "battery",  
    "icon": "mdi:battery",  
    "name": "Battery State",  
    "state": "12345",  
    "type": "sensor",  
    "unique_id": "battery_state",  
    "unit_of_measurement": "%",  
    "state_class": "measurement",  
    "entity_category": "diagnostic",  
    "disabled": true  
  },  
  "type": "register_sensor"  
}  

```

The valid keys are:
Key | Type | Required | Description  
---|---|---|---  
attributes | object | No | Attributes to attach to the sensor  
device_class | string | No | One of the valid device classes. [Binary Sensor Classes](https://www.home-assistant.io/integrations/binary_sensor/#device-class), [Sensor Classes](https://www.home-assistant.io/integrations/sensor/#device-class)  
icon | Material Design Icon (string) | No | Must be prefixed `mdi:`. If not provided, default value is `mdi:cellphone`  
name | string | Yes | The name of the sensor  
state | bool, float, int, string | Yes | The state of the sensor  
type | string | Yes | The type of the sensor. Must be one of `binary_sensor` or `sensor`  
unique_id | string | Yes | An identifier unique to this installation of your app. You'll need this later. Usually best when its a safe version of the sensor name  
unit_of_measurement | string | No | The unit of measurement for the sensor  
state_class | string | No | The [state class](https://developers.home-assistant.io/docs/core/entity/sensor#available-state-classes) of the entity (sensors only)  
entity_category | string | No | The entity category of the entity  
disabled | boolean | No | If the entity should be enabled or disabled.  
Sensors will appear as soon as they are registered.
## Updating a sensor[​](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#updating-a-sensor "Direct link to Updating a sensor")
Once a sensor has been registered, you need to update it. This is very similar to registering it, but you can update all your sensors at the same time.
For example, to update the sensor we registered above, you would send this:
```
{  
  "data": [  
    {  
      "attributes": {  
        "hello": "world"  
      },  
      "icon": "mdi:battery",  
      "state": 123,  
      "type": "sensor",  
      "unique_id": "battery_state"  
    }  
  ],  
  "type": "update_sensor_states"  
}  

```

Only some of the keys are allowed during updates:
Key | Type | Required | Description  
---|---|---|---  
attributes | object | No | Attributes to attach to the sensor  
icon | Material Design Icon (string) | No | Must be prefixed `mdi:`  
state | bool, float, int, string | Yes | The state of the sensor  
type | string | Yes | The type of the sensor. Must be one of `binary_sensor` or `sensor`  
unique_id | string | Yes | An identifier unique to this installation of your app. You'll need this later. Usually best when its a safe version of the sensor name  
The response to updating a sensor is a dictionary with unique_id => update result.
The key `is_disabled` will be added to successful updates if the entity is disabled inside Home Assistant. This means the app can disable sending updates to the sensor.
If an update was unsuccessful, an error is returned.
```
{  
  "battery_state": {  
    "success": true  
  },  
  "battery_level": {  
    "success": true,  
    "is_disabled": true  
  },  
  "battery_charging": {  
    "success": false,  
    "error": {  
      "code": "not_registered",  
      "message": "Entity is not registered",  
    }  
  },  
  "battery_charging_state": {  
    "success": false,  
    "error": {  
      "code": "invalid_format",  
      "message": "Unexpected value for type",  
    }  
}  

```

## Keeping sensors in sync with Home Assistant[​](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#keeping-sensors-in-sync-with-home-assistant "Direct link to Keeping sensors in sync with Home Assistant")
Users can enable and disable entities in Home Assistant. A disabled entity will not be added to Home Assistant, even if offered by the integration. This means that it won't make sense for phones to keep sending data to entities that are not enabled in Home Assistant.
**When a sensor is enabled/disabled in the app** , the app should send a `register_sensor` webhook for this sensor and set `disabled` to `true` or `false`.
**When the mobile app sends an`update_sensor_states` webhook to update the data for an entity that is disabled**, the update result will contain an `is_disabled` key with a value of `true`. This is an indicator that the mobile app needs to synchronize the enabled states from Home Assistant to the mobile app.
```
{  
  "battery_level": {  
    "success": true,  
  },  
  "battery_charging": {  
    "success": true,  
    "is_disabled": true  
  }  
}  

```

**When the user enables/disables an entity in Home Assistant, it needs to be synchronized to the mobile app.** The `get_config` webhook response contains an `entities` key. This is a dictionary mapping `unique_id` to `{"disabled": boolean}`. The mobile app should adopt these enabled settings.
```
{  
  // ...  
  "entities": {  
    "battery_level": {  
      "disabled": false  
    },  
    "battery_charging": {  
      "disabled": true  
    },  
  }  
}  

```

Last updated on **Apr 12, 2023**
[ Previous Sending data home](https://developers.home-assistant.io/docs/api/native-app-integration/sending-data)[Next Push notifications](https://developers.home-assistant.io/docs/api/native-app-integration/notifications)
  * [Registering a sensor](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#registering-a-sensor)
  * [Updating a sensor](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#updating-a-sensor)
  * [Keeping sensors in sync with Home Assistant](https://developers.home-assistant.io/docs/api/native-app-integration/sensors/#keeping-sensors-in-sync-with-home-assistant)


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