import sys
import gettext
import polib
from context import *
from libs.pipeline_classes import *
from libs.utils import *

def generate_language(language):
    print("GENERATING LANGUAGE [" + language + "]")
    src_studies = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    dst_studies = ROOT + WWW + STUDIES

    po = polib.pofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".po")
    po.save_as_mofile(ROOT + LANG + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".mo")

    #gettext.find(FP_DOMAIN, ROOT + LANG, language)
    translation = gettext.translation(FP_DOMAIN, localedir = ROOT + LANG, languages=[language])
    recreate_dir(dst_studies + "/" + language)

    for study in STUDY_LIST:
        print(study.name)
        with open(src_studies + "/" + study.name + ".html") as input_file:
            text = input_file.read()
        parser = ParserSource(text)
        with open(dst_studies + "/" + language + "/" + study.name + ".html", "w") as out_file:
            writer = WriterSink(out_file)
            translator = TranslatorSinkSource()
            translator.language = translation
            parser.sink = translator
            translator.sink = writer
            parser.go()
