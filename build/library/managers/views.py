from rest_framework.decorators import api_view
from django.shortcuts import render
from .helpers import isbn_number_read
from .models import Books

@api_view(['GET', 'POST'])
def ImageUploadView(request):
    if request.method == 'GET':
        return render(request, 'manager-image-uploader.html')
    if request.method == 'POST':
        book_name = request.POST.get('name')
        image = request.FILES['img']
        isbn = isbn_number_read(image)
        if isbn:
            context = {
                'header': 'Success',
                'body': 'Kitap başarı ile sisteme kayıt edildi',
                'url': 'giris/',
                'backto': 'Girise geri don'

            }
            obj, created = Books.objects.get_or_create(isbn=isbn, name=book_name)
            return render(request, 'success.html', context)
        else:
            context = {
                'body': 'ISBN okunamadı lütfen tekrar deneyiniz',
                'url': 'add/book/'
            }
            return render(request, '500-template.html', context)
