from email import message
import os
from pytube import YouTube, exceptions
from sys import argv
# args - (link to youtube video)
# if (len(argv) < 4):
#     print(
#         "usage: video_downloader.py [VIDEO_LINK] [DESTINATION_FOLDER_PATH] [DESTINATION_FILE_NAME]")


def download(link, destination, filename):
    message = 'Downloader init message'
    try:
        yt = YouTube(link)
        print("title: ", yt.title)
        print("views: ", yt.views)
        yd = yt.streams.get_highest_resolution()
        try:
            yd.download(destination, filename)
        except Exception:
            if (os.path.exists(destination+filename)):
                os.remove(destination+filename)
            message = 'Downloaded video corrupted so deleted from local'
    except Exception:
        message = 'Error while downloading video'
    else:
        message = 'Video downloaded successfully'

    return message
