from django.conf.urls import url
from . import views

urlpatterns = [
    # Post
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # Recettes
    url(r'^allrecettes', views.allrecettes, name="allrecettes"),
    url(r'^recette/(?P<id>\d+)/', views.recette, name="recette"),
    # Outils
    url(r'^calc_with_densimetre', views.calc_with_densimetre, name='calc_with_densimetre'),
    url(r'^calc_with_refracto', views.calc_with_refracto, name='calc_with_refracto'),
]