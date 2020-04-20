from django.shortcuts import render
from rest_framework.decorators import api_view
from datetime import datetime
from dateutil.relativedelta import relativedelta

from ..managers.models import Books
from ..profiles.models import Profiles
from ..users.models import UserBooks
from ..managers.helpers import isbn_number_read


@api_view(['GET', 'POST'])
def UserBookSearchView(request, profile_id):
    if request.method == 'GET':
        context = {
            'profile_id': profile_id
        }
        return render(request, 'users/search.html', context)
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
                    'profile_id': profile_id,
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
                    'profile_id': profile_id
                }
                return render(request, 'users/book-list.html', context)
            else:
                context = {
                    'body': 'Girdiğiniz kitap adında yada ISBN numarası ile '
                            ' sistemde  kitap bulunamamıştır.',
                    'url': 'search/book/{}'.format(profile_id)
                }
                return render(request, '500-template.html', context)
        else:
            context = {
                'body': 'Lütfen kitap adı yada ISBN no giriniz',
                'url': 'search/book/{}'.format(profile_id)
            }
            return render(request, '500-template.html', context)


@api_view(['GET', 'POST'])
def UserTakeBooks(request, profile_id):
    if request.method == 'POST':
        books = request.POST.getlist('books')
        profile = Profiles.objects.get(id=profile_id)
        user = profile.users
        requested_books = Books.objects.filter(isbn__in=books)
        if len(requested_books) > 3:
            context = {
                'body': '3 adetten fazla kitap alinamaz',
                'url': 'search/book/{}'.format(profile_id)
            }
            return render(request, '500-template.html', context)
        now = datetime.now()
        receiving_date = now
        delivery_date = now + relativedelta(days=7)
        # user take book conditions
        check = UserBooks.objects.filter(book__in=requested_books)
        if check.exists():
            context = {
                'body': 'Bu kitap bir baskasi tarafindan alinmis',
                'url': 'search/book/{}'.format(profile_id)
            }
            return render(request, '500-template.html', context)
        if (int(user.get_user_number_of_book) + len(requested_books)) > 3:

            context = {
                'body': '3 kitaptan fazla alamzsiniz',
                'url': 'search/book/{}'.format(profile_id)
            }
            return render(request, '500-template.html', context)
        for book in user.book.all():
            if now > book.delivery_date.utcnow():

                context = {
                    'body': 'elinizde teslim tarihi gecmis kitap '
                            'bulundurdugunuz icin kitap alamazsiniz',
                    'url': 'search/book/{}'.format(profile_id)
                }
                return render(request, '500-template.html', context)
        created = []
        for book in requested_books:
            x = UserBooks.objects.create(
                user=user, book=book, receiving_date=receiving_date,
                delivery_date=delivery_date
            )
            created.append(x)

        context = {
            'header': 'Success',
            'body': '{} adet kitap aldiniz'.format(len(created)),
            'url': 'giris/',
            'backto': 'Girise geri don'

        }
        return render(request, 'success.html', context)


@api_view(['GET', 'POST'])
def UserReturnBookView(request, profile_id):
    if request.method == 'GET':
        context = {
            'profile_id': profile_id,
        }
        return render(request, 'users/give-book.html', context)
    if request.method == 'POST':
        image = request.FILES['img']
        isbn = isbn_number_read(image)
        if not isbn:
            context = {
                'body': 'ISBN okunamadı lütfen tekrar deneyiniz',
                'url': 'return/book/{}'.format(profile_id)
            }
            return render(request, '500-template.html', context)
        book = Books.objects.filter(userbooks__user__profile__id=4,
                                    isbn=isbn).last()
        if book:
            ub = UserBooks.objects.filter(book=book).last()
            check = ub.delete()
            if check:
                context = {
                    'header': 'Success',
                    'body': 'Tebrikler kitabi iade ettiniz',
                    'url': 'giris/',
                    'backto': 'Girise geri don'

                }
                return render(request, 'success.html', context)
