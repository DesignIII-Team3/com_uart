import serial

ser = serial.Serial( port="COM6",
                     baudrate=19200,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE)

"""
total = 0
i = 1

while(1):

    value = int(ser.readline().decode())

    #converted_value = (value/pow(2, 12)) *3 *5
    total += (value/pow(2, 12)) *3 
    moyenne = total / i
    i+=1

    print(f"moyenne apres {i:4<} : {moyenne:10.4f}V", end='\r')
"""

while(1):

    value = int(ser.readline().decode())

    converted_value = (value/4095) *3 #*5
    #converted_value = ( ( (value/pow(2, 12)) *3 ) -2.3998 ) / 0.066

    print(f"tension : {converted_value:10.3f}V", end='\r')


    """
    while(ser.read(1) != b'\xff'):
        continue

    rcv_cmd = int.from_bytes(ser.read(1), "big")
    rcv_data_size = int.from_bytes(ser.read(1), "big")

    rcv_data = []
    for i in range(rcv_data_size):
        data = int.from_bytes(ser.read(1), "big")
        rcv_data.append( f"{data:02x}" )
    rcv_data.reverse()
    rcv_data = "0x"+"".join(rcv_data)



    print(f"{rcv_cmd:x} ({rcv_data_size} o) : {rcv_data:<20} = {int(rcv_data, base=16):<20}")
    """