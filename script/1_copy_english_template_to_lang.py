#!/usr/bin/env python3
import os
import shutil
import sys
from context import *
from libs.utils import *

if len(sys.argv) != 2:
    print('Usage: {} <deployment_path>'.format(sys.argv[0]))
    sys.exit()
DEPLOYMENT_FOLDER = sys.argv[1]

dst_path = ROOT + LANG +  ENGLISH_TEMPLATE
if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
shutil.copytree(DEPLOYMENT_FOLDER + TEMPLATE + LANG + ENGLISH_TEMPLATE, dst_path)
