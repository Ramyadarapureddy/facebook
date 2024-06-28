from django.urls import path

from . import views
urlpatterns=[
    path('timeline',views.timeline_page,name='timeline-page'),
    path('home',views.home_page,name='home-page'),
    path('create-post',views.create_post,name='create-post'),
    path('update-like',views.update_like,name='update-like'),
    path('handle-follow/<int:user_id>',views.handle_follow,name='handle-follow'),
    path('add-comment/<int:post_id>', views.add_comment, name='add-comment'),
    path('profile-page/<int:user_id>',views.profile_page,name='profile-page'),
]