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
"Network#show_menu(pvar.mnuNetworkFull)",
"System summary#show_system_summary()",
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
"NFS - Add local export#pnet.add_nfs_local()",
"NFS - Add remote mount#pnet.add_nfs_remote()",
"Back|Quit#"]

