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
if not os.path.isdir(DST_FOLDER):
    print('destination directory not found: ' + DST_FOLDER)
    sys.exit()
    

def prepare_dst_folder():
    dst_path = DST_FOLDER + TEMPLATE
    src_path = ROOT + SRC
    recreate_dir(dst_path)
    
    shutil.copytree(src_path + WWW, dst_path + WWW)
    recreate_dir(dst_path + WWW + STUDIES)
    os.mkdir(dst_path + WWW + STUDIES + ENGLISH_TEMPLATE)
    os.remove(dst_path + WWW + STUDIES_FILE)
    
    shutil.copy(ROOT + LANGUAGES_FILE, dst_path + WWW)
    with open(dst_path + WWW + JS + LANGUAGES_JS, 'w') as ofile:
        ofile.write("LANGUAGES = ");
        with open(ROOT + LANGUAGES_FILE) as ifile:
            ofile.write(ifile.read())
    if not IS_BUILD_MOBILE:
        os.system('mkdir -m 755 ' + dst_path + '/api')
        os.system('cp -r ../server/*.php ' + dst_path + '/api')
        os.system('chmod 644 ' + dst_path + '/api/*.php')
        os.system('touch ' + dst_path + '/api/last_update')
        os.system('pwd > ' + dst_path + '/api/src_path.txt')
        os.system('cp ../server/index.html ' + dst_path)


def generate_studies_templates():
    print("GENERATING STUDIES TEMPLATES")
    src = ROOT + SRC + WWW
    dst = DST_FOLDER + TEMPLATE + WWW + STUDIES + ENGLISH_TEMPLATE
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


def generate_pots_and_english_po():
    path_to_studies = DST_FOLDER + TEMPLATE + WWW + STUDIES + ENGLISH_TEMPLATE
    output_folder =  ROOT + LANG + ENGLISH_TEMPLATE
    studies_pot = []

    print("\nGENERATING TRANSLATION CATALOG")        
    for study in STUDY_LIST:
        study_pot = generate_pot(path_to_studies, study.name)
        studies_pot.append((study.name, study_pot))

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

    identity_translation = polib.POFile(check_for_duplicates = True, wrapwidth = 0)
    for entry in all_studies_file:
        entry.msgstr = entry.msgid   
        identity_translation.append(entry)
    identity_translation.save(ROOT + LANG + EN + LC_MESSAGES + '/' + FP_DOMAIN + ".po")
    
    
def write_flags():
    flag_img_folder = DST_FOLDER + TEMPLATE + WWW + "/images/flags"
    recreate_dir(flag_img_folder)
    for lang in LANGUAGES_LIST:
        shutil.copy(ROOT + LANG + "/" + lang + "/" + FLAG_FILE_NAME, flag_img_folder + "/" + lang + ".png");


g_terms_dict = {}
prepare_dst_folder()
generate_studies_templates()
generate_pots_and_english_po()
write_flags()


print("\n" + str(len(STUDY_LIST)) + " studies processed")

    
    

