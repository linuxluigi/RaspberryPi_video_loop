# RaspberryPi_video_loop

## About

A Python Script witch autostart with the Pi and play videos in an endless loop. 
The playlist depends on the files in the selected directory.

## Prepare Raspberry Pi

### Download Image

Use the Raspbian Image, I recommended a lite version.

Download @ https://www.raspberrypi.org/downloads/raspbian/

### Copy Image on SD Card with Linux
```bash
sudo dd if=path_of_your_image.img of=/dev/sdX bs=1M && sync
```

### First log into your Pi

```bash
ssh pi@raspberrypi
```

Default User: ```pi```
Default Password: ```raspberry```

### expand filesystem

At first expand you SD Card disk size.

Officially Documentation about ```raspi-confi```: https://www.raspberrypi.org/documentation/configuration/raspi-config.md

```bash
sudo raspi-config
```

Don't forget to reboot your Pi

```bash
sudo reboot
```

### Change User Password

```bash
passwd
```

### Update the pi

```bash
sudo apt-get update && sudo apt-get -y dist-upgrade && sudo apt-get -y autoremove
```

### Activate auto security Updates

This will update your Pi daily with important security updates.

```bash
sudo apt-get install unattended-upgrades
sudo echo 'APT::Periodic::Update-Package-Lists "1";' > /etc/apt/apt.conf.d/10periodic
sudo echo 'APT::Periodic::Update-Package-Lists "1";' >> /etc/apt/apt.conf.d/10periodic
sudo echo 'APT::Periodic::Download-Upgradeable-Packages "1";' >> /etc/apt/apt.conf.d/10periodic
sudo echo 'APT::Periodic::AutocleanInterval "7";' >> /etc/apt/apt.conf.d/10periodic
sudo echo 'APT::Periodic::Unattended-Upgrade "1";' >> /etc/apt/apt.conf.d/10periodic
```

## Optional: install Resilio Sync

[Resilio Sync](https://www.resilio.com/) is an decentralized private cloud Software. 
To easy update the video Playlist from your computer or smartphone.

```bash
wget https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz
tar xfvz resilio-sync_arm.tar.gz
sudo mv rslsync /usr/bin/
rm LICENSE.TXT
rm resilio-sync_arm.tar.gz
```

Create a service for reslio sync
```bash
sudo nano /etc/init.d/rslsync
```
And add the following content.
```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides:          /usr/bin/rslsync
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start reslio sync as a damon
# Description:       start reslio sync as a damon
### END INIT INFO
 
# Actions
case "$1" in
    start)
        # START
        /bin/su - pi -c "/usr/bin/rslsync --webui.listen 0.0.0.0:8888"
        ;;
    stop)
        # STOP
        pkill rslsync
        ;;
    restart)
        # RESTART
        pkill rslsync
        /bin/su - pi -c "/usr/bin/rslsync --webui.listen 0.0.0.0:8888"
        ;;
esac
 
exit 0
```

* Make the service executable 
* Add start stop service

```bash
sudo chmod +x /etc/init.d/rslsync
sudo update-rc.d rslsync defaults
sudo reboot
```

To start, stop & restart resilio use:
```bash
sudo service rslsync start
sudo service rslsync stop
sudo service rslsync restart
```

To check if resilio sync is working fine, use ```ps -ef | grep rslsync```
```bash
root       371     1  3 14:52 ?        00:00:01 /usr/bin/rslsync --webui.listen 0.0.0.0:8888
pi         666   636  0 14:53 pts/0    00:00:00 grep --color=auto rslsync

```

## Install RaspberryPi_video_loop

```bash
sudo apt-get install python-dbus
sudo pip install --upgrade --force git+git://github.com/linuxluigi/RaspberryPi_video_loop.git
```

## create a config

Create the file ```/etc/RaspberryPi_video_loop.conf``` with your directory path into it.
Important, the dir path have to end with a ```/``` !!
```bash
sudo sh -c "echo '[Dir]' > /etc/RaspberryPi_video_loop.conf"
sudo sh -c "echo 'dir = /home/pi/Videos/' >> /etc/RaspberryPi_video_loop.conf"
```

### Add RaspberryPi_video_loop to autostart

Create a service for RaspberryPi_video_loop 

```bash
sudo apt-get install xterm
```

```bash
sudo nano /etc/init.d/video_loop
```
And add the following content.

```python /usr/local/lib/python2.7/dist-packages/raspberrypi_video_loop```

```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides:          /usr/bin/omxplayer
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start video_loop
# Description:       start video_loop
### END INIT INFO
 
# Actions
case "$1" in
    start)
        # START
        /bin/su - pi -c "/usr/bin/video_loop"
        ;;
    stop)
        # STOP
        pkill video_loop
        ;;
    restart)
        # RESTART
        pkill video_loopa
        /bin/su - pi -c "/usr/bin/video_loop"
        ;;
esac
 
exit 0
```

edit /etc/kbd/config and set BLANK_TIME=0 and POWERDOWN_TIME=0 then run /etc/init.d/kbd restart.

* Make the service executable 
* Add start stop service

```bash
sudo chmod +x /etc/init.d/video_loop
sudo update-rc.d video_loop defaults
sudo reboot
```

To start, stop & restart resilio use:
```bash
sudo service video_loop start
sudo service video_loop stop
sudo service video_loop restart
```

Add before ```exit 0``` the start script ```/bin/sleep 15  && /usr/local/lib/python2.7/dist-packages/raspberrypi_video_loop &```

To test if the script is working fine reboot your pi ```sudo reboot``` and use 
```ps -ef | grep python``` witch will print something like:

```bash
pi@raspberrypi ps -ef | grep python
root      2055     1 10 13:47 ?        00:00:01 python /usr/local/lib/python2.7/dist-packages/raspberrypi_video_loop
```