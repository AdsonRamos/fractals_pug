from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip('julia.mp4')
clip2 = VideoFileClip('julia2.mp4')

final_clip = concatenate_videoclips(
    [clip1, clip2])
final_clip.write_videofile("julia_set.mp4")
