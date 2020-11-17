#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


#cli = ModbusClient('127.0.0.1', port=5020)
#cli = ModbusClient('192.168.1.131', port=5020)
#cli = ModbusClient('192.168.1.133', port=5020)
cli = ModbusClient('192.168.1.134', port=502)
assert cli.connect()

############################
# Uniquely identifies
############################
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40069, count=1, unit=246)
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
print("Uniquely identifies")
print("%.2f" % decoded)

# fin de la consulta


################################
# Global Horizontal Irradiance #
################################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40071, count=1, unit=246)
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
print("Global Horizontal Irradiance")
print("%.2f" % decoded)

############################
# Temperatura 1
############################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40078, count=1, unit=246)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_16bit_int()
#decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Temperatura 1")
print("%.2f" % decoded)

# fin de la consulta


############################
# Temperatura 2
############################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40079, count=1, unit=246)
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
decoded = decoder.decode_16bit_int()
print("-" * 30)
print("Temperatura 2")
print("%.2f" % decoded)

# fin de la consulta

############################
# Uniquely identifies
############################
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40080, count=1, unit=246)
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
print("Uniquely identifies")
print("%.2f" % decoded)

# fin de la consulta

############################
# Ambient Temperature
############################
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40082, count=1, unit=246)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_16bit_int()

print("-" * 30)
print("Ambient Temperature")
print("%.2f" % (decoded/10))


############################
# Wind Speed
############################
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40085, count=1, unit=246)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_16bit_int()

print("-" * 30)
print("Wind Speed")
print("%.2f" % decoded)

# fin de la consulta 
