#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


#cli = ModbusClient('127.0.0.1', port=5020)
#cli = ModbusClient('192.168.1.131', port=5020)
#cli = ModbusClient('192.168.1.133', port=5020)
cli = ModbusClient('192.168.1.134', port=502)
assert cli.connect()


# Inicio de la consulta F_Active_State_Code
''' La consulta muestra siempre 0'''

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(213, count=1, unit=1)
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
print("-" * 3)
print("F_Active_State_Code")
print("%.2f" % decoded)

# fin de la consulta


# Inicio de la consulta F_Site_Power

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(499, count=2, unit=1)
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
decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("F_Site_Power")
print("%.2f" % decoded)
# fin de la consulta

# Inicio de la consulta F_Site_Energy_Year
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(508, count=2, unit=1)
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
decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("F_Site_Energy_Year")
print("%.2f" % decoded)
# fin de la consulta


########################
# Meter
########################
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40069, count=2, unit=1)
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
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Meter")
print("%.2f" % decoded)
# fin de la consulta

# Inicio de la consulta AC Total Current value
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40071, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Total Current value")
print("%.2f" % decoded)
# fin de la consulta


# Inicio de la consulta AC Phase-A Current value
res1 = cli.read_holding_registers(40073, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Phase-A Current value")
print("%.2f" % decoded)
# fin de la consulta


# Inicio de la consulta AC Phase-B Current value
res1 = cli.read_holding_registers(40075, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Phase-B Current value")
print("%.2f" % decoded)
# fin de la consulta


# Inicio de la consulta AC Phase-C Current value
#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40077, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 30)
print("AC Phase-C Current value")
print("%.2f" % decoded)
# fin de la consulta

# Inicio de la consulta AC Voltage Phase-A-to-neutral value
res1 = cli.read_holding_registers(40085, count=2, unit=1)
assert not res1.isError()

print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Voltage Phase-A-to-neutral value")
print("%.2f" % decoded)
# fin de la consulta


# Inicio de la consulta AC Voltage Phase-B-to-neutral value
res1 = cli.read_holding_registers(40087, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Voltage Phase-B-to-neutral value")
print("%.2f" % decoded)
# fin de la consulta


# Inicio de la consulta AC Voltage Phase-C-to-neutral value
res1 = cli.read_holding_registers(40089, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Voltage Phase-C-to-neutral value")
print("%.2f" % decoded)
# fin de la consulta


# Inicio de la consulta
res1 = cli.read_holding_registers(40091, count=2, unit=1)
assert not res1.isError()
print("-" * 30)
print("Registros")
print(res1.registers)
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
print("-" * 3)
print("AC Power value")
print("%.2f" % decoded)
# fin de la consulta


# AC Frequency value
res1 = cli.read_holding_registers(40093, count=2, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("AC Frequency value")
print("%.2f" % decoded)
# fin de la consulta

# Apparent Power
res1 = cli.read_holding_registers(40095, count=2, unit=1)
assert not res1.isError()

decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Apparent Power")
print("%.2f" % decoded)
# fin de la consulta

# Reactive Power
res1 = cli.read_holding_registers(40097, count=2, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Reactive Power")
print("%.2f" % decoded)
# fin de la consulta

# Power Factor
res1 = cli.read_holding_registers(40099, count=2, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Power Factor")
print("%.2f" % decoded)
# fin de la consulta

# DC Power value
res1 = cli.read_holding_registers(40107, count=2, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("DC Power value")
print("%.2f" % decoded)
# fin de la consulta

# DC Current
res1 = cli.read_holding_registers(40282, count=1, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("DC Current")
print("%.2f" % decoded)
# fin de la consulta

# DC Voltage Los valores que devuelve el fronius no son correctos
res1 = cli.read_holding_registers(40283, count=1, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)

print("-" * 30)
print("Registros")
print(res1.registers)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("DC Voltage 1")
print("%.2f" % decoded)
# fin de la consulta

# DC Power (valores no correctos)
res1 = cli.read_holding_registers(40284, count=1, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
print("-" * 30)
print("Registros")
print(res1.registers)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("DC Power")
print("%.2f" % decoded)
# fin de la consulta

# Lifetime Energy
res1 = cli.read_holding_registers(40285, count=2, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
print("-" * 30)
print("Registros")
print(res1.registers)
#decoded = decoder.decode_32bit_float()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Lifetime Energy")
print("%.2f" % decoded)
# fin de la consulta

# Temperature
res1 = cli.read_holding_registers(40289, count=1, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
print("-" * 30)
print("Registros")
print(res1.registers)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Temperature")
print("%.2f" % decoded)
# fin de la consulta

# Operating State
res1 = cli.read_holding_registers(40290, count=1, unit=1)
assert not res1.isError()
decoder = BinaryPayloadDecoder.fromRegisters(res1.registers,
                                             byteorder=Endian.Big,
                                             wordorder=Endian.Big)
print("-" * 30)
print("Registros")
print(res1.registers)
#decoded = decoder.decode_32bit_float()
decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_16bit_uint()
#decoded = decoder.decode_32bit_int()
#decoded = decoder.decode_32bit_uint()
print("-" * 3)
print("Operating State")
print("%.2f" % decoded)

# fin de la consulta















