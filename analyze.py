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
word_count = 0


original = codecs.open(file_path, 'r', 'utf-8')
stringified = open('twins_stringified', 'w')
string_dict_file = open('twins_stringified_dict_new', 'w')
# create a string dictionary that will be filled
string_dictionary = {}
found = 0
for line in original:
	#for chunk in line.split('"InvertedIndex":'):
	#	word_count += 1
	#	print("chunk is: ", chunk)
	#print('Slice number is: ', word_count)
	body = line.split('"InvertedIndex":')
	abstract = body[1]

	# ending_character is to parse through the file before the last character to turn it into a dictionary
	ending_character = len(abstract)-2
	body_cut = abstract[:ending_character]

	# this is to get the id of the study
	study_id = line[0:10]
	study_id = study_id.replace("\t", "")
	#print('Study id is: ', study_id)
	stringified.write(study_id + ": ")

	# index_length is for generating an empty array to fill
	index_length = body[0]
	index_length = index_length[-5:]

	# cutting the string down to what I know contains the index length
	index_length = re.sub("\D", "", index_length)

	# convert the index_length into type int to generate an empty array
	index_length = int(index_length)
	#print('Array length is: ', index_length)

	# create an empty array of with n empty items to fill with the words from the abstract
	abstract_array = ['a'] * index_length

	# dictionary is to get the body of the inverted index to turn into a dictionary
	try:
                dictionary = ast.literal_eval(body_cut)
	except Exception:
                print('EOF exception caught')
	# iterate through the dictionary key value pairs and place the words into the empty array
	string = ""
	
	for key in dictionary:
		value_list = dictionary[key]
		for item in value_list:
			# the 'item' is the index location of the key
			# TODO clean key up to not include ['/', '\']
			if key == "field-parameterized":
				found += 1
			abstract_array[item] = key
			
	print("found variable for parameterized: ",found)
	for word in abstract_array:
		testing_word = word.encode('ascii', 'ignore')
		string = string + str(testing_word.decode()) + " "
	string_dictionary[study_id] = string
	#print("test string is: ", string)
	#print("string is type: ", type(string))
	stringified.write(string + "\n")
	# convert abstract_array into a string and tell python to ignore ascii code to print
	### problems with encoding adding unwanted characters
	#print(type(abstract_array))
	abstract_array = str(abstract_array)
	#print('Stringified abstract is: ', abstract_array.encode('ascii', 'ignore'))
	#print('Stringified abstract is: ', abstract_array.encode('utf8', 'replace'))

	# print the current line count and increment up one for the next abstract

	print('Current line is: ', line_count)
	line_count += 1

print("\n")
print("final found variable for parameterized: ",found)
string_dictionary = str(string_dictionary)
string_dict_file.write(string_dictionary)

print('Final line count is: ', line_count)
original.close()
stringified.close()
string_dict_file.close()
print('final line count is: ',line_count)
end = time.time()
print('runtime is: ', end - start)
