# Network functions
# TODO - update NFS firewall rule

import os
import python.variables as pvar
import python.general as pgen

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

def add_nfs_export():
	# Check export type + location
	usropt = input("System or Data export? (s/d): ").lower() 
	if usropt == "s": # System export
		defdir = pvar.arrconf['defsysdir']
		#usrdir = input("Path of directory to be shared (press enter for default = " + pvar.arrconf['defsysdir'] + "): ")
		#str = "Path of directory to be shared (press enter for default " + pvar.arrconf['defsysdir'] + "): "
		#usrdir = input(f"Path of directory to be shared (press enter for default {pvar.arrconf['defsysdir']}): ")
		struser = f"Path of directory to be shared (press enter for default {pvar.arrconf['defsysdir']}): "
		usrdir = input(struser)
		nfsdir = defdir if usrdir <= "" else usrdir
	elif usropt == "d": # Data export
		defdir = pvar.arrconf['defdatadir']
		usrdir = input("Path of directory to be shared (press enter for default = " + pvar.arrconf['defdatadir'] + "): ")
		nfsdir = defdir if usrdir <= "" else usrdir
	else:
		input("Invalid entry - press enter to continue")
		return
	# Check exports + add entry
	exp = pgen.check_file("/etc/exports", nfsdir)
	if exp == "NOTEXT": # Add entry
		strcmd = f"echo '{nfsdir} {pvar.arrconf[subnet]}(rw,sync,no_subtree_check,no_root_squash)' >> /etc/exports".strip()
		os.system(strcmd)
		os.system("systemctl daemon-reload")
		input("Export created - press enter to continue")
	elif exp == "TEXT":
		input("Export exists - press enter to continue")
	elif exp == "NOFILE":
		input("File not found - press enter to continue")


def add_nfs_remote():
	remnode = input("Remote node: ")
	usropt = input("System mount or Data share? (s/d): ").lower()
	if usropt == "s": # System share
		defdir = pvar.arrconf['defsysdir']
		usrdir = input("Path of directory to be shared (press enter for default = " + pvar.arrconf['defsysdir'] + "): ")
		nfsdir = defdir if usrdir <= "" else usrdir
	elif usropt == "d": # Data share
		defdir = pvar.arrconf['defdatadir']
		usrdir = input("Path of directory to be shared (press enter for default = " + pvar.arrconf['defdatadir'] + "): ")
		nfsdir = defdir if usrdir <= "" else usrdir
	else:
		input("Invalid entry - press enter to continue")
		return
	print("Remote node: " + remnode)
	print("Def Remote directory: " + defdir)
	print("User Remote directory: " + usrdir)
	print("NFS Remote directory: " + nfsdir)
	with open("/etc/fstab", "a") as f:
		strmount = f"{remnode}:{nfsdir}"
		#strmount = f"{remnode}:{nfsdir} {nfsdir} nfs4 rw,relatime,rsize=32768,wsize=32768,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,local_lock=none 0 0".strip()
		print("str = " + strmount)
		#strmount = remnode + ":" + nfsdir + " " + nfsdir + " nfs4 rw,relatime,rsize=32768,wsize=32768,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,local_lock=none 0 0"
		"".join(strmount.splitlines())
		print("str = " + strmount)
		input("Mount = " + strmount + " - press enter to continue")
		f.write(strmount)
	#echo "$remnode:$mntdir $mntdir    nfs4 rw,relatime,rsize=32768,wsize=32768,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,local_lock=none 0 0" >> /etc/fstab
	input("NFS remote mount done - press enter to continue")
