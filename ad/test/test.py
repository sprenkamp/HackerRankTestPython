from ad import simple_search
class TestSimpleSearch():
    def setup(self):
        self.search = simple_search.Simple_search()
    def test_search_string_in_file_no_match(self):
        file_path = 'testFiles'
        search_string = '{'
        print(file_path)
        result = self.search.search_string_in_file(file_path, search_string)   
        assert result ==  {'c.txt' : 0, 'b.txt': 0, 'a.txt': 0}

    def test_search_string_in_file_with_match(self):
        file_path = 'testFiles'
        search_string = 'any thing'
        print(file_path)
        result = self.search.search_string_in_file(file_path, search_string)   
        assert result ==  {'c.txt' : 89, 'b.txt': 56, 'a.txt': 100}
