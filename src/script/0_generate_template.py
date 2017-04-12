import os
import shutil
from libs.generate_html_template import *
from libs.pipeline_classes import *

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
os.mkdir(dst_root + "lang/en")
os.mkdir(dst_root + "lang/en/LC_MESSAGES")
english_path = dst_root + "lang/en/LC_MESSAGES/"

input_file = open(dst_root + "studies/seeking_god.html")
input_text = input_file.read()

out_file = open(english_path + "seeking_god.po", "w")
writer = WriterSink(out_file)
parser = ParserSource(input_text)
po_generator = POGeneratorSinkSource(False)
parser.sink = po_generator
po_generator.sink = writer
parser.go()

out_file = open(english_path + "seeking_god.pot", "w")
writer = WriterSink(out_file)
parser = ParserSource(input_text)
po_generator = POGeneratorSinkSource(True)
parser.sink = po_generator
po_generator.sink = writer
parser.go()



print("done")

