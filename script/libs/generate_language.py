#!/usr/bin/env python3
import sys
import gettext
import polib
from context import *
from libs.pipeline_classes import *
from libs.utils import *

class FallbackTranslation(gettext.NullTranslations):
    def __init__(self):
        super(FallbackTranslation, self).__init__()
        self.counter = 0
    def gettext(self, msg):
        self.counter += 1;    
        return msg

def generate_language(language):
    print("GENERATING LANGUAGE [" + language + "]")
    src_studies = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    dst_studies = ROOT + WWW + STUDIES

    po = polib.pofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".po")
    po.save_as_mofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".mo")

    #gettext.find(FP_DOMAIN, ROOT + LANG, language)
    translation = gettext.translation(FP_DOMAIN, localedir = ROOT + LANG, languages = [language])
    missed = FallbackTranslation()
    translation.add_fallback(missed)
    recreate_dir(dst_studies + "/" + language)
    nMissedTotal = 0
    nTermsTotal = 0
    for study in STUDY_LIST:
        print(study.name, end = '')
        study_filename = study.name + '.html'
        with open(src_studies + "/" + study_filename) as input_file:
            text = input_file.read()
        parser = ParserSource(text)
        with open(dst_studies + "/" + language + "/" + study.name + ".html", "w") as out_file:
            dispatcher = DispatcherSinkSource()
            parser.sink = dispatcher
            dispatcher.processor = POEntryGeneratorSink(study_filename)
            translator = TranslatorSinkSource()
            translator.language = translation
            dispatcher.sink = translator
            writer = WriterSink(out_file)
            translator.sink = writer
            missed.counter = 0
            parser.go()
            
            nTerms = translator.getNTerms()
            nMissed = missed.counter
            print(' ', str(nTerms - nMissed) + '/' + str(nTerms))
            nTermsTotal += nTerms
            nMissedTotal += nMissed
        sys.exit()
    print('TOTAL:', str(nTermsTotal - nMissedTotal) + '/' + str(nTermsTotal))
    print()

                
            
            
            
