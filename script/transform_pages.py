"""
    Automatic transforming html to template
        deletes spans and scripts
        takes only childs of div with data-role=content
        wraps all not whitespace strings with _("")

"""

from bs4 import BeautifulSoup
import os
import json

ROOT = ".."
HTML_DIR = "old_www"
WWW_DIR = "www"
STUDIES_LIST_FILE = "studies_list.json"
STUDIES_DIR = "studies"
LANGUAGE = "english"

HTML_DIR_PATH = os.path.join(ROOT, HTML_DIR)
WWW_DIR_PATH = os.path.join(ROOT, WWW_DIR)
STUDIES_LIST_PATH = os.path.join(WWW_DIR_PATH, STUDIES_LIST_FILE)
STUDIES_DIR_PATH = os.path.join(WWW_DIR_PATH, STUDIES_DIR, LANGUAGE)

def get_html(filename):
    with open(os.path.join(HTML_DIR_PATH, filename), "r") as file:
        html = file.read()
    return html

def save_template(filename, template):
    with open(os.path.join(STUDIES_DIR_PATH, filename), "w") as file:
        file.write(template)

def remove_spans(soup):
    for span in soup("span"):
        span.replace_with(span.contents[0])

def remove_scripts(soup):
    for script in soup("script"):
        script.decompose()

def wrap_strings(soup):
    for string in soup(string=True):
        if not (string.isspace()):
            parent = string.parent
            if not ("data-rel" in parent.attrs) or parent["data-rel"] != "dialog":
                string.replace_with('_("{}")'.format(string))

def transformPage(html):
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find("div", **{"data-role": "content"})
    remove_spans(content_div)
    remove_scripts(content_div)
    wrap_strings(content_div)
    return "\n".join([child.prettify() for child in content_div.children
                                       if hasattr(child, "prettify")
                     ]), soup.title.string

def from_html_file_to_template_file(filename):
    print(filename)
    html = get_html(filename)
    template, title = transformPage(html)
    save_template(filename, template)
    with open(STUDIES_LIST_PATH, "r+") as file:
        studies_list = json.loads(file.read())
        studies_list[os.path.splitext(filename)[0]] = title
        file.seek(0)
        file.write(json.dumps(studies_list, sort_keys=True, indent=4))
        file.truncate()

pages = [
    "mission.html",
    "cross.html",
    "best_friends_of_all_time.html",
    "church.html",
    "persecution.html",
    "miraculous_gifts_of_the_holy_spirit.html",
    "medical_account.html",
    "christ_is_your_life.html",
    "book_of_acts.html",
    "memory_scriptures.html",
    "after_baptism_now_what.html",
    "baptism_with_the_holy_spirit.html",
    "contact_us.html",
    "new_testament_conversion.html",
];
list(map(from_html_file_to_template_file, pages))
