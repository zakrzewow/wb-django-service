from django.shortcuts import render
from django.views import View


class IndexView(View):
    http_method_names = ['get', 'post']

    def get(self, request):
        context = {}
        return render(request, 'service/index.html', context)

    def post(self, request):
        pass


class HowToView(View):
    http_method_names = ['get']

    def get(self, request):
        return render(request, 'service/howto.html', {})


class AboutView(View):
    http_method_names = ['get']

    def get(self, request):
        return render(request, 'service/about.html', {})