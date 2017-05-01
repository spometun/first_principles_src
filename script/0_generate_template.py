import os
import shutil
from context import *
from libs.utils import *
from libs.generate_html_template import *
from libs.pipeline_classes import *

g_src_data_path = "../data/"
print(ROOT)

def prepare_dst_folder_and_init_pathes():
    dst_path = ROOT + TEMPLATE
    recreate_dir(dst_path)
    recreate_dir(dst_path + WWW)
    copy_fixed_stuff(g_src_data_path, dst_path + WWW)
    os.mkdir(dst_path + WWW + STUDIES)
    os.mkdir(dst_path + WWW + STUDIES + ENGLISH)
    global g_path_to_studies 
    g_path_to_studies = dst_path + WWW + STUDIES + ENGLISH
    os.mkdir(dst_path + LANG)
    os.mkdir(dst_path + LANG + ENGLISH_TEMPLATE)
    global g_path_to_english_template
    g_path_to_english_template = dst_path + LANG + ENGLISH_TEMPLATE

def generate_po(path_to_studies, output_folder, study_name):
    input_file = open(path_to_studies + "/" + study_name + ".html")
    input_text = input_file.read()
    out_file_name = output_folder + "/" + study_name + ".pot"
    out_file = open(out_file_name, "w")
    writer = WriterSink(out_file)
    parser = ParserSource(input_text)
    po_generator = POGeneratorSinkSource()
    parser.sink = po_generator
    po_generator.sink = writer
    parser.go()

def process_index():
    generateIndex(g_src_data_path, g_path_to_studies)
    generate_po(g_path_to_studies, g_path_to_english_template, "index")

def process_study(study_name, study_title):
    generateStudy(g_src_data_path, ROOT + TEMPLATE + WWW + STUDIES + ENGLISH, study_name, study_title)
    generate_po(g_path_to_studies, g_path_to_english_template, study_name)


prepare_dst_folder_and_init_pathes()
process_index()
process_study("seeking_god", "Seeking God")

print("done")

