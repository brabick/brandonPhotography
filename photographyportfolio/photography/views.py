import os
from os.path import join

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from photographyportfolio.photography.models import Post


def getImages(dir):
    images = {'data': []}
    directory = "C:\PhotographyPortfolio\photographyportfolio\photography\static" + dir
    for file in os.listdir(directory):
        # f = os.path.join(directory, file)
        f = dir + file
        images['data'].append('../../static' + f)

    print(images)
    return images


def index(request):
    images = getImages("/img/")

    return render(request, 'pages/index.html', images)


def landscape(request):
    images = getImages("/landscape/")

    return render(request, 'pages/landscape.html', images)


def contact(request):

    return render(request, 'pages/contact.html')


def post_list(request):
    queryset = Post.objects.
    template_name = 'index.html'

    return render(request, 'pages/postlist.html')


def post_detail(request):
    post = Post.objects.filter

    return render(request, 'pages/postdetail.html')
