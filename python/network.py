# Network functions

import os
import python.variables as pvar

def create_user_ssh_keys():
	# Create keys for user
	#runuser -l  $usrname -c "ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -P \"\"" # Works including creates .ssh directory
	#"sudo -u " + usrname + " ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -P ''"
	os.system("sudo -u " + usrname + " ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -P ''")
	strcmd = "echo 'HostKey /home/" + usrname + "/.ssh/id_ed25519' >> /etc/ssh/sshd_config"
	os.system(strcmd)
	os.system("systemctl restart ssh")
	input("SSH key setup done - press enter to continue")

def copy_user_ssh_keys():
	remnode = input("Remote node")
	os.system("sudo -u " + usrname + " ssh-copy-id -i /home/" + usrname + "/.ssh/id_ed25519 " + usrname + "@" + remnode)
	input("SSH key copied - press enter to continue")

def delete_node_from_known_hosts():
	input("TODO - press enter to continue")

def install_nfs_server():
	input("TODO - press enter to continue")

def add_nfs_local():
	input("TODO - press enter to continue")

def add_nfs_remote():
	input("TODO - press enter to continue")
