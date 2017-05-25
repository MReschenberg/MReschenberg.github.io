from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'aboutme.html', context=None)

class ProjectPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'projects.html', context=None)

class OrgPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'organisations.html', context=None)        