# I have created this file - Deep
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
 #   return HttpResponse("""<h1><a href="https://mail.google.com/mail/u/0/#inbox">My Contact Mail</a> </h1>""")
#def about(request):
#    return HttpResponse("""<h3><a href="https://www.kerneloptimizer.com/">That's My Portfolio</a></h3>""")
def index(request):
    return render(request,'index.html')
def about(request):
        return render(request, 'about.html')
def contact(request):
    return render(request,'contact.html')

    #return HttpResponse("Home")
def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default')
    #check box value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter=request.POST.get('charactercounter', 'off')
    #print(removepunc,"\n",djtext)
    #analyze the text
    #analyzed=djtext
    if removepunc=="on":
     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     analyzed=""
     for char in djtext:
         if char not in punctuations:
             analyzed=analyzed+char
     params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
     djtext=analyzed
     #return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover=='on':
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
             analyzed += char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover=='on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
             analyzed += char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if charactercounter=='on':
        analyzed = 0
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "):
             analyzed += 1
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext=analyzed

    return render(request,'analyze.html',params)