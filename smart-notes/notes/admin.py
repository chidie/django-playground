from django.contrib import admin

from . import models

class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface for managing notes in the SmartNote application.
    """
    list_display = ('title', 'created_at', 'number_of_likes')
    search_fields = ('title', 'content')
    list_filter = ('created_at',) 
     
    def number_of_likes(self, obj):
        """
        Returns the number of likes for the note.
        """
        return obj.number_of_likes

    number_of_likes.short_description = 'Likes'

admin.site.register(models.Note, NoteAdmin)

