import sys
sys.path.insert(0,'/usr/lib/python3/dist-packages/')
import gettext
import polib                
from libs.pipeline_classes import *
from libs.utils import *

def generate_language(root, language):
    lang_root = root + "/lang"
    src_studies = root + "/template/www/studies/english"
    dst_studies = root + "/www/studies"

    po = polib.pofile(lang_root + "/" + language + "/LC_MESSAGES/first_principles.po")
    po.save_as_mofile(lang_root + "/" + language + "/LC_MESSAGES/first_principles.mo")

    gettext.find("first_principles", lang_root, language)
    translation = gettext.translation("first_principles", localedir=lang_root, languages=[language])
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
