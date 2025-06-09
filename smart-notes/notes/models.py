from django.db import models

class Note(models.Model):
    """
    Model representing a note in the SmartNote application.
    """
    title = models.CharField(max_length=200, verbose_name='Title of the Note')
    content = models.TextField(verbose_name='Content of the Note')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    number_of_likes = models.PositiveSmallIntegerField(default=0, verbose_name='Number of Likes')