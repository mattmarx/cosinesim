import re, math
from collections import Counter
# import ast so I can convert the strings to dictionaries
import ast
# import json so I can print 
import json

WORD = re.compile(r'\w+')

# function for comparing strings
bunched_file = open('bunched', 'r+')
frequency_dictionary_file = open('new_frequency_dictionary', 'w')
inverse_frequency_dictionary_file = open('new_inverse_frequency_dictionary', 'w')
# get all text from bunched and add to a variable called all_text
all_text = ""
for line in bunched_file:
	all_text = all_text + line
bunched_file.close()

counted = ""
inverse_freq = {}
def create_frequency_dictionaries(text):
	# define global variables
	global inverse_freq
	global frequency_dictionary_file
	global inverse_frequency_dictionary_file
	global counted
	rx = re.compile(r'\w(?:[-\w]*\w)?')
	words = rx.findall(text)
	counted = Counter(words)

	counted_dict = dict(counted)
	for key in counted_dict:
		inversed = 1/counted_dict[key]
		inverse_freq[key] = inversed
	inverse_freq_str = str(inverse_freq)
	inverse_frequency_dictionary_file.write(inverse_freq_str)
	counted_str_dict = str(counted_dict)
	frequency_dictionary_file.write(counted_str_dict)
	print("done!")
# call function to create frequency dictionaries
create_frequency_dictionaries(all_text)


frequency_dictionary_file.close()
inverse_frequency_dictionary_file.close()

# need to make a new text_to_vector function that doesn't split the words

# first pair
text1 = "Until recently, northern Bering Sea ecosystems characterized extensive seasonal sea ice cover, high water column sediment carbon production, tight pelagic-benthic coupling organic production. Here, we show that ecosystems shifting away characteristics. Changes biological communities contemporaneous with shifts regional atmospheric hydrographic forcing. In the past decade, geographic displacement marine mammal population distributions has coincided with a reduction benthic prey populations, increase in pelagic fish, a reduction in sea ice, increase in air ocean temperatures. These changes now observed on the shallow shelf of the northern Bering Sea should be expected to affect a much broader portion of the Pacific-influenced sector of the Arctic Ocean."
text2 = "This paper presents evaluates two perspectives changing climatewalrushuman relationships in the Beringian region, from viewpoints marine biology ecology, indigenous hunters. Bridging these types of knowledge vital order to grasp complexity processes involved advancing understanding of subarctic marine ecosystems that are currently experiencing rapid ecological social change. We argue that despite substantial gaps distinctions, information generated scientists indigenous hunters have many similarities. Differences in interpretation are primarily due to scaling temporal rates change knowledge, which could be rectified through more active sharing expertise records, enhanced documentation of indigenous observations, more collaborative research, increased insight from the social sciences."
# second pair
text3 = "We have used gene targeting to generate mice with a homozygous deficiency in trp2, a cation channel expressed vomeronasal organ (VNO). Trp2 mutant animals reveal a striking reduction in electrophysiological response to pheromones in the VNO, suggesting trp2 plays a central role in mediating pheromone response. These mutants therefore afford the opportunity to examine role VNO in generation of innate sexual social behaviors in mice. Trp2 mutant males nursing females are docile fail to initiate aggressive attacks on intruder males. Malefemale sexual behavior appears normal, trp2 mutant males vigorously mount other males. These results suggest cation channel trp2 is required VNO to detect male-specific pheromones elicit aggressive behaviors dictate choice sexual partners."
text4 = "The mouse vomeronasal organ (VNO) is thought to mediate social behaviors neuroendocrine changes elicited pheromonal cues. The molecular mechanisms underlying sensory response to pheromones behavioral repertoire induced through the VNO are not fully characterized. Using the tools of mouse genetics and multielectrode recording, we demonstrate sensory activation of VNO neurons requires TRP2, a putative ion channel transient receptor potential family expressed exclusively in these neurons. Male mice deficient in TRP2 expression fail to display male-male aggression, initiate sexual courtship behaviors toward both males females. Our study suggests, in the mouse, sensory activation of the VNO is essential for sex discrimination of conspecifics thus ensures gender-specific behavior."


