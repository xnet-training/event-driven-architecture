# Configuracion de Servicios

```sh
VAULT_TOKEN=hvs.uLgB01seI1fahvoEpxoSmv6b VAULT_ADDR=http://172.17.8.220:8200 vault write \
  rabbitmq/config/connection \
  connection_uri="http://172.17.8.220:15672" \
  username=admin \
  password=admin
```

Se obtiene como resultado exitoso lo siguiente.

```txt
Success! Data written to: rabbitmq/config/connection
```
