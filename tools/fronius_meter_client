#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


#cli = ModbusClient('127.0.0.1', port=5020)
#cli = ModbusClient('192.168.1.131', port=5020)
#cli = ModbusClient('192.168.1.133', port=5020)
cli = ModbusClient('192.168.1.134', port=502)
assert cli.connect()



#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40069, count=1, unit=240)
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
print("F_Active_State_Code")
print("%.2f" % decoded)

# fin de la consulta

####################
# AC Power value
####################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40097, count=2, unit=240)
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
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("AC Power value")
print("%.2f" % decoded)

# fin de la consulta

####################
# Total Watt-hours Exported
####################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40129, count=2, unit=240)
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
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total Watt-hours Exported")
print("%.2f" % decoded)

# fin de la consulta

####################
# Total Watt-hours Imported
####################

#res = cli.read_input_registers(30002, count=3, unit=1)
res1 = cli.read_holding_registers(40137, count=2, unit=240)
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
#decoded = decoder.decode_16bit_uint()
decoded = decoder.decode_32bit_float()

print("-" * 30)
print("Total Watt-hours Imported")
print("%.2f" % decoded)

# fin de la consulta

    
    
