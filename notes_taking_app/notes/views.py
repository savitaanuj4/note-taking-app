from django.shortcuts import render
from rest_framework import viewsets
from .models import Note, SharedNote, NoteVersion
from accounts.models import User
from .serializers import NoteSerializer, NoteVersionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsOwnerOrSharedUser
# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrSharedUser]

    def perform_create(self, serializer):
        # Set the user of the note to the currently authenticated user
        serializer.save(created_by=self.request.user)

    def update_share(self, note, user_to_share_with):
        # Update the SharedNote instance or create a new one if it doesn't exist
        SharedNote.objects.update_or_create(note=note, shared_with=user_to_share_with)

    def create(self, request):
        # Create a new note
        response = super().create(request)

        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        # Create a new version when the note is updated
        note = self.get_object()
        NoteVersion.objects.create(note=note, title=note.title, content=note.content, modified_by=request.user)

        return response
    
    @action(detail=False, methods=['POST'], url_path="share")
    def share(self, request):
        note_id = request.data.get("note_id")
        note = Note.objects.get(pk=note_id)
        # Check if the note should be shared with other users
        shared_with_users = request.data.get('shared_with_users', [])

        if shared_with_users:
            for user_id in shared_with_users:
                user_to_share_with = User.objects.get(pk=user_id)
                self.update_share(note, user_to_share_with)

        return Response({"message": "shared the note successfully."})
    
    @action(detail=True, methods=['GET'], url_path='version-history')
    def version_history(self, request, pk=None):
        note = self.get_object()
        versions = note.versions.all()
        serializer = NoteVersionSerializer(versions, many=True)
        return Response(serializer.data)

