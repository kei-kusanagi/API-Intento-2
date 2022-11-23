from rest_framework import serializers
from drfCRUD_app import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )

