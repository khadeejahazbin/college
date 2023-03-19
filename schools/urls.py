from django.urls import path

from . import views
app_name='schools'
urlpatterns = [
    path('',views.home,name='home'),
    path('departments', views.allDepart, name='allDepart'),
    # path('<slug:d_slug>/',views.allDepart,name='allDepart'),
    path('departments/',views.allDepart,name='departments'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('newpage', views.newpage, name='newpage'),
    path('linkpage', views.linkpage, name='linkpage'),
    path('logout', views.logout, name='logout'),
]