[Skip to main content](https://developers.home-assistant.io/docs/api/supervisor/examples/#__docusaurus_skipToContent_fallback)
[![Home Assistant](https://developers.home-assistant.io/img/logo.svg) **Developers**](https://developers.home-assistant.io/)
[Home Assistant](https://developers.home-assistant.io/docs/api/supervisor/examples/)
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
  * Supervisor API
  * Examples


On this page
Examples on how to interface against the supervisor API.
## Get network information with cURL[​](https://developers.home-assistant.io/docs/api/supervisor/examples/#get-network-information-with-curl "Direct link to Get network information with cURL")
```
curl -sSL -H "Authorization: Bearer $SUPERVISOR_TOKEN" http://supervisor/network/info

```

**response:**
```
{
  "result": "ok",
  "data": {
    "interfaces": {
      "eth0": {
        "ip_address": "192.168.1.100/24",
        "gateway": "192.168.1.1",
        "id": "Wired connection 1",
        "type": "802-3-ethernet",
        "nameservers": ["192.168.1.1"],
        "method": "static",
        "primary": true
      }
    }
  }
}

```

## Ping the supervisor[​](https://developers.home-assistant.io/docs/api/supervisor/examples/#ping-the-supervisor "Direct link to Ping the supervisor")
```
curl -sSL http://supervisor/supervisor/ping

```

**response:**
```
{
  "result": "ok",
  "data": {}
}

```

[Previous Models](https://developers.home-assistant.io/docs/api/supervisor/models)
  * [Get network information with cURL](https://developers.home-assistant.io/docs/api/supervisor/examples/#get-network-information-with-curl)
  * [Ping the supervisor](https://developers.home-assistant.io/docs/api/supervisor/examples/#ping-the-supervisor)
