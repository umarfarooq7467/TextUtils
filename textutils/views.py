from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change all the charcter in uppercase', 'analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose':'Total Characters', 'analyzed_text':analyzed}

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'count':
        return HttpResponse("Please Chose A Method Text You Want To Apply!")
    
    return render(request, 'analyze.html', params)
