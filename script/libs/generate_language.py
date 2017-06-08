#!/usr/bin/env python3
import errno
import sys
import gettext
import polib
import shutil
from context import *
from libs.pipeline_classes import *
from libs.utils import *

ENCODING = "UTF-8"

def generate_language(language, dst_folder):
    print("GENERATING LANGUAGE [" + language + "]")
    src_studies = dst_folder + TEMPLATE + WWW + STUDIES + ENGLISH
    dst_studies = dst_folder + WWW + STUDIES

    flag_img_folder = dst_folder + WWW + "/images/flags"
    try:
        os.mkdir(flag_img_folder);
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise
        pass
    shutil.copy(ROOT + LANG + "/" + language + "/flag.png", flag_img_folder + "/" + language + ".png");

    poFile = polib.pofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".po")
#    poFile.save_as_mofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".mo")
    translator = TranslatorSinkSource(poFile)

    #gettext.find(FP_DOMAIN, ROOT + LANG, language)
    #translation = gettext.translation(FP_DOMAIN, localedir = ROOT + LANG, languages = [language])
    #missed = FallbackTranslation()
    #translation.add_fallback(missed)
    recreate_dir(dst_studies + "/" + language)
    nMissedTotal = 0
    nTermsTotal = 0
    for study in STUDY_LIST:
        print(study.name, end = '')
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
            translator.sink = writer
            translator.nMissed = 0
            translator.nTerms = 0
            parser.go()
            
            nTerms = translator.nTerms
            nMissed = translator.nMissed
            print(' ', str(nTerms - nMissed) + '/' + str(nTerms))
            nTermsTotal += nTerms
            nMissedTotal += nMissed
#        sys.exit()
    print('TOTAL:', str(nTermsTotal - nMissedTotal) + '/' + str(nTermsTotal))
    print()

                
            
            
            
