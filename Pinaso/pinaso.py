#!/usr/bin/python3
import FaBo9Axis_MPU9250
import time
import sys
import shlex, subprocess
#from bluedot import BlueDot
#from bluedot.btcomm import BluetoothServer
from signal import pause
#import gps

#def client_connect():
mpu9250 = FaBo9Axis_MPU9250.MPU9250()
print("Funciona Cojonudamente")

try:
    while True:
        gyro = mpu9250.readGyro()
        gx = float ( gyro['x'] )
        gy = float ( gyro['y'] )
        gz = float ( gyro['z'] )
        cont = int(0)
        print(gx,gy,gz)
        if ( gx > 180 or gx < -180 ):
            cont += 1
        if ( gy > 180 or gy < -180 ):
            cont += 1
        if ( gz > 180 or gz < -118 ):
            cont += 1
        if cont >= 2:
            subprocess.call(shlex.split('sudo echo "pinaso">/dev/rfcomm0'))
            archivo = open ("/dev/rfcomm0","w")
            archivo.write("pinaso")
            archivo.close()
            exit()
        time.sleep(0.5)
except KeyboardInterrupt:
    sys.exit()

#bd = BlueDot()
#bd.wait_for_connection(60)
#bd.when_client_connects = client_connect
pause()
