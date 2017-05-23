#!/usr/bin/env python3
import polib

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


class WriterSink:
    def __init__(self, file):
        self.file = file
    def on_input(self, text):
        self.file.write(text)
    def __del__(self):
        self.file.close()


class TranslatorSinkSource:
    def __init__(self):
        self.counter = 0
    def on_input(self, text):
        if(self.counter % 2):
            translated_text = self.language.gettext(text)
        else:
            translated_text = text
        self.sink.on_input(translated_text)
        self.counter += 1


class POGeneratorSinkSource:
    def __init__(self, file_name):
        self.counter = 0
        self.line_number = 0
        self.file_name = file_name
    def output(self, text):
        self.sink.on_input(text)
    def on_input(self, text):
        self.line_number += text.count('\n')
        if(self.counter == 0):
            self.output('# First Principles translation')
        if(self.counter % 2):
            text = text.replace('"', '\\"')
            self.output('\n#: ' + self.file_name + ':' + str(self.line_number))
            self.output('\nmsgid ' + '"' + text + '"')
            self.output('\nmsgstr ' + '"' + '"')
        self.counter += 1


class POGeneratorSink:
    def __init__(self, file_name):
        self.counter = 0
        self.line_number = 0
        self.file_name = file_name
        self.pot = []
    def output(self, text):
        self.sink.on_input(text)
    def on_input(self, text):
        self.line_number += text.count('\n')
#        if(self.counter == 0):
#            self.output('# First Principles translation')
        if(self.counter % 2):
#            text = text.replace('"', '\\"')
             poEntry = polib.POEntry(msgid = text, linenum = str(self.line_number), occurrences = [(self.file_name, self.line_number)])
             self.pot.append(poEntry)                              
#            self.output('\n#: ' + self.file_name + ':' + str(self.line_number))
#            self.output('\nmsgid ' + '"' + text + '"')
#            self.output('\nmsgstr ' + '"' + '"')
        self.counter += 1





