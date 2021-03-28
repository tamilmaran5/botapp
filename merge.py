from moviepy.editor import *


def merge_video(file_1, file_2, output_name):
    clip1 = VideoFileClip(file_1, audio=True)
    clip2 = VideoFileClip(file_2, audio=True)
    final_clip = concatenate_videoclips([clip1, clip2], method="compose")
    final_clip.write_videofile(output_name)


merge_videos("1.mp4", "1.mp4", "final.mp4")
