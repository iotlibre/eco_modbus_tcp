
#!/usr/bin/env python
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import time

#cli = ModbusClient('192.168.1.102', port=502, unit_id=0)
cli = ModbusClient('192.168.3.10', port=502)
assert cli.connect()
time.sleep(1)

#Epoch seconds UTC
res1 = cli.read_holding_registers(40000, 2, slave=0)
assert not res1.isError()

print("Epoch seconds UTC")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_uint()
print("Decoded Data")
print("%.2f" % decoded)

#DST
res1 = cli.read_holding_registers(40004, 1, slave=0)
assert not res1.isError()

print("Data Time Saving")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_16bit_uint()
print("Decoded Data")
print("%.2f" % decoded)

#City
res1 = cli.read_holding_registers(40002, 2, slave=0)
assert not res1.isError()

print("city")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_uint()
print("Decoded Data")
print("%.2f" % decoded)

#Time zone offset
res1 = cli.read_holding_registers(40005, 2, slave=0)
assert not res1.isError()

print("Time zone offset")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_uint()
print("Decoded Data")
print("%.2f" % decoded)

#Local time
res1 = cli.read_holding_registers(40009, 2, slave=0)
assert not res1.isError()

print("Local Time")
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_uint()
print("Decoded Data")
print("%.2f" % decoded)
