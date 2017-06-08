#!/usr/bin/env python3
import datetime
import os
import shutil
import polib
import sys
from context import *
from libs.utils import *
from libs.generate_html_template import *
from libs.pipeline_classes import *

ENCODING = "UTF-8"
if len(sys.argv) != 3 or (sys.argv[2] != "mobile" and sys.argv[2] != "web"):
    print('Usage: {} <destination_path> <mobile|web>'.format(sys.argv[0]))
    sys.exit()
DST_FOLDER = sys.argv[1]
IS_BUILD_MOBILE = sys.argv[2] == 'mobile'

def prepare_dst_folder():
    dst_path = DST_FOLDER + TEMPLATE
    recreate_dir(dst_path)
    recreate_dir(dst_path + WWW)
    copy_fixed_stuff(ROOT + SRC + WWW, dst_path + WWW)
    shutil.copy(ROOT + LANGUAGES_FILE, dst_path + WWW)
    os.mkdir(dst_path + WWW + STUDIES)
    os.mkdir(dst_path + WWW + STUDIES + ENGLISH)
    os.mkdir(dst_path + LANG)
    os.mkdir(dst_path + LANG + ENGLISH_TEMPLATE)

def generate_studies_templates():
    print("GENERATING STUDIES TEMPLATES")
    src = ROOT + SRC + WWW
    dst = DST_FOLDER + TEMPLATE + WWW + STUDIES + ENGLISH
    for study in STUDY_LIST:
        print(study.name)
        generateStudy(src, dst, study, IS_BUILD_MOBILE)    




def generate_pot(path_to_studies, study_name):
    study_filename = os.path.join(path_to_studies, study_name + '.html')
    with open(study_filename, encoding=ENCODING) as input_file:
        input_text = input_file.read()
    parser = ParserSource(input_text, '_("', '")')
    dispatcher = DispatcherSinkSource()
    parser.sink = dispatcher
    dispatcher.processor = POEntryGeneratorSink(study_name + '.html')
    poFileGenerator = POFileGeneratorSink()
    dispatcher.sink = poFileGenerator
    parser.go()
    return poFileGenerator.pot



def post_process_po(output_folder, study_name):
    global g_terms_dict
    study_name = cut_front_number(study_name)
    po = polib.pofile(output_folder + "/" + study_name + ".pot")
    for entry in po:
        if entry.msgid not in g_terms_dict:
            g_terms_dict[entry.msgid] = [study_name]
        else:
            g_terms_dict[entry.msgid].append(study_name)


def generate_translation_templates():
    path_to_studies = DST_FOLDER + TEMPLATE + WWW + STUDIES + ENGLISH
    output_folder =  DST_FOLDER + TEMPLATE + LANG + ENGLISH_TEMPLATE
    studies_pot = []

    print("\nPARSING TRANSLATION TEMPLATES")
    for study in STUDY_LIST:
        print(study.name)
        study_pot = generate_pot(path_to_studies, study.name)
        studies_pot.append((study.name, study_pot))

    print("\nGENERATING TRANSLATION CATALOG")        
    terms = {}
    for name, study_pot in studies_pot:
        value = 1
        if cut_front_number(name) == 'index':
            value = -1000  # reuse translation of any term from index.html
        for entry in study_pot:
            term = entry.msgid
            if term not in terms:
                terms[term] = value
            else:
                terms[term] += value
                
    all_studies_file = polib.POFile(check_for_duplicates = True, wrapwidth = 0)
    all_added_entries = {}  # to add repeated terms only once
    for name, study_pot in studies_pot:
        print(name)
        study_file = polib.POFile(check_for_duplicates = True, wrapwidth = 0)
        study_added_entries = {}  # to add repeated terms only once
        for entry in study_pot:
            if terms[entry.msgid] <= 1:
                entry.msgctxt = None
            if (entry.msgid, entry.msgctxt) not in study_added_entries:
                study_file.append(entry)
                study_added_entries[(entry.msgid, entry.msgctxt)] = True
            if (entry.msgid, entry.msgctxt) not in all_added_entries:
                all_studies_file.append(entry)
                all_added_entries[(entry.msgid, entry.msgctxt)] = True
        study_file.save(output_folder + '/' + name + ".pot")    
    all_studies_file.save(output_folder + '/' + FP_DOMAIN + ".pot")    


g_terms_dict = {};  
prepare_dst_folder()
generate_studies_templates()
generate_translation_templates()


print("\n" + str(len(STUDY_LIST)) + " studies processed")
with open('logs.txt', 'a') as f:
    datetime_str = datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S: ')
    f.write(datetime_str + 'Teplate generation\n');
