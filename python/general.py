# Python generic functions

import os
import python.variables as pvar
import python.hardware as phdw
import python.network as pnet
import python.security as psec

def read_config():
	conf = "/boot/firmware/custom.conf"
	if os.path.exists(conf):
		with open(conf) as f:
			for line in f:
				key = line.split('=')[0]
				val = line.split('=')[1]
				pvar.arrconf[key] = val

def show_config(): # TODO
	data = pvar.arrconf
	for value in data:
		print(value)
	print()
	print(pvar.arrconf['gitrepo']) # Works

def set_owner(path, user):
	id = pvar.usrid
	for root, dirs, files in os.walk(path):
		# set perms on sub-directories  
		for momo in dirs:
			os.chown(os.path.join(root, momo), id, id)
		# set perms on files
		for momo in files:
			os.chown(os.path.join(root, momo), id, id)

def update_setup():
	strdir = pvar.arrconf["gitlocaldir"] + "/" +  pvar.arrconf["gitrepo"].strip()
	gitdir = "".join(strdir.splitlines())
	strurl = "https://github.com/" +  pvar.arrconf["gituser"] + "/" +  pvar.arrconf["gitrepo"] + ".git".strip()
	giturl = "".join(strurl.splitlines())
	cmd = "git pull " + giturl
	os.chdir(gitdir)
	os.system("git stash")
	os.system(cmd)
	set_owner(gitdir, pvar.usrid)
	input("Setup update done, press enter to continue")

def update_system():
	os.system("apt-get -y update")
	os.system("apt-get -y full-upgrade")
	input("System update done, press enter to continue")

def show_system_summary():
	os.system("rpi-eeprom-update")
	os.system("free -mt")
	os.system("nmcli dev status")
	os.system("ufw status")
	input("Press enter to continue")

def install_modules_server():
	os.system("apt-get -y install tcl tcl-dev m4 sphinx autoconf automake autopoint")
	os.system("git clone https://github.com/envmodules/modules.git")
	os.chdir("modules")
	os.system("./configure --prefix=/usr/local")
	os.system("make; make install; ldconfig")
	os.chdir("..")
	# Modules initialization
	with open('.bashrc', 'a') as f:
		f.write(". /usr/local/init/bash")
	os.system("rm -rf modules*")
	input("Environment Modules server install done, press enter to continue")

def install_modules_client():

    apt-get -y install tcl
	os.system("apt-get -y install tcl")
	with open('.bashrc', 'a') as f:
		f.write(". /usr/local/init/bash")
	input("Environment Modules client install done, press enter to continue")

def show_menu(menu):
	prompt = "Select option: "
	while True:
		os.system("clear")
		for item in menu: # Show menu
			if menu.index(item) == 0: # Print underlined title + hostname
				#print("\u0332".join(item.split("#")[0] + " (" + pvar.hstname + " - " + pvar.usrname + )"))
				print("\u0332".join(item.split("#")[0] + " (" + pvar.hstname + " - " + pvar.usrname + ")"))
			else:
				print(f"{menu.index(item)})\t {item.split("#")[0]}".expandtabs(2))
		try: # Process input
			value = input(prompt)
			ival = int(value)
			if 0 < ival < len(menu): # Action selected
				if ival == (len(menu) - 1): # Last menu item = Back/Quit
					break
				else:
					act = menu[ival].split("#")[1]
					exec(f"{act}")                           
			else:
				input("Invalid integer " + str(ival) + " , press enter to continue")
				continue
		except ValueError:
			if value.lower() == "b": # Back selected
				break
			elif value.lower() == "q": # Quit selected
				break
			else:
				input("Invalid input " + value + " , press enter to continue")
				continue
