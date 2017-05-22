#!/usr/bin/env python3
import os
import shutil
import polib
from context import *
from libs.utils import *
from libs.generate_html_template import *
from libs.pipeline_classes import *


def prepare_dst_folder():
    dst_path = ROOT + TEMPLATE
    recreate_dir(dst_path)
    recreate_dir(dst_path + WWW)
    copy_fixed_stuff(ROOT + SRC + WWW, dst_path + WWW)
    os.mkdir(dst_path + WWW + STUDIES)
    os.mkdir(dst_path + WWW + STUDIES + ENGLISH)
    global g_dst_studies 
    g_dst_studies = dst_path + WWW + STUDIES + ENGLISH
    os.mkdir(dst_path + LANG)
    os.mkdir(dst_path + LANG + ENGLISH_TEMPLATE)
    global g_dst_english_template
    g_dst_english_template = dst_path + LANG + ENGLISH_TEMPLATE

def cut_number(filename):
    return filename.split("_", 1)[1];

def generate_po(path_to_studies, output_folder, study_name):
    input_file = open(path_to_studies + "/" + study_name + ".html")
    input_text = input_file.read()
    out_file_name = output_folder + "/" + cut_number(study_name) + ".pot"
    out_file = open(out_file_name, "w")
    writer = WriterSink(out_file)
    parser = ParserSource(input_text)
    po_generator = POGeneratorSinkSource(study_name + ".html")
    parser.sink = po_generator
    po_generator.sink = writer
    parser.go()
    out_file.close()
    po = polib.pofile(out_file_name)
    po.save(out_file_name + "2")


def generate_studies_templates():
    print("GENERATING STUDIES TEMPLATES")
    src = ROOT + SRC + WWW
    dst = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    for study in STUDY_LIST:
        print(study.name)
        generateStudy(src, dst, study)    


def generate_translation_templates():
    print("\nGENERATING TRANSLATION TEMPLATES")
    path_to_studies = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    output_folder =  ROOT + TEMPLATE + LANG + ENGLISH_TEMPLATE
    for study in STUDY_LIST:
        print(study.name)
        generate_po(path_to_studies, output_folder, study.name)

prepare_dst_folder()
generate_studies_templates()
generate_translation_templates()

print("\n" + str(len(STUDY_LIST)) + " studies processed")

