from django.shortcuts import render
from webapp.cats_db import CatsDB
import random
from django.http import HttpResponseRedirect


# Create your views here.
def index_view(request):
    if request.method == "GET":

        return render(request, template_name='index.html', )
    elif request.method == "POST":
        cats = CatsDB.cats
        cat_new = {
            'cat_name': request.POST.get('cat_name'),
            'cat_age': 1,
            'cat_mood': 10,
            'cat_hunger': 40,
            'sleeping': False
        }
        CatsDB.cats.append(cat_new)
        return render(request, template_name='cat_info.html', context=cat_new)


def cat_index(request):
    if request.method == "GET":

        return render(request, template_name='cat_info.html', context=CatsDB.cats[0])
    elif request.method == "POST":
        cats = CatsDB.cats
        if request.POST.get('select') == 'play':
            if cats[0]['sleeping'] == False:
                cats[0]['cat_hunger'] = cats[0]['cat_hunger'] - 10
                random_number = random.randint(1, 3)

                if random_number == 1:
                    cats[0]["cat_mood"] = 0
                else:
                    cats[0]["cat_mood"] += 15
            else:
                cats[0]['sleeping'] = False
                cats[0]['cat_mood'] = cats[0]['cat_mood'] - 5
        elif request.POST.get('select') == 'feed':
            if cats[0]['sleeping'] == False:
                cats[0]['cat_hunger'] += 15
                cats[0]["cat_mood"] += 5
                if cats[0]['cat_hunger'] > 100:
                    cats[0]['cat_mood'] = cats[0]['cat_mood'] - 30
            else:
                cats[0]['cat_hunger'] += 0

        elif request.POST.get('select') == 'sleep':
            cats[0]['sleeping'] = True




        if cats[0]['cat_mood'] < 0:
            cats[0]['cat_mood'] = 0
        if cats[0]['cat_mood'] > 100:
            cats[0]['cat_mood'] = 100
        if cats[0]['cat_hunger'] < 0:
            cats[0]['cat_hunger'] = 0
        if cats[0]['cat_hunger'] > 100:
            cats[0]['cat_hunger'] = 100

        return render(request, template_name='cat_info.html', context=cats[0])
