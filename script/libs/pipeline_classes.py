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


class DispatcherSinkSource:
    def __init__(self):
        self.counter = 0
        self.line_number = 0
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
    def on_input(self, text, line_number):
        self.state = polib.POEntry(msgid = text, linenum = str(line_number), occurrences = [(self.file_name, line_number)])


class TranslatorSinkSource:
    def __init__(self):
        self.counter = 0
    def on_input(self, data):
        if(isinstance(data, str)):
            translated_text = text
        else:
            translated_text = self.language.gettext(text)
            self.counter += 1
        self.sink.on_input(translated_text)
    def getNTerms(self):
        return self.counter


class POFileGeneratorSink:
    def __init__(self):
        self.pot = []
    def on_input(self, data):
        if(isinstance(data, polib.POEntry)):
             self.pot.append(data)                              




