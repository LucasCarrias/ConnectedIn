from django.shortcuts import render, get_object_or_404
from .models import Enquete


def bemvindo(request):
    return render(request, 'enquetes/bemvindo.html')


def enquete(request, id_enquete):
    enquete = get_object_or_404(Enquete, pk=id_enquete)
    return render(request, 'enquetes/enquete.html', {'enquete':enquete})
