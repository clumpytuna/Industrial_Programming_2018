from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:affair_id>/doer/', views.doer, name='doer'),
    path('/adder', views.adder, name='adder')
]