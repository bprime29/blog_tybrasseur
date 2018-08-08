from django.conf.urls import url
from blog.views.post import *
from blog.views.outils import *
from blog.views.recettes import *


urlpatterns = [
    # Post
    url(r'^$', post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    url(r'^drafts/$', post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', post_remove, name='post_remove'),
    # Recettes
    url(r'^allrecettes', allrecettes, name="allrecettes"),
    url(r'^recette/(?P<id>\d+)/', recette, name="recette"),
    # Outils
    url(r'^calc_with_densimetre', calc_with_densimetre, name='calc_with_densimetre'),
    url(r'^calc_with_refracto', calc_with_refracto, name='calc_with_refracto'),
]