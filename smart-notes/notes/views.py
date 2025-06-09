from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Note

class NotesView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Note
    context_object_name = "note"
