# Security functions

import os

# fail2ban

# ufw
def get_ufw_status():
  os.system("ufw status")
