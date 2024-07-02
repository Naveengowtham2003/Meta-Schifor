import requests
from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            posts = response.json()
            return render(request, 'home.html', {'posts': posts})
        else:
            error_message = "Failed to fetch data"
            return render(request, 'error.html', {'error_message': error_message})

    elif request.method == 'POST':

        data = {'title': 'New Post', 'body': 'This is a new post'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts', json=data)
        if response.status_code == 201:
            return render(request, 'post_success.html')
        else:
            error_message = "Failed to create a new post"
            return render(request, 'error.html', {'error_message': error_message})

    elif request.method == 'PUT':

        return render(request, 'put_success.html')

    elif request.method == 'PATCH':

        return render(request, 'patch_success.html')

    elif request.method == 'DELETE':

        return render(request, 'delete_success.html')

    elif request.method == 'HEAD':

        return render(request, 'head_success.html')

    elif request.method == 'OPTIONS':

        return render(request, 'options_success.html')

    elif request.method == 'TRACE':

        return render(request, 'trace_success.html')
