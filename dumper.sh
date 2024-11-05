#!/bin/bash
set -e

# load CONTAINER_NAME and POSTGRES_USER from .env
source ./.env

BACKUP_DIR="/var/pg_dump"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

BACKUP_FILE="$BACKUP_DIR/${CONTAINER_NAME}_$TIMESTAMP.dump"

mkdir -p "$BACKUP_DIR"

echo "Dumping..."
docker exec -t "$CONTAINER_NAME" pg_dump -U "$POSTGRES_USER" -Fc > "$BACKUP_FILE"

# Optional: Remove backups older than 7 days
echo "Remove backups older than 7 days"
find "$BACKUP_DIR" -type f -name "*.dump" -mtime +7 -exec rm {} \;

echo "Loading to s3"
./venv/bin/python dumper.py $BACKUP_FILE

echo "Success!"
