# Create and setup temporal database
temporal-sql-tool --plugin mysql8 --ep ${MYSQL_SEEDS} -u ${MYSQL_USER} -p ${DB_PORT:-3306} --db temporal create
temporal-sql-tool --plugin mysql8 --ep ${MYSQL_SEEDS} -u ${MYSQL_USER} -p ${DB_PORT:-3306} --db temporal setup-schema -v 0.0
temporal-sql-tool --plugin mysql8 --ep ${MYSQL_SEEDS} -u ${MYSQL_USER} -p ${DB_PORT:-3306} --db temporal update-schema -d /etc/temporal/schema/mysql/v8/temporal/versioned
