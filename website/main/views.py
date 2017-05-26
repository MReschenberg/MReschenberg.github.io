from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'aboutme.html', context=None)

class ProjectsPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'projlanding.html', context=None)

class OrgPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'organisations.html', context=None)        

class CalTeachPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'calteach.html', context=None)

class CSPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'cs.html', context=None)        

class PhotogPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'photography.html', context=None)