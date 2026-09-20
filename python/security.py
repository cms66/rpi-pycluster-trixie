# Security functions

import os
import python.variables as pvar
import python.general as pgen

# fail2ban

# ufw
def get_ufw_status():
	os.system("ufw status")
