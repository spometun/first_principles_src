import gettext
from libs.pipeline_classes import *

src_root = "../../1_template_with_languages/"
dst_root = "../../2_multilanguage/"


#gettext.find("test", "lang", "ru")
ru = gettext.translation("seeking_god", localedir=src_root + "lang", languages=["ru"])
print(ru.gettext("God knows your needs"))
print(ru.gettext("Hello World"))

'''
input_file = open("../lessons/seeking_god_text.html")
text = input_file.read()
parser = ParserSource(text)
out_file = open("../generated/seeking_god.html", "w")
writer = WriterSink(out_file)
translator = TranslatorSinkSource()
translator.language = ru
parser.sink = translator
translator.sink = writer
parser.go()
'''