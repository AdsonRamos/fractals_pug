import os
import glob
from natsort import natsorted
from moviepy.editor import *


def make_video(path, name_final, time):
    fps = 24

    file_list = glob.glob(path)  # Get all the pngs in the current directory
    file_list_sorted = natsorted(file_list, reverse=False)  # Sort the images

    clips = [ImageClip(m).set_duration(time)
             for m in file_list_sorted]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(name_final, fps=fps)


make_video('./res/*.png', "julia2.mp4", 0.05)
