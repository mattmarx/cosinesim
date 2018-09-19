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
# create an array that represents the array of id's for testing
start = time.time()

arguments = str(sys.argv)
arguments = arguments.split(',')

file_path = arguments[1]
file_path = file_path.replace("'","")
file_path = file_path.replace("]","")
file_path = file_path.replace(" ","")

print('using file: ', file_path)

line_count = 0
error_count = 0
original = codecs.open(file_path, 'r', 'utf-8')

string_dict_file = open('clean_twins_stringified_dict_new', 'w')
# create a string dictionary that will be filled
string_dictionary = {}
found = 0
for line in original:
        line_array = line.split(":")
        try:
                abstract_id = line_array[0]
                abstract_body = line_array[1]
                string_dictionary[abstract_id] = abstract_body
                line_count += 1
        except Exception as e:
                print("Error caught: ", e)
                error_count += 1
        #abstract_id = line_array[0]
        #abstract_body = line_array[1]
        #string_dictionary[abstract_id] = abstract_body
        print(line_array[0])
        line_count += 1
string_dictionary = str(string_dictionary)
string_dict_file.write(string_dictionary)

#print('Final line count is: ', line_count)
original.close()

string_dict_file.close()
print('final line count is: ',line_count)
print('final error count is: ', error_count)
end = time.time()
print('runtime is: ', end - start)
