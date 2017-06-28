#!/usr/bin/env python3
import os

SCRIPTURES_DIR = "../www/studies/english/scriptures"
USD21_LINK = "http://www.usd21.org/"

def get_link(text):
    link_index = text.find(USD21_LINK)
    link_end_index = text.find('"', link_index)
    link = text[link_index:link_end_index]
    return [link_index, link_end_index, link]

def change_link(link):
    scripture_name_start = link.rfind("/")+1
    scripture_name_end = link.rfind(".html")
    scripture_name = link[scripture_name_start:scripture_name_end]
    name_parts = scripture_name.split('-')
    num_count = 0
    while name_parts[len(name_parts) - 1 - num_count].isdigit():
        num_count += 1
    if num_count < 1 or num_count > 4:
        return text
    nums_index = len(name_parts) - 1 - num_count
    book_name = "_".join(name_parts[:nums_index+1])
    new_scripture_name = book_name + "+" + name_parts[nums_index - 1]
    for i in range(1, num_count):
        new_scripture_name += "-" if i == 2 else "%3A"
        new_scripture_name += name_parts[nums_index + i]
    link = "https://www.biblegateway.com/passage/?version=NIV&interface=print&search=" + new_scripture_name
    return link

def insert_links(filename, text):
    [link_index, link_end_index, link] = get_link(text)
    text = text[:link_index] + change_link(link) + text[link_end_index:]
    return text

for filename in os.listdir(SCRIPTURES_DIR):
    with open(os.path.join(SCRIPTURES_DIR, filename), "r+") as file:
        text = file.read()
        file.seek(0)
        new_text = insert_links(filename, text)
        file.write(new_text)
