#!/usr/bin/env python3
import polib
from libs.utils import *

class ParserSource:
    def __init__(self, text):
        self.text = text
    def output(self, text):
        self.sink.on_input(text)
    def go(self):
        level1 = self.text.split('_("')
        self.output(level1.pop(0))
        for pair in level1:
            terms = pair.split('")')
            if(len(terms) != 2) :
                error_msg = "parsing error near\n " + pair + "\nlen(terms)= " + str(len(terms))
                raise RuntimeError(error_msg)
            self.output(terms[0])
            self.output(terms[1])


class DispatcherSinkSource:
    def __init__(self):
        self.counter = 0
        self.line_number = 1
    def on_input(self, text):
        self.line_number += text.count('\n')
        if(self.counter % 2):
            self.processor.on_input(text, self.line_number)
            result = self.processor.state
        else:
            result = text
        self.sink.on_input(result)
        self.counter += 1
    



class WriterSink:
    def __init__(self, file):
        self.file = file
    def on_input(self, text):
        self.file.write(text)
    def __del__(self):
        self.file.close()


class POEntryGeneratorSink:
    def __init__(self, file_name):
        self.file_name = file_name
        self.term_counter = {}
    def on_input(self, text, line_number):
        if text not in self.term_counter:
            self.term_counter[text] = 1
        else:
            self.term_counter[text] += 1
        context = cut_html_extension(cut_front_number(self.file_name))  + ' #' + str(self.term_counter[text])
        self.state = polib.POEntry(msgid = text, linenum = str(line_number),
         occurrences = [(self.file_name, line_number)], msgctxt = context)


class TranslatorSinkSource:
    def __init__(self, poFile):
        self.nTerms = 0
        self.nMissed = 0
        self.translation = {}
        for entry in poFile:
            self.translation[(entry.msgid, entry.msgctxt)] = entry.msgstr
    def on_input(self, data):
        translated_text = ''
        if(isinstance(data, str)):
            translated_text = data
        else:
            if (data.msgid, data.msgctxt) in self.translation:
                translated_text = self.translation[(data.msgid, data.msgctxt)]                
            else:
                if (data.msgid, None) in self.translation:
                    translated_text = self.translation[(data.msgid, None)]                
                else:
                    print('\n\n********************** WARNING **********************')
                    print('couldn\'t find translation for:')
                    print('msgid =' + data.msgid + '   [at file', data.occurrences[0][0], ' line:', data.occurrences[0][1], ']')
            self.nTerms += 1
            if translated_text == '':
                translated_text = data.msgid
                self.nMissed += 1                                   
        self.sink.on_input(translated_text)


class POFileGeneratorSink:
    def __init__(self):
        self.pot = []
    def on_input(self, data):
        if(isinstance(data, polib.POEntry)):
             self.pot.append(data)                              




