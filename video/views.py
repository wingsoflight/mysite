from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
import cv2
import time

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret,frame = self.video.read()
        #frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame.tobytes()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(frame)

def index(request):
    return render(request, 'video/index.html')

