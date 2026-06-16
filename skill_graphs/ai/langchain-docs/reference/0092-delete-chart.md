# Delete Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/delete-chart

/langsmith/langsmith-platform-openapi.json delete /api/v1/charts/{chart_id}
Delete a chart.

# Delete Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/delete-section

/langsmith/langsmith-platform-openapi.json delete /api/v1/charts/section/{section_id}
Delete a section.

# Org Create Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-create-chart

/langsmith/langsmith-platform-openapi.json post /api/v1/org-charts/create
Create a new chart.

# Org Create Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-create-section

/langsmith/langsmith-platform-openapi.json post /api/v1/org-charts/section
Create a new section.

# Org Delete Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-delete-chart

/langsmith/langsmith-platform-openapi.json delete /api/v1/org-charts/{chart_id}
Delete a chart.

# Org Delete Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-delete-section

/langsmith/langsmith-platform-openapi.json delete /api/v1/org-charts/section/{section_id}
Delete a section.

# Org Read Chart Preview
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-read-chart-preview

/langsmith/langsmith-platform-openapi.json post /api/v1/org-charts/preview
Get a preview for a chart without actually creating it.

# Org Read Charts
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-read-charts

/langsmith/langsmith-platform-openapi.json post /api/v1/org-charts
Get all charts for the tenant.

# Org Read Sections
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-read-sections

/langsmith/langsmith-platform-openapi.json get /api/v1/org-charts/section
Get all sections for the tenant.

# Org Read Single Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-read-single-chart

/langsmith/langsmith-platform-openapi.json post /api/v1/org-charts/{chart_id}
Get a single chart by ID.

# Org Read Single Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-read-single-section

/langsmith/langsmith-platform-openapi.json post /api/v1/org-charts/section/{section_id}
Get a single section by ID.

# Org Update Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-update-chart

/langsmith/langsmith-platform-openapi.json patch /api/v1/org-charts/{chart_id}
Update a chart.

# Org Update Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/org-update-section

/langsmith/langsmith-platform-openapi.json patch /api/v1/org-charts/section/{section_id}
Update a section.

# Read Chart Preview
Source: https://docs.langchain.com/langsmith/smith-api/charts/read-chart-preview

/langsmith/langsmith-platform-openapi.json post /api/v1/charts/preview
Get a preview for a chart without actually creating it.

# Read Charts
Source: https://docs.langchain.com/langsmith/smith-api/charts/read-charts

/langsmith/langsmith-platform-openapi.json post /api/v1/charts
Get all charts for the tenant.

# Read Sections
Source: https://docs.langchain.com/langsmith/smith-api/charts/read-sections

/langsmith/langsmith-platform-openapi.json get /api/v1/charts/section
Get all sections for the tenant.

# Read Single Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/read-single-chart

/langsmith/langsmith-platform-openapi.json post /api/v1/charts/{chart_id}
Get a single chart by ID.

# Read Single Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/read-single-section

/langsmith/langsmith-platform-openapi.json post /api/v1/charts/section/{section_id}
Get a single section by ID.

# Update Chart
Source: https://docs.langchain.com/langsmith/smith-api/charts/update-chart

/langsmith/langsmith-platform-openapi.json patch /api/v1/charts/{chart_id}
Update a chart.

# Update Section
Source: https://docs.langchain.com/langsmith/smith-api/charts/update-section

/langsmith/langsmith-platform-openapi.json patch /api/v1/charts/section/{section_id}
Update a section.

# Create Comment
Source: https://docs.langchain.com/langsmith/smith-api/comments/create-comment

/langsmith/langsmith-platform-openapi.json post /api/v1/comments/{owner}/{repo}

# Create Sub Comment
Source: https://docs.langchain.com/langsmith/smith-api/comments/create-sub-comment

/langsmith/langsmith-platform-openapi.json post /api/v1/comments/{owner}/{repo}/{parent_comment_id}

# Get Comments
Source: https://docs.langchain.com/langsmith/smith-api/comments/get-comments

/langsmith/langsmith-platform-openapi.json get /api/v1/comments/{owner}/{repo}

# Get Sub Comments
Source: https://docs.langchain.com/langsmith/smith-api/comments/get-sub-comments

/langsmith/langsmith-platform-openapi.json get /api/v1/comments/{owner}/{repo}/{parent_comment_id}

# Like Comment
Source: https://docs.langchain.com/langsmith/smith-api/comments/like-comment

/langsmith/langsmith-platform-openapi.json post /api/v1/comments/{owner}/{repo}/{parent_comment_id}/like

# Unlike Comment
Source: https://docs.langchain.com/langsmith/smith-api/comments/unlike-comment

/langsmith/langsmith-platform-openapi.json delete /api/v1/comments/{owner}/{repo}/{parent_comment_id}/like

# Create a commit
Source: https://docs.langchain.com/langsmith/smith-api/commits/create-a-commit

/langsmith/langsmith-platform-openapi.json post /commits/{owner}/{repo}
Creates a new commit in a repository.
Requires authentication and write access to the repository.

# Get a commit
Source: https://docs.langchain.com/langsmith/smith-api/commits/get-a-commit

/langsmith/langsmith-platform-openapi.json get /commits/{owner}/{repo}/{commit}
Retrieves a specific commit by hash, tag, or "latest" for a repository.
This endpoint supports both authenticated and unauthenticated access.
Authenticated users can access private repos, while unauthenticated users can only access public repos.
Commit resolution logic:
- "latest" or empty: Get the most recent commit
- Less than 8 characters: Only check for tags
- 8 or more characters: Prioritize commit hash over tag, check both

# List commits
Source: https://docs.langchain.com/langsmith/smith-api/commits/list-commits

/langsmith/langsmith-platform-openapi.json get /commits/{owner}/{repo}
Lists all commits for a repository with pagination support.
This endpoint supports both authenticated and unauthenticated access.
Authenticated users can access private repos, while unauthenticated users can only access public repos.
The include_stats parameter controls whether download and view statistics are computed (defaults to true).

# Create a new data plane
Source: https://docs.langchain.com/langsmith/smith-api/data_planes/create-a-new-data-plane

/langsmith/langsmith-platform-openapi.json post /orgs/current/data-planes
Creates a new data plane object. Persists the rendered data plane spec, and returns 202 with the data plane in status=requested. Requires BYOC enabled org and org admin.

# List data planes for the current organization
Source: https://docs.langchain.com/langsmith/smith-api/data_planes/list-data-planes-for-the-current-organization

/langsmith/langsmith-platform-openapi.json get /orgs/current/data-planes
Returns up to 50 data planes owned by the caller's organization. Sorted status priority (active first), then newest first. Requires BYOC to be enabled for the org.

# Clone Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/clone-dataset

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/clone
Clone a dataset.

# Create Comparative Experiment
Source: https://docs.langchain.com/langsmith/smith-api/datasets/create-comparative-experiment

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/comparative
Create a comparative experiment.

# Create Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/create-dataset

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets
Create a new dataset.

# Delete Comparative Experiment
Source: https://docs.langchain.com/langsmith/smith-api/datasets/delete-comparative-experiment

/langsmith/langsmith-platform-openapi.json delete /api/v1/datasets/comparative/{comparative_experiment_id}
Delete a specific comparative experiment.

# Delete Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/delete-dataset

/langsmith/langsmith-platform-openapi.json delete /api/v1/datasets/{dataset_id}
Delete a specific dataset.

# Delete Datasets
Source: https://docs.langchain.com/langsmith/smith-api/datasets/delete-datasets

/langsmith/langsmith-platform-openapi.json delete /api/v1/datasets
Delete multiple datasets.

# Diff Dataset Versions
Source: https://docs.langchain.com/langsmith/smith-api/datasets/diff-dataset-versions

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/versions/diff
Get diff between two dataset versions.

# Download Dataset Csv
Source: https://docs.langchain.com/langsmith/smith-api/datasets/download-dataset-csv

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/csv
Download a dataset as CSV format.

# Download Dataset Jsonl
Source: https://docs.langchain.com/langsmith/smith-api/datasets/download-dataset-jsonl

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/jsonl
Download a dataset as CSV format.

# Download Dataset Openai
Source: https://docs.langchain.com/langsmith/smith-api/datasets/download-dataset-openai

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/openai
Download a dataset as OpenAI Evals Jsonl format.

# Download Dataset Openai Ft
Source: https://docs.langchain.com/langsmith/smith-api/datasets/download-dataset-openai-ft

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/openai_ft
Download a dataset as OpenAI Jsonl format.

# Generate
Source: https://docs.langchain.com/langsmith/smith-api/datasets/generate

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/generate
Generate synthetic examples for a dataset.

# Get Dataset Splits
Source: https://docs.langchain.com/langsmith/smith-api/datasets/get-dataset-splits

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/splits

# Get Dataset Version
Source: https://docs.langchain.com/langsmith/smith-api/datasets/get-dataset-version

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/version
Get dataset version by as_of or exact tag.

# Get Dataset Versions
Source: https://docs.langchain.com/langsmith/smith-api/datasets/get-dataset-versions

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/versions
Get dataset versions.

# Read Comparative Experiments
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-comparative-experiments

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/comparative
Get all comparative experiments for a given dataset.

# Read Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-dataset

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}
Get a specific dataset.

# Read Dataset Share State
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-dataset-share-state

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/{dataset_id}/share
Get the state of sharing a dataset

# Read Datasets
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-datasets

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets
Get all datasets by query params and owner.

# Read Datasets Stream
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-datasets-stream

/langsmith/langsmith-platform-openapi.json get /api/v1/datasets/stream
Stream all datasets by query params and owner as JSON patches.

# Read Delta
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-delta

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/runs/delta
Fetch the number of regressions/improvements for each example in a dataset, between sessions[0] and sessions[1].

# Read Delta Stream
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-delta-stream

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/runs/delta/stream
Stream feedback deltas for multiple feedback keys.

Returns results in chunks as they become available. Each chunk contains
results for one or more feedback keys. Errors for individual chunks are
included in the response rather than failing the entire operation.

Response format (SSE):
    event: data
    data: {"feedback_deltas": {"key1": {session_id: {...}}, ...}, "errors": null}

    event: data
    data: {"feedback_deltas": {"key2": {...}}, "errors": null}

    event: end

# Read Examples With Runs
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-examples-with-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/runs
Fetch examples for a dataset, and fetch the runs for each example if they are associated with the given session_ids.

# Read Examples With Runs Grouped
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-examples-with-runs-grouped

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/group/runs
Fetch examples for a dataset, and fetch the runs for each example if they are associated with the given session_ids.

# Read Grouped Experiments
Source: https://docs.langchain.com/langsmith/smith-api/datasets/read-grouped-experiments

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/experiments/grouped
Stream grouped and aggregated experiments.

# Share Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/share-dataset

/langsmith/langsmith-platform-openapi.json put /api/v1/datasets/{dataset_id}/share
Share a dataset.

# Studio Experiment
Source: https://docs.langchain.com/langsmith/smith-api/datasets/studio-experiment

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/studio_experiment

# Unshare Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/unshare-dataset

/langsmith/langsmith-platform-openapi.json delete /api/v1/datasets/{dataset_id}/share
Unshare a dataset.

# Update Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/update-dataset

/langsmith/langsmith-platform-openapi.json patch /api/v1/datasets/{dataset_id}
Update a specific dataset.

# Update Dataset Splits
Source: https://docs.langchain.com/langsmith/smith-api/datasets/update-dataset-splits

/langsmith/langsmith-platform-openapi.json put /api/v1/datasets/{dataset_id}/splits

# Update Dataset Version
Source: https://docs.langchain.com/langsmith/smith-api/datasets/update-dataset-version

/langsmith/langsmith-platform-openapi.json put /api/v1/datasets/{dataset_id}/tags
Set a tag on a dataset version.

# Upload Csv Dataset
Source: https://docs.langchain.com/langsmith/smith-api/datasets/upload-csv-dataset

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/upload
Create a new dataset from a CSV or JSONL file.

# Upload Experiment
Source: https://docs.langchain.com/langsmith/smith-api/datasets/upload-experiment

/langsmith/langsmith-platform-openapi.json post /api/v1/datasets/upload-experiment
Upload an experiment that has already been run.

# Create directory commit
Source: https://docs.langchain.com/langsmith/smith-api/directories/create-directory-commit

/langsmith/langsmith-platform-openapi.json post /v1/platform/hub/repos/{owner}/{repo}/directories/commits
Creates a new directory commit for an agent or skill repository by applying file/link create, update, and delete operations.

# Delete directory repository
Source: https://docs.langchain.com/langsmith/smith-api/directories/delete-directory-repository

/langsmith/langsmith-platform-openapi.json delete /v1/platform/hub/repos/{owner}/{repo}/directories
Deletes an agent or skill repository and its owned child file repositories.

# Get directory contents
Source: https://docs.langchain.com/langsmith/smith-api/directories/get-directory-contents

/langsmith/langsmith-platform-openapi.json get /v1/platform/hub/repos/{owner}/{repo}/directories
Resolves the flattened file tree for an agent or skill repository at a specific commit, tag, or latest.

# Respond to Engine trial ending notice
Source: https://docs.langchain.com/langsmith/smith-api/engine-trial/respond-to-engine-trial-ending-notice

/langsmith/langsmith-platform-openapi.json post /v1/platform/engine/trial-response
Records a user's response to the Engine trial ending modal.
action must be "acknowledge", "opt_out", or "mark_seen".

# Bulk delete evaluators
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/bulk-delete-evaluators

/langsmith/langsmith-platform-openapi.json delete /v1/platform/evaluators
Delete multiple evaluators by their IDs. Returns per-item success/failure.

# Create evaluator
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/create-evaluator

/langsmith/langsmith-platform-openapi.json post /v1/platform/evaluators
Create a new LLM or code evaluator for the current workspace.

# Delete evaluator
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/delete-evaluator

/langsmith/langsmith-platform-openapi.json delete /v1/platform/evaluators/{evaluator_id}
Delete an evaluator. When delete_run_rules is true, all run rules referencing this evaluator are deleted first (same tenant). Associated llm_evaluators and code_evaluators rows are removed by foreign-key cascade when the evaluator row is deleted.

# Get evaluator
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/get-evaluator

/langsmith/langsmith-platform-openapi.json get /v1/platform/evaluators/{evaluator_id}
Retrieve a single evaluator by its ID.

# Get evaluator spend
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/get-evaluator-spend

/langsmith/langsmith-platform-openapi.json get /v1/platform/evaluators/spend
Returns per-day LLM evaluator spend for the requested 7-day period, grouped by evaluator, resource, or run rule. Exactly one of group_by, evaluator_id, session_id, or dataset_id is required. resource_id, type, and feedback_key may be supplied with group_by to narrow listing aggregations.

# List evaluators
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/list-evaluators

/langsmith/langsmith-platform-openapi.json get /v1/platform/evaluators
List evaluators for the current workspace, with optional filtering by type, name, tag, feedback key, or resource ID.

# Update evaluator
Source: https://docs.langchain.com/langsmith/smith-api/evaluators/update-evaluator

/langsmith/langsmith-platform-openapi.json patch /v1/platform/evaluators/{evaluator_id}
Update an existing evaluator's name, LLM configuration, or code configuration.

# Count Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/count-examples

/langsmith/langsmith-platform-openapi.json get /api/v1/examples/count
Count all examples by query params

# Create Example
Source: https://docs.langchain.com/langsmith/smith-api/examples/create-example

/langsmith/langsmith-platform-openapi.json post /api/v1/examples
Create a new example.

# Create Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/create-examples

/langsmith/langsmith-platform-openapi.json post /api/v1/examples/bulk
Create bulk examples.

# Delete Example
Source: https://docs.langchain.com/langsmith/smith-api/examples/delete-example

/langsmith/langsmith-platform-openapi.json delete /api/v1/examples/{example_id}
Soft delete an example. Only deletes the example in the 'latest' version of the dataset.

# Delete Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/delete-examples

/langsmith/langsmith-platform-openapi.json delete /api/v1/examples
Soft delete examples. Only deletes the examples in the 'latest' version of the dataset.

# Hard Delete Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/hard-delete-examples

/langsmith/langsmith-platform-openapi.json post /v1/platform/datasets/examples/delete
This endpoint hard deletes *all* versions of a dataset example(s).
Deletion is performed by setting inputs, outputs, and metadata to null and deleting attachment files while keeping the example ID, dataset ID, and creation timestamp.
IMPORTANT: attachment files can take up to 7 days to be deleted. inputs, outputs and metadata are nullified immediately.

# Legacy Update Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/legacy-update-examples

/langsmith/langsmith-platform-openapi.json patch /api/v1/examples/bulk
Legacy update examples in bulk. For update involving attachments, use PATCH /v1/platform/datasets/{dataset_id}/examples instead.

# Read Example
Source: https://docs.langchain.com/langsmith/smith-api/examples/read-example

/langsmith/langsmith-platform-openapi.json get /api/v1/examples/{example_id}
Get a specific example.

# Read Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/read-examples

/langsmith/langsmith-platform-openapi.json get /api/v1/examples
Get all examples by query params

# Update Example
Source: https://docs.langchain.com/langsmith/smith-api/examples/update-example

/langsmith/langsmith-platform-openapi.json patch /api/v1/examples/{example_id}
Update a specific example.

# Update Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/update-examples

/langsmith/langsmith-platform-openapi.json patch /v1/platform/datasets/{dataset_id}/examples
This endpoint allows clients to update existing examples in a specified dataset by sending a multipart/form-data PATCH request.
Each form part contains either JSON-encoded data or binary attachment files to update an example.

# Upload Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/upload-examples

/langsmith/langsmith-platform-openapi.json post /v1/platform/datasets/{dataset_id}/examples
This endpoint allows clients to upload examples to a specified dataset by sending a multipart/form-data POST request.
Each form part contains either JSON-encoded data or binary attachment files associated with an example.

# Upload Examples From Csv
Source: https://docs.langchain.com/langsmith/smith-api/examples/upload-examples-from-csv

/langsmith/langsmith-platform-openapi.json post /api/v1/examples/upload/{dataset_id}
Upload examples from a CSV file.

Note: For non-csv upload, please use
the POST /v1/platform/datasets/{dataset_id}/examples endpoint which provides more efficient upload.

# Validate Example
Source: https://docs.langchain.com/langsmith/smith-api/examples/validate-example

/langsmith/langsmith-platform-openapi.json post /api/v1/examples/validate
Validate an example.

# Validate Examples
Source: https://docs.langchain.com/langsmith/smith-api/examples/validate-examples

/langsmith/langsmith-platform-openapi.json post /api/v1/examples/validate/bulk
Validate examples in bulk.

# Create new experiment view override configuration for a dataset
Source: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/create-new-experiment-view-override-configuration-for-a-dataset

/langsmith/langsmith-platform-openapi.json post /datasets/{dataset_id}/experiment-view-overrides
Creates a new experiment view override configuration for a dataset with column display settings.
This endpoint allows you to customize how experiment results are displayed by configuring
column-specific overrides including colors, precision, and visibility.

The request must include a 'column_overrides' array with at least one override configuration.
Each column override can specify:
- column: Required field name (must start with inputs, outputs, reference_outputs, feedback, metrics, attachments, or metadata)
- color_gradient: Optional array of [number, color] tuples for numeric data visualization
- precision: Optional number (1-6) for decimal places in numeric columns
- hide: Optional boolean to control column visibility

Example request body:
{
"column_overrides": [
{
"column": "outputs.accuracy",
"color_gradient": [[0.0, "#ff0000"], [0.5, "#ffff00"], [1.0, "#00ff00"]],
"precision": 3
},
{
"column": "inputs.model_type",
"hide": false
}
]
}

This operation fails if an override already exists for the dataset (use PATCH to update).

# Delete experiment view override configuration
Source: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/delete-experiment-view-override-configuration

/langsmith/langsmith-platform-openapi.json delete /datasets/{dataset_id}/experiment-view-overrides/{id}
Permanently deletes an experiment view override configuration for a dataset.
This operation removes all column override settings including color gradients,
precision configurations, and visibility settings.

After deletion, the experiment view will revert to default column display settings.
This action cannot be undone - you will need to recreate the override configuration
if you want to restore custom column settings.

Both the dataset and override must exist and be accessible by the authenticated user.
The operation will fail if the override doesn't exist or if the user doesn't have
appropriate permissions for the dataset.

# Get experiment view override configuration by specific ID
Source: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/get-experiment-view-override-configuration-by-specific-id

/langsmith/langsmith-platform-openapi.json get /datasets/{dataset_id}/experiment-view-overrides/{id}
Retrieves a specific experiment view override configuration using both dataset ID and override ID.
This endpoint provides more precise access to experiment view overrides when you have
the specific override ID, useful for direct links or cached references.

The response includes the same column override information as the dataset-level endpoint:
- Column identifiers with validation prefixes
- Color gradient settings for numeric data visualization
- Numeric precision configurations
- Column visibility controls

Both the dataset and override must exist and be accessible by the authenticated user.

# Get experiment view override configurations for a dataset
Source: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/get-experiment-view-override-configurations-for-a-dataset

/langsmith/langsmith-platform-openapi.json get /datasets/{dataset_id}/experiment-view-overrides
Retrieves all experiment view override configurations for a specific dataset.
This endpoint returns column display overrides including color gradients,
precision settings, and column visibility configurations that customize how
experiment results are displayed in the UI.

The response includes all column overrides with their display settings:
- Column identifiers (must start with inputs, outputs, reference_outputs, feedback, metrics, attachments, or metadata)
- Color gradients for numeric data visualization
- Precision settings for numeric columns (1-6 decimal places)
- Hide flags to control column visibility

# Update existing experiment view override configuration
Source: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/update-existing-experiment-view-override-configuration

/langsmith/langsmith-platform-openapi.json patch /datasets/{dataset_id}/experiment-view-overrides/{id}
Updates an existing experiment view override configuration by completely replacing
the column overrides for the specified dataset and override ID.

This endpoint performs a complete replacement of the column overrides configuration.
All existing column overrides will be replaced with the new configuration provided
in the request body. To add or modify individual columns, include the complete
desired configuration in the request.

The request format is identical to the create endpoint:
- column_overrides: Required array with at least one override configuration
- Each override can specify color gradients, precision, and visibility

Example request body:
{
"column_overrides": [
{
"column": "metrics.f1_score",
"color_gradient": [[0.0, "#ff4444"], [0.8, "#44ff44"]],
"precision": 4
},
{
"column": "feedback.rating",
"hide": false
}
]
}

Both the dataset and override must exist and be accessible by the authenticated user.

# Evaluate Experiment Adhoc
Source: https://docs.langchain.com/langsmith/smith-api/experiments/evaluate-experiment-adhoc

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/experiments/{experiment_id}/evaluate
Evaluate an existing experiment with a specific evaluator.

This triggers immediate evaluation using the run_over_dataset approach,
processing runs in batches to handle large experiments efficiently.

# Delete default model for a feature
Source: https://docs.langchain.com/langsmith/smith-api/features/delete-default-model-for-a-feature

/langsmith/langsmith-platform-openapi.json delete /v1/platform/features/{feature}/default-model
Removes the default model for a feature in the workspace.

# Disable a model for a feature
Source: https://docs.langchain.com/langsmith/smith-api/features/disable-a-model-for-a-feature

/langsmith/langsmith-platform-openapi.json put /v1/platform/features/{feature}/disabled-models
Adds a model to the disabled list for a feature in the workspace.

# List feature configurations
Source: https://docs.langchain.com/langsmith/smith-api/features/list-feature-configurations

/langsmith/langsmith-platform-openapi.json get /v1/platform/features
Returns a consolidated view of default models and disabled models per feature for the workspace.

# Re-enable a disabled model for a feature
Source: https://docs.langchain.com/langsmith/smith-api/features/re-enable-a-disabled-model-for-a-feature

/langsmith/langsmith-platform-openapi.json delete /v1/platform/features/{feature}/disabled-models/{model}
Removes a model from the disabled list for a feature in the workspace.

# Set default model for a feature
Source: https://docs.langchain.com/langsmith/smith-api/features/set-default-model-for-a-feature

/langsmith/langsmith-platform-openapi.json put /v1/platform/features/{feature}/default-model
Sets or replaces the default model for a feature in the workspace.

# Create Feedback Config Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/feedback-configs/create-feedback-config-endpoint

/langsmith/langsmith-platform-openapi.json post /api/v1/feedback-configs

# Delete Feedback Config Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/feedback-configs/delete-feedback-config-endpoint

/langsmith/langsmith-platform-openapi.json delete /api/v1/feedback-configs
Soft delete a feedback config by marking it as deleted.

The config can be recreated later with the same key (simple reuse pattern).
Existing feedback records with this key will remain unchanged.

# List Feedback Configs Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/feedback-configs/list-feedback-configs-endpoint

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback-configs

# Update Feedback Config Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/feedback-configs/update-feedback-config-endpoint

/langsmith/langsmith-platform-openapi.json patch /api/v1/feedback-configs

# Create Feedback
Source: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback

/langsmith/langsmith-platform-openapi.json post /api/v1/feedback
Create a new feedback.

# Create Feedback Formula Ep
Source: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-formula-ep

/langsmith/langsmith-platform-openapi.json post /api/v1/feedback/formulas
Create a new feedback formula

# Create Feedback Ingest Token
Source: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-ingest-token

/langsmith/langsmith-platform-openapi.json post /api/v1/feedback/tokens
Create a new feedback ingest token.

# Create Feedback With Token Get
Source: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-with-token-get

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback/tokens/{token}
Create a new feedback with a token.

# Create Feedback With Token Post
Source: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-with-token-post

/langsmith/langsmith-platform-openapi.json post /api/v1/feedback/tokens/{token}
Create a new feedback with a token.

# Delete Feedback
Source: https://docs.langchain.com/langsmith/smith-api/feedback/delete-feedback

/langsmith/langsmith-platform-openapi.json delete /api/v1/feedback/{feedback_id}
Delete a feedback.

# Delete Feedback Formula Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/feedback/delete-feedback-formula-endpoint

/langsmith/langsmith-platform-openapi.json delete /api/v1/feedback/formulas/{feedback_formula_id}
Delete a feedback formula by id

# Eagerly Create Feedback
Source: https://docs.langchain.com/langsmith/smith-api/feedback/eagerly-create-feedback

/langsmith/langsmith-platform-openapi.json post /api/v1/feedback/eager
Create a new feedback.

This method is invoked under the assumption that the run
is already visible in the app, thus already present in DB

# Get Feedback Formula Ep
Source: https://docs.langchain.com/langsmith/smith-api/feedback/get-feedback-formula-ep

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback/formulas/{feedback_formula_id}
Get a feedback formula by id

# List Feedback Formula Ep
Source: https://docs.langchain.com/langsmith/smith-api/feedback/list-feedback-formula-ep

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback/formulas
List feedback formulas for a given dataset or tracing project

# List Feedback Ingest Tokens
Source: https://docs.langchain.com/langsmith/smith-api/feedback/list-feedback-ingest-tokens

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback/tokens
List all feedback ingest tokens for a run.

# Read Feedback
Source: https://docs.langchain.com/langsmith/smith-api/feedback/read-feedback

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback/{feedback_id}
Get a specific feedback.

# Read Feedbacks
Source: https://docs.langchain.com/langsmith/smith-api/feedback/read-feedbacks

/langsmith/langsmith-platform-openapi.json get /api/v1/feedback
List all Feedback by query params.

# Update Feedback
Source: https://docs.langchain.com/langsmith/smith-api/feedback/update-feedback

/langsmith/langsmith-platform-openapi.json patch /api/v1/feedback/{feedback_id}
Replace an existing feedback entry with a new, modified entry.

# Update Feedback Formula Ep
Source: https://docs.langchain.com/langsmith/smith-api/feedback/update-feedback-formula-ep

/langsmith/langsmith-platform-openapi.json put /api/v1/feedback/formulas/{feedback_formula_id}
Update a feedback formula

# Create a gateway policy
Source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/create-a-gateway-policy

/langsmith/langsmith-platform-openapi.json post /v1/platform/gateway-policies
Creates a gateway policy for the calling organization.

**policy_type** is one of `spend_cap`, `default_spend_cap`, or
`guard`. The shape of `config` depends on policy_type:
- `spend_cap` / `default_spend_cap`:
`{"window": "hourly"|"daily"|"weekly"|"monthly", "limit_usd": <number>}`
- `guard`:
`{"version": 1, "detect": {"pii": <bool>, "secrets": <bool>}, "timeout_seconds": <number>}`
`timeout_seconds` (optional, 0.1–30) caps guard pipeline execution time; defaults to 2s.

**subject_matchers** is a list of `{key, value}` pairs.
`key` is one of `organization_id`, `workspace_id`, `user_id`,
`api_key_id`, or `run_rule_id`. Multiple matchers AND together. A
`default_spend_cap` uses `{key, value: ""}` so the runtime
materializes a per-subject child for every distinct subject
of that kind it sees in request metadata.

**action** is currently always `block`. Spend caps reject the
request with 402 when the limit is hit; guard policies redact
matched content in-place before forwarding upstream.

**Upsert by matchers:** if a policy with the same
`subject_matchers` already exists in this organization, the
existing policy is updated in place instead of a duplicate
being created. `id` is preserved. Returns 201 either way.

# Delete a gateway policy
Source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/delete-a-gateway-policy

/langsmith/langsmith-platform-openapi.json delete /v1/platform/gateway-policies/{id}
Deletes a gateway policy. Subsequent reads return 404.

**default_spend_cap cascade:** deleting a `default_spend_cap`
also deletes every child policy materialized from it.

# Get a gateway policy
Source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/get-a-gateway-policy

/langsmith/langsmith-platform-openapi.json get /v1/platform/gateway-policies/{id}
Returns a single gateway policy by id. Cross-org access is
rejected with 404

**Spend tracking:** spend-cap policies include
`current_spend_usd` for the active window so callers can
read per-policy cost without hitting a separate endpoint.
Guard policies leave it null.

# List gateway policies
Source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/list-gateway-policies

/langsmith/langsmith-platform-openapi.json get /v1/platform/gateway-policies
Returns every gateway policy in the current organization.
The response includes both admin-created policies and
runtime-materialized children of `default_spend_cap`
policies (children carry `parent_policy_id`).

**Spend tracking:** each spend-cap policy carries
`current_spend_usd` — the spend accumulated in the policy's
active window.

# Update a gateway policy
Source: https://docs.langchain.com/langsmith/smith-api/gateway-policies/update-a-gateway-policy

/langsmith/langsmith-platform-openapi.json patch /v1/platform/gateway-policies/{id}
Partially updates a gateway policy. Only fields present in
the request body are applied; absent fields are left
unchanged. `policy_type` is immutable — to change a
policy's type, delete it and create a new one.

**config** if supplied must match the policy's type:
- spend-cap: `{"window": ..., "limit_usd": ...}`
- guard:     `{"version": 1, "detect": {...}, "timeout_seconds": <number>}`
Mismatched shapes are rejected with 400.

**default_spend_cap cascade:** editing a `default_spend_cap`
updates the config/action/enabled/priority on every
attached child policy so the template stays the source of
truth across rollouts.

# Create hub environments model
Source: https://docs.langchain.com/langsmith/smith-api/hub_environments/create-hub-environments-model

/langsmith/langsmith-platform-openapi.json post /api/v1/hub/environments
Creates the hub environments configuration for the current tenant.

# Delete hub environments model
Source: https://docs.langchain.com/langsmith/smith-api/hub_environments/delete-hub-environments-model

/langsmith/langsmith-platform-openapi.json delete /api/v1/hub/environments/{id}
Deletes the hub environments configuration. Tenant reverts to defaults.

# List hub environments
Source: https://docs.langchain.com/langsmith/smith-api/hub_environments/list-hub-environments

/langsmith/langsmith-platform-openapi.json get /api/v1/hub/environments
Returns the hub environments model for the current tenant.
Returns 404 if no custom configuration exists.

# Update hub environments model
Source: https://docs.langchain.com/langsmith/smith-api/hub_environments/update-hub-environments-model

/langsmith/langsmith-platform-openapi.json patch /api/v1/hub/environments/{id}
Replaces the environments array on an existing model.

# Get Health Info
Source: https://docs.langchain.com/langsmith/smith-api/info/get-health-info

/langsmith/langsmith-platform-openapi.json get /api/v1/info/health
Get health information about the current deployment of LangSmith.

# Get Server Info
Source: https://docs.langchain.com/langsmith/smith-api/info/get-server-info

/langsmith/langsmith-platform-openapi.json get /api/v1/info
Get information about the current deployment of LangSmith.

# Get Agent Builder integrations settings
Source: https://docs.langchain.com/langsmith/smith-api/integrations/get-agent-builder-integrations-settings

/langsmith/langsmith-platform-openapi.json get /v1/agent-builder/integrations
Returns default policy, integration overrides, and known integrations for the current workspace.

# Update Agent Builder integrations settings
Source: https://docs.langchain.com/langsmith/smith-api/integrations/update-agent-builder-integrations-settings

/langsmith/langsmith-platform-openapi.json put /v1/agent-builder/integrations
Replaces default policy and integration overrides for the current workspace.

# [Beta] Create the issues agent for a session
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-create-the-issues-agent-for-a-session

/langsmith/langsmith-platform-openapi.json post /v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Configures the issues agent for the given tracer session and enqueues
the initial scan. Fails if an agent already exists for the session.

# [Beta] Delete the issues agent for a session
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-delete-the-issues-agent-for-a-session

/langsmith/langsmith-platform-openapi.json delete /v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Removes the agent config, its issues, and the agent-overview hub repo.

# [Beta] Get the issues agent config for a session
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-get-the-issues-agent-config-for-a-session

/langsmith/langsmith-platform-openapi.json get /v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Returns the issues agent config attached to the given tracer session.

# [Beta] List issues agent configs
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-list-issues-agent-configs

/langsmith/langsmith-platform-openapi.json get /v1/platform/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Returns every issues agent config configured for the authenticated tenant.

# [Beta] Save the agent overview for a session
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-save-the-agent-overview-for-a-session

/langsmith/langsmith-platform-openapi.json patch /v1/platform/sessions/{session_id}/issues-agent/overview
**Beta:** This endpoint is in active development and may change without notice.

Saves the issues agent overview content server-side, creating or updating
the backing private Prompt Hub repo and linking it to the issues agent config.

# [Beta] Update the issues agent config for a session
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/[beta]-update-the-issues-agent-config-for-a-session

/langsmith/langsmith-platform-openapi.json patch /v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Patches the agent config. All side effects (clearing fix fields when
the GitHub repo changes, setting agent_overview_repo_id) happen in a
single CRUD transaction. Omitted fields are left unchanged.

# Get issues-agent (Engine) LCU spend per project for the calling org
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/get-issues-agent-engine-lcu-spend-per-project-for-the-calling-org

/langsmith/langsmith-platform-openapi.json get /issues-agent/lcu-spend
Returns one flat row per (tenant, session) pair in the
caller's organization that has Engine spend in the
window, each carrying its workspace name, project
(session) name, and Engine LCU spend. The caller groups
rows by tenant for display and sums the `lcu_total`
field across items for the org-wide total (the UI tile
does both). The window defaults to the current calendar
month (UTC) and can be overridden with `start` and `end`
(RFC 3339, capped at 31 days). Hours where the rate card
did not price a (provider, model) pair are excluded from
each row's `lcu_total` and surfaced as
`lcu_unpriced_row_count` so callers can detect billing
coverage gaps without inflating the spend number.

# Roll an issues agent webhook signing secret
Source: https://docs.langchain.com/langsmith/smith-api/issues-agent/roll-an-issues-agent-webhook-signing-secret

/langsmith/langsmith-platform-openapi.json post /v1/platform/sessions/{session_id}/issues-agent/webhooks/{id}/roll-secret
Replaces the signing secret for the given issues agent webhook and returns the
updated webhook. Future deliveries are signed with the new secret immediately.

# [Beta] List issues
Source: https://docs.langchain.com/langsmith/smith-api/issues/[beta]-list-issues

/langsmith/langsmith-platform-openapi.json get /v1/platform/issues
**Beta:** This endpoint is in active development and may change without notice.

Returns issues for the authenticated tenant, optionally filtered
by session, status, severity, tag, or last modified time.

# [Beta] List viewed issues for a session
Source: https://docs.langchain.com/langsmith/smith-api/issues/[beta]-list-viewed-issues-for-a-session

/langsmith/langsmith-platform-openapi.json get /v1/platform/sessions/{session_id}/issues/views
**Beta:** Returns the issues in this session that the current
user has opened, with timestamps. Used by the UI to derive
the per-row "unread" indicator and the Engine tab badge.

# [Beta] Mark issue viewed
Source: https://docs.langchain.com/langsmith/smith-api/issues/[beta]-mark-issue-viewed

/langsmith/langsmith-platform-openapi.json post /v1/platform/issues/{id}/views
**Beta:** Records that the current user opened this issue.
Idempotent. Drives the Engine tab unread-issues badge.

# Like Repo
Source: https://docs.langchain.com/langsmith/smith-api/likes/like-repo

/langsmith/langsmith-platform-openapi.json post /api/v1/likes/{owner}/{repo}
Like a repo.

# Get Tools
Source: https://docs.langchain.com/langsmith/smith-api/mcp/get-tools

/langsmith/langsmith-platform-openapi.json get /api/v1/mcp/tools
Return MCP tools — from cache if fresh, otherwise by fetching from remote.

On cache miss, tries manifest fetch first (fast), then falls back to full
MCP handshake. Caches the result before returning.

Pass force_refresh=true to bypass the cache and always fetch from the
remote server (the result is still cached via upsert for future requests).

The ls_user_id query parameter allows service-key callers (which don't carry
ls_user_id in auth) to specify the user for per-user OAuth cache lookups.

# Invalidate Tools Cache
Source: https://docs.langchain.com/langsmith/smith-api/mcp/invalidate-tools-cache

/langsmith/langsmith-platform-openapi.json delete /api/v1/mcp/tools
Invalidate cached MCP tools for a given server URL.

Called when a tool call fails with a stale-tools error, so subsequent
requests to GET /mcp/tools will re-fetch from the remote server.

# Proxy
Source: https://docs.langchain.com/langsmith/smith-api/mcp/proxy

/langsmith/langsmith-platform-openapi.json post /api/v1/mcp/proxy

# Proxy Get
Source: https://docs.langchain.com/langsmith/smith-api/mcp/proxy-get

/langsmith/langsmith-platform-openapi.json get /api/v1/mcp/proxy

# Create vendor settings
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/create-vendor-settings

/langsmith/langsmith-platform-openapi.json post /v1/platform/mcp-vendors/{vendor_slug}/settings
Initializes vendor settings.

# Delete vendor settings
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/delete-vendor-settings

/langsmith/langsmith-platform-openapi.json delete /v1/platform/mcp-vendors/{vendor_slug}/settings
Removes vendor settings.

# Get MCP vendor
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/get-mcp-vendor

/langsmith/langsmith-platform-openapi.json get /v1/platform/mcp-vendors/{vendor_slug}
Returns vendor metadata and current settings.
