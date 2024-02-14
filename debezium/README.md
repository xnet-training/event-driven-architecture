

# Configuraicon

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


