
def list_all_js_function_names(path_to_js_file):

    """This function does the following:
    1) opens a js file from a path on the user's hard drive, reads it and prints the rows of the files as a list of strings.
    2) it then iterates through the file, searching for all strings with the sting'function' as a substring
    3) it stores the results in a new list then searches for the names of functions in the js file, using 'function' as an identifier
    4) the patterns for the searches are formulated using regular expressions"""
    
    functionlist = strings_with_function_substrings(path_to_js_file)
    
    funcnames = list_all_function_names(functionlist)
      
    return funcnames
        


def strings_with_function_substrings(path_to_js_file):
    with open(path_to_js_file, "r") as jsfile:
        # for jsfilelist in jsfile:
        jsfilecontents = jsfile.readlines()
        #print(jsfilecontents)

        functionlist = [x for x in jsfilecontents if 'function' in x]
            
    
    return functionlist

def list_all_function_names(functionlist):
    import re
    funcnames = []
    
    for name in functionlist:
        if re.findall(r'(?<=function)\s\b.*\b(?=\()', name):
            pattern = re.findall(r'(?<=function\s)\b.*\b(?=\()', name)
            funcnames.append(pattern)
            check = True
        else:
            pattern = re.findall(r'.*\b\s(?==\sfunction)', name)
            funcnames.append(pattern)
            check = True

            
    return funcnames, check



if __name__ == "__main__":
    
    path_to_js_file = "/home/hlobisile/tdd2/script.js"
    print(list_all_js_function_names(path_to_js_file))








            
            



    
        

        


