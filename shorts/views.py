from email import message
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils import clip_extractor, video_downloader

# Create your views here.


def hello(request):
    return HttpResponse('Hello World!')


@csrf_exempt
def generate(request):
    json_request = json.loads(request.body)
    video_link = json_request['video_link']
    number_clips = json_request['number_of_shorts']
    print(video_link)
    print(number_clips)
    downloader_message = video_downloader.download(
        video_link, "./inter", "video.mp4")+';'
    shorts_extractor_message = clip_extractor.extract_clips(
        number_clips, "./inter/video.mp4", "./inter/shorts/", 10, 50, True, True) + ';'
    response = {}
    response["code"] = 200
    response["downloader_message"] = downloader_message
    response["shorts_extractor_message"] = shorts_extractor_message
    return JsonResponse(response, safe=False)
