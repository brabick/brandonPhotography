import os
from os.path import join

from django.http import HttpResponse
from django.shortcuts import render


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

