import sys,os
from fuzzywuzzy import fuzz
import collections
import pytest
from io import StringIO

class Simple_search:
    def search_string_in_file(self,file_path,search_string):
        file_names = os.listdir(file_path)
        filename_with_score = {}
        for file_name in file_names:   
            with open(file_path + '/' + file_name, 'r') as f:
                lines = ''
                for line in f:
                    lines = lines + ' ' + line
                match_string_ratio = fuzz.partial_ratio(search_string, lines)
                filename_with_score [file_name] = match_string_ratio
        sorted_filename_with_score = sorted(filename_with_score.items(), key=lambda kv: kv[1], reverse = True)
        top10_filename_with_score_list = sorted_filename_with_score[0:10]
        top10_filename_with_score_dict = collections.OrderedDict(top10_filename_with_score_list)
        return top10_filename_with_score_dict

    def main(self):
        file_path = sys.argv[1]
        while True:
            search_string = None
            try:
                search_string = input("search>")
            except:
                pass
            if search_string is None:
                break
            elif search_string == ":quit":
                break
            top10_filename_with_score_dict = self.search_string_in_file(file_path, search_string)
            dict_first_value = next(iter(top10_filename_with_score_dict.values()))
            if dict_first_value == 0:
                print('no matches found')
            else:
                for file_name, search_match_score in top10_filename_with_score_dict.items(): 
                    print(file_name, ":", search_match_score)

if __name__ == "__main__":
    search_string_in_file = Simple_search()
    search_string_in_file.search_string_in_file('test/testFiles','any')
    search_string_in_file.main()
    