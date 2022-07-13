from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.training_detail, name='trainin_detail'),
    path('', views.enter, name='enter'),
    path('mainscreen/', views.add_training, name='add_training'),

]