# Temporal Service level Archival config
archival:
  # Event History configuration
  history:
    # Archival is enabled at the Temporal Service level
    state: 'enabled'
    enableRead: true
    # Namespaces can use either the local filestore provider or the Google Cloud provider
    provider:
      filestore:
        fileMode: '0666'
        dirMode: '0766'
      gstorage:
        credentialsPath: '/tmp/gcloud/keyfile.json'
