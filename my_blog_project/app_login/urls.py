from django.conf import settings
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns,static
from django.urls import path
from . import views

app_name='app_login'


urlpatterns=[
    path('signup/', views.sign_up,name='signup'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('change-profile/', views.user_change,name='change_profile'),
    path('change-password/', views.pass_change,name='change_password'),
    path('add-pro-pic/', views.add_pro_pic,name='add_pro_pic'),
    path('change-pro-pic/', views.change_pro_pic,name='change_pro_pic')
]


