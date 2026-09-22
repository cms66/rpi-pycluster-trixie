# rpi-pycluster-trixie
Python setup and management for a home RPi cluster (Debian Trixie).

## Assumptions
- Router is configured with reserved IP addresses for nodes.

## First setup
- Burn image
- Create files in visible partition
  - hosts.txt (add entries for nodes in your cluster)

```
192.168.1.1   pinode-1  pinode-1.local 
```

  - custom.conf (add/modify following lines)

```
  wificountry=GB
  wifissid=
  wifipassword=
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
