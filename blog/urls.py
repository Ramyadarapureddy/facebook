from django.urls import path

from . import views
urlpatterns=[
    path('timeline',views.timeline_page,name='timeline-page'),
    path('home',views.home_page,name='home-page'),
    path('create-post',views.create_post,name='create-post'),
    path('update-like',views.update_like,name='update-like'),
]