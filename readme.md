# eco_modbus_tcp

<img src="https://github.com/iotlibre/eco_modbus_tcp/blob/master/client_modbus_tcp/docs/frame.png" align="right">
EcoModbusTCP esta pensado para acceder a las los inversores solares y otros equipos que implementan MODBUS

Este software esta hecho en Python mas concretamente en Python3 y complementa a otros sistemas de medida para la monitorización y el control energético de una vivienda o empresa.

El software puede ejecutarse en cualquier servidor que implemente python aconsejándose el uso de una Raspberry Pi

## Descripción de los ficheros
Los directorios y ficheros que se incluyen son:
- client_modbus_tcp: Programa principal que pregunta el valor de las variables al dispositivo (el inversor) y lo transmite al servidor EmonCMS
- congig.ini: Fichero con todos los parámetros de funcionamiento del programa
  - emoncms: Parámetros del servidor donde se manda la información
  - Servidores modbus: Inversores u otros dispositivos de los que se recogen sus variables (bombas de calor, Smart meters ... ). Se diferencian del resto de variables porque tienen el campo 'url'
  - Registros: Variables que se leen de cada uno de los dispositivos. Se diferencian porque contienen la variable 'server'
- logs: Directorio donde se guardan los logs. La configuración de estos logs se hace en el programa principal 'client_modbus_tcp'
- tools: Herramientas para facilitar las pruebas para el desarrollo del código

## tools
Las principales herramientas son:
- server_payload: Crea un servidor para hacer pruebas desde el cliente
- server_payload_write: Graba en el servidor algunas variables para que luego puedan ser leídas desde el cliente
