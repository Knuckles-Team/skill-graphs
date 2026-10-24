# Validate required environment variables
: "${ES_SCHEME:?ERROR: ES_SCHEME environment variable is required}"
: "${ES_HOST:?ERROR: ES_HOST environment variable is required}"
: "${ES_PORT:?ERROR: ES_PORT environment variable is required}"
: "${ES_VISIBILITY_INDEX:?ERROR: ES_VISIBILITY_INDEX environment variable is required}"
: "${ES_VERSION:?ERROR: ES_VERSION environment variable is required}"

: "${MYSQL_SEEDS:?ERROR: MYSQL_SEEDS environment variable is required}"
: "${MYSQL_USER:?ERROR: MYSQL_USER environment variable is required}"

echo 'Starting MySQL and Elasticsearch schema setup...'
echo 'Waiting for MySQL port to be available...'
nc -z -w 10 ${MYSQL_SEEDS} ${DB_PORT:-3306}
echo 'MySQL port is available'
