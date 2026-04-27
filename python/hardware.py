# Hardware functions
import os
import python.variables as pvar

def setup_pcie():
	# TODO - Check Model
	# Enable Gen 3 - Check for Pi 5/CM5
	with open('/etc/exports', 'a') as f:
	with open('/boot/firmware/config.txt', 'a') as f:
		content = f.read()
		if "pciex1_gen" in content:
			input("PCIe Gen 3 already enabled, press enter to continue")
	#	else:
	#		f.write("dtparam=pciex1")
	#		f.write("dtparam=pciex1_gen=3")
			input("PCIe Gen 3 enabled (reboot required), press enter to continue")
	#return
	input("PCIe = TODO - press enter to continue")
	
def setup_cam_csi():
	input("CSI Cam = TODO - press enter to continue")


