# Python main entry point for setup + management

import os
import python.general as pgen
import python.hardware as phdw
import python.variables as pvar
	
def main():
	pgen.read_config()
	#pgen.show_config()
	#phdw.setup_cam_csi()
	#pgen.show_menu(pvar.mnuMainFull)

if __name__ == "__main__":
	main()
