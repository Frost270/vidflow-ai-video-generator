from diffusers import StableDiffusionPipeline
import torch
import os

pipe= StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

def generate_image(prompt, index):

    image = pipe(prompt).images[0]

    os.makedirs("frames", exist_ok=True)
    
    path = f"frames/frame_{index}.png"

    image.save(path)

    return path