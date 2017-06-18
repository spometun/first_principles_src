#!/usr/bin/env python3
import errno
import sys
import gettext
import json
import polib
import shutil
from context import *
from libs.pipeline_classes import *
from libs.utils import *

ENCODING = "UTF-8"

def get_language_url(language, study_name):
    with open(ROOT + LANG + "/" + language + "/" + POEDITOR_LANGUAGE_ID_FILE) as f:
        language_id = str(json.load(f))
        study_name = str(STUDY_TAGS[study_name])
        return POEDITOR_PROJECT_URL + "&id_language=" + language_id + "&tags%5B%5D=" + study_name

def generate_language(language, dst_folder):
    print("GENERATING LANGUAGE [" + language + "]")
    src_studies = dst_folder + TEMPLATE + WWW + STUDIES + ENGLISH_TEMPLATE
    dst_studies = dst_folder + WWW + STUDIES

    poFile = polib.pofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".po")
    translator = TranslatorSinkSource(poFile)

    recreate_dir(dst_studies + "/" + language)
    nMissedTotal = 0
    nTermsTotal = 0
    for study in STUDY_LIST:
        print(study.name, end = '')

        language_url = get_language_url(language, study.name)
        substitutor = SubstitutorSinkSource(POEDITOR_IMPROVE_TRANSLATION_ID, language_url, 1)

        study_filename = study.name + '.html'
        with open(src_studies + "/" + study_filename, encoding=ENCODING) as input_file:
            text = input_file.read()
        parser = ParserSource(text, '_("', '")')
        with open(dst_studies + "/" + language + "/" + study.name + ".html", "w", encoding=ENCODING) as out_file:
            dispatcher = DispatcherSinkSource()
            parser.sink = dispatcher
            dispatcher.processor = POEntryGeneratorSink(study_filename)
            dispatcher.sink = translator
            writer = WriterSink(out_file)
            translator.sink = substitutor
            translator.nMissed = 0
            translator.nTerms = 0
            substitutor.sink = writer
            parser.go()
            
            nTerms = translator.nTerms
            nMissed = translator.nMissed
            print(' ', str(nTerms - nMissed) + '/' + str(nTerms))
            nTermsTotal += nTerms
            nMissedTotal += nMissed
    print('TOTAL:', str(nTermsTotal - nMissedTotal) + '/' + str(nTermsTotal))
    print()

                
            
            
            
