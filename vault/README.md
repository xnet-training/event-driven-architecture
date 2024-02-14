# Configuracion de Servicios

```sh
export VAULT_TOKEN=hvs.uLgB01seI1fahvoEpxoSmv6b 
export VAULT_ADDR=http://172.17.8.220:8200
```

## Habilitación del servicio

```sh
vault secrets enable rabbitmq
```

## Configuración de conexión con RabbitMQ

```sh
vault write \
  rabbitmq/config/connection \
  connection_uri="http://172.17.8.220:15672" \
  username=admin \
  password=admin
```

Se obtiene como resultado exitoso lo siguiente.

```txt
Success! Data written to: rabbitmq/config/connection
```

## Definición del Role

```sh
vault write rabbitmq/roles/app \
  vhosts='{"default":{"configure": ".*", "write": ".*", "read": ".*"}}' \
  vhost_topics='{"default": {"amq.topic": {"write": ".*", "read": ".*"}}}'
```

  tags='administrator'
```

## Establecimiento de tiempo de vigencia de credenciales

> se expresan en segundos. El ttl = 24 horas * 60 minutos * 60 segundos = 86400 y max_ttl para 7 dias

```sh
vault write rabbitmq/config/lease ttl=86400 max_ttl=604800
```

## Generar credencial

```sh
vault read rabbitmq/creds/app
```

Se genera una nueva credencial para acceder a RabbitMQ

```sh
Key                Value
---                -----
lease_id           rabbitmq/creds/app/CYhjQhPHZqIytHUcBWnT3jdv
lease_duration     768h
lease_renewable    true
password           YKrWGfZ5imIUxOqWzdZbuprdWJTuXX32UKIF
username           root-acf86dc6-478a-6d96-592b-ad10912a6769
```
