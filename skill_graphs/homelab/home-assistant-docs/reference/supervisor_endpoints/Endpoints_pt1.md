# Endpoints
For API endpoints marked with 🔒 you need use an authorization header with a `Bearer` token.
The token is available for apps (formerly known as add-ons) and Home Assistant using the `SUPERVISOR_TOKEN` environment variable.
To see more details about each endpoint, click on it to expand it.
### Apps[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#apps "Direct link to Apps")
get
`/addons`
🔒
Return overview information about installed apps.
**Payload:**
key | type | description
---|---|---
addons | list | A list of [Addon models](https://developers.home-assistant.io/docs/api/supervisor/models#addon)
**Example response:**
```
{
  "addons": [
    {
      "name": "Awesome app",
      "slug": "awesome_addon",
      "description": "My awesome app",
      "advanced": false,
      "stage": "stable",
      "repository": "core",
      "version": null,
      "version_latest": "1.0.1",
      "update_available": false,
      "installed": false,
      "detached": true,
      "available": true,
      "build": false,
      "url": null,
      "icon": false,
      "logo": false,
      "system_managed": false
    }
  ]
}

```

post
`/addons/reload`
🔒
Reloads the information stored about apps.
get
`/addons/<addon>/changelog`
🔒
Get the changelog for an app.
get
`/addons/<addon>/documentation`
🔒
Get the documentation for an app.
get
`/addons/<addon>/logs`
🔒
Get logs for an app via the Systemd journal backend.
The endpoint accepts the same headers and provides the same functionality as `/host/logs`.
get
`/addons/<addon>/logs/follow`
🔒
Identical to `/addons/<addon>/logs` except it continuously returns new log entries.
get
`/addons/<addon>/logs/latest`
🔒
Return all logs of the latest startup of the app container.
The `Range` header is ignored but the `lines` query parameter can be used.
get
`/addons/<addon>/logs/boots/<bootid>`
🔒
Get logs for an app related to a specific boot.
The `bootid` parameter is interpreted in the same way as in `/host/logs/boots/<bootid>` and the endpoint otherwise provides the same functionality as `/host/logs`.
get
`/addons/<addon>/logs/boots/<bootid>/follow`
🔒
Identical to `/addons/<addon>/logs/boots/<bootid>` except it continuously returns new log entries.
get
`/addons/<addon>/icon`
🔒
Get the app icon
get
`/addons/<addon>/info`
🔒
Get details about an app
**Returned data:**
key | type | description
---|---|---
advanced | boolean |  `true` if advanced mode is enabled
apparmor | string | disabled, default or the name of the profile
arch | list | A list of supported architectures for the app
audio | boolean |  `true` if audio is enabled
audio_input | float or null | The device index
audio_output | float or null | The device index
auth_api | boolean |  `true` if auth api access is granted is enabled
auto_uart | boolean |  `true` if auto_uart access is granted is enabled
auto_update | boolean |  `true` if auto update is enabled
available | boolean |  `true` if the app is available
boot | string | "auto" or "manual"
boot_config | string | Default boot mode of addon or "manual_only" if boot mode cannot be auto
build | boolean |  `true` if local app
changelog | boolean |  `true` if changelog is available
description | string | The app description
detached | boolean |  `true` if the app is running detached
devices | list | A list of attached devices
devicetree | boolean |  `true` if devicetree access is granted is enabled
discovery | list | A list of discovery services
dns | list | A list of DNS servers used by the app
docker_api | boolean |  `true` if docker_api access is granted is enabled
documentation | boolean |  `true` if documentation is available
full_access | boolean |  `true` if full access access is granted is enabled
gpio | boolean |  `true` if gpio access is granted is enabled
hassio_api | boolean |  `true` if hassio api access is granted is enabled
hassio_role | string | The hassio role (default, homeassistant, manager, admin)
homeassistant | string or null | The minimum Home Assistant Core version
homeassistant_api | boolean |  `true` if homeassistant api access is granted is enabled
host_dbus | boolean |  `true` if host dbus access is granted is enabled
host_ipc | boolean |  `true` if host ipc access is granted is enabled
host_network | boolean |  `true` if host network access is granted is enabled
host_pid | boolean |  `true` if host pid access is granted is enabled
host_uts | boolean |  `true` if host UTS namespace access is enabled.
hostname | string | The host name of the app
icon | boolean |  `true` if icon is available
ingress | boolean |  `true` if ingress is enabled
ingress_entry | string or null | The ingress entrypoint
ingress_panel | boolean or null |  `true` if ingress_panel is enabled
ingress_port | int or null | The ingress port
ingress_url | string or null | The ingress URL
ip_address | string | The IP address of the app
kernel_modules | boolean |  `true` if kernel module access is granted is enabled
logo | boolean |  `true` if logo is available
long_description | string | The long app description
machine | list | A list of supported machine types for the app
name | string | The name of the app
network | dictionary or null | The network configuration for the app
network_description | dictionary or null | The description for the network configuration
options | dictionary | The app configuration
privileged | list | A list of hardwars/system attributes the app has access to
protected | boolean |  `true` if protection mode is enabled
rating | int | The addon rating
repository | string | The URL to the app repository
schema | dictionary or null | The schema for the app configuration
services_role | list | A list of services and the apps role for that service
slug | string | The app slug
stage | string | The app stage (stable, experimental, deprecated)
startup | string | The stage when the app is started (initialize, system, services, application, once)
state | string or null | The state of the app (started, stopped)
stdin | boolean |  `true` if the app accepts stdin commands
system_managed | boolean | Indicates whether the app is managed by Home Assistant
system_managed_config_entry | string | Provides the configuration entry ID if the app is managed by Home Assistant
translations | dictionary | A dictionary containing content of translation files for the app
udev | boolean |  `true` if udev access is granted is enabled
update_available | boolean |  `true` if an update is available
url | string or null | URL to more information about the app
usb | list | A list of attached USB devices
version | string | The installed version of the app
version_latest | string | The latest version of the app
video | boolean |  `true` if video is enabled
watchdog | boolean |  `true` if watchdog is enabled
webui | string or null | The URL to the web UI for the app
signed | boolean | True if the image is signed and trust
**Example response:**
```
{
  "advanced": false,
  "apparmor": "default",
  "arch": ["armhf", "aarch64", "i386", "amd64"],
  "audio_input": null,
  "audio_output": null,
  "audio": false,
  "auth_api": false,
  "auto_uart": false,
  "auto_update": false,
  "available": false,
  "boot": "auto",
  "boot_config": "auto",
  "build": false,
  "changelog": false,
  "description": "description",
  "detached": false,
  "devices": ["/dev/xy"],
  "devicetree": false,
  "discovery": ["service"],
  "dns": [],
  "docker_api": false,
  "documentation": false,
  "full_access": false,
  "gpio": false,
  "hassio_api": false,
  "hassio_role": "default",
  "homeassistant_api": false,
  "homeassistant": null,
  "host_dbus": false,
  "host_ipc": false,
  "host_network": false,
  "host_pid": false,
  "host_uts": false,
  "hostname": "awesome-addon",
  "icon": false,
  "ingress_entry": null,
  "ingress_panel": true,
  "ingress_port": 1337,
  "ingress_url": null,
  "ingress": false,
  "ip_address": "172.0.0.21",
  "kernel_modules": false,
  "logo": false,
  "long_description": "Long description",
  "machine": ["raspberrypi2", "tinker"],
  "name": "Awesome app",
  "network_description": "{}|null",
  "network": {},
  "options": {},
  "privileged": ["NET_ADMIN", "SYS_ADMIN"],
  "protected": false,
  "rating": "1-6",
  "repository": "12345678",
  "schema": {},
  "services_role": ["service:access"],
  "slug": "awesome_addon",
  "stage": "stable",
  "startup": "application",
  "state": "started",
  "stdin": false,
  "system_managed": true,
  "system_managed_config_entry": "abc123",
  "translations": {
    "en": {
      "configuration": {
        "lorem": "ipsum"
      }
    }
  },
  "udev": false,
  "update_available": false,
  "url": null,
  "usb": ["/dev/usb1"],
  "version_latest": "1.0.2",
  "version": "1.0.0",
  "video": false,
  "watchdog": true,
  "webui": "http://[HOST]:1337/xy/zx",
  "signed": false
}

```

post
`/addons/<addon>/install`
🔒
Install an app
**Deprecated!** Use [`/store/addons/<addon>/install`](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#store) instead.
get
`/addons/<addon>/logo`
🔒
Get the app logo
post
`/addons/<addon>/options`
🔒
Set the options for an app.
To reset customized network/audio/options, set it `null`.
**Payload:**
key | type | description
---|---|---
boot | string | (auto, manual)
auto_update | boolean |  `true` if the app should auto update
network | dictionary | A map of network configuration.
options | dictionary | The app configuration
audio_output | float or null | The index of the audio output device
audio_input | float or null | The index of the audio input device
ingress_panel | boolean |  `true` if ingress_panel is enabled
watchdog | boolean |  `true` if watchdog is enabled
**You need to supply at least one key in the payload.**
**Example payload:**
```
{
  "boot": "manual",
  "auto_update": false,
  "network": {
    "CONTAINER": "1337"
  },
  "options": {
    "awesome": true
  },
  "watchdog": true
}

```

post
`/addons/<addon>/sys_options`
🔒
Change options specific to system managed addons.
This endpoint is only callable by Home Assistant and not by any other client.
**Payload**
key | type | description
---|---|---
system_managed | boolean |  `true` if managed by Home Assistant
system_managed_config_entry | boolean | ID of config entry managing addon
**You need to supply at least one key in the payload.**
**Example payload:**
```
{
  "system_managed": true,
  "system_managed_config_entry": "abc123"
}

```

post
`/addons/<addon>/options/validate`
🔒
Run a configuration validation against the current stored app configuration or payload.
**Payload:**
Optional the raw app options.
**Returned data:**
key | type | description
---|---|---
message | string | Include the error message
valid | boolean | If config is valid or not
pwned | boolean | None
get
`/addons/<addon>/options/config`
🔒
The Data endpoint to get his own rendered configuration.
post
`/addons/<addon>/rebuild`
🔒
Rebuild the app, only supported for local build apps.
**Payload:**
key | type | optional | description
---|---|---|---
force | boolean | True | Force rebuild of the app even if pre-built images are provided
post
`/addons/<addon>/restart`
🔒
Restart an app
post
`/addons/<addon>/security`
🔒
Set the protection mode on an app.
This function is not callable by itself and you can not use `self` as the slug here.
**Payload:**
key | type | description
---|---|---
protected | boolean |  `true` if protection mode is on
post
`/addons/<addon>/start`
🔒
Start an app
get
`/addons/<addon>/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the app.
**Example response:**
```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}

```

post
`/addons/<addon>/stdin`
🔒
Write data to app stdin.
The payload you want to pass into the addon you give the endpoint as the body of the request.
post
`/addons/<addon>/stop`
🔒
Stop an app
post
`/addons/<addon>/uninstall`
🔒
Uninstall an app
**Payload:**
key | type | optional | description
---|---|---|---
remove_config | boolean | True | Delete addon's config folder (if used)
post
`/addons/<addon>/update`
🔒
Update an app
**Deprecated!** Use [`/store/addons/<addon>/update`](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#store) instead.
### Audio[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#audio "Direct link to Audio")
post
`/audio/default/input`
🔒
Set a profile as the default input profile
**Payload:**
key | type | optional | description
---|---|---|---
name | string | False | The name of the profile
post
`/audio/default/output`
🔒
Set a profile as the default output profile
**Payload:**
key | type | optional | description
---|---|---|---
name | string | False | The name of the profile
get
`/audio/info`
🔒
Return information about the audio plugin.
**Returned data:**
key | type | description
---|---|---
host | string | The IP address of the plugin
version | string | The installed observer version
version_latest | string | The latest published version
update_available | boolean |  `true` if an update is available
audio | dictionary | An [Audio model](https://developers.home-assistant.io/docs/api/supervisor/models#audio)
**Example response:**
```
{
  "host": "172.0.0.19",
  "version": "1",
  "latest_version": "2",
  "update_available": true,
  "audio": {
    "card": [
      {
        "name": "Awesome card",
        "index": 1,
        "driver": "Awesome driver",
        "profiles": [
          {
            "name": "Awesome profile",
            "description": "My awesome profile",
            "active": false
          }
        ]
      }
    ],
    "input": [
      {
        "name": "Awesome device",
        "index": 0,
        "description": "My awesome device",
        "volume": 0.3,
        "mute": false,
        "default": false,
        "card": null,
        "applications": [
          {
            "name": "Awesome application",
            "index": 0,
            "stream_index": 0,
            "stream_type": "INPUT",
            "volume": 0.3,
            "mute": false,
            "addon": "awesome_addon"
          }
        ]
      }
    ],
    "output": [
      {
        "name": "Awesome device",
        "index": 0,
        "description": "My awesome device",
        "volume": 0.3,
        "mute": false,
        "default": false,
        "card": 1,
        "applications": [
          {
            "name": "Awesome application",
            "index": 0,
            "stream_index": 0,
            "stream_type": "INPUT",
            "volume": 0.3,
            "mute": false,
            "addon": "awesome_addon"
          }
        ]
      }
    ],
    "application": [
      {
        "name": "Awesome application",
        "index": 0,
        "stream_index": 0,
        "stream_type": "OUTPUT",
        "volume": 0.3,
        "mute": false,
        "addon": "awesome_addon"
      }
    ]
  }
}

```

get
`/audio/logs`
🔒
Get logs for the audio plugin container via the Systemd journal backend.
The endpoint accepts the same headers and provides the same functionality as `/host/logs`.
get
`/audio/logs/follow`
🔒
Identical to `/audio/logs` except it continuously returns new log entries.
get
`/audio/logs/latest`
🔒
Return all logs of the latest startup of the audio plugin container.
The `Range` header is ignored but the `lines` query parameter can be used.
get
`/audio/logs/boots/<bootid>`
🔒
Get logs for the audio plugin container related to a specific boot.
The `bootid` parameter is interpreted in the same way as in `/host/logs/boots/<bootid>` and the endpoint otherwise provides the same functionality as `/host/logs`.
get
`/audio/logs/boots/<bootid>/follow`
🔒
Identical to `/audio/logs/boots/<bootid>` except it continuously returns new log entries.
post
`/audio/mute/input`
🔒
Mute input devices
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
active | boolean | False |  `true` if muted
post
`/audio/mute/input/<application>`
🔒
Mute input for a specific application
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
active | boolean | False |  `true` if muted
post
`/audio/mute/output`
🔒
Mute output devices
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
active | boolean | False |  `true` if muted
post
`/audio/mute/output/<application>`
🔒
Mute output for a specific application
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
active | boolean | False |  `true` if muted
post
`/audio/profile`
🔒
Create an audio profile
**Payload:**
key | type | optional | description
---|---|---|---
card | string | False | The name of the audio device
name | string | False | The name of the profile
post
`/audio/reload`
🔒
Reload audio information
post
`/audio/restart`
🔒
Restart the audio plugin
get
`/audio/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the audio plugin.
**Example response:**
```
{
  "cpu_percent": 14.0,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}

```

post
`/audio/update`
🔒
Update the audio plugin
**Payload:**
key | type | description
---|---|---
version | string | The version you want to install, default is the latest version
post
`/audio/volume/input`
🔒
Set the input volume
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
volume | float | False | The volume (between `0.0`and `1.0`)
post
`/audio/volume/input/<application>`
🔒
Set the input volume for a specific application
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
volume | float | False | The volume (between `0.0`and `1.0`)
post
`/audio/volume/output`
🔒
Set the output volume
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
volume | float | False | The volume (between `0.0`and `1.0`)
post
`/audio/volume/output/<application>`
🔒
Set the output volume for a specific application
**Payload:**
key | type | optional | description
---|---|---|---
index | string | False | The index of the device
volume | float | False | The volume (between `0.0`and `1.0`)
### Auth[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#auth "Direct link to Auth")
get
`/auth`
🔒
You can do authentication against Home Assistant Core using Basic Authentication. Use the `X-Supervisor-Token` header to provide the Supervisor authentication token. See the corresponding POST method to provide JSON or urlencoded credentials.
post
`/auth`
🔒
You can do authentication against Home Assistant Core. You can POST the data as JSON, as urlencoded (with `application/x-www-form-urlencoded` header) or by using use basic authentication. For using Basic authentication, you can use the `X-Supervisor-Token` for Supervisor authentication token.
**Payload:**
key | type | description
---|---|---
username | string | The username for the user
password | string | The password for the user
post
`/auth/reset`
🔒
Set a new password for a Home Assistant Core user.
**Payload:**
key | type | description
---|---|---
username | string | The username for the user
password | string | The new password for the user
delete
`/auth/cache`
🔒
Reset internal authentication cache, this is useful if you have changed the password for a user and need to clear the internal cache.
get
`/auth/list`
🔒
List all users in Home Assistant to help with credentials recovery. Requires an admin level authentication token.
**Payload:**
key | type | description
---|---|---
users | list | List of the Home Assistant [users](https://developers.home-assistant.io/docs/api/supervisor/models#user).
### Backup[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#backup "Direct link to Backup")
get
`/backups`
🔒
Return a list of [Backups](https://developers.home-assistant.io/docs/api/supervisor/models#backup)
**Example response:**
```
{
  "backups": [
    {
      "slug": "skuwe823",
      "date": "2020-09-30T20:25:34.273Z",
      "name": "Awesome backup",
      "type": "partial",
      "size": 44,
      "protected": true,
      "location": "MountedBackups",
      "compressed": true,
      "content": {
        "homeassistant": true,
        "addons": ["awesome_addon"],
        "folders": ["ssl", "media"]
      }
    }
  ]
}

```

get
`/backups/info`
🔒
Return information about backup manager.
**Returned data:**
key | type | description
---|---|---
backups | list | A list of [Backups](https://developers.home-assistant.io/docs/api/supervisor/models#backup)
days_until_stale | int | Number of days until a backup is considered stale
**Example response:**
```
{
  "backups": [
    {
      "slug": "skuwe823",
      "date": "2020-09-30T20:25:34.273Z",
      "name": "Awesome backup",
      "type": "partial",
      "size": 44,
      "protected": true,
      "compressed": true,
      "location": null,
      "content": {
        "homeassistant": true,
        "addons": ["awesome_addon"],
        "folders": ["ssl", "media"]
      }
    }
  ],
  "days_until_stale": 30
}

```

post
`/backups/new/full`
🔒
Create a full backup.
**Payload:**
key | type | optional | description
---|---|---|---
name | string | True | The name you want to give the backup
password | string | True | The password you want to give the backup
compressed | boolean | True |  `false` to create uncompressed backups
location | string or null | True | Name of a backup mount or `null` for /backup
homeassistant_exclude_database | boolean | True | Exclude the Home Assistant database file from backup
background | boolean | True | Return `job_id` immediately, do not wait for backup to complete. Clients must check job for status and slug.
**Example response:**
```
{
  "slug": "skuwe823"
}

```

post
`/backups/new/upload`
🔒
Upload a backup.
**Example response:**
```
{
  "slug": "skuwe823",
  "job_id": "abc123"
}

```

Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened. Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.
post
`/backups/new/partial`
🔒
Create a partial backup.
**Payload:**
key | type | optional | description
---|---|---|---
name | string | True | The name you want to give the backup
password | string | True | The password you want to give the backup
homeassistant | boolean | True | Add home assistant core settings to the backup
addons | list | True | A list of strings representing app slugs
folders | list | True | A list of strings representing directories
compressed | boolean | True |  `false` to create uncompressed backups
location | string or null | True | Name of a backup mount or `null` for /backup
homeassistant_exclude_database | boolean | True | Exclude the Home Assistant database file from backup
background | boolean | True | Return `job_id` immediately, do not wait for backup to complete. Clients must check job for status and slug.
**You need to supply at least one key in the payload.**
**Example response:**
```
{
  "slug": "skuwe823",
  "job_id": "abc123"
}

```

Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened. Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.
post
`/backups/options`
🔒
Update options for backup manager, you need to supply at least one of the payload keys to the API call.
**Payload:**
key | type | description
---|---|---
days_until_stale | int | Set number of days until a backup is considered stale
**You need to supply at least one key in the payload.**
post
`/backups/reload`
🔒
Reload backup from storage.
post
`/backups/freeze`
🔒
Put Supervisor in a freeze state and prepare Home Assistant and addons for an external backup.
This does not take a backup. It prepares Home Assistant and addons for one but the expectation is that the user is using an external tool to make the backup. Such as the snapshot feature in KVM or Proxmox. The caller should call `/backups/thaw` when done.
**Payload:**
key | type | optional | description
