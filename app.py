import gradio as gr
from video_generator import generate_video


def generate(prompt):

    video_path = generate_video(prompt)

    return video_path


interface = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="Enter Video Prompt"),
    outputs=gr.Video(label="Generated Video"),
    title="VidFlow AI Video Generator"
)

interface.launch()