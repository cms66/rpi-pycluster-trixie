# Python main entry point for setup + management

import os
import python.variables as pvar
import python.general as pgen
import python.hardware as phdw
import python.network as pnet
import python.security as psec
import python.envmod as pmod

def main():
	pgen.read_config()
	pgen.show_menu(pvar.mnuMainFull)

if __name__ == "__main__":
	main()
