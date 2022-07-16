from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
    path('post/<int:pk>/', views.training_detail, name='trainin_detail'),
    path('post/<int:pk>/delete', views.TrainingDelete.as_view(), name='delete'),
    path('post/<int:pk>/exercise_delete', views.ExerciseDelete.as_view(), name='exercise_delete'),

]