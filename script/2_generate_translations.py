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

recreate_dir(DEPLOYMENT_FOLDER + WWW);
copy_fixed_stuff(DEPLOYMENT_FOLDER + TEMPLATE + WWW, DEPLOYMENT_FOLDER + WWW)
shutil.copy(DEPLOYMENT_FOLDER + TEMPLATE + WWW + "/languages.js", DEPLOYMENT_FOLDER + WWW + "/js")
os.mkdir(DEPLOYMENT_FOLDER + WWW + STUDIES)

generate_language("en", DEPLOYMENT_FOLDER)
generate_language("ru", DEPLOYMENT_FOLDER)
generate_language("uk", DEPLOYMENT_FOLDER)
generate_language("sv", DEPLOYMENT_FOLDER)


with open('logs.txt', 'a') as f:
    datetime_str = datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S: ')
    f.write(datetime_str + 'Translations generations\n');
