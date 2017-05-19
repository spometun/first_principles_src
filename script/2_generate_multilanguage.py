#!/usr/bin/env python3
from context import *
from libs.utils import *
from libs.pipeline_classes import *
from libs.generate_language import *


recreate_dir(ROOT + WWW);
copy_fixed_stuff(ROOT + TEMPLATE + WWW, ROOT + WWW)
os.mkdir(ROOT + WWW + STUDIES)

generate_language("en")
generate_language("ru")
generate_language("uk")
