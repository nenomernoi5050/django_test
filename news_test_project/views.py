from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'test_project/home.html', {'object_list': qs, 'form': form})

# Поиск по тексту из GET
# def home(request):
#     city = request.GET.get('city')
#     language = request.GET.get('language')
#     qs = []
#     if city or language:
#         _filter = {}
#         if city:
#             _filter['city__name'] = city
#         if language:
#             _filter['language__name'] = language
#         qs = Vacancy.objects.filter(**_filter)
#     return render(request, 'test_project/home.html', {'object_list': qs})
