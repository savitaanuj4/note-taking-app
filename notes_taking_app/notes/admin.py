from django.contrib import admin
from .models import Note, SharedNote, NoteVersion

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_by', 'created_at']
    search_fields = ['title', 'created_by']

class SharedNoteAdmin(admin.ModelAdmin):
    list_display = ['note', 'shared_with']

admin.site.register(Note, NoteAdmin)
admin.site.register(SharedNote, SharedNoteAdmin)
admin.site.register(NoteVersion)