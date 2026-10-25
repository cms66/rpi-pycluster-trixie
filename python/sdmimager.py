# SDM functions
# Imports
import os
import python.variables as pvar

def install_sdm_server():
	os.system("apt-get -y install rpiboot") # For Compute module eMMC drives
	os.system("curl -L https://raw.githubusercontent.com/gitbls/sdm/master/install-sdm | bash")
	os.makedirs("/data/current/sdm/images/archive", exist_ok=True)
	os.makedirs("/data/current/sdm/images/current", exist_ok=True)
	os.makedirs("/data/current/sdm/images/latest", exist_ok=True)
	input("SDM server install done, press enter to continue")
	
def install_sdm_client():
	input("install client - TODO, press enter to continue")

def update_latest_images():
	input("update latest images - TODO, press enter to continue")

def create_image():
	input("create image - TODO, press enter to continue")

def modify_image():
	input("modify image - TODO, press enter to continue")

def burn_image():
	input("burn image - TODO, press enter to continue")
