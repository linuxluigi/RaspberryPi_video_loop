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
sudo apt-get update && sudo apt-get dist-upgrade
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
echo 'deb http://linux-packages.resilio.com/resilio-sync/deb resilio-sync non-free' | sudo tee --append /etc/apt/sources.list.d/resilio-sync.list > /dev/null
wget -qO - https://linux-packages.resilio.com/resilio-sync/key.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y resilio-sync
sudo sed -i 's/WantedBy=multi-user.target/WantedBy=default.target/g' /usr/lib/systemd/user/resilio-sync.service
systemctl --user enable resilio-sync
systemctl --user start resilio-sync
```

## Install RaspberryPi_video_loop

```bash
sudo apt-get install python-dbus
sudo pip install git+git://github.com/linuxluigi/RaspberryPi_video_loop.git
```

## create a config

Create the file ```/etc/RaspberryPi_video_loop.conf``` with your directory path into it.
Important, the dir path have to end with a ```/``` !!
```bash
sudo sh -c "echo '[Dir]' > /etc/RaspberryPi_video_loop.conf"
sudo sh -c "echo 'dir = /Path/to/Your/dir!/' >> /etc/RaspberryPi_video_loop.conf"
```

### Add RaspberryPi_video_loop to autostart

```bash
sudo nano /etc/rc.local
```

Add before ```exit 0``` the start script ```/bin/sleep 15  && /usr/local/lib/python2.7/dist-packages/raspberrypi_video_loop &```

To test if the script is working fine reboot your pi ```sudo reboot``` and use 
```ps -ef | grep python``` witch will print something like:

```bash
pi@raspberrypi ps -ef | grep python
root      2055     1 10 13:47 ?        00:00:01 python /usr/local/lib/python2.7/dist-packages/raspberrypi_video_loop
```