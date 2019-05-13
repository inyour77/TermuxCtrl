#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
from time import sleep

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

os.system("clear")
gilang=(a+"""
==============<·~~~~~~~~~~~~>·==============
| Author : InYourXerXez7                 |
| Team   : Buft~2e4h                     |
| ThankTo: My Friends && Allah           |
| Codex  :https://github.com/gillanggans7|
| Contack: @XerXezOficial                |
==============<·~~~~~~~~~~~~>·==============
""")
os.system("clear")
gilang3=(a+"""
Sedang Menginstall (####......................)
Sedang Menginstall (##########................)
Sedang Menginstall (#############.............)
Sedang Menginstall (###################.......)
Sedang Menginstall (#####################.....)
Sedang Menginstall (##########################)
""")
os.system("clear")
gl7=(p+"""
__  __                            _
|  \/  | ___ _ __ ___  _   _  __ _| |_
| |\/| |/ _ \ '_ ` _ \| | | |/ _` | __|
| |  | |  __/ | | | | | |_| | (_| | |_ _ _
|_|  |_|\___|_| |_| |_|\__,_|\__,_|\__( | )
                                      |/|/
""")

os.system("clear")
gl2=(p+"""
 _  __       __  __        _____
\ \/ /___ _ _\ \/ /___ ___|___  |
 \  // _ \ '__\  // _ \_  /  / /
 /  \  __/ |  /  \  __// /  / /
/_/\_\___|_| /_/\_\___/___|/_/
""")
slowprints(gilang)
input('\nSiap?? cick Enter~$ ')
slowprints(gl2)
print(bt+"")
slowprints("[!] Mulai Menginstall files...")
sleep(4)
slowprints(gilang3)
sleep(20)
print(g+"""
          -o          o-      ~\InYourSistem
          +hydNNNNdyh+          ------------
        +mMMMMMMMMMMMMm+         NAME : gilang
      `dMM[•]MMMMM[•]MMd`        Team : 2e4h
      hM\MMMMMMMMMMMM/MMMh       Versi: 1.0
  ..  yyy\__________/yyyyyy  ..  Nick : InYour
.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm. 2e4hTeam
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM: For : Termux
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:     ||
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-======|
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+-======|
      mMMMMMMMMMMMMMMMMMMm           ||
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
        mmmmmmâ  ammmmmm
      mmmmmmmmm  mmmmmmmmm
[<>]<<<<<<<<<<<|>>>>>>>>>>>>[<>]
""")
sleep(30)
slowprints(gl7)
sleep(5)
try:
      os.mkdir("/data/data/com.termux/files/home/.termux")
except:
      pass
slowprints("~$ Berhasil Menginstall!")
sleep(3)
slowprints("~$ Sedamg Membuat Pengaturan file Sabar menunggu")
sleep(1)
shortcutkey = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
script = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
script.write(shortcutkey)
script.close()
sleep(1)
print(p+"")
sleep(2)
slowprints("\n~$ Sedang Menyimpan data pengaturan")
sleep(2)
os.system("termux-reload-settings")
slowprints(gilang)
print(g+"""
~$-TOLONG KETIK ENTER SETELAH INIH TUNGU 10
""")
sleep(10)
input('\nRoot~InYourXerXez7~$     ')
os.system("clear")
os.system('exit')
