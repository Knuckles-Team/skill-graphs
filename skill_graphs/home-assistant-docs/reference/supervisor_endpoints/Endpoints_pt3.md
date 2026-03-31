    },  
    {  
      "id": "addons_config",  
      "label": "Addons configuration",  
      "used_space": 5283318814  
    },  
    {  
      "id": "media",  
      "label": "Media",  
      "used_space": 476680019  
    },  
    {  
      "id": "share",  
      "label": "Share",  
      "used_space": 37477206419  
    },  
    {  
      "id": "backup",  
      "label": "Backup",  
      "used_space": 268350699520  
    },  
    {  
      "id": "ssl",  
      "label": "SSL",  
      "used_space": 202912633  
    },  
    {  
      "id": "homeassistant",  
      "label": "Home assistant",  
      "used_space": 444090152  
    }  
  ]  
}  

```

### Ingress[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#ingress "Direct link to Ingress")
get
`/ingress/panels`
🔒
**Returned data:**
key | type | description  
---|---|---  
panels | dictionary | dictionary of [Panel models](https://developers.home-assistant.io/docs/api/supervisor/models#panel)  
**Example response:**
```
{  
  "panels": {  
    "addon_slug": {  
      "enable": true,  
      "icon": "mdi:awesome-icon",  
      "title": "Awesome app",  
      "admin": true  
    }  
  }  
}  

```

post
`/ingress/session`
🔒
Create a new session for access to the ingress service.
**Payload:**
key | type | optional | description  
---|---|---|---  
user_id | string | True | The ID of the user authenticated for the new session  
**Returned data:**
key | type | optional | description  
---|---|---|---  
session | string | False | The token for the ingress session  
post
`/ingress/validate_session`
🔒
Validate an ingress session, extending it's validity period.
**Payload:**
key | type | optional | description  
---|---|---|---  
session | string | False | The token for the ingress session  
### Jobs[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#jobs "Direct link to Jobs")
get
`/jobs/info`
🔒
Returns info on ignored job conditions and currently running or completed jobs
**Returned data:**
key | type | description  
---|---|---  
ignore_conditions | list | List of job conditions being ignored  
jobs | list | List of running or completed [Jobs](https://developers.home-assistant.io/docs/api/supervisor/models#job)  
**Example response:**
```
{  
  "ignore_conditions": [],  
  "jobs": [{  
    "name": "backup_manager_full_backup",  
    "reference": "a01bc3",  
    "uuid": "123456789",  
    "progress": 0,  
    "stage": "addons",  
    "done": false,  
    "child_jobs": [],  
    "extra": null  
  }]  
}  

```

post
`/jobs/options`
🔒
Set options for job manager
**Payload:**
key | type | description  
---|---|---  
ignore_conditions | list | List of job conditions to ignore (replaces existing list)  
get
`/jobs/<job_id>`
🔒
Returns info on a currently running or completed job
**Returned data:**
See [Job](https://developers.home-assistant.io/docs/api/supervisor/models#job) model
**Example response:**
```
{  
  "name": "backup_manager_full_backup",  
  "reference": "a01bc3",  
  "uuid": "123456789",  
  "progress": 0,  
  "stage": "addons",  
  "done": false,  
  "child_jobs": [],  
  "extra": null  
}  

```

delete
`/jobs/<job_id>`
🔒
Removes a completed job from Supervisor cache if client is no longer interested in it
post
`/jobs/reset`
🔒
Reset job manager to defaults (stops ignoring any ignored job conditions)
### Root[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#root "Direct link to Root")
get
`/available_updates`
🔒
Returns information about available updates
**Example response:**
```
{  
  "available_updates": [  
  {  
      "panel_path": "/update-available/core",  
      "update_type": "core",  
      "version_latest": "321",  
    },  
    {  
      "panel_path": "/update-available/os",  
      "update_type": "os",  
      "version_latest": "321",  
    },  
    {  
      "panel_path": "/update-available/supervisor",  
      "update_type": "supervisor",  
      "version_latest": "321",  
    },  
    {  
      "name": "Awesome addon",  
      "icon": "/addons/awesome_addon/icon",  
      "panel_path": "/update-available/awesome_addon",  
      "update_type": "addon",  
      "version_latest": "321",  
    }  
  ]  
}  

```

**Returned data:**
key | type | description  
---|---|---  
update_type | string |  `addon`, `os`, `core` or `supervisor`  
name | string | Returns the name (only if the `update_type` is `addon`)  
icon | string | Returns the path for the icon if any (only if the `update_type` is `addon`)  
version_latest | string | Returns the available version  
panel_path | string | Returns path where the UI can be loaded  
post
`/reload_updates`
🔒
This reloads information about main components (OS, Supervisor, Core, and Plug-ins).
post
`/refresh_updates`
🔒
This reloads information about app repositories and fetches new version files. This endpoint is currently discouraged. Use `/reload_updates` or `/store/reload` instead.
get
`/info`
🔒
Returns a dict with selected keys from other `/*/info` endpoints.
**Returned data:**
key | type | description  
---|---|---  
supervisor | string | The installed version of the supervisor  
homeassistant | string | The installed version of Home Assistant  
hassos | string or null | The version of Home Assistant OS or null  
docker | string | The docker version on the host  
hostname | string | The hostname on the host  
operating_system | string | The operating system on the host  
features | list | A list ov available features on the host  
machine | string | The machine type  
machine_id | string or null | The machine ID of the underlying operating system  
arch | string | The architecture on the host  
supported_arch | list | A list of supported host architectures  
supported | boolean |  `true` if the environment is supported  
channel | string | The active channel (stable, beta, dev)  
logging | string | The active log level (debug, info, warning, error, critical)  
state | string | The core state of the Supervisor.  
timezone | string | The current timezone  
**Example response:**
```
{  
  "supervisor": "300",  
  "homeassistant": "0.117.0",  
  "hassos": "5.0",  
  "docker": "24.17.2",  
  "hostname": "Awesome Hostname",  
  "operating_system": "Home Assistant OS",  
  "features": ["shutdown", "reboot", "hostname", "services", "hassos"],  
  "machine": "ova",  
  "arch": "amd64",  
  "supported_arch": ["amd64"],  
  "supported": true,  
  "channel": "stable",  
  "logging": "info",  
  "state": "running",  
  "timezone": "Europe/Brussels"  
}  

```

### Mounts[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#mounts "Direct link to Mounts")
get
`/mounts`
🔒
Returns information about mounts configured in Supervisor
**Returned data:**
key | type | description  
---|---|---  
mounts | list | A list of [Mounts](https://developers.home-assistant.io/docs/api/supervisor/models#mount)  
default_backup_mount | string or null | Name of a backup mount or `null` for /backup  
**Example response:**
```
{  
  "default_backup_mount": "my_share",  
  "mounts": [  
    {  
      "name": "my_share",  
      "usage": "media",  
      "type": "cifs",  
      "server": "server.local",  
      "share": "media",  
      "state": "active",  
      "read_only": false  
    }  
  ]  
}  

```

post
`/mounts/options`
🔒
Set mount manager options
**Payload:**
key | type | optional | description  
---|---|---|---  
default_backup_mount | string or null | True | Name of a backup mount or `null` for /backup  
**You need to supply at least one key in the payload.**
post
`/mounts`
🔒
Add a new mount in Supervisor and mount it
**Payload:**
Accepts a [Mount](https://developers.home-assistant.io/docs/api/supervisor/models#mount)
Value in `name` must be unique and can only consist of letters, numbers and underscores.
**Example payload:**
```
{  
  "name": "my_share",  
  "usage": "media",  
  "type": "cifs",  
  "server": "server.local",  
  "share": "media",  
  "username": "admin",  
  "password": "password",  
  "read_only": false  
}  

```

put
`/mounts/<name>`
🔒
Update an existing mount in Supervisor and remount it
**Payload:**
Accepts a [Mount](https://developers.home-assistant.io/docs/api/supervisor/models#mount).
The `name` field should be omitted. If included the value must match the existing name, it cannot be changed. Delete and re-add the mount to change the name.
**Example payload:**
```
{  
  "usage": "media",  
  "type": "nfs",  
  "server": "server.local",  
  "path": "/media/camera",  
  "read_only": true  
}  

```

delete
`/mounts/<name>`
🔒
Unmount and delete an existing mount from Supervisor.
post
`/mounts/<name>/reload`
🔒
Unmount and remount an existing mount in Supervisor using the same configuration.
### Multicast[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#multicast "Direct link to Multicast")
get
`/multicast/info`
🔒
Returns information about the multicast plugin
**Returned data:**
key | type | description  
---|---|---  
version | string | The installed multicast version  
version_latest | string | The latest published version  
update_available | boolean |  `true` if an update is available  
**Example response:**
```
{  
  "version": "1",  
  "version_latest": "2",  
  "update_available": true  
}  

```

get
`/multicast/logs`
🔒
Get logs for the multicast plugin via the Systemd journal backend.
The endpoint accepts the same headers and provides the same functionality as `/host/logs`.
get
`/multicast/logs/follow`
🔒
Identical to `/multicast/logs` except it continuously returns new log entries.
get
`/multicast/logs/latest`
🔒
Return all logs of the latest startup of the multicast plugin container.
The `Range` header is ignored but the `lines` query parameter can be used.
get
`/multicast/logs/boots/<bootid>`
🔒
Get logs for the multicast plugin related to a specific boot.
The `bootid` parameter is interpreted in the same way as in `/host/logs/boots/<bootid>` and the endpoint otherwise provides the same functionality as `/host/logs`.
get
`/multicast/logs/boots/<bootid>/follow`
🔒
Identical to `/multicast/logs/boots/<bootid>` except it continuously returns new log entries.
post
`/multicast/restart`
🔒
Restart the multicast plugin.
get
`/multicast/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the multicast plugin.
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
`/multicast/update`
🔒
Update the multicast plugin
**Payload:**
key | type | description  
---|---|---  
version | string | The version you want to install, default is the latest version  
### Network[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#network "Direct link to Network")
get
`/network/info`
🔒
Get network information.
**Returned data:**
key | description  
---|---  
interfaces | A list of [Network interface models](https://developers.home-assistant.io/docs/api/supervisor/models#network-interface)  
docker | Information about the internal docker network  
host_internet | Boolean to indicate if the host can reach the internet.  
supervisor_internet | Boolean to indicate if the Supervisor can reach the internet.  
**Example response:**
```
{  
  "interfaces": [  
    {  
      "interface": "eth0",  
      "type": "ethernet",  
      "primary": true,  
      "enabled": true,  
      "connected": true,  
      "ipv4": {  
        "method": "static",  
        "ip_address": "192.168.1.100/24",  
        "gateway": "192.168.1.1",  
        "nameservers": ["192.168.1.1"],  
      },  
      "ipv6": null,  
      "wifi": null,  
      "vlan": null,  
    }  
  ],  
  "docker": {  
    "interface": "hassio",  
    "address": "172.30.32.0/23",  
    "gateway": "172.30.32.1",  
    "dns": "172.30.32.3"  
  },  
  "host_internet": true,  
  "supervisor_internet": true  
}  

```

get
`/network/interface/<interface>/info`
🔒
Returns a [Network interface model](https://developers.home-assistant.io/docs/api/supervisor/models#network-interface) for a specific network interface.
post
`/network/reload`
🔒
Update all Network interface data.
post
`/network/interface/<interface>/update`
🔒
Update the settings for a network interface.
**Payload:**
key | type | optional | description  
---|---|---|---  
enabled | bool | True | Enable/Disable an ethernet interface / VLAN got removed with disabled  
ipv6 | dict | True | A struct with ipv6 interface settings  
ipv4 | dict | True | A struct with ipv4 interface settings  
wifi | dict | True | A struct with Wireless connection settings  
**ipv6:**
key | type | optional | description  
---|---|---|---  
method | string | True | Set IP configuration method can be `auto` for DHCP or Router Advertisements, `static` or `disabled`  
addr_gen_mode | string | True | Address generation mode can be `eui64`, `stable-privacy`, `default-or-eui64` or `default`  
ip6_privacy | string | True | Privacy extensions options are `disabled`, `enabled-prefer-public`, `enabled` or `default`  
address | list | True | The new IP address for the interface in the ::/XX format as list  
nameservers | list | True | List of DNS servers to use  
gateway | string | True | The gateway the interface should use  
route_metric | int | True | Route metric. Lower value has higher priority. The kernel accepts zero (0) but coerces it to 1024 (user default)  
**ipv4:**
key | type | optional | description  
---|---|---|---  
method | string | True | Set IP configuration method can be `auto` for DHCP, `static` or `disabled`  
address | list | True | The new IP address for the interface in the X.X.X.X/XX format as list  
nameservers | list | True | List of DNS servers to use  
gateway | string | True | The gateway the interface should use  
route_metric | int | True | Route metric. Lower value has higher priority  
**wifi:**
key | type | optional | description  
---|---|---|---  
mode | string | True | Set the mode `infrastructure` (default), `mesh`, `adhoc` or `ap`  
auth | string | True | Set the auth mode: `open` (default), `web`, `wpa-psk`  
ssid | string | True | Set the SSID for connect into  
psk | string | True | The shared key which is used with `web` or `wpa-psk`  
get
`/network/interface/<interface>/accesspoints`
🔒
Return a list of available [Access Points](https://developers.home-assistant.io/docs/api/supervisor/models#access-points) on this Wireless interface.
**This function only works with Wireless interfaces!**
**Returned data:**
key | description  
---|---  
accesspoints | A list of [Access Points](https://developers.home-assistant.io/docs/api/supervisor/models#access-points)  
**Example response:**
```
{  
  "accesspoints": [  
    {  
      "mode": "infrastructure",  
      "ssid": "MY_TestWifi",  
      "mac": "00:00:00:00",  
      "frequency": 24675,  
      "signal": 90  
    }  
  ]  
}  

```

post
`/network/interface/<interface>/vlan/<id>`
🔒
Create a new VLAN _id_ on this network interface.
**This function only works with ethernet interfaces!**
**Payload:**
key | type | optional | description  
---|---|---|---  
ipv6 | dict | True | A struct with ipv6 interface settings  
ipv4 | dict | True | A struct with ipv4 interface settings  
### Observer[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#observer "Direct link to Observer")
get
`/observer/info`
🔒
Returns information about the observer plugin
**Returned data:**
key | type | description  
---|---|---  
host | string | The IP address of the plugin  
version | string | The installed observer version  
version_latest | string | The latest published version  
update_available | boolean |  `true` if an update is available  
**Example response:**
```
{  
  "host": "172.0.0.17",  
  "version": "1",  
  "version_latest": "2",  
  "update_available": true  
}  

```

get
`/observer/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the observer plugin.
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
`/observer/update`
🔒
Update the observer plugin
**Payload:**
key | type | description  
---|---|---  
version | string | The version you want to install, default is the latest version  
### OS[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#os "Direct link to OS")
post
`/os/config/sync`
🔒
Load host configurations from a USB stick.
get
`/os/info`
🔒
Returns information about the OS.
**Returned data:**
key | type | description  
---|---|---  
version | string | The current version of the OS  
version_latest | string | The latest published version of the OS in the active channel  
update_available | boolean |  `true` if an update is available  
board | string | The name of the board  
boot | string | Which slot that are in use  
data_disk | string | Device which is used for holding OS data persistent  
boot_slots | dict | Dictionary of [boot slots](https://developers.home-assistant.io/docs/api/supervisor/models#boot-slot) keyed by name  
**Example response:**
```
{  
  "version": "4.3",  
  "version_latest": "5.0",  
  "update_available": true,  
  "board": "ova",  
  "boot": "slot1",  
  "data_disk": "BJTD4R-0x123456789",  
  "boot_slots": {  
    "A": {  
      "state": "inactive",  
      "status": "good",  
      "version": "10.1"  
    },  
    "B": {  
      "state": "active",  
      "status": "good",  
      "version": "10.2"  
    }  
  }  
}  

```

post
`/os/update`
🔒
Update Home Assistant OS
**Payload:**
key | type | description  
---|---|---  
version | string | The version you want to install, default is the latest version  
post
`/os/boot-slot`
🔒
Change the active boot slot, **This will also reboot the device!**
**Payload:**
key | type | description  
---|---|---  
boot_slot | string | Boot slot to change to. See options in `boot_slots` from `/os/info` API.  
get
`/os/config/swap`
🔒
Get current HAOS swap configuration. Unavailable on Supervised.
**Returned data:**
key | type | description  
---|---|---  
swap_size | string | Current swap size.  
swappiness | int | Current kernel swappiness value.  
**Example response:**
```
{  
  "swap_size": "2G",  
  "swappiness": 1  
}  

```

post
`/os/config/swap`
🔒
Set HAOS swap configuration. Unavailable on Supervised.
**Payload:**
key | type | description  
---|---|---  
swap_size | string | New swap siz as number with optional units (K/M/G). Anything lower than 40K disables swap.  
swappiness | int | New swappiness value (0-100).  
get
`/os/datadisk/list`
🔒
Returns possible targets for the new data partition.
**Returned data:**
key | type | description  
---|---|---  
devices | list | List of IDs of possible data disk targets  
disks | list | List of [disks](https://developers.home-assistant.io/docs/api/supervisor/models#disk) which are possible data disk targets  
**Example response:**
```
{  
  "devices": [  
    "Generic-Flash-Disk-123ABC456",  
    "SSK-SSK-Storage-ABC123DEF"  
  ],  
  "disks": [  
    {  
      "name": "Generic Flash Disk (123ABC456)",  
      "vendor": "Generic",  
      "model": "Flash Disk",  
      "serial": "123ABC456",  
      "size": 8054112256,  
      "id": "Generic-Flash-Disk-123ABC456",  
      "dev_path": "/dev/sda"  
    },  
    {  
      "name": "SSK SSK Storage (ABC123DEF)",  
      "vendor": "SSK",  
      "model": "SSK Storage",  
      "serial": "ABC123DEF",  
      "size": 250059350016,  
      "id": "SSK-SSK-Storage-ABC123DEF",  
      "dev_path": "/dev/sdb"  
    }  
  ]  
}  

```

post
`/os/datadisk/move`
🔒
Move datadisk to a new location, **This will also reboot the device!**
**Payload:**
key | type | description  
---|---|---  
device | string | ID of the disk device which should be used as the target for the data migration  
post
`/os/datadisk/wipe`
🔒
Wipe the datadisk including all user data and settings, **This will also reboot the device!** This API requires an admin token
This API will wipe all config/settings for addons, Home Assistant and the Operating System and any locally stored data in config, backups, media, etc. The machine will reboot during this.
After the reboot completes the latest stable version of Home Assistant and Supervisor will be downloaded. Once the process is complete the user will see onboarding, like during initial setup.
This wipe also includes network settings. So after the reboot the user may need to reconfigure those in order to access Home Assistant again.
The operating system version as well as its boot configuration will be preserved.
get
`/os/boards/{board}`
🔒
Returns information about your board if it has features or settings that can be modified from Home Assistant. The value for `board` is the value in the `board` field returned by `/os/info`.
Boards with such options are documented below.
get
`/os/boards/yellow`
🔒
If running on a yellow board, returns current values for its settings.
**Returned data:**
key | type | description  
---|---|---  
disk_led | boolean | Is the disk LED enabled  
heartbeat_led | boolean | Is the heartbeat LED enabled  
power_led | boolean | Is the power LED enabled  
**Example response:**
```
{  
  "disk_led": true,  
  "heartbeat_led": true,  
  "power_led": false  
}  

```

post
`/os/boards/yellow`
🔒
If running on a yellow board, changes one or more of its settings.
**Payload:**
key | type | description  
---|---|---  
disk_led | boolean | Enable/disable the disk LED  
heartbeat_led | boolean | Enable/disable the heartbeat LED  
power_led | boolean | Enable/disable the power LED  
get
`/os/boards/green`
🔒
If running on a green board, returns current values for its settings.
**Returned data:**
key | type | description  
---|---|---  
activity_led | boolean | Is the green activity LED enabled  
power_led | boolean | Is the white power LED enabled  
system_health_led | boolean | Is the yellow system health LED enabled  
**Example response:**
```
{  
  "activity_led": true,  
  "power_led": true,  
  "system_health_led": false  
}  

```

post
`/os/boards/green`
🔒
If running on a green board, changes one or more of its settings.
**Payload:**
key | type | description  
---|---|---  
activity_led | boolean | Enable/disable the green activity LED  
power_led | boolean | Enable/disable the white power LED  
system_health_led | boolean | Enable/disable the yellow system health LED  
### Resolution[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#resolution "Direct link to Resolution")
get
`/resolution/info`
🔒
**Returned data:**
key | type | description  
---|---|---  
unsupported | list | A list of reasons why an installation is marked as unsupported (container, dbus, docker_configuration, docker_version, lxc, network_manager, os, privileged, systemd)  
unhealthy | list | A list of reasons why an installation is marked as unhealthy (docker, supervisor, privileged, setup)  
issues | list | A list of [Issue models](https://developers.home-assistant.io/docs/api/supervisor/models#issues)  
suggestions | list | A list of [Suggestion models](https://developers.home-assistant.io/docs/api/supervisor/models#suggestion) actions  
checks | list | A list of [Check models](https://developers.home-assistant.io/docs/api/supervisor/models#check)  
**Example response:**
```
{  
  "unsupported": ["os"],  
  "unhealthy": ["docker"],  
  "issues": [  
    {  
      "uuid": "A89924620F9A11EBBDC3C403FC2CA371",  
      "type": "free_space",  
      "context": "system",  
      "reference": null  
     }  
  ],  
  "suggestions": [  
    {  
      "uuid": "B9923620C9A11EBBDC3C403FC2CA371",  
      "type": "clear_backups",  
      "context": "system",  
      "reference": null,  
      "auto": false  
    }  
  ],  
  "checks": [  
    {  
      "slug": "free_space",  
      "enabled": true  
    }  
  ]  
}  

```

post
`/resolution/suggestion/<suggestion>`
🔒
Apply a suggested action
delete
`/resolution/suggestion/<suggestion>`
🔒
Dismiss a suggested action
get
`/resolution/issue/<issue>/suggestions`
🔒
Get suggestions that would fix an issue if applied.
**Returned data:**
key | type | description  
---|---|---  
suggestions | list | A list of [Suggestion models](https://developers.home-assistant.io/docs/api/supervisor/models#suggestion) actions  
**Example response:**
```
{  
  "suggestions": [  
    {  
      "uuid": "B9923620C9A11EBBDC3C403FC2CA371",  
      "type": "clear_backups",  
      "context": "system",  
      "reference": null,  
      "auto": false  
    }  
  ]  
}  

```

delete
`/resolution/issue/<issue>`
🔒
Dismiss an issue
post
`/resolution/healthcheck`
🔒
Execute a healthcheck and autofix & notification.
post
`/resolution/check/<check>/options`
🔒
Set options for this check.
**Payload:**
key | type | description  
---|---|---  
enabled | bool | If the check should be enabled or disabled  
post
`/resolution/check/<check>/run`
🔒
Execute a specific check right now.
### Service[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#service "Direct link to Service")
get
`/services`
🔒
**Returned data:**
key | type | description  
---|---|---  
services | dictionary | dictionary of [Service models](https://developers.home-assistant.io/docs/api/supervisor/models#service)  
