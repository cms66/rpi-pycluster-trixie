# Python variables
import os
from pwd import getpwnam
	
hstname = str(os.uname()[1])
usrname = os.getlogin() # Gives user with/without sudo
usrid = getpwnam(usrname).pw_uid
arrconf = {}

# Menus


