
from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path('', views.home,name='home'),
    path('<room>/', views.room,name='room'),
    path('checkview', views.checkview,name='checkview'),
    path('msgsnd/<pk>/<user>', views.msgsnd,name='msgsnd'),
]
