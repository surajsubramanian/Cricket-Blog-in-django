from django.shortcuts import render

from django.http import HttpResponse
from .forms import BatBowlForm


def batvsbowl(request):
    if request.method == 'GET':
        form = BatBowlForm(request.GET)
    return render(request, './batvsbowl/batvsbowl.html', {form: BatBowlForm})


def results(request):
    return render(request, 'batvsbowl/results.html', {'title': 'results'})
