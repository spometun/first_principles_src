#!/usr/bin/env python3
import datetime
import os
import shutil
import polib
import sys
from context import *
from libs.utils import *
from libs.generate import *
from libs.pipeline_classes import *

ENCODING = "UTF-8"
if len(sys.argv) != 1:
    print('Usage: {}'.format(sys.argv[0]))
    sys.exit()
    


# generate_pots
output_folder =  ROOT + LANG + ENGLISH_TEMPLATE
print('Generating translation templates into ' + output_folder, end = '')
studies_pot = []

for study in STUDY_LIST:
    study_template = generate_study_template(study, False)
    study_pot = generate_pot(study_template, study.name + '.html')
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

# generate english po
identity_translation = polib.POFile(check_for_duplicates = True, wrapwidth = 0)
for entry in all_studies_file:
    entry.msgstr = entry.msgid   
    identity_translation.append(entry)
identity_translation.save(ROOT + LANG + EN + LC_MESSAGES + '/' + FP_DOMAIN + ".po")
    

print(': ' + str(len(STUDY_LIST)) + " studies processed")

    
    

