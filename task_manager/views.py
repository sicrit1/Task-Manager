from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class LoveIt(View):

    def get(self, request, *args, **kwargs):
        response = HttpResponse()
        response.write("<p><strong><BLOCKQUOTE><font size='20' color= 'FF0000'>Солнышко, я тебя люблю!!</BLOCKQUOTE></strong></p>")
        return response

