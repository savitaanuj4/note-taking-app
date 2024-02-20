from rest_framework import serializers
from .models import Note, NoteVersion

class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.email
    
    class Meta:
        model = Note
        fields = ['id','title', 'content', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

class NoteVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteVersion
        fields = ['id', 'note', 'title', 'content', 'modified_by', 'modified_at']