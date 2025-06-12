from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView, CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm

class NotesDeleteView(DeleteView):
    model = Note
    template_name = "notes/confirm_delete.html"
    success_url = reverse_lazy('notes_list')  # Redirect to notes list after deletion

    def get_object(self, queryset=None):
        """Override to handle object retrieval."""
        try:
            return super().get_object(queryset)
        except Note.DoesNotExist:
            raise Http404("Note not found")
        
class NotesUpdateView(UpdateView):
    model = Note
    template_name = "notes/notes_form.html"
    success_url = reverse_lazy('notes_list')  # Redirect to notes list after creation
    form_class = NoteForm  # Use the default form class

    # def get_object(self, queryset=None):
    #     """Override to handle object retrieval."""
    #     try:
    #         return super().get_object(queryset)
    #     except Note.DoesNotExist:
    #         raise Http404("Note not found")

class NotesView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"
    
    def get_queryset(self):
        # return Note.objects.filter(number_of_likes__gte=10)  # To filter notes based on likes
        return self.request.user.notes.all()  # Return notes created by the logged-in user


class NotesCreateView(CreateView):
    model = Note
    template_name = "notes/notes_form.html"
    success_url = 'list'  # Redirect to notes list after creation
    form_class = NoteForm  # Use the default form class

    def form_valid(self, form):
        # return super().form_valid(form)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    # Uncomment if you want to handle form invalid cases    
    # def form_invalid(self, form):
    #     return super().form_invalid(form)

class PopularNotesView(ListView):
    """This view displays notes with at least 2 likes."""
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Note.objects.filter(number_of_likes__gte=2)

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = "note"

class NotesPublicDetailView(DetailView):
    model = Note
    context_object_name = "note"
    queryset = Note.objects.filter(is_public=True)  # Only show public notes


# @csrf_exempt
# def note_like(request, pk):
#     """
#     View to handle liking a note.
#     Increments the number of likes for the specified note.
#     """
#     try:
#         if request.method != 'POST':
#             return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
#         else:
#             note = Note.objects.get(pk=pk)
#             note.number_of_likes += 1
#             note.save()
#             return JsonResponse({'status': 'success', 'likes': note.number_of_likes})
#     except Note.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Note not found'}, status=404)

def note_like(request, pk):
    """
    View to handle liking a note.
    Increments the number of likes for the specified note.
    """
    if request.method != 'POST':
        return Http404
    
    try:
        note = get_object_or_404(Note, pk=pk)
        note.number_of_likes += 1
        note.save()
        return HttpResponseRedirect(reverse_lazy('note_detail', args=(pk, )))  # Redirect to notes list after liking
    except Note.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Note not found'}, status=404)

@require_POST
def toggle_public(request, pk):
    """
    View to toggle the public status of a note.
    """
    try:
        note = get_object_or_404(Note, pk=pk, user=request.user)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse_lazy('note_detail', args=(pk, )))  # Redirect to note detail after toggling
    except Note.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Note not found'}, status=404)