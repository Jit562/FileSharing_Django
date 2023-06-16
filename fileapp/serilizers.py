from .models import *
from rest_framework import serializers
import shutil

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files

        fields = '__all__'

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False, use_url = False)
    )

    folder = serializers.CharField(required = False)
    
    #create the zip file
    def zip_folder(self, folder):
        shutil.make_archive(f'public/static/zip/{folder}' , 'zip', f'public/static/{folder}')

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        
        file_obj = []

        for file in files:
            file_objs = Files.objects.create(folder=folder, file=file)
            file_obj.append(file_objs)

        self.zip_folder(folder.uid)

        return {'files':{}, 'folder':str(folder.uid)}