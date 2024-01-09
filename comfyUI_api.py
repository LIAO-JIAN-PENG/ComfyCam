import json
from pathlib import Path
from urllib import request, parse
import random

from prompt import generate_outfits_man, generate_outfits_woman

'''
Quick generate outfit API
This file directly sends a prompt queue to the ComfyUI server.
'''

# ======================================================================
# This function sends a prompt workflow to the specified URL
# (http://127.0.0.1:8188/prompt) and queues it on the ComfyUI server
# running at that address.
def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode("utf-8")
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)
# ======================================================================

# read workflow api data from file and convert it into dictionary
# assign to var prompt_workflow
prompt_workflow = json.load(open("outfit_api.json"))

# create a list of prompts
prompt_list = []
# TODO: Add prompts to list
for i in range(20):
    prompt_list.append(generate_outfits_man()) # add prompts to list
    prompt_list.append(generate_outfits_woman())

# give some easy-to-remember names to the nodes
prompt_pos_node = prompt_workflow["6"]
empty_latent_img_node = prompt_workflow["5"]
ksampler_node = prompt_workflow["3"]
input_img_node = prompt_workflow["11"]
save_image_node = prompt_workflow["12"]

# print out the workflow
# for workflow in prompt_workflow:
#     print(workflow, prompt_workflow[workflow])

# set input image
output_dir = Path("AI_Project")
input_dir = Path.cwd() / "input"
img = 'IMG_0929.jpg'
input_img_node["inputs"]["image"] = str(input_dir / img)
# each prompt will produce a batch of 4 images
empty_latent_img_node["inputs"]["batch_size"] = 16

# for every prompt in prompt_list...
for index, prompt in enumerate(prompt_list):
    print("Prompt:", prompt)
    # set the text prompt for positive CLIPTextEncode node
    prompt_pos_node["inputs"]["text"] = prompt

    # set a random seed in KSampler node
    ksampler_node["inputs"]["seed"] = random.randint(1, 18446744073709551614)

    # set filename prefix to be the same as prompt
    fileprefix = img
    save_image_node["inputs"]["filename_prefix"] = str(output_dir / fileprefix)

    # everything set, add entire workflow to queue.
    queue_prompt(prompt_workflow)
