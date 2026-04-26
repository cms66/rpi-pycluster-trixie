# Python variables
import os
from pwd import getpwnam
	
hstname = str(os.uname()[1])
usrname = os.getlogin() # Gives user with/without sudo
usrid = getpwnam(usrname).pw_uid
arrconf = {}

# Menus
mnuMainFull = [
"Setup - Main menu#",
"Update setup#update_setup()",
"Update system#update_system()",
"Hardware#show_menu(pvar.mnuHardwareFull)",
"Back|Quit#"]

mnuHardwareFull=[
"Setup - Hardware menu#",
"PCIe#phdw.setup_pcie()",
"Camera - CSI#phdw.setup_camera_csi()",
"Back|Quit#"]
