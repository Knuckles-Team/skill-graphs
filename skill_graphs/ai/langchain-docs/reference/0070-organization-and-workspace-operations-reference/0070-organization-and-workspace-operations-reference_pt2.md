| Create a run rule       |        ✓        |         ✓        |         ✗        | `rules:create`      |
| Update a run rule       |        ✓        |         ✓        |         ✗        | `rules:update`      |
| Delete a run rule       |        ✓        |         ✓        |         ✗        | `rules:delete`      |
| View rule logs          |        ✓        |         ✓        |         ✓        | `rules:read`        |
| Get last applied rule   |        ✓        |         ✓        |         ✓        | `rules:read`        |
| Manually trigger a rule |        ✓        |         ✓        |         ✗        | `rules:update`      |
| Trigger multiple rules  |        ✓        |         ✓        |         ✗        | `rules:update`      |

### Alerts

Alert rules for monitoring run conditions.

| Operation         | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| Create alert rule |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Update alert rule |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Delete alert rule |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Get alert rule    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| List alert rules  |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Test alert action |        ✓        |         ✓        |         ✓        | `runs:read`         |

### Datasets

Test datasets with examples for evaluation.

| Operation                                    | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission                                  |
| -------------------------------------------- | :-------------: | :--------------: | :--------------: | ---------------------------------------------------- |
| Create a dataset                             |        ✓        |         ✓        |         ✗        | `datasets:create`                                    |
| List datasets                                |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| View dataset details                         |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Update dataset metadata                      |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Delete a dataset                             |        ✓        |         ✗        |         ✗        | `datasets:delete`                                    |
| Upload CSV dataset                           |        ✓        |         ✓        |         ✗        | `datasets:create`                                    |
| Clone dataset                                |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Get dataset version                          |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Get dataset versions                         |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Diff dataset versions                        |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Update dataset version (tags)                |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Download dataset (OpenAI format)             |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Download dataset (OpenAI fine-tuning format) |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Download dataset (CSV)                       |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Download dataset (JSONL)                     |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| View dataset sharing state                   |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Share dataset publicly                       |        ✓        |         ✗        |         ✗        | `datasets:share`                                     |
| Unshare dataset                              |        ✓        |         ✗        |         ✗        | `datasets:share`                                     |
| Get index info                               |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Index dataset                                |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Sync dataset index                           |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Remove dataset index                         |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Search dataset                               |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Generate synthetic examples                  |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Get dataset splits                           |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Update dataset splits                        |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Run playground experiment (batch)            |        ✓        |         ⚠        |         ✗        | `prompts:read` + `datasets:read` + `projects:create` |
| Run playground experiment (stream)           |        ✓        |         ⚠        |         ✗        | `prompts:read` + `datasets:read` + `projects:create` |
| Run studio experiment                        |        ✓        |         ⚠        |         ✗        | `datasets:read` + `projects:create`                  |

<Note>
  Workspace Editors have partial access because they cannot create projects, which limits their ability to create new experiments.
</Note>

### Examples

Individual examples within datasets.

| Operation                       | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| Count examples                  |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| View a specific example         |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| List examples                   |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| Create a new example            |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Create examples (bulk)          |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Update a single example         |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Update examples (bulk)          |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Update examples (multipart)     |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Upload examples from CSV        |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Upload examples from JSONL      |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Delete a single example         |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Delete examples (bulk)          |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| View examples with runs         |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| View grouped examples with runs |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| Validate a single example       |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| Validate examples (bulk)        |        ✓        |         ✓        |         ✓        | `datasets:read`     |

### Experiments

Comparative experiments for evaluating LLM outputs.

| Operation                       | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission                                                       |
| ------------------------------- | :-------------: | :--------------: | :--------------: | ------------------------------------------------------------------------- |
| View comparative experiments    |        ✓        |         ✓        |         ✓        | `projects:read`                                                           |
| Create comparative experiment   |        ✓        |         ⚠        |         ✗        | `projects:create`                                                         |
| Delete comparative experiment   |        ✓        |         ✗        |         ✗        | `projects:delete`                                                         |
| View examples with runs         |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| View grouped examples with runs |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| View grouped experiments        |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| View feedback delta             |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| Upload experiment results       |        ✓        |         ⚠        |         ✗        | `datasets:create` + `datasets:update` + `projects:create` + `runs:create` |
| Get experiment view overrides   |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |
| Create experiment view override |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |
| Update experiment view override |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |
| Delete experiment view override |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |

<Note>
  Workspace Editors have partial access because they cannot create projects, which limits their ability to create new experiments.
</Note>

### Feedback

Scores, labels, and corrections on LLM outputs.

| Operation                                     | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| --------------------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List feedback formulas                        |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Get feedback formula                          |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Create feedback formula                       |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Update feedback formula                       |        ✓        |         ✓        |         ✗        | `feedback:update`   |
| Delete feedback formula                       |        ✓        |         ✓        |         ✗        | `feedback:delete`   |
| View specific feedback                        |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| List feedbacks                                |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Create feedback                               |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Eagerly create feedback                       |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Update feedback                               |        ✓        |         ✓        |         ✗        | `feedback:update`   |
| Delete feedback                               |        ✓        |         ✓        |         ✗        | `feedback:delete`   |
| Batch ingest feedback                         |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Create feedback ingest token                  |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| List feedback ingest tokens                   |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Create feedback with token (no auth required) |        ✓        |         ✓        |         ✓        | N/A (token-based)   |
| List feedback configs                         |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Create feedback config                        |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Update feedback config                        |        ✓        |         ✓        |         ✗        | `feedback:update`   |

### Annotation queues

Human review queues for LLM outputs.

| Operation                                   | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission        |
| ------------------------------------------- | :-------------: | :--------------: | :--------------: | -------------------------- |
| List annotation queues                      |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get annotation queue                        |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Create annotation queue                     |        ✓        |         ✓        |         ✗        | `annotation-queues:create` |
| Update annotation queue                     |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Delete annotation queue                     |        ✓        |         ✗        |         ✗        | `annotation-queues:delete` |
| Populate annotation queue                   |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Get runs from queue                         |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get run from queue (by index)               |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queues for run                          |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queue total size                        |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queue total archived                    |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queue size                              |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Add runs to queue                           |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Update run in queue                         |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Delete run from queue                       |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Delete runs from queue (bulk)               |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Create identity annotation queue run status |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Export archived runs                        |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |

### Prompts

Prompt templates and chains in the LangChain Hub.

| Operation               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List prompt repos       |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| View prompt repo        |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create prompt repo      |        ✓        |         ✓        |         ✗        | `prompts:create`    |
| Fork prompt repo        |        ✓        |         ✓        |         ✗        | `prompts:create`    |
| Update prompt repo      |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| Delete prompt repo      |        ✓        |         ✓        |         ✗        | `prompts:delete`    |
| List commits            |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| View commit             |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Push commit             |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| List repo tags          |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Get all tags            |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create tag              |        ✓        |         ✓        |         ✗        | `prompts:tag`       |
| Update tag              |        ✓        |         ✓        |         ✗        | `prompts:tag`       |
| Delete tag              |        ✓        |         ✓        |         ✗        | `prompts:tag`       |
| View events             |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| List comments           |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create comment          |        ✓        |         ✓        |         ✗        | `prompts:read`      |
| Delete comment          |        ✓        |         ✓        |         ✗        | `prompts:read`      |
| Toggle like             |        ✓        |         ✓        |         ✗        | `prompts:read`      |
| Optimize prompt         |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| List optimization jobs  |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create optimization job |        ✓        |         ✓        |         ✗        | `prompts:create`    |
| Update optimization job |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| Delete optimization job |        ✓        |         ✓        |         ✗        | `prompts:delete`    |
| Invoke prompt canvas    |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| List quick actions      |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create quick action     |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Delete quick action     |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Update quick action     |        ✓        |         ✓        |         ✓        | `prompts:read`      |

<Note>
  Some prompt operations support public access for shared prompts.
</Note>

### Charts

Custom visualizations and dashboards.

| Operation               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List charts             |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Get chart by ID         |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Create chart            |        ✓        |         ✓        |         ✗        | `charts:create`     |
| Update chart            |        ✓        |         ✓        |         ✗        | `charts:update`     |
| Delete chart            |        ✓        |         ✓        |         ✗        | `charts:delete`     |
| Render chart            |        ✓        |         ✓        |         ✓        | `charts:read`       |
| List chart sections     |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Get chart section by ID |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Create chart section    |        ✓        |         ✓        |         ✗        | `charts:create`     |
| Update chart section    |        ✓        |         ✓        |         ✗        | `charts:update`     |
| Delete chart section    |        ✓        |         ✓        |         ✗        | `charts:delete`     |
| Render chart section    |        ✓        |         ✓        |         ✓        | `charts:read`       |

### Deployments

[LangSmith Deployment](/langsmith/deployment) configurations.

| Operation         | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission  |
| ----------------- | :-------------: | :--------------: | :--------------: | -------------------- |
| Create deployment |        ✓        |         ✓        |         ✗        | `deployments:create` |
| View deployment   |        ✓        |         ✓        |         ✓        | `deployments:read`   |
| Update deployment |        ✓        |         ✓        |         ✗        | `deployments:update` |
| Delete deployment |        ✓        |         ✗        |         ✗        | `deployments:delete` |

### Workspace settings and management

| Operation                                                 | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission         |
| --------------------------------------------------------- | :-------------: | :--------------: | :--------------: | --------------------------- |
| View workspace info                                       |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View workspace statistics                                 |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Update workspace (name, description)                      |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |
| Delete workspace                                          |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |
| View workspace members                                    |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View active workspace members                             |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View pending workspace members                            |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Add member to workspace                                   |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Add members (batch)                                       |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Update workspace member role                              |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Remove workspace member                                   |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Delete pending workspace member                           |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| View workspace trace retention settings                   |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
