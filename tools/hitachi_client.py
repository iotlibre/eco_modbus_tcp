#!/usr/bin/env python
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


cli = ModbusClient('192.168.3.141', port=502)
assert cli.connect()

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1000, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de unidad Marcha/Paro")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1001, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de unidad de modo")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1002, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1 de Marcha/Paro")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1003, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1 OTC para calefacción")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1004, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1 OTC para enfriamiento")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1005, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control circuito 1: Temperatura de ajuste fija para calentamiento de agua")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1006, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control circuito 1: Temperatura de ajuste fija para enfriamiento de agua")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1007, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1: modo ECO")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1008, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1: temperatura de compensación ECO de calefacción")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1009, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1: temperatura de compensación ECO de enfriamiento (*2)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1010, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1: termostato disponible (*7)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1011, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control de circuito 1: termostato de la temperatura de ajuste")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1024, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control del depósito de ACS Marcha/Paro")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1025, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control consigna del depósito ACS")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1026, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control impulso de ACS")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1027, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control modo de demanda de ACS")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1030, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control Antilegionela Marcha (*9)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1031, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control Antilegionela consigna")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1032, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control Bloqueo/Desbloqueo Menú (*6)")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1033, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control Alarma del BMS (*4)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1050, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
print("-" * 30)
print("Estado de la unidad marcha/paro (marcha = 1) (1050)")
print("%.2f" % decoded)

# fin de la consulta




#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1051, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado unidad modo")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1052, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de circuito 1 Marcha/Paro")
print("%.2f" % decoded)

# fin de la consulta




#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1053, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado calefacción OTC circuito 1")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1054, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado modo OTC enfriamiento circuito 1 (*2)")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1055, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado circuito 1: Temperatura de ajuste fija para calentamiento de agua")
print("%.2f" % decoded)

# fin de la consulta
#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1056, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado circuito 1: Temperatura de ajuste fija para enfriamiento de agua (*2)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1057, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado del circuito 1: modo ECO")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1058, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de circuito 1: temperatura de compensación ECO de calefacción")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1059, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de circuito 1: temperatura de compensación ECO de enfriamiento (*2)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1060, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de circuito 1: termostato de la temperatura de ajuste")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1061, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de circuito 1: termostato de la temperatura de la habitación")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1076, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado depósito ACS Marcha/Paro")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1077, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado depósito ACS consigna")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1078, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Control impulso de ACS")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1079, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado modo de demanda de ACS")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1080, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado temperatura ACS")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1084, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado Antilegionela Marcha")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1085, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado Antilegionela consigna")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1086, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Estado Bloqueo/Desbloqueo Menú (*6)")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("sustituir")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1087, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado alarma BMS")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1088, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Modo central")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1089, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Configuración del sistema")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1090, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de operación")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1091, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Temperatura ambiente exterior")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1092, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Temperatura de entrada agua")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
#############################

res1 = cli.read_holding_registers(1000, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("sustituir")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(1093, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Temperatura Salida Agua")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(1094, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Estado de comunicación H-LINK (0: sin alarma)")
print("%.2f" % decoded)

# fin de la consulta




#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1097, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Capacidad de la unidad")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1098, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Consumo energético de la unidad")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1200, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Temperatura de salida del agua de la bomba de calor")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1201, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Ta2: Temperatura ambiente media de la unidad exterior")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1204, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("O2: Temperatura de salida del agua 2 (Two2)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1205, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("O3: Temperatura de salida del agua 3 (Two3)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1206, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Tg: Temperatura del gas (THMg)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1207, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("TI: Temperatura del líquido (THMI)")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1208, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Td: Temperatura del gas de descarga")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1209, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Te: Temperatura de evaporación")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1210, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("EVI: Apertura de la válvula de expansión interior")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1211, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("EVO: Válvula de expansión exterior (0~100) %")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1212, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("H4: Frecuencia de funcionamiento del inverter")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1213, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("DI: Causa de la parada")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1214, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("P1: Corriente de funcionamiento del compresor")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1216, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("MVP: Posición de la válvula mixta")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1217, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Descarche")
print("%.2f" % decoded)

# fin de la consulta


#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1219, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Th: Ajuste de la temperatura del agua (Ttwo)")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1220, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Caudal de agua")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1221, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Velocidad de la bomba de agua")
print("%.2f" % decoded)

# fin de la consulta




#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1222, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Estado del sistema 2")
print("%.2f" % decoded)

# fin de la consulta



#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1223, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Número de alarma")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1224, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Temperatura de descarga R134a")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1225, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Temperatura de aspiración R134a")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1226, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Presión de descarga R134a")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1227, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Presión de aspiración R134a")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1228, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Frecuencia del compresor R134a")
print("%.2f" % decoded)

# fin de la consulta

#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1229, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Apertura de la válvula 2 de expansión interior R134a")
print("%.2f" % decoded)

# fin de la consulta
#############################
# Inicio de la consulta
##############################

res1 = cli.read_holding_registers(1230, count=1, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Valor actual del compresor R134a")
print("%.2f" % decoded)

# fin de la consulta














































































