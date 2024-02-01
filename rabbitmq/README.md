# Messaging Middleware

## Instalación y Configuración (Instancia Única)

```sh
docker compose up -d
```

## Roles (tags)

|Role|Alcance|
|-|-|
|(none)|No access to the management plugin|
|management|Todo lo que se permite sobre protocolos de mensajes, pero además listar vhosts, ver colas, exchanges y bindings, ver y cerrar su propios canales y conexiones, ver estadísticas globales|
|policymaker|Incluye `management`, perdo además administrar politicas y parámetros de vhosts|
|monitoring|Incluye `management, pero además ver vhosts, conexiones, canales, uso de memoria, clusterizacion y estadístocas|
|administrator|Incluye `policymaker` y `monitoring`, pero además gestionar vhosts, usuarios, permisos y conexiones|
