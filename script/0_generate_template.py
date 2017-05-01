import os
import shutil
from libs.generate_html_template import *
from libs.pipeline_classes import *

src_root = "../data/"
dst_root = "../../template/"

def recreate_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)


def prepare_dst_folder_and_init_pathes(src_path, dst_path):
    recreate_dir(dst_path)
    recreate_dir(dst_path + "/www")
    shutil.copytree(src_path + "/jquery", dst_path + "/www/jquery")
    shutil.copytree(src_path + "/images", dst_path + "/www//images")
    shutil.copy(src_path + "/style.css", dst_path + "/www/style.css")
    os.mkdir(dst_path + "/www/studies")
    global g_path_to_studies
    g_path_to_studies = dst_path + "/www/studies"
    os.mkdir(dst_path + "/lang")
    os.mkdir(dst_path + "/lang/english_templates")
    global g_path_to_english_messages
    g_path_to_english_messages = dst_path + "/lang/english_templates/"

def generate_po(path_to_studies, output_folder, study_name, is_generate_template):
    input_file = open(path_to_studies + "/" + study_name + ".html")
    input_text = input_file.read()
    out_file_name = output_folder + "/" + study_name + ".po"
    if is_generate_template:
        out_file_name += "t"
    out_file = open(out_file_name, "w")
    writer = WriterSink(out_file)
    parser = ParserSource(input_text)
    po_generator = POGeneratorSinkSource(is_generate_template)
    parser.sink = po_generator
    po_generator.sink = writer
    parser.go()

def process_index():
    generateIndex(src_root, g_path_to_studies)
    #generate_po(g_path_to_studies, g_path_to_english_messages, "index", False)
    generate_po(g_path_to_studies, g_path_to_english_messages, "index", True)

def process_study(study_name, study_title):
    generateStudy(src_root, g_path_to_studies, study_name, study_title)
    #generate_po(g_path_to_studies, g_path_to_english_messages, study_name, False)
    generate_po(g_path_to_studies, g_path_to_english_messages, study_name, True)


prepare_dst_folder_and_init_pathes(src_root, dst_root)
process_index()
process_study("seeking_god", "Seeking God")

print("done")

