import cv2
import os

def create_video():

    image_folder = "frames"
    video_path = "outputs/video.mp4"

    images = sorted(os.listdir(image_folder))

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, Layers = frame.shape

    os.makedirs("outputs", exist_ok=True)

    video = cv2.VideoWriter(video_path, 0, 5, (width, height))

    for image in images:

        img_path = os.path.join(image_folder, image)

        video.write(cv2.imread(img_path))

    video.release()

    return video_path

