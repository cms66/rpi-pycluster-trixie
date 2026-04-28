# Python generic functions

import os
import python.variables as pvar
import python.hardware as phdw
import python.network as pnet
import python.security as psec
import python.envmod as pmod

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

def setup_opencv():
	# TODO - Check for previous installation
	strdep = "libjpeg-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libcanberra-gtk* libgtk-3-dev libgstreamer1.0-dev gstreamer1.0-gtk3 libgstreamer-plugins-base1.0-dev gstreamer1.0-gl libxvidcore-dev libx264-dev python3-numpy python3-pip libtbbmalloc2 libdc1394-dev libv4l-dev v4l-utils libopenblas-dev libblas-dev liblapack-dev gfortran libhdf5-dev libprotobuf-dev libgoogle-glog-dev libgflags-dev protobuf-compiler"
	usropt = input("Install Server or Client (s/c): ").lower()
	if usropt == "s": # Server install
		check_file("/etc/exports", "/usr/local")
		#os.system("apt-get -y install " + strdep)
		input("OpenCV server install done - press enter to continue")
	elif usropt == "c": # Client install
		check_file("/etc/fstab", "/usr/local")
		#os.system("apt-get -y install " + strdep)
		#os.system("ldconfig")
		input("OpenCV client install done - press enter to continue")
	else:
		input("Invalid entry - press enter to continue")	

def check_file(file, str):
	try:
		os.path.isfile(file)
	except:
		res = f"{file} NOT found"
	else:
		with open (file, 'r') as f:
			content = f.read()
			if str in content:
				res = f"{str} found in {file}"
			else:
				res = f"{str} NOT found in {file}"

	#if os.path.exists(file):
	#	print("File: " + file)
	#	print("String: " + str)
	#	with open (file, 'a') as f:
	#		content = f.read()
	#		if str in content:
	#			res = f"{str} found in {file}"
	#		else:
	#			res = f"{str} NOT found in {file}"
	#else:
	#	res = f"{file} NOT found"
	input(f"File check done {res} press enter to continue")

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
