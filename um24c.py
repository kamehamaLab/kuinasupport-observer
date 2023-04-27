from time import sleep
import serial
import sys

rfcomm = serial.Serial("/dev/rfcomm0",baudrate=9600,timeout=0.5)


while True:
    rfcomm.write([0xf0])
    rx = rfcomm.read(130)
    if (sys.getsizeof(rx) < 130): continue
    print(rx)
    v = float(rx[2]<<8|rx[3])/100.0
    i = float(rx[4]<<8|rx[5])/1000.0
    w = v * i
    print(v)
    with open('Logs/BatteryLog.csv', 'a') as f:
        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y_%m_%d-%H_%M_%S')
        writer = csv.writer(f)
        writer.writerow([dt_now_str, str(v), str(i), str(w)])
    sleep(3)
rfcomm.close()
