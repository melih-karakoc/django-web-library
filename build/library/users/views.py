from django.shortcuts import render
from rest_framework.decorators import api_view
from ..managers.models import Books

@api_view(['GET', 'POST'])
def UserBookSearchView(request):
    if request.method == 'GET':
        return render(request, 'users/search.html')
    if request.method == 'POST':
        isbn_no = request.POST.get('isbn-no')
        book_name = request.POST.get('book-name')
        if isbn_no:
            isbn_no = int(isbn_no)
            books = Books.objects.filter(isbn=isbn_no)
            if books.exists():
                data = []
                for b in books:
                    data.append({
                        'book_name': b.name,
                        'book_isbn': b.isbn,
                    })
                context = {
                    'books': data,
                }
                return render(request, 'users/book-list.html', context)
        if book_name:
            books = Books.objects.filter(name__icontains=book_name)
            if books.exists():
                data = []
                for b in books:
                    data.append({
                        'book_name': b.name,
                        'book_isbn': b.isbn,
                    })
                context = {
                    'books': data,
                }
                return render(request, 'users/book-list.html', context)
            else:
                context = {
                    'body': 'Girdiğiniz kitap adında yada ISBN numarası ile '
                            ' sistemde  kitap bulunamamıştır.',
                    'url': 'search/book/'
                }
                return render(request, '500-template.html', context)
        else:
            context = {
                'body': 'Lütfen kitap adı yada ISBN no giriniz',
                'url': 'search/book/'
            }
            return render(request, '500-template.html', context)
