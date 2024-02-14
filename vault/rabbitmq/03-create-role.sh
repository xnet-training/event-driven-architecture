#!/usr/bin/env sh

curl \
    --header "X-Vault-Token: $VAULT_TOKEN "\
    --request POST \
    --data @03-rabbitmq-role.json \
    $VAULT_ADDR/v1/rabbitmq/roles/app
