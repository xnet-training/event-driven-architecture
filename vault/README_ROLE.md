

```sh
vault auth enable approle
```

```sh
vault policy write ms-policy policy.hcl
```

```sh
vault write auth/approle/role/ms1 \
  secret_id_ttl=10m \
  token_num_uses=10 \
  token_ttl=20m \
  token_max_ttl=30m \
  secret_id_num_uses=40 \
  token_policies=ms-policy
```

## Obtener el ID del Role

El role-id no es un dato sensible. Se puede almacenar en SCM, archivo de propiedades, archivo de configuración como texto plano.

```sh
MS1_ROLE_ID=$(vault read -field=role_id auth/approle/role/ms1/role-id)
```

## Obtener el Secret ID

El secret-id es un dato sensible y tiene un TTL definido es la especificación del role

```sh
MS1_SECRET_ID=$(vault write -field=secret_id -f auth/approle/role/ms1/secret-id)
```

## Obtener token a partir del secret-id

```sh
MY_TOKEN=$(vault write -field=token auth/approle/login role_id=$MS1_ROLE_ID secret_id=$MS1_SECRET_ID)
```

## Acceder a secreto

Para acceder a la información que se almacena en un secreto.

```sh
vault read -format=json secrets/data/ms1 --token=$MY_TOKEN
```

```json
{
  "request_id": "9b272b35-bef4-1512-ce48-be5b3b161c43",
  "lease_id": "",
  "lease_duration": 0,
  "renewable": false,
  "data": {
    "data": {
      "password": "welcome1",
      "username": "microservicio"
    },
    "metadata": {
      "created_time": "2024-02-17T05:03:37.876273339Z",
      "custom_metadata": null,
      "deletion_time": "",
      "destroyed": false,
      "version": 1
    }
  },
  "warnings": [
    "Endpoint ignored these unrecognized parameters: [--token]"
  ]
}
```

A modo simplificado, una consulta solo de la data del secret:

```sh
vault read -format=json -field=data secrets/data/ms1
```

```json
{
  "password": "welcome1",
  "username": "microservicio"
}
```
