from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), 
    url(r'^projects/$', views.ProjectsPageView.as_view()), 
    url(r'^organisations/$', views.OrgPageView.as_view()), 
    url(r'^calteach/$', views.CalTeachPageView.as_view()), 
    url(r'^cs/$', views.CSPageView.as_view()), 
    url(r'^photography/$', views.PhotogPageView.as_view()), 

]