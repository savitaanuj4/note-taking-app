from django.db import models
from accounts.models import User

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.pk} by {self.created_by.email}"
    
class SharedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='shared_notes')
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_notes')
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.note.pk} shared with {self.shared_with.email} at {self.shared_at}"

class NoteVersion(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='versions')
    title = models.CharField(max_length=50)
    content = models.TextField()
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note Version {self.pk} of Note {self.note.pk} by {self.modified_by.email} at {self.modified_at}"