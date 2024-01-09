import json
import random

'''
This file generates a JSON file containing 50 unique outfit combinations.
closet.json contains the outfit attributes, and this file uses those
attributes to create unique outfit combinations.
'''


# Re-loading the JSON file for the new task
with open('closet.json', 'r') as file:
    closet_data = json.load(file)

# Expanded categories for more comprehensive outfit combinations for both men and women
man_expanded_categories = [
    closet_data['man']['sleeve'],
    closet_data['man']['shirts'],
    closet_data['man']['pants'],
    closet_data['man']['shorts'],
    closet_data['man']['shoes'],
    closet_data['man']['sweaters'],
    closet_data['man']['jackets'],
    closet_data['man']['coat'],
    closet_data['man']['accessory'],
    closet_data['man']['hat']
]

woman_expanded_categories = [
    closet_data['woman']['short_sleve_shirt'],
    closet_data['woman']['long_sleve_shirt'],
    closet_data['woman']['pants'],
    closet_data['woman']['skirt'],
    closet_data['woman']['dress'],
    closet_data['woman']['shoes'],
    closet_data['woman']['accessory'],
    closet_data['woman']['hat'],
    closet_data['woman']['sweaters'],
    closet_data['woman']['jackets'],
    closet_data['woman']['coat'],
]

def generate_outfits_man(num_combinations=50):
    combinations = set()
    while len(combinations) < num_combinations:
        sleeve = random.choice(closet_data['man']['sleeve'])
        shirt = random.choice(closet_data['man']['shirts'])
        pants = random.choice(closet_data['man']['pants'])
        shorts = random.choice(closet_data['man']['shorts'])
        shoes = random.choice(closet_data['man']['shoes'])
        sweater = random.choice(closet_data['man']['sweaters'])
        jacket = random.choice(closet_data['man']['jackets'])
        coat = random.choice(closet_data['man']['coat'])
        accessory = ",".join(random.choices(closet_data['man']['accessory'], k=random.randint(1, 4)))
        hat = random.choice(closet_data['man']['hat'])

        combination = f"{random.choice(['', sleeve+','])}"
        combination = f"{combination} {shirt},"
        combination = f"{combination} {','.join(random.choices(['', sweater, jacket, coat], weights=[0.4, 0.2, 0.2, 0.2]))},"  
        combination = f"{combination} {','.join(random.choices([pants, shorts], weights=[0.7, 0.3]))},"
        combination = f"{combination} {','.join(random.choices(['', 'shoes', shoes], weights=[0.3, 0.1, 0.6]))},"
        combination = f"{combination} {','.join(random.choices(['', accessory, hat], weights=[0.7, 0.2, 0.1]))},"

        combination = combination.replace(" ,", "").replace("  ", " ").strip()
        combinations.add(combination)
    return list(combinations)

def generate_outfits_woman(num_combinations=50):
    combinations = set()
    while len(combinations) < num_combinations:
        short_sleve_shirt = random.choice(closet_data['woman']['short_sleve_shirt'])
        long_sleve_shirt = random.choice(closet_data['woman']['long_sleve_shirt'])
        pants = random.choice(closet_data['woman']['pants'])
        skirt = random.choice(closet_data['woman']['skirt'])
        dress = random.choice(closet_data['woman']['dress'])
        shoes = random.choice(closet_data['woman']['shoes'])
        sweater = random.choice(closet_data['woman']['sweaters'])
        jacket = random.choice(closet_data['woman']['jackets'])
        coat = random.choice(closet_data['woman']['coat'])
        accessory = ",".join(random.choices(closet_data['woman']['accessory'], k=random.randint(1, 4)))
        hat = random.choice(closet_data['woman']['hat'])

        if random.random() < 0.7:
            combination = f"{random.choice([short_sleve_shirt, long_sleve_shirt])},"
            combination = f"{combination} {','.join(random.choices(['', sweater, jacket, coat], weights=[0.4, 0.2, 0.2, 0.2]))},"
            combination = f"{combination} {','.join(random.choices([pants, skirt, dress], weights=[0.4, 0.5, 0.1]))},"
            combination = f"{combination} {','.join(random.choices(['', shoes], weights=[0.3, 0.7]))},"
            combination = f"{combination} {','.join(random.choices(['', accessory, hat], weights=[0.7, 0.25, 0.05]))},"
        else:
            combination = f"{dress},"
            combination = f"{combination} {','.join(random.choices(['', 'shoes', shoes], weights=[0.3, 0.1, 0.6]))},"
            combination = f"{combination} {','.join(random.choices(['', accessory, hat], weights=[0.7, 0.2, 0.1]))},"

        
        combination = combination.replace(" ,", "").replace("  ", " ")
        combinations.add(combination)
    return list(combinations)

# Generating 100 outfits for each
man_outfits_expanded = sorted(generate_outfits_man(300))
woman_outfits_expanded = sorted(generate_outfits_woman(300))

# Creating the expanded JSON structure
expanded_outfits_json = {
    "outfits": {
        "man": man_outfits_expanded,
        "woman": woman_outfits_expanded
    }
}

# Save the generated outfits to a JSON file
expanded_output_file_path = 'data/outfits.json'
with open(expanded_output_file_path, 'w') as file:
    json.dump(expanded_outfits_json, file, indent=4)

expanded_output_file_path
