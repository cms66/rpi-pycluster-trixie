# Python variables
import os

hstname = str(os.uname()[1])
usrname = os.getlogin() # Gives user with/without sudo
# TODO get usrid from usrname 
#usrid = os.getuid()
#usrid = int(os.system("cat /etc/passwd | grep " + usrname + " | cut -d ':' -f 3"))
usrid = 1000
arrconf = {}
