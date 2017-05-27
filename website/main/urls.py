from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^about/$', views.AboutPageView.as_view()), 
    url(r'^projects/$', views.ProjectsPageView.as_view()), 
    url(r'^organisations/$', views.OrgPageView.as_view()), 
    url(r'^projects/calteach/$', views.CalTeachPageView.as_view()), 
    url(r'^projects/cs/$', views.CSPageView.as_view()), 
    url(r'^projects/photography/$', views.PhotogPageView.as_view()), 
]