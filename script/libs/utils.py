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
    shutil.copy(src_path + "/style.css", dst_path + "/style.css")


