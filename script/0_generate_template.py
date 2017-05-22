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
    os.mkdir(dst_path + LANG)
    os.mkdir(dst_path + LANG + ENGLISH_TEMPLATE)

def generate_studies_templates():
    print("GENERATING STUDIES TEMPLATES")
    src = ROOT + SRC + WWW
    dst = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    for study in STUDY_LIST:
        print(study.name)
        generateStudy(src, dst, study)    


def cut_front_number(filename):
    return filename.split("_", 1)[1];


def generate_po(path_to_studies, output_folder, study_name):
    input_file = open(path_to_studies + "/" + study_name + ".html")
    input_text = input_file.read()
    out_file_name = output_folder + "/" + cut_front_number(study_name) + ".pot"
    out_file = open(out_file_name, "w")
    writer = WriterSink(out_file)
    parser = ParserSource(input_text)
    po_generator = POGeneratorSinkSource(study_name + ".html")
    parser.sink = po_generator
    po_generator.sink = writer
    parser.go()


def post_process_po(output_folder, study_name):
    global g_terms_dict
    study_name = cut_front_number(study_name)
    po = polib.pofile(output_folder + "/" + study_name + ".pot")
    for entry in po:
        if entry.msgid not in g_terms_dict:
            g_terms_dict[entry.msgid] = [study_name]
        else:
            g_terms_dict[entry.msgid].append(study_name)

 #   po.save(out_file_name + "2")


def generate_translation_templates():
    print("\nGENERATING TRANSLATION TEMPLATES")
    path_to_studies = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    output_folder =  ROOT + TEMPLATE + LANG + ENGLISH_TEMPLATE
    for study in STUDY_LIST:
        print(study.name)
        generate_po(path_to_studies, output_folder, study.name)
        post_process_po(output_folder, study.name)
    print("\n\nREPEATED TERMS (except index):\n")
    for key in g_terms_dict:
        studies = g_terms_dict[key]
        if(len(studies) >= 2 and studies.count("index") == 0):
            print(key, "    ", studies)

g_terms_dict = {};  
prepare_dst_folder()
generate_studies_templates()
generate_translation_templates()


print("\n" + str(len(STUDY_LIST)) + " studies processed")

