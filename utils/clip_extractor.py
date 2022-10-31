# args - [start time in seconds] [number of clips needed]
# randomly extracts clips


from fileinput import filename
from math import floor
from os import system
import os
from random import randrange
from moviepy.editor import VideoFileClip
from moviepy.video.fx import crop


def extract_clips(number_of_clips, video_path, clips_destination, min_dur, max_dur, overwrite, is_shorts):
    message = 'Started extracting clips...'
    try:
        video = VideoFileClip(video_path)
        video_length = video.duration
        j = 0
        for i in range(number_of_clips):
            clip_length = randrange(min_dur, max_dur)
            start = randrange(0, floor(video_length-clip_length))
            clip = video.subclip(start, start+clip_length)
            if (is_shorts):
                clip_width = clip.w
                cropwidth = clip_width//3
                croppedclip = crop.crop(clip, x1=cropwidth, width=cropwidth)
                clip = croppedclip
            filename = str(i)+'.mp4'
            if (overwrite):
                clip.write_videofile(clips_destination+filename)
            else:
                print("entered here")
                while (True):
                    k = i+j
                    print("k : ", k)
                    filename = str(k)+'.mp4'
                    print("filename : ", filename)
                    if (not os.path.exists(clips_destination+filename)):
                        break
                    j += 1
                clip.write_videofile(clips_destination+filename)
    except Exception:
        message = 'Something went wrong'
    else:
        message = 'Clips extracted successfully'

    return message
