class ParserSource:
    def __init__(self, text):
        self.text = text
    def output(self, text):
        self.sink.on_input(text)
    def go(self):
        level1 = self.text.split("_(\"")
        self.output(level1.pop(0))
        for pair in level1:
            terms = pair.split("\")")
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
    def __init__(self):
        self.counter = 0
    def output(self, text):
        self.sink.on_input(text)
    def on_input(self, text):
        if(self.counter == 0):
            self.output("# First Principles translation")
        if(self.counter % 2):
            self.output("\nmsgid " + "\"" + text + "\"")
            self.output("\nmsgstr " + "\"" + "\"")
        self.counter += 1




