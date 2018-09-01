# import codecs so I can handle the unicode text
import codecs
# import json so I can convert the text into JSON
import json
# import sys so I can handle command line arguments
import sys
# import ast so I can convert the strings to dictionaries
import ast
# import re so I can strip strings of non-numbers
import re
# import timer so I can track my function
import time

def get_pair_generator(dictionary):
        twin_pair_ids = codecs.open('twin_pairs.csv', 'r', 'utf-8')
        twin_pairs_complete = codecs.open('twin_pairs_complete.csv', 'r', 'utf-8')

        for pairs in twin_pairs_complete:
                seperated = pairs.split(",")
                pair_id = seperated[0]
                abstract_ids = seperated[1:]
                abstract_ids[1] = abstract_ids[1].replace("\n","")
                dictionary[pair_id] = abstract_ids
        twin_pair_ids.close()
        twin_pairs_complete.close()

pair_test = {}
get_pair_generator(pair_test)

