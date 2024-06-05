import json
import defs

this_file = "course_file.py"

def import_language_from_json(file_path):
    # Initial Checks
    try:
        course_file = open(file_path, "r")
    except OSError:
        print(f"ERROR ({this_file}): Course file could not be opened.")
        return 0

    course_data = json.loads(course_file.read())
    
    no_dict = False

    if (not "Language" in course_data.keys()):
        print(f"ERROR ({this_file}): Language name missing in course file.")
        return 0
    
    if (not "From" in course_data.keys()):
        print(f"ERROR ({this_file}): Origin language missing in course file.")
        return 0
    
    if (not "Dictionary" in course_data.keys()):
        print(f"WARNING ({this_file}): Dictionary data not found.")

    print("File opened successfully.")

    # Loading Data
    new_lang = defs.Language()
    new_lang.official_name = course_data["Language"]
    new_lang.from_name = course_data["From"]
    if (no_dict == False):
        try:
            for i in course_data["Dictionary"].keys():
                word_location = course_data["Dictionary"][i]
                new_word = i
                new_lang.dictionary[new_word] = defs.Word()
                new_lang.dictionary[new_word].translations = word_location["Meaning"]
                new_lang.dictionary[new_word].word_class = word_location["Class"]
                new_lang.dictionary[new_word].word_subclass = word_location["Sub-Class"]
                new_lang.dictionary[new_word].composition = word_location["Composition"]
                new_lang.dictionary[new_word].article = word_location["Article"]
        except:
            print(f"ERROR ({this_file}): Failed to parse dictionary data.")
            return 0

    # Returning
    print("Finished loading data, printing result:\n")
    print(f"Language: {new_lang.official_name}")
    print(f"Learning from: {new_lang.from_name}")
    if (no_dict == False):
        print("List of words:")
        for i in new_lang.dictionary.keys():
            print(f" - {i}")

    return new_lang