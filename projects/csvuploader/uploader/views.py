from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploader/upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'uploader/upload.html')

