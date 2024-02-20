

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

```sql
insert into tb_outpost values('LoanRejected','1234567','{"account": "1234-3234-2334-2345"}');
```
