from simple_search import Simple_search
def test_search_string_in_file_no_match():
    file_path = 'abc'
    search_string = '{'
    result = Simple_search.search_string_in_file(file_path, search_string)   
    assert result ==  {'c.txt' : 0, 'b.txt': 0, 'a.txt': 0}
