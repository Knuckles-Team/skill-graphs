##  [Custom SIEM Log Streaming](https://vercel.com/docs/audit-log#custom-siem-log-streaming)[](https://vercel.com/docs/audit-log#custom-siem-log-streaming)
Custom SIEM Log Streaming is available for purchase on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
In addition to the standard audit log functionalities, Vercel supports custom log streaming to your Security Information and Event Management (SIEM) system of choice. This allows you to integrate Vercel audit logs with your existing observability and security infrastructure.
We support the following SIEM options out of the box:
  * AWS S3
  * Splunk
  * Datadog
  * Google Cloud Storage


We also support streaming logs to any HTTP endpoint, secured with a custom header.
###  [Allowlisting IP addresses](https://vercel.com/docs/audit-log#allowlisting-ip-addresses)[](https://vercel.com/docs/audit-log#allowlisting-ip-addresses)
If your SIEM requires IP allowlisting, please use the following IP addresses:
```
23.21.184.92
34.204.154.149
44.213.245.178
44.215.236.82
50.16.203.9
52.1.251.34
52.21.49.187
174.129.36.47
```

###  [Setup process](https://vercel.com/docs/audit-log#setup-process)[](https://vercel.com/docs/audit-log#setup-process)
To set up custom log streaming to your SIEM:
  * From your [dashboard](https://vercel.com/dashboard), go to Team Settings, open [Security & Privacy](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fsecurity&title=Go+to+Security+settings) in the sidebar, and scroll to Audit Log
  * Click the Configure button
  * Select one of the supported SIEM providers and follow the step-by-step guide

![Select one of the supported SIEM providers](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Faudit-log-streams-light.png&w=3840&q=75)![Select one of the supported SIEM providers](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Faudit-log-streams-dark.png&w=3840&q=75)Select one of the supported SIEM providers
The HTTP POST provider is generic solution to stream audit logs to any configured endpoint. To set this up, you need to provide:
  * URL: The endpoint that will accept HTTP POST requests
  * HTTP Header Name: The name of the header, such as `Authorization`
  * HTTP Header Value: The corresponding value, e.g. `Bearer <token>`


For the request body format, you can choose between:
  * JSON: Sends a JSON array containing event objects
  * NDJSON: Sends events as newline-delimited JSON objects, enabling individual processing


###  [Audit Logs CSV file structure](https://vercel.com/docs/audit-log#audit-logs-csv-file-structure)[](https://vercel.com/docs/audit-log#audit-logs-csv-file-structure)
The CSV file can be opened using any spreadsheet-compatible software, and includes the following fields:
Property | Description
---|---
timestamp | Time and date at which the event occurred
action | Name for the specific event. E.g, `project.created`, `team.member.left`, `project.transfer_out.completed`, `auditlog.export.downloaded`, `auditlog.export.requested`, etc. [Learn more about it here](https://vercel.com/docs/audit-log#actions).
actor_vercel_id | User ID of the team member responsible for an event
actor_name | Account responsible for the action. For example, username of the team member
actor_email | Email address of the team member responsible for a specific event
location | IP address from where the action was performed
user_agent | Details about the application, operating system, vendor, and/or browser version used by the team member
previous | Custom metadata (JSON object) showing the object's previous state
next | Custom metadata (JSON object) showing the object's updated state
