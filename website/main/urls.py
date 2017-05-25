from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), 
    url(r'^projects/$', views.ProjectPageView.as_view()), 
    url(r'^organisations/$', views.OrgPageView.as_view()), 

]