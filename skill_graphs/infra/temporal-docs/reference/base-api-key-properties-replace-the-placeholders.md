# Base API key properties (replace the placeholders)
temporal --profile prod config set --prop address --value "<region>.<cloud_provider>.api.temporal.io:7233"
temporal --profile prod config set --prop namespace --value "<namespace_id>.<account_id>"
temporal --profile prod config set --prop api_key --value "<your-api-key>"
