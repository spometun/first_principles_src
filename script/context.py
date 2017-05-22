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

STUDY_LIST = []
Study = namedtuple("Study", "name title")

with open(ROOT + SRC + WWW + "/studies_list.json") as data:
    studies = json.load(data)
for name in studies:
    STUDY_LIST.append(Study(name, studies[name]))
    STUDY_LIST.sort()
    
    

