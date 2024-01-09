import json
import random

'''
This file generates a JSON file containing 50 unique hair style combinations.
hair_style.json contains the hair style attributes, and this file uses those
attributes to create unique hair style combinations.
'''

# Loading the hair style data
hair_style_data = './hair_style.json'

# Extracting the hair style options from the JSON data
hair_style_data = json.load(open(hair_style_data))

lengths = hair_style_data["hair_style"]["lenght"]
textures = hair_style_data["hair_style"]["hair texture"]
cuts = hair_style_data["hair_style"]["hair cut"]
colors = hair_style_data["hair_style"]["hair color"]
inners = hair_style_data["hair_style"]["inner color"]

# Function to create a unique and reasonable combination of hair style attributes
def create_hair_style_combinations(num_combinations=50):
    combinations = set()
    while len(combinations) < num_combinations:
        length = random.choice(lengths)
        texture = random.choice(textures)
        cut = random.choice(cuts)
        color = random.choice(colors)
        inner = random.choice(inners)
        combination = f"{length}, {texture}, {cut} hair"

        if random.random() < 0.6:
            combination = f"{combination}, {color} hair,"
        elif random.random() < 0.65:
            combination = f"{combination}, {color} hair, ({inner} inner hair:1.3),"
        
        combinations.add(combination)
    return list(combinations)

# Generating 50 unique hair style combinations
hair_styles = create_hair_style_combinations(100)
hair_styles = sorted(hair_styles)

# Creating the JSON structure
hair_styles_json = json.dumps({"hairs": hair_styles}, indent=4)

# Saving the JSON to a file
output_file_path = 'data/hairs.json'
with open(output_file_path, 'w') as file:
    file.write(hair_styles_json)

output_file_path