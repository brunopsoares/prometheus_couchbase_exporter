#!/bin/sh

set -e

echo "Waiting for couchbase to be available at ${COUCHBASE_HOST}:${COUCHBASE_PORT}..."
until curl -s -o /dev/null http://${COUCHBASE_HOST}:${COUCHBASE_PORT}/pools -u ${COUCHBASE_USERNAME}:${COUCHBASE_PASSWORD}
do
  echo "Waiting for couchbase to be available at ${COUCHBASE_HOST}:${COUCHBASE_PORT}..."
  sleep 1
done

exec "$@"
