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


#recreate_dir(DEPLOYMENT_FOLDER + WWW);
#copy_fixed_stuff(DEPLOYMENT_FOLDER + TEMPLATE + WWW, DEPLOYMENT_FOLDER + WWW)
#shutil.copy(DEPLOYMENT_FOLDER + TEMPLATE + WWW + LANGUAGES_JS, DEPLOYMENT_FOLDER + WWW + JS)
if os.path.exists(DEPLOYMENT_FOLDER + WWW):
    shutil.rmtree(DEPLOYMENT_FOLDER + WWW)
os.system('rm -rf ' + DEPLOYMENT_FOLDER + WWW)
os.system('rm -rf ' + DEPLOYMENT_FOLDER + API)
os.system('cp -r ' + DEPLOYMENT_FOLDER + TEMPLATE + '/*' + ' ' + DEPLOYMENT_FOLDER)
os.system('rm -r ' + DEPLOYMENT_FOLDER + WWW + STUDIES + ENGLISH_TEMPLATE)
os.system('rm ' + DEPLOYMENT_FOLDER + WWW + LANGUAGES_FILE)
#shutil.copytree(DEPLOYMENT_FOLDER + TEMPLATE, DEPLOYMENT_FOLDER)
#shutil.rmtree(DEPLOYMENT_FOLDER + WWW + STUDIES + ENGLISH_TEMPLATE)
#os.mkdir(DEPLOYMENT_FOLDER + WWW + STUDIES)

for lang in LANGUAGES_LIST:
    generate_language(lang, DEPLOYMENT_FOLDER)


#with open('logs.txt', 'a') as f:
#    datetime_str = datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S: ')
#    f.write(datetime_str + 'Translations generations\n');
