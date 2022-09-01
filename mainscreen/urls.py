from django.urls import path
from . import views


urlpatterns = [
    path('', views.TrainingsView.as_view(), name='post_list'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('post/<int:pk>/', views.TrainingsDetailView.as_view(), name='training_detail'),
    path('post/<int:pk>/delete', views.TrainingDelete.as_view(), name='delete'),
    path('post/<int:pk>/exercise_delete', views.ExerciseDelete.as_view(), name='exercise_delete'),
    path('photo/', views.PhotosView.as_view(), name='photo'),
    path('photo/<int:pk>/photo_delete', views.PhotoDelete.as_view(), name='photo_delete'),
    path('notes/', views.NotesView.as_view(), name='notes_list'),
    path('notes/<int:pk>/', views.NoteUpdate.as_view(), name='note_edit'),
    path('notes/<int:pk>/note_delete', views.NoteDelete.as_view(), name='note_delete'),
    path('chart/', views.ChartsView.as_view(), name='chart'),


]