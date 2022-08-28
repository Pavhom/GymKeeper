from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.TrainingList.as_view(), name='post_list'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('post/<int:pk>/', views.training_detail, name='trainin_detail'),
    path('post/<int:pk>/delete', views.TrainingDelete.as_view(), name='delete'),
    path('post/<int:pk>/exercise_delete', views.ExerciseDelete.as_view(), name='exercise_delete'),
    path('photo/', views.photo, name='photo'),
    path('photo/<int:pk>/photo_delete', views.PhotoDelete.as_view(), name='photo_delete'),
    path('notes/', views.notes_list, name='notes_list'),
    path('notes/<int:pk>/', views.NoteUpdate.as_view(), name='note_edit'),
    path('notes/<int:pk>/note_delete', views.NoteDelete.as_view(), name='note_delete'),
    path('chart/', views.Chart.as_view(), name='chart'),

]