# eco_modbus_tcp

<img src="https://github.com/iotlibre/EcoPower/blob/master/docs/ecopower_equipo.png" align="right">
EcoModbusTCP esta pensado para acceder a las medidas de los inversores que son instalados para aprovechar la energía solar
Este software esta hecho en Python mas concretamente en Python3 y complementa a otros sistemas de medida para la monitorización y el control energético de una vivienda o empresa. El software puede correr en cualquier servidor que tenga acceso al Inversor aconsejándose el uso de una Raspberry

## Descripción de los ficheros
Los directorios y ficheros que se incluyen son:
client_modbus_tcp
- logs
tools









## Puesta a punto
La puesta a punto de EcoPower consta de dos partes:
- La configuración en la instalación
- El firmware de Arduino

### La configuración en la instalación
En este punto se definen los parámetros del servidor de destino y la wifi local a la que va a estar conectado el dispositivo. Con este fin, la primera vez que se ponga en servicio el ESP y siempre que no encuentre la WIFI configurada, el ESP 8266 12E creará su propio punto de acceso, su propia red WIFI . Conectandose a cualquier dirección a través de este punto de acceso nos aparecerá la página de configuración del ESP. Tengase en cuenta que una  vez configurado el ESP y conectado a una red WIFI el router le asignará una única dirección IP a la que será necesario acceder para cambiar la configuración.

En caso de que se quiera actualizar el firmware del ESP a la última versión, este se puede encontrar en: [EcoPower-emonESP ](https://github.com/iotlibre/20180328_EmonESP)

### El firmware de Arduino
El firmware que que esta cargado por defecto en el arduino nano funciona correctamente para tranformadores de intensidad de 100A/50mA sin embargo, si quiere cambiar la configuración puede encontrar la última actualización del firmware en este repositorio:[EcoPower-iotpow_serial ](https://github.com/iotlibre/EcoPower/tree/master/firmware/iotpower_serial/iotpow_serial)
