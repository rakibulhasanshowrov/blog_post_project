from django.urls import path,re_path
from . import views

app_name='app_blog'

urlpatterns=[
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<slug:slug>',views.blog_details,name='blog_details'),
    re_path(r'^details/(?P<slug>[\w\W-]+)/$', views.blog_details, name='blog_details'),
    path('liked/<pk>/',views.liked,name="liked_post"),
    path('unliked/<pk>/',views.unliked,name="unliked_post"),
    path('my-blogs/',views.MyBlogs.as_view(),name='my_blogs'),
     path('edit/<pk>',views.UpdateBlog.as_view(),name='edit_blog'),
    
]