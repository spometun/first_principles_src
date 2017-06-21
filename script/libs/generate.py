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

def generate_study_template(study, is_show_update_controls):
    studies_folder = ROOT + SRC + WWW + "/studies"
    header_filename = "header_web.html" if is_show_update_controls else "header_mobile.html"
    study_filename = studies_folder + "/english/" + study.name + ".html"
	
    header_file = open(studies_folder + "/" + header_filename, "r", encoding = ENCODING)
    footer_file = open(studies_folder + "/footer.html", "r", encoding = ENCODING)
    study_file = open(study_filename, "r", encoding = ENCODING)

    header = header_file.read()
    header = header.replace("study_title", "_(\"" + study.title + "\")")
    header = header.replace("study_header", "_(\"" + study.title + "\")")
    footer = footer_file.read()
    body = study_file.read()
    
    header_file.close()
    footer_file.close()
    study_file.close()

    study = header + body + footer
    return study


def generate_pot(template, comment_file_name):
    parser = ParserSource(template, '_("', '")')
    dispatcher = DispatcherSinkSource()
    parser.sink = dispatcher
    dispatcher.processor = POEntryGeneratorSink(comment_file_name)
    poListGenerator = POListGeneratorSink()
    dispatcher.sink = poListGenerator
    parser.go()
    return poListGenerator.pot


def get_poeditor_url(language, study_name):
    with open(ROOT + LANG + "/" + language + "/" + POEDITOR_LANGUAGE_ID_FILE) as f:
        language_id = str(json.load(f))
        study_name = str(STUDY_TAGS[study_name])
        return POEDITOR_PROJECT_URL + "&id_language=" + language_id + "&tags%5B%5D=" + study_name


def translate_template(template, comment_file_name, translator, substitutor):
    parser = ParserSource(template, '_("', '")')
    dispatcher = DispatcherSinkSource()
    parser.sink = dispatcher
    dispatcher.processor = POEntryGeneratorSink(comment_file_name)
    dispatcher.sink = translator
    translator.sink = substitutor
    stringWriter = StringWriterSink()
    substitutor.sink = stringWriter
    translator.nMissed = 0
    translator.nTerms = 0
    parser.go()
    return stringWriter.text
    

def generate_language(language, dst_folder, is_show_update_controls):
    print("Generating language [" + language + "]", end = '')
    dst_studies = dst_folder + WWW + STUDIES

    poFile = polib.pofile(ROOT + LANG + "/" + language + LC_MESSAGES + "/" + FP_DOMAIN + ".po")
    translator = TranslatorSinkSource(poFile)

    recreate_dir(dst_studies + "/" + language)
    nMissedTotal = 0
    nTermsTotal = 0
    for study in STUDY_LIST:
#        print(study.name, end = '')

        poeditor_url = get_poeditor_url(language, study.name)
        substitutor = SubstitutorSinkSource(POEDITOR_IMPROVE_TRANSLATION_ID, poeditor_url)

        template = generate_study_template(study, is_show_update_controls)
        comment_file_name = study.name + '.html'
        translated = translate_template(template, comment_file_name, translator, substitutor)
        with open(dst_studies + "/" + language + "/" + study.name + ".html", "w", encoding = ENCODING) as out_file:
            out_file.write(translated)

        nTerms = translator.nTerms
        nMissed = translator.nMissed
#        print(' ', str(nTerms - nMissed) + '/' + str(nTerms))
        nTermsTotal += nTerms
        nMissedTotal += nMissed

    print(':', str(nTermsTotal - nMissedTotal) + '/' + str(nTermsTotal))
 

                
            
            
            
