# Optional TLS overrides (only needed when you must pin certs or tweak SNI)
temporal --profile prod config set --prop tls.server_name --value "<namespace_id>.<account_id>"
temporal --profile prod config set --prop tls.ca_cert_path --value "/path/to/ca.pem"
