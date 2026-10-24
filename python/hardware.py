# Hardware functions
import os
import python.variables as pvar

from pathlib import Path

def check_pcie_gen3_config():
    path = Path("/proc/device-tree/model")
    if not path.exists():
        return False
    model = path.read_bytes().rstrip(b"\0").decode()
    return (
        "Raspberry Pi 5" in model
        or "Compute Module 5" in model
    )


def setup_pcie():
	# Check Model
	if check_pcie_gen3_config():
		# Check Gen 3 not enabled
		with open('/boot/firmware/config.txt', 'a+') as f:
			content = f.read()
			if "pciex1_gen" in content:
				input("PCIe Gen 3 already enabled, press enter to continue")
			else:
				f.write("dtparam=pciex1")
				f.write("dtparam=pciex1_gen=3")
				input("PCIe Gen 3 enabled (reboot required), press enter to continue")
				os.system("reboot")
	else:
		input("PCIe Gen 3 not available, press enter to continue")
	
def setup_cam_csi():
	input("CSI Cam = TODO - press enter to continue")


