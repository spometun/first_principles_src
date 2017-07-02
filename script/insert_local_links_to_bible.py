#!/usr/bin/env python3
import os

FILES_DIR = "../www/studies/english"
FILES = [ 
    "00_index.html",
    "01_introduction.html",
    "02_course_information.html",                 
    "03_book_of_john.html",                       
    "04_seeking_god.html",                        
    "05_word_of_god.html",                        
    "06_discipleship.html",                       
    "07_coming_of_the_kingdom.html",              
    "08_light_and_darkness.html",                 
    "09_new_testament_conversion.html",           
    "10_cross.html",                              
    "11_medical_account.html",                    
    "12_baptism_with_the_holy_spirit.html",       
    "13_miraculous_gifts_of_the_holy_spirit.html",
    "14_church.html",                             
    "15_book_of_acts.html",                       
    "16_after_baptism_now_what.html",             
    "17_christ_is_your_life.html",                
    "18_best_friends_of_all_time.html",           
    "19_mission.html",                            
    "20_persecution.html",                        
    "21_memory_scriptures.html",                  
    "22_contact_us.html",        
        ]

def insert_links(text):
    SCRIPTURES_PATTERN = 'href="scriptures/'
    href_index = text.find(SCRIPTURES_PATTERN)
    while href_index != -1:
        book_index = href_index + len(SCRIPTURES_PATTERN)
        book_end_index = text.find('"', book_index)
        new_book = text[book_index:book_end_index].replace("-", "_")
        text = text[:book_index] + new_book + text[book_end_index:]
        href_index = text.find(SCRIPTURES_PATTERN, href_index + 1)
    return text

for filename in FILES:
    with open(os.path.join(FILES_DIR, filename), "r+") as file:
        text = file.read()
        file.seek(0)
        new_text = insert_links(text)
        file.write(new_text)


