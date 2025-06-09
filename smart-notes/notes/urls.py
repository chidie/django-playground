from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesView.as_view(), name='notes_list'),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name='note_detail'),
]