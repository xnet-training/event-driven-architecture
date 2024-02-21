
# Iniciar Debezium

```sh
docker compose -f docker-compose-v3.yml up -d
```

# Configuraicon

## MySQL

```sql
GRANT RELOAD, SUPER, REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'microservicio'@'%' IDENTIFIED BY 'secr3t!';
```

## Registro del Conector

```sh
curl -X POST -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  http://0.0.0.0:28083/connectors \
  -d @mysql-connector.json
```

## Listar los conectores registrados

```sh
curl -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  http://0.0.0.0:28083/connectors
```

## Eliminar conector

```sh
curl -X DELETE http://0.0.0.0:28083/connectors/partyreferencedata-connector
```

## Prueba de la Configuracion

> El password es `secr3t!`

```sh
docker exec -it dev-environment-db-1 mysql -u microservice -p
```

```sql
insert partyreferencedata.tb_outbox values('11111111-1111-1111-11111111-1111',
  'ConsumerLoan','1234567890','ConsumerLoanApproved',
  '{"CustomerId": "1234567666", "Ammount": 6}');
```
