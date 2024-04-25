from django.shortcuts import render,redirect
from pytube import *

# Create your views here.
def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('url')
        print(link)
        video = YouTube(link)
        stream = video.streams.get_by_resolution('720p')
        print(stream)
        stream.download()
        return render(request, 'index.html', {"message":"Video downloaded Successfully!!"})
    return render(request, 'index.html', {"message":"Please enter URL in the field above"})