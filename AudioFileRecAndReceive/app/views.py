"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from app.mfcc.mfccLoader import loadMfccJson

def home(request):
    data = loadMfccJson( )
    context = {'data':data}
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'data':context
        }
    )

def audioSplitter(request) : 
    data = loadMfccJson( )
    context = {'data':data}
    return render(request, 'app/audioSplitter.html')

i = 0

@csrf_exempt
def upload(request):
    global i
    i += 1
    name = "f_" + str(i) + ".wav"
    print(name)
    customHeader = request.META['HTTP_MYCUSTOMHEADER']
    uploadedFile = open(name, "wb")
    uploadedFile.write(request.body)
    uploadedFile.close()
    return HttpResponse("")

@csrf_exempt
def sendMfccData(request):
    uploadedFile = open("mfccData.json", "wb")
    uploadedFile.write(request.body)
    uploadedFile.close()
    print(request.body)
    return JsonResponse({'email':'django1@mail.com', 'password':'django1'})

@csrf_exempt
def loadMfccData(request):
    mfccFile = open( "mfccData.json", "r" )
    mfccData = json.load(mfccFile)
    return JsonResponse(mfccData)

