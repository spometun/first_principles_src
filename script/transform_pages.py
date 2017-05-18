"""
    Automatic transforming html to template
        deletes spans and scripts
        takes only childs of div with data-role=content
        wraps all not whitespace strings with _("")

"""

from bs4 import BeautifulSoup

with open("../old_www/mission.html", "r") as file:
    html = file.read()

def remove_spans(soup):
    for span in soup("span"):
        span.replace_with(span.contents[0])

def remove_scripts(soup):
    for script in soup("script"):
        script.decompose()

def wrap_strings(soup):
    for string in soup(string=True):
        if not (string.isspace()):
            string.replace_with('_("{}")'.format(string))
        
soup = BeautifulSoup(html, "html.parser")
soup = soup.find("div", **{"data-role": "content"})
remove_spans(soup)
remove_scripts(soup)
wrap_strings(soup)

with open("test_page.html", "w") as file:
    for child in soup.children:
        if hasattr(child, "prettify"):
            file.write(child.prettify())

