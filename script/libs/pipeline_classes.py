#!/usr/bin/env python3
import polib
import sys
from libs.utils import *

class ParserSource:
    def __init__(self, text, tag_open, tag_close):
        self.text = text
        self.tag_open = tag_open
        self.tag_close = tag_close
    def output(self, text):
        self.sink.on_input(text)
    def go(self):
        level1 = self.text.split(self.tag_open)
        self.output(level1.pop(0))
        for pair in level1:
            terms = pair.split(self.tag_close)
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
    

class NullSink:
    def on_input(self, text):
        return

class WriterSink:
    def __init__(self, file):
        self.file = file
    def on_input(self, text):
        self.file.write(text)
    def __del__(self):
        self.file.close()

class SubstitutorSinkSource:
    def __init__(self, old_sub_str, new_sub_str, expected_count):
        self.old = old_sub_str
        self.new = new_sub_str
        self.expected_count = expected_count
        self.nSubstituted = 0
    def on_input(self, text):
        new_text = text.replace(self.old, self.new)
        self.nSubstituted += int(text != new_text)
        self.sink.on_input(new_text)
    def __del__(self):
        if self.nSubstituted != self.expected_count:
            print("WARNING: Wrong number of substitution for " + self.old + " ( nSubstitutions = " + str(self.nSubstituted) + " while expected = " + str(self.expected_count) + ")\n")

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
                    message = '{}  [{}:{}]'.format(data.msgid, data.occurrences[0][0], data.occurrences[0][1])
                    sys.stdout.buffer.write(message.encode('utf8'))
                    translated_text = '_("' + data.msgid + '")'
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




