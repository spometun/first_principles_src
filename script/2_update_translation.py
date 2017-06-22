#!/usr/bin/env python3
from context import *
import datetime
import shutil
import sys
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate import *

if len(sys.argv) != 4 or (sys.argv[2] != "mobile" and sys.argv[2] != "web"):
    print('Usage: {} <destination_path> <mobile|web> <language|all>'.format(sys.argv[0]))
    sys.exit()

is_mobile = sys.argv[2] == 'mobile'
is_web = not is_mobile

DST_FOLDER = sys.argv[1]
if not os.path.isdir(DST_FOLDER):
    print('destination directory not found: ' + DST_FOLDER)
    sys.exit()


if sys.argv[3] != 'all':
    languages = [sys.argv[3]]
else:
    languages = LANGUAGES_LIST

for lang in languages:
    is_show_update_controls = lang != 'en' and is_web 
    generate_language(lang, DST_FOLDER, is_show_update_controls)


