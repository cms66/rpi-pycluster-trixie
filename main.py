# Python main entry point for setup + management

import os
import python.functions as pfunc
import python.variables as pvar
	
def main():
	pfunc.read_config()
	pfunc.show_menu(pvar.mnuMainFull)

if __name__ == "__main__":
	main()
