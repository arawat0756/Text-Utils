from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>harry</h1> <a href="https://www.youtube.com/"> youtube page </a>''')
#
# def about(request):
#     return HttpResponse("hello ankit bhai")


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuations', 'analyze_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Change to uppercase", 'analyze_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover =='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': "Removed NewLine", 'analyze_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': "Extra space remover", 'analyze_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")

    if (removepunc != 'on' and newlineremover !='on' and extraspaceremover !='on' and fullcaps !='on'):
        return HttpResponse("Please select the opretions")

    return render(request, 'analyze.html', params)


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("Charcount")

