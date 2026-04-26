# Network functions

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
	os.system("sudo -u " + pvar.usrname + " ssh-keygen -f /home/" + pvar.usrname + "/.ssh/known_hosts -R " + remnode
	input(remnode + " removed from known hosts - press enter to continue")

def install_nfs_server():
	input("TODO - press enter to continue")

def add_nfs_local():
	input("TODO - press enter to continue")

def add_nfs_remote():
	input("TODO - press enter to continue")
