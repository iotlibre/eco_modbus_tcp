#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

cli = ModbusClient('192.168.0.101', port=1502)
assert cli.connect()

####################
res1 = cli.read_holding_registers(4, count=1, unit=71)
assert not res1.isError()
print("-" * 30)
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Unit-ID")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(5, count=1, unit=71)
assert not res1.isError()
print("-" * 30)
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("MODBUS Byte Order")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(100, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total DC power")
print("%.2f" % decoded)


####################
res1 = cli.read_holding_registers(108, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()
print("-" * 30)
print("Consumption from grid")
print("%.2f" % decoded)


####################
res1 = cli.read_holding_registers(112, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total home consumption Grid")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(114, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total home consumption PV")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(118, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total home consumption")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(152, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Grid frequency")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(172, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total AC active power")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(320, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total yield")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(575, count=1, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_16bit_int()

print("-" * 30)
print("Inverter Generation Power")
print("%.2f" % decoded)

####################
res1 = cli.read_holding_registers(577, count=2, unit=71)
assert not res1.isError()
print("-" * 30)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Little)
decoded = decoder.decode_32bit_uint()

print("-" * 30)
print(" Generation Energy")
print("%.2f" % decoded)