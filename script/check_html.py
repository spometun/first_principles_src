#!/usr/bin/env python3
import sys
from libs.pipeline_classes import *
from context import *

def purify(text):
    text = text.strip()
    if(text[:6] == '&nbsp;'):
        return purify(text[6:])
    if(text[-6:] == '&nbsp;'):
        return purify(text[:-6])
    if(text[:6] == '&copy;'):
        return purify(text[6:])

    return text
    
        
class PrinterSink2:
    def __init__(self):
        self.counter = 0
        self.line_number = 1
    def on_input(self, text):
        self.counter += 1
        self.line_number += text.count('\n')
        if(self.counter % 2):
            text = purify(text)
            if(text == ''):
                return
            if(text[:3] == '_("' and text[-2:] == '")'):
                return
            print(text)


def check_html(file_name):
#    print(file_name)
    with open(file_name, encoding=ENCODING) as input_file:
        input_text = input_file.read()
    parser = ParserSource(input_text, '<', '>')
    parser.sink = PrinterSink2()
    parser.go()
    
 
check_html(sys.argv[1]) 
 

