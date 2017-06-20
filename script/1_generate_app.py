#!/usr/bin/env python3
import sys
import os
import shutil
from context import *
from libs.utils import *

if len(sys.argv) != 3 or (sys.argv[2] != "mobile" and sys.argv[2] != "web"):
    print('Usage: {} <destination_path> <mobile|web>'.format(sys.argv[0]))
    sys.exit()

DST_FOLDER = sys.argv[1]
IS_MOBILE = sys.argv[2] == 'mobile'
if not os.path.isdir(DST_FOLDER):
    print('destination directory not found: ' + DST_FOLDER)
    sys.exit()
    

dst_path = DST_FOLDER
src_path = ROOT + SRC
recreate_dir(dst_path)
  
shutil.copytree(src_path + WWW, dst_path + WWW)
os.remove(dst_path + WWW + STUDIES_FILE)
recreate_dir(dst_path + WWW + STUDIES)

with open(dst_path + WWW + JS + LANGUAGES_JS, 'w') as ofile:
    ofile.write("LANGUAGES = ");
    with open(ROOT + LANGUAGES_FILE) as ifile:
        ofile.write(ifile.read())
if not IS_MOBILE:
    os.system('mkdir -m 755 ' + dst_path + '/api')
    os.system('cp -r ../server/*.php ' + dst_path + '/api')
    os.system('chmod 644 ' + dst_path + '/api/*.php')
    os.system('touch ' + dst_path + '/api/last_update')
    os.system('pwd > ' + dst_path + '/api/src_path.txt')
    os.system('cp ../server/index.html ' + dst_path)

