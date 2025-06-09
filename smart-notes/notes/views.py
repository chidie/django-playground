from django.shortcuts import render
from django.http import Http404

from .models import Note

def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        # return render(request, 'notes/404.html', status=404)
        raise Http404("Note does not exist")
    
    return render(request, 'notes/note_detail.html', {'note': note})
