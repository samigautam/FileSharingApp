from rest_framework import serializers
from .models import *

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 10000000, allow_empty_file = False, use_url = False)
    )

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs =[]
        for file in files:
            files_obj = File.objects.create(folder= folder, file = file)
            files_objs.append(files_obj)

        return Files.files_obj