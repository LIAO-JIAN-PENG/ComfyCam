import json
import random

'''
ComfyUI workflow: outfit_api.json
SDXL model: https://civitai.com/models/124421/xxmix9realisticsdxl
'''

hair_path = 'data/hairs.json'
outfit_path = 'data/outfits.json'

hair_data = json.load(open(hair_path))['hairs']
outfit_data = json.load(open(outfit_path))['outfits']
man_outfit_data = outfit_data['man']
woman_outfit_data = outfit_data['woman']

man_prompt = "a man, male"
woman_prompt = "xxmixgirl,\na girl"

def generate_outfits_man():
    hair = random.choice(hair_data)
    man_outfit = random.choice(man_outfit_data)

    return f"{man_prompt},\n{hair}\n{man_outfit}"

def generate_outfits_woman():
    hair = random.choice(hair_data)
    woman_outfit = random.choice(woman_outfit_data)

    return f"{woman_prompt},\n{hair}\n{woman_outfit}"