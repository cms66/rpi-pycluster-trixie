# Environment Modules funcions

import os

def install_modules_server():
	#os.system("apt-get -y install tcl tcl-dev m4 sphinx autoconf automake autopoint")
	#os.system("git clone https://github.com/envmodules/modules.git")
	#os.chdir("modules")
	#os.system("./configure --prefix=/usr/local")
	#os.system("make; make install; ldconfig")
	os.chdir("..")
	# Modules initialization
	with open('.bashrc', 'a') as f:
		f.write(". /usr/local/init/bash")
	os.system("rm -rf modules*")
	input("Environment Modules server install done, press enter to continue")

def install_modules_client():
	os.system("apt-get -y install tcl")
	with open('.bashrc', 'a') as f:
		f.write(". /usr/local/init/bash")
	input("Environment Modules client install done, press enter to continue")
