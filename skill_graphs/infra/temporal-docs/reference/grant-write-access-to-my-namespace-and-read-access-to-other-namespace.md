# Grant write access to my-namespace and read access to other-namespace:
temporal cloud user set-namespace-permissions --user-id my-user-id \
  --namespace-access my-namespace.my-account=write \
  --namespace-access other-namespace.my-account=read
