# Find a group by name, then list its integrations
GROUP_ID=$(postiz integrations:groups | jq -r '.[] | select(.name=="My Company") | .id')
postiz integrations:list --group "$GROUP_ID"
```

## Getting Settings

Each platform has its own settings schema with character limits, required fields, and available options. Retrieve it with:

```bash theme={null}
postiz integrations:settings <integration-id>
```

The response tells you:

* What fields are available (title, privacy level, subreddit, etc.)
* Which fields are required
* Character limits and validation rules
* Available dynamic tools you can trigger

<Tip>
  Always check `integrations:settings` before posting to a new platform to understand what settings are available.
</Tip>

## Triggering Tools

Some platforms expose dynamic tools — for example, fetching Reddit flairs, YouTube playlists, or LinkedIn company pages. These return data you need when constructing platform-specific settings.

```bash theme={null}
postiz integrations:trigger <integration-id> <method-name>
```

Pass additional data with `-d`:

```bash theme={null}
postiz integrations:trigger <integration-id> <method-name> -d '{"key":"value"}'
```

### Examples

**Get Reddit flairs for a subreddit:**

```bash theme={null}
postiz integrations:trigger reddit-id getFlairs -d '{"subreddit":"programming"}'
```

**Get YouTube playlists:**

```bash theme={null}
postiz integrations:trigger youtube-id getPlaylists
```

**Get LinkedIn company pages:**

```bash theme={null}
postiz integrations:trigger linkedin-id getCompanies
```

**Get Pinterest boards:**

```bash theme={null}
postiz integrations:trigger pinterest-id getBoards
```

**Search Instagram audio for a Reel** (Facebook Business-linked channels only, empty `q` returns trending audio):

```bash theme={null}
postiz integrations:trigger instagram-id audioSearch -d '{"q":"summer vibes","type":"music"}'
```

## Discovery Workflow

When working with a new platform, follow this workflow:

```bash theme={null}
