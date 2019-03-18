#!bin/bash

cd /
sudo rfcomm watch hci0 1 getty rfcomm0 1151200 vt100 -a pi &
cd /home/pi/Desktop/Pinaso/
sudo python3 pinaso.py
cd /
