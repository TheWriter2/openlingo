class Word:
    def __init__(self):
        self.word = ""
        self.translations = [""]
        self.word_class = ""
        self.word_subclass = ""
        self.radical = ""
        self.article = ""

class Language:
    def __init__(self):
        self.dictionary = {}
        self.from_name = ""
        self.official_name = ""

class Lesson:
    def __init__(self):
        pass

def import_lang(file):
    fhandle = open(file, "r")
    contents = fhandle.readlines()
    new_lang = Language()
    temp_raw = ""
    temp_code = ""
    temp_dict_pointer = 0
    temp_word = Word()

    if ("lang:" in contents and "from:" in contents and "code:" in contents):
        temp_raw = contents[contents.index("lang:")]
        new_lang.official_name = temp_raw.split(":")[1].strip()

        temp_raw = contents[contents.index("lang:")]
        new_lang.from_name = temp_raw.split(":")[1].strip()

        temp_raw = contents[contents.index("code:")]
        temp_code = temp_raw.split(":")[1].strip()
    else:
        return 1

    if ("dict:" in contents):
        temp_dict_pointer = contents.index("dict:")

        for i in range(temp_dict_pointer + 1, len(contents)):
            temp_raw = contents[i]
            
            temp_word = Word()
            temp_word.word = temp_raw.split(",")[0].lower()