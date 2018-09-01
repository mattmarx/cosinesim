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
# import twin_pair_generator so I can get the dictionary I need to of pair_ids with abstract_ids
import twin_pair_generator
# import the compare.py function so that I can compare the abstracts that I need to and store their cosine similarities into another dictionary
from compare import *
# create an array that represents the array of id's for testing
start = time.time()
# create variable to keep track of pairs at the end (should be comparing 28,207 pairs)
pair_count = 0
# create variable to keep track of the errors I get
error_count = 0
# getting my file path argument for the file I want to process
arguments = str(sys.argv)
arguments = arguments.split(',')

file_path = arguments[1]
file_path = file_path.replace("'","")
file_path = file_path.replace("]","")
file_path = file_path.replace(" ","")
print('using file: ', file_path)

output_file_path = arguments[2]
output_file_path = output_file_path.replace("'","")
output_file_path = output_file_path.replace("]","")
output_file_path = output_file_path.replace(" ","")



# using twin_pair_generator to create the dictionary of pairs and abstract_ids
twin_pairs = {}
twin_pair_generator.get_pair_generator(twin_pairs)

abstract_dictionary_file = codecs.open(file_path, 'r', 'utf-8')
analyzed_abstracts = codecs.open('analyzed_abstracts.txt', 'w')
# create a variable for abstract_dictionary_file
dict_string = ""

# take the text from abstract_dictionary_file and add it to the string
print("starting to create abstract dictionary string representation")
for line in abstract_dictionary_file:
        dict_string = dict_string + line
# take the string and turn it into a dictionary for simple key value check when comparing the abstracts
print("starting to create abstract dictionary")
abstract_dictionary = ast.literal_eval(dict_string)

# TODO: iterate through and compare the files using abstract_dictionary and twin_pairs. We will use twin_pairs to select the abstract_ids,
#       then use abstract_dicionary to grab the abstracts I need to compare, using the compare.py module
print("starting to compare abstracts")
error_array = []
for key in twin_pairs:
        #twin_id = key.decode(encoding='UTF-8')
        twin_id = key.encode('ascii', 'ignore')
        twin_id = str(twin_id)
        twin_id = twin_id.replace('b', '')
        abstract_id_list = twin_pairs[key]
        abstract1_id = abstract_id_list[0]
        abstract1_id = abstract1_id.replace("'", "")
        abstract1_id = abstract1_id.replace("\r", "")
        abstract2_id = abstract_id_list[1]
        abstract2_id = abstract2_id.replace("'", "")
        abstract2_id = abstract2_id.replace("\r", "")
        try:
                compare_abstracts(twin_id, abstract_dictionary[abstract1_id], abstract_dictionary[abstract2_id])
                pair_count += 1
        except Exception as e:
                error_array.append(e)
                error_count += 1
abstract_dictionary_file.close()
analyzed_abstracts.close()
end = time.time()
print('runtime is: ', end - start)
print('pair count is: ', pair_count)
print('error count is: ', error_count)
print('variable total is: ', pair_count + error_count)
debug_file = codecs.open('debug.txt', 'w')
for x in range(len(error_array)):
        print(error_array[x])
        debug_file.write(str(error_array[x]))
debug_file.close()

print_dictionary(output_file_path)
# add an argument to print_dictionary
# current is analysis_results.txt
