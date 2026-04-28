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
	os.chdir(pvar.usrpath)
	# TODO - Check for previous installation
	strdep = "libjpeg-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libcanberra-gtk* libgtk-3-dev libgstreamer1.0-dev gstreamer1.0-gtk3 libgstreamer-plugins-base1.0-dev gstreamer1.0-gl libxvidcore-dev libx264-dev python3-numpy python3-pip libtbbmalloc2 libdc1394-dev libv4l-dev v4l-utils libopenblas-dev libblas-dev liblapack-dev gfortran libhdf5-dev libprotobuf-dev libgoogle-glog-dev libgflags-dev protobuf-compiler"
	usropt = input("Install Server or Client (s/c): ").lower()
	if usropt == "s": # Server install
		if check_file("/etc/exports", "/usr/local") == "NOTEXT": # Server installed, add export
			with open("/etc/exports","a") as f:
				f.write("/usr/local 192.168.0.0/24(rw,sync,no_subtree_check,no_root_squash)")
		os.system("apt-get -y install " + strdep)
		os.system("git clone https://github.com/opencv/opencv.git")
		os.system("git clone https://github.com/opencv/opencv_contrib.git")
		os.mkdir("opencv/build")
		os.chdir("opencv/build")
		os.system("cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=$usrpath/opencv_contrib/modules -D ENABLE_NEON=ON -D WITH_OPENMP=ON -D WITH_OPENCL=OFF -D BUILD_TIFF=ON -D WITH_FFMPEG=ON -D WITH_TBB=ON -D BUILD_TBB=ON -D WITH_GSTREAMER=ON -D BUILD_TESTS=OFF -D WITH_EIGEN=OFF -D WITH_V4L=ON -D WITH_LIBV4L=ON -D WITH_VTK=OFF -D WITH_QT=OFF -D WITH_PROTOBUF=ON -D OPENCV_ENABLE_NONFREE=ON -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D PYTHON3_PACKAGES_PATH=/usr/local/lib/python3.13/dist-packages -D OPENCV_GENERATE_PKGCONFIG=ON -D BUILD_EXAMPLES=OFF ..")
		os.system("make -j4 all; make install; ldconfig")
		os.chdir(pvar.usrpath)
		os.system("rm -rf opencv*")
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
		with open (file, 'r') as f:
			content = f.read()
			if str in content:
				res = "TEXT"
			else:
				res = "NOTEXT"                
	except:
		res = "NOFILE"
	input(f"Result: {res} press enter to continue")

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
