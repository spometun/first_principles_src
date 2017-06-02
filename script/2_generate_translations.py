#!/usr/bin/env python3
from context import *
import shutil
import sys
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *

if len(sys.argv) != 2:
    print('Usage: {} <destination_path>'.format(sys.argv[0]))
    sys.exit()
DST_FOLDER = sys.argv[1]

recreate_dir(DST_FOLDER + WWW);
copy_fixed_stuff(DST_FOLDER + TEMPLATE + WWW, DST_FOLDER + WWW)
shutil.copy(DST_FOLDER + TEMPLATE + WWW + "/languages.json", DST_FOLDER + WWW)
os.mkdir(DST_FOLDER + WWW + STUDIES)

generate_language("en", DST_FOLDER)
generate_language("ru", DST_FOLDER)
generate_language("uk", DST_FOLDER)
generate_language("sv", DST_FOLDER)
