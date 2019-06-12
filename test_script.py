from pathscript import list_of_rows_with_the_word_function, list_of_all_function_names, list_all_js_function_names

def test_list_of_rows_with_the_word_function():
        path_to_js_file = '/js_file_function/pathscript.py'
                
        for substring in list_of_rows_with_the_word_function(path_to_js_file):
                assert "function" in substring

def test_list_of_all_function_names():
        path_to_js_file = '/js_file_function/pathscript.py'
        list_of_rows_with_functionsubstring = list_of_rows_with_the_word_function(path_to_js_file)
        functionnames = list_of_all_function_names(list_of_rows_with_functionsubstring)
              
        assert len(functionnames) == len(list_of_rows_with_functionsubstring) 
    
    


    
