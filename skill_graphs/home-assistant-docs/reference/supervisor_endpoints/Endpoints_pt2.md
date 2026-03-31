---|---|---|---  
timeout | int | True | Seconds before freeze times out and thaw begins automatically (default: 600).  
post
`/backups/thaw`
🔒
End a freeze initiated by `/backups/freeze` and resume normal behavior in Home Assistant and addons.
get
`/backups/<backup>/download`
🔒
Download the backup file with the given slug.
get
`/backups/<backup>/info`
🔒
Returns a [Backup details model](https://developers.home-assistant.io/docs/api/supervisor/models#backup-details) for the app.
delete
`/backups/<backup>`
🔒
Removes the backup file with the given slug.
post
`/backups/<backup>/restore/full`
🔒
Does a full restore of the backup with the given slug.
**Payload:**
key | type | optional | description  
---|---|---|---  
password | string | True | The password for the backup if any  
background | boolean | True | Return `job_id` immediately, do not wait for restore to complete. Clients must check job for status.  
**Example response:**
```
{  
  "job_id": "abc123"  
}  

```

Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened. Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.
post
`/backups/<backup>/restore/partial`
🔒
Does a partial restore of the backup with the given slug.
**Payload:**
key | type | optional | description  
---|---|---|---  
homeassistant | boolean | True |  `true` if Home Assistant should be restored  
addons | list | True | A list of app slugs that should be restored  
folders | list | True | A list of directories that should be restored  
password | string | True | The password for the backup if any  
background | boolean | True | Return `job_id` immediately, do not wait for restore to complete. Clients must check job for status.  
**You need to supply at least one key in the payload.**
**Example response:**
```
{  
  "job_id": "abc123"  
}  

```

Error responses from this API may also include a `job_id` if the message alone cannot accurately describe what happened. Callers should direct users to review the job or supervisor logs to get an understanding of what occurred.
### CLI[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#cli "Direct link to CLI")
get
`/cli/info`
🔒
Returns information about the CLI plugin
**Returned data:**
key | type | description  
---|---|---  
version | string | The installed cli version  
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
`/cli/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the CLI plugin.
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
`/cli/update`
🔒
Update the CLI plugin
**Payload:**
key | type | description  
---|---|---  
version | string | The version you want to install, default is the latest version  
### Core[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#core "Direct link to Core")
get
`/core/api`
🔒
Proxy GET API calls to the Home Assistant API
post
`/core/api`
🔒
Proxy POST API calls to the Home Assistant API
post
`/core/check`
🔒
Run a configuration check
get
`/core/info`
🔒
Returns information about the Home Assistant core
**Returned data:**
key | type | description  
---|---|---  
version | string | The installed core version  
version_latest | string | The latest published version in the active channel  
update_available | boolean |  `true` if an update is available  
arch | string | The architecture of the host (armhf, aarch64, i386, amd64)  
machine | string | The machine type that is running the host  
ip_address | string | The internal docker IP address to the supervisor  
image | string | The container image that is running the core  
boot | boolean |  `true` if it should start on boot  
port | int | The port Home Assistant is running on  
ssl | boolean |  `true` if Home Assistant is using SSL  
watchdog | boolean |  `true` if watchdog is enabled  
wait_boot | int | Max time to wait during boot  
audio_input | string or null | The description of the audio input device  
audio_output | string or null | The description of the audio output device  
backups_exclude_database | boolean | Backups exclude Home Assistant database file by default  
duplicate_log_file | boolean | Home Assistant duplicates logs to a file  
**Example response:**
```
{  
  "version": "0.117.0",  
  "version_latest": "0.117.0",  
  "update_available": true,  
  "arch": "arch",  
  "machine": "amd64",  
  "ip_address": "172.0.0.15",  
  "image": "homeassistant/home-assistant",  
  "boot": true,  
  "port": 8123,  
  "ssl": false,  
  "watchdog": true,  
  "wait_boot": 800,  
  "audio_input": "AMCP32",  
  "audio_output": "AMCP32"  
}  

```

get
`/core/logs`
🔒
Get logs for the Home Assistant Core container via the Systemd journal backend.
The endpoint accepts the same headers and provides the same functionality as `/host/logs`.
get
`/core/logs/follow`
🔒
Identical to `/core/logs` except it continuously returns new log entries.
get
`/core/logs/latest`
🔒
Return all logs of the latest startup of the Home Assistant Core container.
The `Range` header is ignored but the `lines` query parameter can be used.
get
`/core/logs/boots/<bootid>`
🔒
Get logs for the Home Assistant Core container related to a specific boot.
The `bootid` parameter is interpreted in the same way as in `/host/logs/boots/<bootid>` and the endpoint otherwise provides the same functionality as `/host/logs`.
get
`/core/logs/boots/<bootid>/follow`
🔒
Identical to `/core/logs/boots/<bootid>` except it continuously returns new log entries.
post
`/core/options`
🔒
Update options for Home Assistant, you need to supply at least one of the payload keys to the API call. You need to call `/core/restart` after updating the options.
Passing `image`, `refresh_token`, `audio_input` or `audio_output` with `null` resets the option.
**Payload:**
key | type | description  
---|---|---  
boot | boolean | Start Core on boot  
image | string or null | Name of custom image  
port | int | The port that Home Assistant run on  
ssl | boolean |  `true` to enable SSL  
watchdog | boolean |  `true` to enable the watchdog  
wait_boot | int | Time to wait for Core to startup  
refresh_token | string or null | Token to authenticate with Core  
audio_input | string or null | Profile name for audio input  
audio_output | string or null | Profile name for audio output  
backups_exclude_database | boolean |  `true` to exclude Home Assistant database file from backups  
duplicate_log_file | boolean |  `true` to duplicate Home Assistant logs to a file  
**You need to supply at least one key in the payload.**
post
`/core/rebuild`
🔒
Rebuild the Home Assistant core container
**Payload:**
key | type | optional | description  
---|---|---|---  
safe_mode | boolean | True | Rebuild Core into safe mode  
force | boolean | True | Force rebuild during a Home Assistant offline db migration  
post
`/core/restart`
🔒
Restart the Home Assistant core container
**Payload:**
key | type | optional | description  
---|---|---|---  
safe_mode | boolean | True | Restart Core into safe mode  
force | boolean | True | Force restart during a Home Assistant offline db migration  
post
`/core/start`
🔒
Start the Home Assistant core container
get
`/core/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the Home Assistant core.
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
`/core/stop`
🔒
Stop the Home Assistant core container
**Payload:**
key | type | optional | description  
---|---|---|---  
force | boolean | True | Force stop during a Home Assistant offline db migration  
post
`/core/update`
🔒
Update Home Assistant core
**Payload:**
key | type | description  
---|---|---  
version | string | The version you want to install, default is the latest version  
backup | boolean | Create a partial backup of core and core configuration before updating, default is false  
get
`/core/websocket`
🔒
Proxy to Home Assistant Core websocket.
### Discovery[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#discovery "Direct link to Discovery")
get
`/discovery`
🔒
Return information about enabled discoveries.
**Returned data:**
key | type | description  
---|---|---  
discovery | list | A list of [Discovery models](https://developers.home-assistant.io/docs/api/supervisor/models#discovery)  
services | dictionary | A dictionary of services that contains a list of apps that have that service.  
**Example response:**
```
{  
  "discovery": [  
    {  
      "addon": "awesome_addon",  
      "service": "awesome.service",  
      "uuid": "fh874r-fj9o37yr3-fehsf7o3-fd798",  
      "config": {}  
    }  
  ],  
  "services": {  
    "awesome": ["awesome_addon"]  
  }  
}  

```

post
`/discovery`
🔒
Create a discovery service
**Payload:**
key | type | optional | description  
---|---|---|---  
service | string | False | The name of the service  
config | dictionary | False | The configuration of the service  
**Example response:**
```
{  
  "uuid": "uuid"  
}  

```

get
`/discovery/<uuid>`
🔒
Get a [discovery model](https://developers.home-assistant.io/docs/api/supervisor/models#discovery) for a UUID.
delete
`/discovery/<uuid>`
🔒
Delete a specific service.
### DNS[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#dns "Direct link to DNS")
get
`/dns/info`
🔒
Return information about the DNS plugin.
**Returned data:**
key | type | description  
---|---|---  
fallback | bool | Try fallback DNS on failure  
host | string | The IP address of the plugin  
llmnr | bool | Can resolve LLMNR hostnames  
locals | list | A list of DNS servers  
mdns | bool | Can resolve MulticastDNS hostnames  
servers | list | A list of DNS servers  
update_available | boolean |  `true` if an update is available  
version | string | The installed observer version  
version_latest | string | The latest published version  
**Example response:**
```
{  
  "host": "127.0.0.18",  
  "version": "1",  
  "version_latest": "2",  
  "update_available": true,  
  "servers": ["dns://8.8.8.8"],  
  "locals": ["dns://127.0.0.18"],  
  "mdns": true,  
  "llmnr": false,  
  "fallback": true  
}  

```

get
`/dns/logs`
🔒
Get logs for the DNS plugin container via the Systemd journal backend.
The endpoint accepts the same headers and provides the same functionality as `/host/logs`.
get
`/dns/logs/follow`
🔒
Identical to `/dns/logs` except it continuously returns new log entries.
get
`/dns/logs/latest`
🔒
Return all logs of the latest startup of the DNS plugin container.
The `Range` header is ignored but the `lines` query parameter can be used.
get
`/dns/logs/boots/<bootid>`
🔒
Get logs for the DNS plugin container related to a specific boot.
The `bootid` parameter is interpreted in the same way as in `/host/logs/boots/<bootid>` and the endpoint otherwise provides the same functionality as `/host/logs`.
get
`/dns/logs/boots/<bootid>/follow`
🔒
Identical to `/dns/logs/boots/<bootid>` except it continuously returns new log entries.
post
`/dns/options`
🔒
Set DNS options
**Payload:**
key | type | optional | description  
---|---|---|---  
fallback | bool | True | Enable/Disable fallback DNS  
servers | list | True | A list of DNS servers  
**You need to supply at least one key in the payload.**
post
`/dns/reset`
🔒
Reset the DNS configuration.
post
`/dns/restart`
🔒
Restart the DNS plugin
get
`/dns/stats`
🔒
Returns a [Stats model](https://developers.home-assistant.io/docs/api/supervisor/models#stats) for the dns plugin.
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
`/dns/update`
🔒
Update the DNS plugin
**Payload:**
key | type | description  
---|---|---  
version | string | The version you want to install, default is the latest version  
### Docker[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#docker "Direct link to Docker")
get
`/docker/info`
🔒
Returns information about the docker instance.
**Returned data:**
key | type | description  
---|---|---  
version | string | The version of the docker engine  
enable_ipv6 | bool | Enable/Disable IPv6 for containers  
storage | string | The storage type  
logging | string | The logging type  
registries | dictionary | A dictionary of dictionaries containing `username` and `password` keys for registries.  
**Example response:**
```
{  
  "version": "1.0.1",  
  "enable_ipv6": true,  
  "storage": "overlay2",  
  "logging": "journald",  
  "registries": {}  
}  

```

post
`/docker/options`
🔒
Set docker options
**Payload:**
key | type | optional | description  
---|---|---|---  
enable_ipv6 | bool | True | Enable/Disable IPv6 for containers  
**You need to supply at least one key in the payload.**
get
`/docker/registries`
🔒
Get all configured container registries, this returns a dict with the registry hostname as the key, and a dictionary containing the username configured for that registry.
**Example response:**
```
{  
  "registry.example.com": {  
    "username": "AwesomeUser"  
  }  
}  

```

post
`/docker/registries`
🔒
Add a new container registry.
**Payload:**
key | type | description  
---|---|---  
hostname | dictionary | A dictionary containing `username` and `password` keys for the registry.  
**Example payload:**
```
{  
  "registry.example.com": {  
    "username": "AwesomeUser",  
    "password": "MySuperStrongPassword!"  
  }  
}  

```

To login to the default container registry (Docker Hub), use `hub.docker.com` as the registry.
delete
`/docker/registries/<registry>`
🔒
Delete a registry from the configured container registries.
post
`/docker/migrate-storage-driver`
🔒
Schedule a Docker storage driver migration. The migration will be applied on the next system reboot.
This endpoint allows migrating to either:
  * `overlayfs`: The Containerd overlayfs driver
  * `overlay2`: The Docker graph overlay2 driver


This endpoint requires Home Assistant OS 17.0 or newer. A `404` error will be returned on older versions or non-HAOS installations.
**Payload:**
key | type | optional | description  
---|---|---|---  
storage_driver | string | False | The target storage driver (`overlayfs` or `overlay2`)  
**Example payload:**
```
{  
  "storage_driver": "overlayfs"  
}  

```

After calling this endpoint, a reboot is required to apply the migration. The response will create a `reboot_required` issue in the resolution center.
### Hardware[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#hardware "Direct link to Hardware")
get
`/hardware/info`
🔒
Get hardware information.
**Example response:**
```
{  
    "devices": [  
      {  
        "name": "ttyACM0",  
        "sysfs": "/sys/devices/usb/00:01",  
        "dev_path": "/dev/ttyACM0",  
        "by_id": "/dev/serial/by-id/usb-Silicon_Labs-RFUSB_9017F723B061A7C01410CFCF-if00-port1",  
        "subsystem": "tty",  
        "parent": null,  
        "attributes": {  
          "MINOR": "5"  
        },  
        "children": [  
          "/sys/devices/soc/platform/00ef"  
        ]  
      }  
    ],  
    "drives": [  
      {  
        "vendor": "Generic",  
        "model": "Flash Disk",  
        "revision": "8.07",  
        "serial": "AABBCCDD",  
        "id": "Generic-Flash-Disk-AABBCCDD",  
        "size": 8054112256,  
        "time_detected": "2023-02-15T21:44:22.504878+00:00",  
        "connection_bus": "usb",  
        "seat": "seat0",  
        "removable": true,  
        "ejectable": true,  
        "filesystems": [  
          {  
            "device": "/dev/sda1",  
            "id": "by-uuid-1122-1ABA",  
            "size": 67108864,  
            "name": "",  
            "system": false,  
            "mount_points": []  
          }  
        ]  
      }  
    ]  
}  

```

**Returned data:**
key | description  
---|---  
devices | A list of [Device models](https://developers.home-assistant.io/docs/api/supervisor/models#device)  
drives | A list of [Drive models](https://developers.home-assistant.io/docs/api/supervisor/models#drive)  
get
`/hardware/audio`
🔒
Get audio devices
**Example response:**
```
{  
  "audio": {  
    "input": {  
      "0,0": "Mic"  
    },  
    "output": {  
      "1,0": "Jack",  
      "1,1": "HDMI"  
    }  
  }  
}  

```

### Host[​](https://developers.home-assistant.io/docs/api/supervisor/endpoints/#host "Direct link to Host")
get
`/host/info`
🔒
Return information about the host.
**Returned data**
key | type | description  
---|---|---  
agent_version | string or null | Agent version running on the Host  
apparmor_version | string or null | The AppArmor version from host  
boot_timestamp | int | The timestamp for the last boot in microseconds  
broadcast_llmnr | bool or null | Host is broadcasting its LLMNR hostname  
broadcast_mdns | bool or null | Host is broadcasting its MulticastDNS hostname  
chassis | string or null | The chassis type  
virtualization | string or null | Virtualization hypervisor in use (if any)  
cpe | string or null | The local CPE  
deployment | string or null | The deployment stage of the OS if any  
disk_total | float | Total space of the disk in MB  
disk_used | float | Used space of the disk in MB  
disk_free | float | Free space of the disk in MB  
features | list | A list of features available for the host  
hostname | string or null | The hostname of the host  
kernel | string or null | The kernel version on the host  
llmnr_hostname | string or null | The hostname currently exposed on the network via LLMNR for host  
operating_system | string | The operating system on the host  
startup_time | float | The time in seconds it took for last boot  
disk_life_time | float or null | Percentage of estimated disk lifetime used (0–100). Not all disks provide this information, returns `null` if unavailable.  
timezone | string | The current timezone of the host.  
dt_utc | string | Current UTC date/time of the host in ISO 8601 format.  
dt_synchronized | bool |  `true` if the host is synchronized with an NTP service.  
use_ntp | bool |  `true` if the host is using an NTP service for time synchronization.  
**Example response:**
```
{  
  "agent_version": "1.2.0",  
  "apparmor_version": "2.13.2",  
  "chassis": "specific",  
  "cpe": "xy",  
  "deployment": "stable",  
  "disk_total": 32.0,  
  "disk_used": 30.0,  
  "disk_free": 2.0,  
  "features": ["shutdown", "reboot", "hostname", "services", "haos"],  
  "hostname": "Awesome host",  
  "llmnr_hostname": "Awesome host",  
  "kernel": "4.15.7",  
  "operating_system": "Home Assistant OS",  
  "boot_timestamp": 1234567788,  
  "startup_time": 12.345,  
  "broadcast_llmnr": true,  
  "broadcast_mdns": false,  
  "virtualization": "",  
  "disk_life_time": 10.0,  
  "timezone": "Europe/Brussels",  
  "dt_utc": "2025-09-08T12:00:00.000000+00:00",  
  "dt_synchronized": true,  
  "use_ntp": true  
}  

```

get
`/host/logs`
🔒
Get systemd Journal logs from the host. Returns log entries in plain text, one log record per line.
**HTTP Request Headers**
Header | optional | description  
---|---|---  
Accept | true | Type of data (text/plain or text/x-log)  
Range | true | Range of log entries. The format is `entries=cursor[[:num_skip]:num_entries]`  
**HTTP Query Parameters**
These are a convenience alternative to the headers shown above as query parameters are easier to use in development and with the Home Assistant proxy. You should only provide one or the other.
Query | type | description  
---|---|---  
verbose | N/A | If included, uses `text/x-log` as log output type (alternative to `Accept` header)  
lines | int | Number of lines of output to return (alternative to `Range` header)  
no_colors | N/A | If included, ANSI escape codes for terminal coloring will be stripped from the output  
Example query string:
```
?verbose&lines=100&no_colors  

```

To get the last log entries the Range request header supports negative values as `num_skip`. E.g. `Range: entries=:-9:` returns the last 10 entries. Or `Range: entries=:-200:100` to see 100 entries starting from the one 200 ago.
API returns the last 100 lines by default. Provide a value for `Range` to see logs further in the past.
The `Accept` header can be set to `text/x-log` to get logs annotated with extra information, such as the timestamp and Systemd unit name. If no identifier is specified (i.e. for the host logs containing logs for multiple identifiers/units), this option is ignored - these logs are always annotated.
get
`/host/logs/follow`
🔒
Identical to `/host/logs` except it continuously returns new log entries.
`/host/logs/identifiers`
🔒
Returns a list of syslog identifiers from the systemd journal that you can use with `/host/logs/identifiers/<identifier>` and `/host/logs/boots/<bootid>/identifiers/<identifier>`.
get
`/host/logs/identifiers/<identifier>`
🔒
Get systemd Journal logs from the host for entries related to a specific log identifier. Some examples of useful identifiers here include
  * `audit` - If developing an apparmor profile shows you permission issues
  * `NetworkManager` - Shows NetworkManager logs when having network issues
  * `bluetoothd` - Shows bluetoothd logs when having bluetooth issues


A call to `GET /host/logs/identifiers` will show the complete list of possible values for `identifier`.
Otherwise it provides the same functionality as `/host/logs`.
get
`/host/logs/identifiers/<identifier>/follow`
🔒
Identical to `/host/logs/identifiers/<identifier>` except it continuously returns new log entries.
`/host/logs/boots`
🔒
Returns a dictionary of boot IDs for this system that you can use with `/host/logs/boots/<bootid>` and `/host/logs/boots/<bootid>/identifiers/<identifier>`.
The key for each item in the dictionary is the boot offset. 0 is the current boot, a negative number denotes how many boots ago that boot was.
get
`/host/logs/boots/<bootid>`
🔒
Get systemd Journal logs from the host for entries related to a specific boot. Call `GET /host/info/boots` to see the boot IDs. Alternatively you can provide a boot offset:
  * 0 - The current boot
  * Negative number - Count backwards from current boot (-1 is previous boot)
  * Positive number - Count forward from last known boot (1 is last known boot)


Otherwise it provides the same functionality as `/host/logs`.
get
`/host/logs/boots/<bootid>/follow`
🔒
Identical to `/host/logs/boots/<bootid>` except it continuously returns new log entries.
get
`/host/logs/boots/<bootid>/identifiers/<identifier>`
🔒
Get systemd Journal logs entries for a specific log identifier and boot. A combination of `/host/logs/boots/<bootid>` and `/host/logs/identifiers/<identifier>`.
get
`/host/logs/boot/<bootid>/<identifier>/entries/follow`
🔒
Identical to `/host/logs/boots/<bootid>/identifiers/<identifier>` except it continuously returns new log entries.
post
`/host/options`
🔒
Set host options
**Payload:**
key | type | optional | description  
---|---|---|---  
hostname | string | True | A string that will be used as the new hostname  
**You need to supply at least one key in the payload.**
post
`/host/reboot`
🔒
Reboot the host
**Payload:**
key | type | optional | description  
---|---|---|---  
force | boolean | True | Force reboot during a Home Assistant offline db migration  
post
`/host/reload`
🔒
Reload host information
post
`/host/service/<service>/start`
🔒
Start a service on the host.
post
`/host/service/<service>/stop`
🔒
Stop a service on the host.
post
`/host/service/<service>/reload`
🔒
Reload a service on the host.
get
`/host/services`
🔒
Get information about host services.
**Returned data:**
key | description  
---|---  
services | A dictionary of [Host service models](https://developers.home-assistant.io/docs/api/supervisor/models#host-service)  
**Example response:**
```
{  
  "services": [  
    {  
      "name": "awesome.service",  
      "description": "Just an awesome service",  
      "state": "active"  
    }  
  ]  
}  

```

post
`/host/shutdown`
🔒
Shutdown the host
**Payload:**
key | type | optional | description  
---|---|---|---  
force | boolean | True | Force shutdown during a Home Assistant offline db migration  
get
`/host/disks/<disk>/usage`
🔒
Get detailed disk usage information in bytes.
The only supported `disk` for now is "default". It will return usage info for the data disk.
Supports an optional `max_depth` query param. Defaults to 1
**Example response:**
```
{  
  "id": "root",  
  "label": "Default",  
  "total_space": 503312781312,  
  "used_space": 430245011456,  
  "children": [  
    {  
      "id": "system",  
      "label": "System",  
      "used_space": 75660903137  
    },  
    {  
      "id": "addons_data",  
      "label": "Addons data",  
      "used_space": 42349200762  
