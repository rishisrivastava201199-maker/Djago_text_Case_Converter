from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    checkingonly = {'name': 'Rishi', 'age': 22} 
    return render(request, 'index.html', checkingonly)

def about(request):
    return HttpResponse("This is about website")

def demo(request):
    return HttpResponse("<h1>This is my page</h1>")

def remove(request):
    text = request.GET.get('text', '')
    context = {'submitted_text': text, 'name': 'Rishi', 'age': 22}
    return render(request, 'index.html', context)

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    removespaces = request.GET.get('removespaces', 'off')

    analyzed = djtext

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = "".join([char for char in analyzed if char not in punctuations])

    if fullcaps == "on":
        analyzed = analyzed.upper()
    
    if removespaces == "on":                    # naya
        analyzed = " ".join(analyzed.split())  

    params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

    