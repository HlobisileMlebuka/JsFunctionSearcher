
def list_all_js_function_names(path_to_js_file):

    """This function does the following:
    1) opens a js file from a path on the user's hard drive, reads it and prints the rows of the files as a list of strings.
    2) it then iterates through the file, searching for all strings with the sting'function' as a substring
    3) it stores the results in a new list then searches for the names of functions in the js file, using 'function' as an identifier
    4) the patterns for the searches are formulated using regular expressions"""
    
    list_of_rows_with_functionsubstring = list_of_rows_with_the_word_function(path_to_js_file)
    
    functionnames = list_of_all_function_names(list_of_rows_with_functionsubstring)
      
    return functionnames
        


def list_of_rows_with_the_word_function(path_to_js_file):
    with open(path_to_js_file, "r") as jsfile:
        jsfilecontents = jsfile.readlines()
        
        list_of_rows_with_functionsubstring = [x for x in jsfilecontents if 'function' in x]
       
    return  list_of_rows_with_functionsubstring

def list_of_all_function_names(list_of_rows_with_functionsubstring):
    import re
    functionnames = []
    
    for name in list_of_rows_with_functionsubstring:
        if re.findall(r'(?<=function)\s\b.*\b(?=\()', name):
            pattern = re.findall(r'(?<=function\s)\b.*\b(?=\()', name)
            functionnames.append(pattern)
            
        else:
            pattern = re.findall(r'.*\b\s(?==\sfunction)', name)
            functionnames.append(pattern)
              
    return functionnames



if __name__ == "__main__":
    
    path_to_js_file = "/scriptjs/script.js"
    print(list_all_js_function_names(path_to_js_file))








            
            



    
        

        


