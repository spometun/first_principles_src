#!/usr/bin/env python3
import os
import shutil
from context import  *

def recreate_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def copy_fixed_stuff(src_path, dst_path):
    shutil.copytree(src_path + "/jquery", dst_path + "/jquery")
    shutil.copytree(src_path + "/images", dst_path + "/images")
    shutil.copytree(src_path + "/js", dst_path + "/js")

    shutil.copy(src_path + "/languages.json", dst_path + "/languages.json")
    shutil.copy(src_path + "/style.css", dst_path + "/style.css")
    
def cut_front_number(filename):
    return filename.split("_", 1)[1];
    
def cut_html_extension(filename):
    return filename[:-5];
