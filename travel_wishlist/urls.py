from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name = 'place_list'),
    url(r'^visited$', views.places_visited, name = 'places_visited'), #add url for places visited
    # url(r'^visited$', views.places_is_visited, name = 'place_is_visited'),
    url(r'^place/$', views.place_info, name = 'place_info'),



]
