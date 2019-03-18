# Pinaso_V.1
ASIR
sudo nano /lib/systemd/bluetooth.service
ExcecStart=/usr/lib/bluetooth/bluetoothd -C
ExecStartPost=/usr/bin/sdptool add SP
ExecStartPost=/bin/hciconfig hci0 piscan
crt+x
crontab -e
@rebbot sudo bash /home/pi/Desktop/Pinaso/pinaso.sh
sudo raspi-config
#I2C should be enabled
