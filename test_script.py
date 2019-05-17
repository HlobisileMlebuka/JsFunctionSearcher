
from pathscript import strings_with_function_substrings, list_all_function_names, list_all_js_function_names

def test_strings_with_function_substrings():

    file_path = '/home/hlobisile/tdd2/script.js'
    
    for substring in strings_with_function_substrings(file_path):
        assert "function" in substring

def test_list_all_function_names():
    
    file_path = '/home/hlobisile/tdd2/script.js'
    funcnames, check = list_all_function_names(strings_with_function_substrings(file_path))
    assert check
    


    
