#!/usr/bin/env python3
import sys
import os
import shutil
from context import *

if len(sys.argv) != 2:
    print('Usage: {} <destination_path>'.format(sys.argv[0]))
    sys.exit()

DEPLOYMENT_FOLDER = sys.argv[1]
if not os.path.isdir(DEPLOYMENT_FOLDER):
    print('destination directory not found: ' + DEPLOYMENT_FOLDER)
    sys.exit()

os.system('rm -rf ' + DEPLOYMENT_FOLDER + WWW)
os.system('rm -rf ' + DEPLOYMENT_FOLDER + API)
os.system('cp -r ' + DEPLOYMENT_FOLDER + TEMPLATE + '/*' + ' ' + DEPLOYMENT_FOLDER)
os.system('rm -r ' + DEPLOYMENT_FOLDER + WWW + STUDIES + ENGLISH_TEMPLATE)
os.system('rm ' + DEPLOYMENT_FOLDER + WWW + LANGUAGES_FILE)




