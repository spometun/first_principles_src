#!/usr/bin/env python3
from context import *
import datetime
import shutil
import sys
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *

if len(sys.argv) != 2:
    print('Usage: {} <destination_path>'.format(sys.argv[0]))
    sys.exit()

DEPLOYMENT_FOLDER = sys.argv[1]
if not os.path.isdir(DEPLOYMENT_FOLDER):
    print('destination directory not found: ' + DEPLOYMENT_FOLDER)
    sys.exit()

for lang in LANGUAGES_LIST:
    generate_language(lang, DEPLOYMENT_FOLDER)


