from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Contact


def main_page(request):
    lista = [1, 2, 3, 4, 5]
    lists_posts = Post.objects.all()
    second_list = Post.objects.filter(name="joao")
    data = {'name': 'Lucas Guedes',
            'lista': lista,
            'Posts': lists_posts,
            'Test': second_list
            }

    return render(request, 'index.html', data)


def save_form(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    Contact.objects.create(
        name=name,
        email=email,
        message=message
    )

    data = {'name': name, 'email': email, 'message': message}

    return render(request, 'contatorecebido.html', data)
