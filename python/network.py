# Network functions
# TODO - update NFS firewall rule

import os
import python.variables as pvar

def create_user_ssh_keys():
	# Create keys for user
	os.system("sudo -u " + pvar.usrname + " ssh-keygen -t ed25519 -f /home/" + pvar.usrname + "/.ssh/id_ed25519 -P ''")
	os.system("echo 'HostKey /home/" + pvar.usrname + "/.ssh/id_ed25519' >> /etc/ssh/sshd_config")
	os.system("systemctl restart ssh")
	input("SSH key setup done - press enter to continue")

def copy_user_ssh_keys():
	remnode = input("Remote node: ")
	os.system("sudo -u " + pvar.usrname + " ssh-copy-id -i /home/" + pvar.usrname + "/.ssh/id_ed25519 " + pvar.usrname + "@" + remnode)
	input("SSH key copied to " + remnode + " - press enter to continue")

def delete_node_from_known_hosts():
	remnode = input("Remote node: ")
	os.system("sudo -u " + pvar.usrname + " ssh-keygen -f /home/" + pvar.usrname + "/.ssh/known_hosts -R " + remnode)
	input(remnode + " removed from known hosts - press enter to continue")

def install_nfs_server():
	os.system("apt-get -y install nfs-kernel-server")
	with open("/etc/default/nfs-kernel-server", "a") as f:
		f.write("RPCMOUNTDOPTS='--manage-gids -N 2 -N 3'\n")
		f.write("RPCNFSDOPTS='-N 2 -N 3'\n")
	# os.system("ufw allow from 192.168.0.0/24 to any port nfs") # TODO or Not needed?
	input("NFS server install done - press enter to continue")

def add_nfs_local():
	usropt = input("System mount or Data share? (s/d): ").lower()
	if usropt == "s": # System share
		defdir = pvar.arrconf['defsysdir']
		usrdir = input("Path of directory to be shared (press enter for default = " + pvar.arrconf['defsysdir'] + "): ")
		nfsdir = (defdir, usrdir)[usrdir > ""]
	else: # Data share
		defdir = pvar.arrconf['defdatadir']
		usrdir = input("Path of directory to be shared (press enter for default = " + pvar.arrconf['defdatadir'] + "): ")
		nfsdir = (defdir, usrdir)[usrdir != ""]
	with open('/etc/exports', 'a') as f: # Check for existing export and add if not
		content = f.read()
		if nfsdir in content:
			print('Export already exists')
		else:
			#f.write(nfsdir + " " + pvar.arrconf['subnet'] + "(rw,sync,no_subtree_check,no_root_squash)")
			#os.system("exportfs -ra")
			print('Export does not exist')
	input(nfsdir + " NFS share added - press enter to continue")

def add_nfs_remote():
	input("TODO - press enter to continue")
