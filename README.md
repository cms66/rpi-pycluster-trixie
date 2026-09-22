# rpi-pycluster-trixie
Python setup and management for a home RPi cluster (64-bit Debian Trixie).

## Assumptions
- Router is configured with reserved IP addresses. My example uses
  - Nodes - LAN = 192.168.1.1 to 192.168.1.99
  - Nodes - WiFi = 192.168.1.100 to 192.168.1.199
  - Other devices = 192.168.1.200 to 192.168.1.253
  - Router = 192.168.1.254

## First setup
- Burn image (latest 64 bit Lite version) using Raspberry Pi Imager or similar
- Remount drive (if needed)
- Create files in visible partition
  - hosts.txt (add entries for nodes in your cluster)
```
192.168.1.1   pinode-1  pinode-1.local 
```
  - custom.conf (add/modify following lines)
```
  wificountry=mycountry
  wifissid=myssid
  wifipassword=mywifipassword
  gituser=cms66
  gitrepo=rpi-pycluster-trixie
  gitlocaldir=/data/current/src/git
  defsysdir=/usr/local
  defdatadir=/data/current
  cams=("imx708" "imx219" "ov5647")
  subnet=192.168.1.0/24
```

- Login as created user and run 

```
wget https://raw.githubusercontent.com/cms66/rpi-pycluster-trixie/main/setup.py; sudo python ./setup.py
```
A reboot is recommended, otherwise reload bash

```
source .bashrc
```

You can then use bash aliases
- mps (Setup menu)
- mvp (Activate python Virtual Environment)
- dvp (Deactivate python Virtual Environment)
- spr (Reboot)
- spo (Poweroff)


