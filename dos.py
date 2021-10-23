#!/usr/bin/env python
import os
import glob
from shutil import which
from pathlib import Path
import sys

#modify pwscf.k.pdos_atm#*(Al*)_wfc#*(*) as per sum required
directory = Path(os.getcwd())
pwscf_files = directory.glob('pwscf.k.pdos_atm#*(Al*)_wfc#*(*)')
fil = open('inp', 'a')
for files in pwscf_files:
    fx = str(files)
    fx = fx.split('/')[-1]
    #print(fx)
    fil.write("'"+fx+"'"+"\n")

fil.close()
