#!/usr/bin/env python3
from context import *
import sys
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *

DST_FOLDER = sys.argv[1] if len(sys.argv) > 1 else ROOT

recreate_dir(ROOT + WWW);
copy_fixed_stuff(DST_FOLDER + TEMPLATE + WWW, ROOT + WWW)
os.mkdir(ROOT + WWW + STUDIES)

generate_language("en")
generate_language("ru")
generate_language("uk")
generate_language("sv")
