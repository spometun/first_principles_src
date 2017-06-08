#!/usr/bin/env python3
import json
from collections import namedtuple

ROOT = "../.."
WWW = "/www"  # do not change, used by cordova (?)
LANG = "/lang"  # do not change, used by gettext
SRC = "/src"
STUDIES = "/studies"
ENGLISH = "/english"
TEMPLATE = "/template"
ENGLISH_TEMPLATE = "/english_template"
FP_DOMAIN = "first_principles"
ENCODING = "UTF-8"
LANGUAGES_FILE = "/languages.cfg"
STUDIES_FILE = "/studies_list.json"

STUDY_LIST = []
Study = namedtuple("Study", "name title")

with open(ROOT + SRC + WWW + STUDIES_FILE) as data:
    studies = json.load(data)
for name in studies:
    STUDY_LIST.append(Study(name, studies[name]))
    STUDY_LIST.sort()
    
LANGUAGES_LIST = []
with open(ROOT + LANGUAGES_FILE) as data:
    LANGUAGES_LIST = json.load(data)


    

