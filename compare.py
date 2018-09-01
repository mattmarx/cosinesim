import re, math
from collections import Counter
# import ast so I can convert the strings to dictionaries
import ast
# import json so I can print 
import json
# import sys so I can iterate through arguments
import sys

# create string to fill with inverse frequency string
inv_freq_string = ""
# open the inverse frequency dictionary
inverse = open('new_inverse_frequency_dictionary', 'r+')

# iterate through the file and place the contents into the string 
for line in inverse:
     inv_freq_string = inv_freq_string + line
# convert the string to a dictionary for quick use in comparisons
inv_freq_dict = ast.literal_eval(inv_freq_string)

WORD = re.compile(r'\w+')

# function for comparing strings

keylist = []

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([(vec1[x]* round(inv_freq_dict[x], 20)) * (vec2[x]*round(inv_freq_dict[x], 20)) for x in intersection])
     # the variable below is the original sum1 variable without inverse frequency applied 
     #sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum1 = sum([ ((vec1[x]* round(inv_freq_dict[x], 20)**2)) for x in vec1.keys()])

     # the variable below is the original sum1 variable without inverse frequency applied 
     #sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     sum2 = sum([ ((vec2[x]* round(inv_freq_dict[x], 20)**2)) for x in vec2.keys() ])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     #print('Denominator without inverted is: 211.16')
     #print('Denominator with inverted is: ', denominator)
     if not denominator:
          return 0.0
     else:
          return float(numerator) / denominator
print(keylist)

def text_to_vector(text):
     rx = re.compile(r'\w(?:[-\w]*\w)?')
     words = rx.findall(text)
     return Counter(words)

# need to make a new text_to_vector function that doesn't split the words

# first pair
text1 = "Until recently, northern Bering Sea ecosystems characterized extensive seasonal sea ice cover, high water column sediment carbon production, tight pelagic-benthic coupling organic production. Here, we show that ecosystems shifting away characteristics. Changes biological communities contemporaneous with shifts regional atmospheric hydrographic forcing. In the past decade, geographic displacement marine mammal population distributions has coincided with a reduction benthic prey populations, increase in pelagic fish, a reduction in sea ice, increase in air ocean temperatures. These changes now observed on the shallow shelf of the northern Bering Sea should be expected to affect a much broader portion of the Pacific-influenced sector of the Arctic Ocean."
text2 = "This paper presents evaluates two perspectives changing climatewalrushuman relationships in the Beringian region, from viewpoints marine biology ecology, indigenous hunters. Bridging these types of knowledge vital order to grasp complexity processes involved advancing understanding of subarctic marine ecosystems that are currently experiencing rapid ecological social change. We argue that despite substantial gaps distinctions, information generated scientists indigenous hunters have many similarities. Differences in interpretation are primarily due to scaling temporal rates change knowledge, which could be rectified through more active sharing expertise records, enhanced documentation of indigenous observations, more collaborative research, increased insight from the social sciences."
# second pair
text3 = "We have used gene targeting to generate mice with a homozygous deficiency in trp2, a cation channel expressed vomeronasal organ (VNO). Trp2 mutant animals reveal a striking reduction in electrophysiological response to pheromones in the VNO, suggesting trp2 plays a central role in mediating pheromone response. These mutants therefore afford the opportunity to examine role VNO in generation of innate sexual social behaviors in mice. Trp2 mutant males nursing females are docile fail to initiate aggressive attacks on intruder males. Malefemale sexual behavior appears normal, trp2 mutant males vigorously mount other males. These results suggest cation channel trp2 is required VNO to detect male-specific pheromones elicit aggressive behaviors dictate choice sexual partners."
text4 = "The mouse vomeronasal organ (VNO) is thought to mediate social behaviors neuroendocrine changes elicited pheromonal cues. The molecular mechanisms underlying sensory response to pheromones behavioral repertoire induced through the VNO are not fully characterized. Using the tools of mouse genetics and multielectrode recording, we demonstrate sensory activation of VNO neurons requires TRP2, a putative ion channel transient receptor potential family expressed exclusively in these neurons. Male mice deficient in TRP2 expression fail to display male-male aggression, initiate sexual courtship behaviors toward both males females. Our study suggests, in the mouse, sensory activation of the VNO is essential for sex discrimination of conspecifics thus ensures gender-specific behavior."
# third pair
text5 = "ultra-violette"
text6 = "It ultra-violette"

vector1 = text_to_vector(text5)
vector2 = text_to_vector(text6)

cosine = get_cosine(vector1, vector2)
analysis_results_dict = {}
error_count = 0
def compare_abstracts(twin_id, abstract1, abstract2):
     global error_count
     vector1 = text_to_vector(abstract1)
     vector2 = text_to_vector(abstract2)
     try:
          cosine = get_cosine(vector1, vector2)
          analysis_results_dict[twin_id] = cosine
     except Exception as e:
          print(e)
          error_count += 1
def print_dictionary(file_path):
     # create the file that we will add the results dictionary to
     analysis_results_file = open(file_path, 'w')
     global error_count
     global analysis_results
     # print(json.dumps(analysis_results_dict, indent=1))
     # add analysis_results to the file
     analysis_results_str = str(analysis_results_dict)
     analysis_results_file.write(analysis_results_str)
     analysis_results_file.close()
     print("error count: ", error_count)
#print('Cosine without inverted is: 0.464')
#print ('Cosine with inverted is: ', cosine*100)
