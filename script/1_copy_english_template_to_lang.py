#!/usr/bin/env python3
import os
import shutil
from context import *
from libs.utils import *


dst_path = ROOT + LANG +  ENGLISH_TEMPLATE
if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
shutil.copytree(ROOT + TEMPLATE + LANG + ENGLISH_TEMPLATE, dst_path)
