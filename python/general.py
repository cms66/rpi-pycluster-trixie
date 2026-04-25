# Python generic functions

import os
import python.variables as pvar

def read_config():
	conf = "/boot/firmware/custom.conf"
	if os.path.exists(conf):
		with open(conf) as f:
			for line in f:
				key = line.split('=')[0]
				val = line.split('=')[1]
				pvar.arrconf[key] = val

def show_config():
  
