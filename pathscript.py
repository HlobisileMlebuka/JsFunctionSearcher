import os
import re

PATH = os.environ.get("JSPATH")


def list_of_rows_with_the_word_function(PATH):
    with open(PATH, "r") as jsfile:
        js_file_contents = jsfile.readlines()
        rows_with_functionsubstring = [x for x in js_file_contents if "function" in x]

    return rows_with_functionsubstring


def list_of_all_function_names(rows_with_functionsubstring):

    function_names = []


    for name in rows_with_functionsubstring:
        
        if re.findall(r"(?<=function)\s\b.*\b(?=\()", name):
            pattern = re.findall(r"(?<=function\s)\b.*\b(?=\()", name)
            function_names.append(pattern)

        else:
            pattern = re.findall(r".*\b\s(?==\sfunction)", name)
            function_names.append(pattern)
    
    #flatten list of lists
    return [item for sublist in function_names for item in sublist]    

def list_all_js_function_names(PATH):

    """This function does the following:
    1) opens a js file from a path on the user's hard drive, reads it and prints the rows of the files as a list of strings.
    2) it then iterates through the file, searching for all strings with the sting'function' as a substring
    3) it stores the results in a new list then searches for the names of functions in the js file, using 'function' as an identifier
    4) the patterns for the searches are formulated using regular expressions"""

    rows_with_functionsubstring = list_of_rows_with_the_word_function(PATH)

    function_names = list_of_all_function_names(rows_with_functionsubstring)

    return function_names


if __name__ == "__main__":

    print(list_all_js_function_names(PATH))


