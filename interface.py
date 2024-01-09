import gradio as gr
from PIL import Image

import json
from pathlib import Path
from urllib import request, parse
import random
import os

from uuid import uuid4
from prompt import generate_outfits_man, generate_outfits_woman

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

prompt_workflow = json.load(open("outfit_api.json"))

# give some easy-to-remember names to the nodes
prompt_pos_node = prompt_workflow["6"]
empty_latent_img_node = prompt_workflow["5"]
ksampler_node = prompt_workflow["3"]
input_img_node = prompt_workflow["11"]
save_image_node = prompt_workflow["12"]

# batch size
empty_latent_img_node["inputs"]["batch_size"] = 4

# set input image
output_dir = Path("AI_Project")
output_root = Path("C:/Users/Jpeng/Project/ComfyUI_windows_portable/ComfyUI/output")
input_dir = Path.cwd() / "input"
gen_func = [generate_outfits_woman, generate_outfits_man]

def process_image(input_image, ismale):
    output_images = []
    
    # save input image
    file_name = str(uuid4()) + ".jpg"
    print(f"[Input] : {file_name}")
    input_image.save(str(input_dir / file_name))
    input_img_node["inputs"]["image"] = str(input_dir / file_name)

    # set prompt
    prompt_pos_node["inputs"]["text"] = gen_func[ismale]() # add prompts to list
    ksampler_node["inputs"]["seed"] = random.randint(1, 18446744073709551614)

    # file_prefix
    fileprefix = file_name.split(".")[0]

    # create output dir
    print(f"Create output dir: {str(output_root/ output_dir / fileprefix)}")
    os.mkdir(str(output_root/ output_dir / fileprefix))
    save_image_node["inputs"]["filename_prefix"] = os.path.join(str(output_dir), fileprefix) + '/result'
    
    # queue prompt
    queue_prompt(prompt_workflow)

    # wait for output
    while len(os.listdir(str(output_root/ output_dir / fileprefix))) < 4:
        pass

    # get output
    for output in os.listdir(str(output_root/ output_dir / fileprefix)):
        print(f"[Output] : {output}")
        output_images.append(Image.open(output_root/ output_dir / fileprefix / output))
    
    return prompt_pos_node["inputs"]["text"], *output_images

# 创建 Gradio 界面
iface = gr.Interface(
    fn=process_image,
    inputs=[gr.components.Image(type="pil", label='個人臉部照片'), gr.Radio([("男", 1), ("女", 0)], label="生成性别", value=0)],
    outputs=[gr.components.Textbox(label="Prompt 生圖內容"), 
             gr.components.Image(type="pil", label="造型1"),
             gr.components.Image(type="pil", label="造型2"),
             gr.components.Image(type="pil", label="造型3"),
             gr.components.Image(type="pil", label="造型4")],
    title="Comfycam 輕鬆讓你的自拍變成專業照片"
)

# 启动界面
if __name__ == "__main__":
    iface.launch()
