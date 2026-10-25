# Python variables
import os
from pwd import getpwnam
	
hstname = str(os.uname()[1])
usrname = os.getlogin() # Gives user with/without sudo
usrid = getpwnam(usrname).pw_uid
usrpath = f"/home/{usrname}"
arrconf = {}

# Menus
mnuMainFull = [
"Setup - Main menu#",
"System summary#show_system_summary()",
"Update setup#update_setup()",
"Update system#update_system()",
"Hardware#show_menu(pvar.mnuHardwareFull)",
"Network#show_menu(pvar.mnuNetworkFull)",
"Environment Modules#show_menu(pvar.mnuModulesFull)",
"OpenCV#setup_opencv()",
"SDM#show_menu(pvar.mnuSDMFull)",
"Test#test_func()",
"Back|Quit#"]

mnuHardwareFull=[
"Setup - Hardware menu#",
"PCIe#phdw.setup_pcie()",
"Camera - CSI#phdw.setup_cam_csi()",
"Back|Quit#"]

mnuNetworkFull=[
"Setup - Network menu#",
"SSH - Create user keys#pnet.create_user_ssh_keys()",
"SSH - Copy user key to host#pnet.copy_user_ssh_keys()",
"SSH - Remove host from known hosts#pnet.delete_node_from_known_hosts()",
"NFS - Install Server#pnet.install_nfs_server()",
"NFS - Add local export#pnet.add_nfs_export()",
"NFS - Add remote mount#pnet.add_nfs_remote()",
"Back|Quit#"]

mnuSecurityFull=[
"Setup - Security menu#",
"UFW - Status#psec.get_ufw_status()",
"Back|Quit#"]

mnuModulesFull=[
"Setup - Modules menu#",
"Install - Server#pmod.install_modules_server()",
"Install - Client#pmod.install_modules_client()",
"Back|Quit#"]

mnuSDMFull=[
"Setup - SDM menu#",
"Install - Server#psdm.setup_sdm_server()",
"Install - Client#psdm.setup_sdm_client()",
"Back|Quit#"]
