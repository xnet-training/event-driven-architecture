#!/usr/bin/env sh

curl \
    --header "X-Vault-Token: $VAULT_TOKEN "\
    --request POST \
    --data @02-rabbitmq-connection.json \
    $VAULT_ADDR/v1/rabbitmq/config/connection
