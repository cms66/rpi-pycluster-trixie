# Hardware functions
import os
import python.variables as pvar

def setup_pcie():
	# Check Model
	with open("/proc/device-tree/model", "rb") as f:
		model = f.read().rstrip(b"\0").decode()
	if ("Raspberry Pi 5" or "Compute Module 5" in model):
		input("PCIe Gen 3 is available, press enter to continue")
		# Check Gen 3 not enabled
		with open('/boot/firmware/config.txt', 'a+') as f:
			content = f.read()
			if "dtparam=pciex1_gen" in content:
				input("PCIe Gen 3 already enabled, press enter to continue")
			else:
				f.write("dtparam=pciex1\n")
				f.write("dtparam=pciex1_gen=3\n")
				input("PCIe Gen 3 enabled (reboot required), press enter to continue")
				#os.system("reboot")
	else:
		input("PCIe Gen 3 not available, press enter to continue")
	
def setup_cam_csi():
	input("CSI Cam = TODO - press enter to continue")


