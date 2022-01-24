from django.shortcuts import render
import requests

def home(request):
    app_id = "8a74d3f5"
    app_key = "a1836ea680601c16b6a9c45d3c02395d"

    if request.method == 'GET':
        q = request.GET.get('q')
        if q is not None:
            query = q
        else:
            query = ''

    #https://developer.edamam.com/edamam-docs-recipe-api
    url = f'https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}&from=0&to=30'
    response = requests.get(url)

    data = response.json()
    recipies = data["hits"]

    context = {
        'recipies': recipies,
        'query':query
    }

    return render(request, 'home.html', context)