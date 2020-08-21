from django.shortcuts import render

def bemvindo(request):
    return render(request, 'enquetes/bemvindo.html')
