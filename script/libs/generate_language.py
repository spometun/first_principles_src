import sys
sys.path.insert(0,'/usr/lib/python3/dist-packages/')
import gettext
import polib
from context import *
from libs.pipeline_classes import *
from libs.utils import *

def generate_language(language):
    lang_root = ROOT + LANG
    src_studies = ROOT + TEMPLATE + WWW + STUDIES + ENGLISH
    dst_studies = ROOT + WWW + STUDIES

    po = polib.pofile(lang_root + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".po")
    po.save_as_mofile(lang_root + "/" + language + "/LC_MESSAGES/" + FP_DOMAIN + ".mo")

    gettext.find(FP_DOMAIN, lang_root, language)
    translation = gettext.translation(FP_DOMAIN, localedir=lang_root, languages=[language])
    print(translation)
    print(translation.gettext("God knows your needs"))
    print(translation.gettext("Hello World"))
    recreate_dir(dst_studies + "/" + language)
    
    input_file = open(src_studies + "/seeking_god.html")
    text = input_file.read()
    parser = ParserSource(text)
    out_file = open(dst_studies + "/" + language + "/" + "/seeking_god.html", "w")
    writer = WriterSink(out_file)
    translator = TranslatorSinkSource()
    translator.language = translation
    parser.sink = translator
    translator.sink = writer
    parser.go()
