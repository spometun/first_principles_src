#!/usr/bin/env python3
import json
from collections import namedtuple

ROOT = "../.."
WWW = "/www"  # do not change, used by cordova (?)
LANG = "/lang"  # do not change, used by gettext (?)
API = "/api"
SRC = "/src"
ENGLISH_TEMPLATE = "/english_template"
STUDIES = "/studies"
AUDIO = "audio"
AUDIO_EXTENSIONS = ["m4a", "ogg", "mp3"]
AUDIO_MIME_TYPES = { "m4a": "audio/aac", "ogg": "audio/ogg", "mp3": "audio/mpeg" }
AUDIO_SOURCES_ID = "audio_sources"
AUDIO_CONTROLS_DISPLAY_ID = "audio_controls_display"
FP_DOMAIN = "first_principles"
ENCODING = "UTF-8"
LANGUAGES_FILE = "/languages.cfg"
LANGUAGES_JS = "/languages.js"
JS = "/js"
EN = "/en"
STUDIES_FILE = "/studies_list.json"
POEDITOR_IMPROVE_TRANSLATION_ID = "improve_translation_url"
POEDITOR_PROJECT_URL = "https://poeditor.com/projects/po_edit?id=106095"
POEDITOR_LANGUAGE_ID_FILE = "poeditor_id.json"
LC_MESSAGES = "/LC_MESSAGES"
FLAG_FILE_NAME = "flag.png"



STUDY_LIST = []
STUDY_TAGS = {}
Study = namedtuple("Study", "name title")

with open(ROOT + SRC + WWW + STUDIES_FILE) as data:
    studies = json.load(data)
for name in studies:
    STUDY_LIST.append(Study(name, studies[name]["title"]))
    STUDY_TAGS[name] = studies[name]["poeditor_tag"]
    STUDY_LIST.sort()
    
LANGUAGES_LIST = []
with open(ROOT + LANGUAGES_FILE) as data:
    LANGUAGES_LIST = json.load(data)


    

