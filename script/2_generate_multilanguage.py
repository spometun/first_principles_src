#!/usr/bin/env python3
from context import *
import sys
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *

DST_FOLDER = sys.argv[1] if len(sys.argv) > 1 else ROOT

recreate_dir(DST_FOLDER + WWW);
copy_fixed_stuff(DST_FOLDER + TEMPLATE + WWW, DST_FOLDER + WWW)
os.mkdir(DST_FOLDER + WWW + STUDIES)

generate_language("en", DST_FOLDER)
generate_language("ru", DST_FOLDER)
generate_language("uk", DST_FOLDER)
generate_language("sv", DST_FOLDER)
