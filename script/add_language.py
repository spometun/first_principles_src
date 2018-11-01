#!/usr/bin/env python3
import os
import sys
from context import *
from libs.utils import *

if (len(sys.argv) != 4 or sys.argv[3][-4:] != ".png"):
    print('Usage: {} <language> <poeditor_language_id> <flag_file>'.format(sys.argv[0]))
    print('<flag_file> must have .png extention')
    sys.exit()

flag_path = sys.argv[3]
if (not os.path.isfile(flag_path)):
    print("Coudn't find regular file: " + flag_path);
    sys.exit()
    
language_id = sys.argv[2]
language = sys.argv[1]

lang_dir = ROOT + LANG + '/' + language
if os.path.exists(lang_dir):
    print('{} already exists'.format(lang_dir))
    sys.exit()

os.mkdir(lang_dir)
os.mkdir(lang_dir + LC_MESSAGES)
shutil.copyfile(ROOT + LANG + ENGLISH_TEMPLATE + '/' + FP_DOMAIN + '.pot', lang_dir + LC_MESSAGES + '/' + FP_DOMAIN + '.po')
shutil.copyfile(flag_path, lang_dir + '/' + FLAG_FILE_NAME)
with open(lang_dir + '/' + POEDITOR_LANGUAGE_ID_FILE, 'w') as language_id_file:
    language_id_file.write(language_id)
    
languages_list = []
with open(ROOT + LANGUAGES_FILE) as languages_file:
    languages_list = json.load(languages_file)
    if language not in languages_list:
        languages_list.append(language)
        languages_file.close()
        with open(ROOT + LANGUAGES_FILE, 'w') as outfile:
            json.dump(languages_list, outfile)

print('Lanugage [' + language + '] added to lang/\nTo finish adding language you need:')
print('1. Commit and push lang/ repository')
print('2. Go to poeditor.com, find GitHub Integration page, and integrate ' + language + '/LC_MESSAGES/' + FP_DOMAIN + '.po to poeditor')
print('3. Deploy changes')

  
