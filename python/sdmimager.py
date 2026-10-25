# SDM functions
# Imports
import os
import python.variables as pvar

def install_sdm_server():
	os.system("apt-get -y install rpiboot") # For Compute module eMMC drives
	os.system("curl -L https://raw.githubusercontent.com/gitbls/sdm/master/install-sdm | bash")
	
	
