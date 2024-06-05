import defs
import course_file

if __name__ == "__main__":
    testing_file = course_file.import_language_from_json("courses/en_es.json")
    if (testing_file != 0):
        quit("\nNice :)")
    
    quit("\nSad :(")