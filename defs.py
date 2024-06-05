class Word:
    def __init__(self):
        self.translations = [""]
        self.word_class = ""
        self.word_subclass = ""
        self.composition = {
            "Complexity":0,
            "Base":[""]
        }
        self.article = ""

class Language:
    def __init__(self):
        self.dictionary = {}
        self.from_name = ""
        self.official_name = ""

class Lesson:
    def __init__(self):
        pass
