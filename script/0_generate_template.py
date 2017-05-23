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

def generate_pot(path_to_studies, study_name):
    input_file = open(path_to_studies + "/" + study_name + ".html")
    input_text = input_file.read()
    parser = ParserSource(input_text)
    po_generator = POGeneratorSink(study_name + ".html")
    parser.sink = po_generator
    parser.go()
    return po_generator.pot



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
    path_to_studies = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    output_folder =  ROOT + TEMPLATE + LANG + ENGLISH_TEMPLATE
    studies_pot = []

    print("\nPARSING TRANSLATION TEMPLATES")
    for study in STUDY_LIST:
        print(study.name)
        study_pot = generate_pot(path_to_studies, study.name)
        studies_pot.append((study.name, study_pot))

    print("\nGENERATION TRANSLATION CATALOG")        
    terms = {}
    for name, study_pot in studies_pot:
        for entry in study_pot:
            term = entry.msgid
            if term not in terms:
                terms[term] = 1
            else:
                terms[term] += 1
                
    all_studies_file = polib.POFile(check_for_duplicates = True, wrapwidth = 0)   
    for name, study_pot in studies_pot:
        print(name)
        study_file = polib.POFile(check_for_duplicates = True, wrapwidth = 0)
        for entry in study_pot:
            if terms[entry.msgid] >= 2:
                entry.msgctxt = name  + '.html line:' + entry.linenum
            study_file.append(entry)
            all_studies_file.append(entry)
        study_file.save(output_folder + '/' + name + ".pot")    
    all_studies_file.save(output_folder + '/' + FP_DOMAIN + ".pot")    
    

g_terms_dict = {};  
prepare_dst_folder()
generate_studies_templates()
generate_translation_templates()


print("\n" + str(len(STUDY_LIST)) + " studies processed")

