from moviepy.editor import VideoFileClip

clip = VideoFileClip("julia_set.mp4")
clip.write_gif("julia_set.gif")
