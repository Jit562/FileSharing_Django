from django.urls import path
from fileapp.views import HandleFileUpload


urlpatterns = [
    path('', HandleFileUpload.as_view(), name='handlefile'),
]