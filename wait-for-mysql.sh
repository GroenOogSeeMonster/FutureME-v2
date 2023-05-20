#!/bin/sh
# wait-for-mysql.sh

set -e

host="$1"
shift
cmd="$@"

# Wait for the DB to be ready
python db_check.py "mysql://fmsa:fmsa-1598753@db/futureme"

>&2 echo "MySQL is up - executing command"
echo $SQLALCHEMY_DATABASE_URI
exec $cmd