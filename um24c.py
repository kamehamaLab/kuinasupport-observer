
import serial

h = serial.Serial("/dev/ttyS5",baudrate=9600,timeout=0.5)

h.write(b"\xf0")
rx = h.readline()

#raw data
print(f'0x{rx[2]:02x}{rx[3]:02x}')
print(f'0x{rx[4]:02x}{rx[5]:02x}')

v = float(rx[2]<<8|rx[3])/100.0
i = float(rx[4]<<8|rx[5])/1000.0
w = v * i

print(f'V:{v:.2f} [V]')
print(f'I:{i:.3f}[A]')
print(f'W:{w:.2f} [W]')

h.close()

while True:
    h = serial.Serial("/dev/ttyS5",baudrate=9600,timeout=0.5)
    h.write(b"\xf0")
    rx = h.readline()
    v = float(rx[2]<<8|rx[3])/100.0
    i = float(rx[4]<<8|rx[5])/1000.0
    w = v * i
    with open('Logs/BatteryLog.csv', 'a') as f:
        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y_%m_%d-%H_%M_%S')
        writer = csv.writer(f)
        writer.writerow([dt_now_str, str(data)])
        #print("save temp")