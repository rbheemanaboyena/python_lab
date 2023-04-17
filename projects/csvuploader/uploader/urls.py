from django.urls import path
from uploader.views import upload_file

urlpatterns = [
    path('', upload_file, name='upload_file'),
]

