**Example response:**
```
{
  "services": [
    {
      "slug": "name",
      "available": true,
      "providers": ["awesome_addon"]
    }
  ]
}

```

get
`/services/mqtt`
🔒
**Returned data:**
key | type | description
---|---|---
addon | string | The app slug
host | string | The IP of the addon running the service
port | string | The port the service is running on
ssl | boolean |  `true` if SSL is in use
username | string | The username for the service
password | string | The password for the service
protocol | string | The MQTT protocol
**Example response:**
```
{
  "addon": "awesome_mqtt",
  "host": "172.0.0.17",
  "port": "8883",
  "ssl": true,
  "username": "awesome_user",
  "password": "strong_password",
  "protocol": "3.1.1"
}

```

post
`/services/mqtt`
🔒
Create a service definition
**Payload:**
key | type | description
---|---|---
host | string | The IP of the addon running the service
port | string | The port the service is running on
ssl | boolean |  `true` if SSL is in use
username | string | The username for the service
password | string | The password for the service
protocol | string | The MQTT protocol
delete
`/services/mqtt`
🔒
Deletes the service definitions
get
`/services/mysql`
🔒
**Returned data:**
key | type | description
---|---|---
addon | string | The app slug
host | string | The IP of the addon running the service
port | string | The port the service is running on
ssl | boolean |  `true` if SSL is in use
username | string | The username for the service
password | string | The password for the service
protocol | string | The MQTT protocol
**Example response:**
```
{
  "addon": "awesome_mysql",
  "host": "172.0.0.17",
  "port": "8883",
  "username": "awesome_user",
  "password": "strong_password"
}

```

post
`/services/mysql`
🔒
Create a service definition
**Payload:**
key | type | description
---|---|---
host | string | The IP of the addon running the service
port | string | The port the service is running on
username | string | The username for the service
password | string | The password for the service
delete
`/services/mysql`
🔒
Deletes the service definitions
### Store[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#store "Direct link to Store")
get
`/store`
🔒
Returns app store information.
**Example response:**
```
{ "addons":
  [
    {
      "name": "Awesome app",
      "slug": "7kshd7_awesome",
      "description": "Awesome description",
      "repository": "https://example.com/addons",
      "version": "1.0.0",
      "installed": "1.0.0",
      "icon": false,
      "logo": true,
      "state": "started"
    }
  ],
  "repositories": [
    {
      "slug": "awesom_repository",
      "name": "Awesome Repository",
      "source": "https://example.com/addons",
      "url": "https://example.com/addons",
      "maintainer": "Awesome Maintainer"
    }
  ]
}

```

get
`/store/addons`
🔒
Returns a list of store apps
**Example response:**
```
[
  {
    "name": "Awesome app",
    "slug": "7kshd7_awesome",
    "description": "Awesome description",
    "repository": "https://example.com/addons",
    "version": "1.0.0",
    "installed": "1.0.0",
    "icon": false,
    "logo": true,
    "state": "started"
  }
]

```

get
`/store/addons/<addon>`
🔒
Returns information about a store app
**Example response:**
```
{
  "advanced": false,
  "apparmor": "default",
  "arch": ["armhf", "aarch64", "i386", "amd64"],
  "auth_api": true,
  "available": true,
  "build": false,
  "description": "Awesome description",
  "detached": false,
  "docker_api": false,
  "documentation": true,
  "full_access": true,
  "hassio_api": false,
  "hassio_role": "manager",
  "homeassistant_api": true,
  "homeassistant": "2021.2.0b0",
  "host_network": false,
  "host_pid": false,
  "icon": false,
  "ingress": true,
  "installed": false,
  "logo": true,
  "long_description": "lorem ipsum",
  "name": "Awesome app",
  "rating": 5,
  "repository": "core",
  "signed": false,
  "slug": "7kshd7_awesome",
  "stage": "stable",
  "update_available": false,
  "url": "https://example.com/addons/tree/main/awesome_addon",
  "version_latest": "1.0.0",
  "version": "1.0.0"
}

```

post
`/store/addons/<addon>/install`
🔒
Install an app from the store.
**Payload:**
key | type | description
---|---|---
background | boolean | Return `job_id` immediately, do not wait for install to complete. Clients must check job for status
post
`/store/addons/<addon>/update`
🔒
Update an app from the store.
**Payload:**
key | type | description
---|---|---
backup | boolean | Create a partial backup of the app, default is false
background | boolean | Return `job_id` immediately, do not wait for update to complete. Clients must check job for status
get
`/store/addons/<addon>/changelog`
🔒
Get the changelog for an app.
get
`/store/addons/<addon>/documentation`
🔒
Get the documentation for an app.
get
`/store/addons/<addon>/icon`
🔒
Get the app icon
get
`/store/addons/<addon>/logo`
🔒
Get the app logo
get
`/store/addons/<addon>/availability`
🔒
Returns 200 success status if the latest version of the app is able to be installed on the current system. Returns a 400 error status if it is not with a message explaining why.
post
`/store/reload`
🔒
Reloads the information stored about apps.
get
`/store/repositories`
🔒
Returns a list of store repositories
**Example response:**
```
[
  {
    "slug": "awesom_repository",
    "name": "Awesome Repository",
    "source": "https://example.com/addons",
    "url": "https://example.com/addons",
    "maintainer": "Awesome Maintainer"
  }
]

```

post
`/store/repositories`
🔒
Add an addon repository to the store
**Payload:**
key | type | description
---|---|---
repository | string | URL of the addon repository to add to the store.
**Example payload:**
```
{
  "repository": "https://example.com/addons"
}

```

get
`/store/repositories/<repository>`
🔒
Returns information about a store repository
**Example response:**
```
{
  "slug": "awesom_repository",
  "name": "Awesome Repository",
  "source": "https://example.com/addons",
  "url": "https://example.com/addons",
  "maintainer": "Awesome Maintainer"
}

```

delete
`/store/repositories/<repository>`
🔒
Remove an unused addon repository from the store.
post
`/store/repositories/<repository>/repair`
🔒
Repair/reset an addon repository in the store that is missing or showing incorrect information.
### Security[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#security "Direct link to Security")
get
`/security/info`
🔒
Returns information about the security features
**Returned data:**
key | type | description
---|---|---
pwned | bool | If pwned check is enabled or disabled on the backend
force_security | bool | If force-security is enabled or disabled on the backend
**Example response:**
```
{
  "pwned": true,
  "force_security": false,
}

```

post
`/security/options`
🔒
**Payload:**
key | type | description
---|---|---
pwned | bool | Disable/Enable pwned
force_security | bool | Disable/Enable force-security
### Supervisor[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#supervisor "Direct link to Supervisor")
get
`/supervisor/info`
🔒
Returns information about the supervisor
**Returned data:**
key | type | description
---|---|---
version | string | The installed supervisor version
version_latest | string | The latest published version in the active channel
update_available | boolean |  `true` if an update is available
arch | string | The architecture of the host (armhf, aarch64, i386, amd64)
channel | string | The active channel (stable, beta, dev)
timezone | string | The current timezone
healthy | bool | The supervisor is in a healthy state
supported | bool | The environment is supported
logging | string | The current log level (debug, info, warning, error, critical)
ip_address | string | The internal docker IP address to the supervisor
wait_boot | int | Max time to wait during boot
debug | bool | Debug is active
debug_block | bool |  `true` if debug block is enabled
diagnostics | bool or null | Sending diagnostics is enabled
addons_repositories | list | A list of app repository URL's as strings
auto_update | bool | Is auto update enabled for supervisor
detect_blocking_io | bool | Supervisor raises exceptions for blocking I/O in event loop
**Example response:**
```
{
  "version": "246",
  "version_latest": "version_latest",
  "update_available": true,
  "arch": "amd64",
  "channel": "dev",
  "timezone": "TIMEZONE",
  "healthy": true,
  "supported": false,
  "logging": "debug",
  "ip_address": "172.0.0.2",
  "wait_boot": 800,
  "debug": false,
  "debug_block": false,
  "diagnostics": null,
  "addons_repositories": ["https://example.com/addons"],
  "auto_update": true,
  "detect_blocking_io": false
}

```

get
`/supervisor/logs`
🔒
Get logs for the Supervisor container via the Systemd journal backend. If the Systemd journal gateway fails to provide the logs, raw Docker container logs are returned as the fallback.
The endpoint accepts the same headers and provides the same functionality as `/host/logs`.
get
`/supervisor/logs/follow`
🔒
Identical to `/supervisor/logs` except it continuously returns new log entries.
get
`/supervisor/logs/latest`
🔒
Return all logs of the latest startup of the Supervisor container.
The `Range` header is ignored but the `lines` query parameter can be used.
get
`/supervisor/logs/boots/<bootid>`
🔒
Get logs for the Supervisor container related to a specific boot.
The `bootid` parameter is interpreted in the same way as in `/host/logs/boots/<bootid>` and the endpoint otherwise provides the same functionality as `/host/logs`.
get
`/supervisor/logs/boots/<bootid>/follow`
🔒
Identical to `/supervisor/logs/boots/<bootid>` except it continuously returns new log entries.
post
`/supervisor/options`
🔒
Update options for the supervisor, you need to supply at least one of the payload keys to the API call. You need to call `/supervisor/reload` after updating the options.
**Payload:**
key | type | description
---|---|---
channel | string | Set the active channel (stable, beta, dev)
timezone | string | Set the timezone
wait_boot | int | Set the time to wait for boot
debug | bool | Enable debug
debug_block | bool | Enable debug block
logging | string | Set logging level
addons_repositories | list | Set a list of URL's as strings for app repositories
auto_update | bool | Enable/disable auto update for supervisor
detect_blocking_io | string | Enable blocking I/O in event loop detection. Valid values are `on`, `off` and `on_at_startup`.
get
`/supervisor/ping`
🔓
Ping the supervisor to check if it can return a response.
post
`/supervisor/reload`
🔒
Reload parts of the supervisor, this enable new options, and check for updates.
post
`/supervisor/restart`
🔒
Restart the supervisor, can help to get the supervisor healthy again.
post
`/supervisor/repair`
🔒
Repair docker overlay issues, and lost images.
get
`/supervisor/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the supervisor.
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
`/supervisor/update`
🔒
Update the supervisor
**Payload:**
key | type | description
---|---|---
version | string | The version to install. Defaults to the latest version. Development only: Only works in the Supervisor development environment.
### Placeholders[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#placeholders "Direct link to Placeholders")
Some of the endpoints uses placeholders indicated with `<...>` in the endpoint URL.
placeholder | description
---|---
addon | The slug for the addon, to get the slug you can call `/addons`, to call endpoints for the app calling the endpoints you can use `self`as the slug.
application | The name of an application, call `/audio/info` to get the correct name
backup | A valid backup slug, example `skuwe823`, to get the slug you can call `/backups`
bootid | An id or offset of a particular boot, used to filter logs. Call `/host/logs/boots` to get a list of boot ids or see `/host/logs/boots/<bootid>` to understand boot offsets
check | The slug of a system check in Supervisor's resolution manager. Call `/resolution/info` for a list of options from the `checks` field
disk | Identifier of a disk attached to host or `default`. See `/host/disks/<disk>/usage` for more details
id | Numeric id of a vlan on a particular interface. See `/network/interface/<interface>/vlan/<id>` for details
identifier | A syslog identifier used to filter logs. Call `/host/logs/identifiers` to get a list of options. See `/host/logs/identifiers/<identifier>` for some common examples
interface | A valid interface name, example `eth0`, to get the interface name you can call `/network/info`. You can use `default` to get the primary interface
issue | The UUID of an issue with the system identified by Supervisor. Call `/resolution/info` for a list of options from the `issues` field
job_id | The UUID of a currently running or completed Supervisor job
name | Name of a mount added to Supervisor. Call `/mounts` to get a list of options from `mounts` field
registry | A registry hostname defined in the container registry configuration, to get the hostname you can call `/docker/registries`
repository | The slug of an addon repository added to Supervisor. Call `/store` for a list of options from the `repositories` field
service | The service name for a service on the host.
suggestion | The UUID of a suggestion for a system issue identified by Supervisor. Call `/resolution/info` for a list of options from the `suggestions` field
uuid | The UUID of a discovery service, to get the UUID you can call `/discovery`
Last updated on **Mar 13, 2026**
[ Previous Debugging](https://developers.home-assistant.io/docs/supervisor/debugging)[Next Models](https://developers.home-assistant.io/docs/api/supervisor/models)
  * [Apps](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#apps)
  * [Audio](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#audio)
  * [Auth](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#auth)
  * [Backup](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#backup)
  * [CLI](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#cli)
  * [Core](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#core)
  * [Discovery](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#discovery)
  * [DNS](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#dns)
  * [Docker](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#docker)
  * [Hardware](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#hardware)
  * [Host](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#host)
  * [Ingress](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#ingress)
  * [Jobs](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#jobs)
  * [Root](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#root)
  * [Mounts](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#mounts)
  * [Multicast](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#multicast)
  * [Network](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#network)
  * [Observer](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#observer)
  * [OS](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#os)
  * [Resolution](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#resolution)
  * [Service](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#service)
  * [Store](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#store)
  * [Security](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#security)
  * [Supervisor](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#supervisor)
  * [Placeholders](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#placeholders)


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
