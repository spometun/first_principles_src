import os
import shutil
from libs.generate_html_template import *

src_root = "../data/"
dst_root = "../../0_template/"

if os.path.exists(dst_root):
    shutil.rmtree(dst_root)
os.mkdir(dst_root)

shutil.copytree(src_root + "jquery", dst_root + "jquery")
shutil.copytree(src_root + "images", dst_root + "images")
shutil.copy(src_root + "style.css", dst_root + "style.css")


os.mkdir(dst_root + "studies")
generateFullHtml(src_root, dst_root, "index", False)
generateFullHtml(src_root, dst_root, "seeking_god")

os.mkdir(dst_root + "lang")
