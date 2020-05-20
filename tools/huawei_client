#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import time




#cli = ModbusClient('192.168.1.102', port=502, unit_id=0)
cli = ModbusClient('192.168.1.102', port=502)
assert cli.connect()
time.sleep(1)

#Model ID
res1 = cli.read_holding_registers(30070, 1, unit=0)
assert not res1.isError()

print("Model ID")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
print("Decoded Data")
print("%.2f" % decoded)

#Rated power
res1 = cli.read_holding_registers(30073,2, unit=0)
assert not res1.isError()
print("Rated power")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

decoded = decoder.decode_32bit_uint()
print("Decoded Data")
print("%.2f" % decoded)


#Input power
res1 = cli.read_holding_registers(32064,2, unit=0)
assert not res1.isError()
print("Input power")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_int()
print("Decoded Data")
print("%.2f" % decoded)

#Power grid voltage
res1 = cli.read_holding_registers(32066,1, unit=0)
assert not res1.isError()
print("Power grid voltage")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Decoded Data")
print("%.2f" % decoded)

#Phase A
res1 = cli.read_holding_registers(32069,1, unit=0)
assert not res1.isError()
print("Phase A")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_16bit_uint()
print("-" * 30)
print("Decoded Data")
print("%.2f" % decoded)
