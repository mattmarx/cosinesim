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
test_count = 0
original = codecs.open(file_path, 'r', 'utf-8')
bunched = open('bunched', 'w')
for line in original:
	body = line[11:]
	if ":" in line:
		body = line[11:]
	else:
		body = line
	if "field-parameterized" in body:
		print("got it!")
		test_count += 1
	bunched.write(body)
	print("Line count is: ", line_count)
	line_count += 1
print('Final line count is: ', line_count)
print('final test count for field-parameterized is: ', test_count)
original.close()
bunched.close()
print('final line count is: ',line_count)
end = time.time()
print('runtime is: ', end - start)
