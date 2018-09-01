# analyze.py

() analyze.py takes an inverted abstract file AS AN ARGUMENT – file is currently abstractsim/analysis/twin_abstracts.txt and turns it into two files: * twins_stringified and {} twins_stringified_dict_new

* twins_stringified is a text file that contains abstract_id: abstract, created by analyze.py

{} twins_stringified_dict_new is a text representation of a dictionary with abstract_id: abstract, created analyze.py
 
# bunch_real.py
() bunch_real.py takes twins_stringified as an argument and creates a bunched file titled 'bunched' (no extension)
new_frequency.py (no args, but assumes ./bunched), outputs new_frequency_dictionary & new_inverse_frequency_dictionary
 
# abstract_analysis.py
() abstract_analysis.py is the ultimate function, importing the twin_pair_generator.py and compare.py, with the argument of the a dictionary (twins_stringified_dict_new) with abstract_id: abstract (assumes that new_inverse_frequency_dictionary is in place) . It iterates through the pair_id's with the lists of the abstract id's, compares them, and will eventually store the cosine value in a dictionary with pair_id: cosine value outputs analysis_results.txt
 
 
From: Christopher Ackerman <caa96@bu.edu>
Sent: Thursday, August 16, 2018 2:05 PM
To: Marx, Matt <mattmarx@bu.edu>
Subject: Instructions text
 
# python file section (inputs and description)
() = function file
* = text file to be processed
{} = dictionary




# twin_pair_generator.py

() twin_pair_generator.py takes two csv files(below) to create a dictionary with pair_id: [abstract1_id, abstract2_id]

* twin_pairs.csv is a csv file of pair ID's

* twin_pairs_complete.csv is a csv with lists of pair ID, abstract1 ID, abstract2 ID

