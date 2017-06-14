#!/usr/bin/env python3
import os
import shutil
from context import  *

def recreate_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def cut_front_number(filename):
    return filename.split("_", 1)[1];
    
def cut_html_extension(filename):
    return filename[:-5];
