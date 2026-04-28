# Security functions

import os
import python.variables as pvar
import python.general as pgen

def test_func():
	print(pvar.usrname)
	print(pvar.usrid)
	print(pvar.usrpath)
	print(pvar.hstname)
	print(pvar.arrconf['gitrepo'])

# fail2ban

# ufw
def get_ufw_status():
	os.system("ufw status")
