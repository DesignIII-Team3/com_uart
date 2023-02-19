import serial

ser = serial.Serial( port="COM6",
                     baudrate=19200,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE)

def decodeUART(p_cmd, p_data):
    data_converted = None

    if p_cmd == 0x00:  # decode lecture de tension
        data_int = int(p_data, base=16)
        data_convertded = (data_int / 4095) * 3.3 #* 6.67 

    elif p_cmd == 0x01:
        data_int = int(p_data, base=16)
        data_convertded = (((data_int / 4095)*3.3 ) -2.630 ) / 0.066
        
    return data_convertded

courant = 0
tension = 0
batterie = 5400
print(f"mesure |{'V': ^7}|{'A': ^7}|{'W': ^7}|{'%bat.': ^7}")

while(1):

    while(ser.read(1) != b'\xff'):
        #print("wait data")
        continue

    rcv_cmd = int.from_bytes(ser.read(1), "big")
    rcv_data_size = int.from_bytes(ser.read(1), "big")

    #print(f"{rcv_cmd:x} ({rcv_data_size} o)")

    rcv_data = []
    for i in range(rcv_data_size):
        data = int.from_bytes(ser.read(1), "big")
        rcv_data.append( f"{data:02x}" )
    rcv_data.reverse()
    rcv_data = "0x"+"".join(rcv_data)

    converted_value = decodeUART(rcv_cmd, rcv_data)

    if rcv_cmd == 0x00:
        tension = converted_value
    elif rcv_cmd == 0x01:
        courant = converted_value
        
        batterie -= courant
        if batterie < 0:
            batterie = 0

    #print(f"{rcv_cmd:x} ({rcv_data_size} o) : {rcv_data:<20} = {int(rcv_data, base=16):<20}")
    print(f"        {tension:^7.3f}|{courant:^7.3f}|{courant*tension:^7.3f}|{batterie/5400*100: ^7.2f}", end='\r')