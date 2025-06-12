from django.urls import path

from . import views

urlpatterns = [
    path('notes/list', views.NotesView.as_view(), name='notes_list'),
    path('notes/popular', views.PopularNotesView.as_view(), name='popular_notes'),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='note_delete'),
    path('notes/<int:pk>/like', views.note_like, name='note_like'),
    path('notes/new', views.NotesCreateView.as_view(), name='note_new'),
    path('notes/<int:pk>/toggle_public', views.toggle_public, name='toggle_public'),
    path('notes/<int:pk>/share', views.NotesPublicDetailView.as_view(), name='note_share'),
]