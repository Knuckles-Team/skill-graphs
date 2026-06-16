# Validate required environment variables
: "${MYSQL_SEEDS:?ERROR: MYSQL_SEEDS environment variable is required}"
: "${MYSQL_USER:?ERROR: MYSQL_USER environment variable is required}"

echo 'Starting MySQL schema setup...'
echo 'Waiting for MySQL port to be available...'
nc -z -w 10 ${MYSQL_SEEDS} ${DB_PORT:-3306}
echo 'MySQL port is available'
