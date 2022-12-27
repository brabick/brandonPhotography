import os
from os.path import join

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Post


def getImages(dir):
    images = {'data': [],
              'count': 0}
    directory = "C:\PhotographyPortfolio\photographyportfolio\photography\static" + dir
    for file in os.listdir(directory):
        # f = os.path.join(directory, file)
        f = dir + file
        images['data'].append('../../static' + f)
        images['count'] += 1

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


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'pages/blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'