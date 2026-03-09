from prompt_engine import expand_prompt
from image_generator import generate_image
from video_renderer import create_video
import os


def generate_video(prompt):

    # clear old frames
    if os.path.exists("frames"):
        for f in os.listdir("frames"):
            os.remove(f"frames/{f}")

    scenes = expand_prompt(prompt)

    for i, scene in enumerate(scenes):

        generate_image(scene, i)

    video = create_video()

    return video