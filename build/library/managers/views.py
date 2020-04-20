from rest_framework.decorators import api_view
from django.shortcuts import render
from .helpers import isbn_number_read
from .models import Books, TimeJumps
from ..users.models import UserBooks


@api_view(['GET', 'POST'])
def ImageUploadView(request, profile_id):
    if request.method == 'GET':
        context = {
            'profile_id': profile_id,
        }
        return render(request, 'manager-image-uploader.html', context)
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
            try:
                Books.objects.create(isbn=isbn, name=book_name)
            except Exception:
                context = {
                    'body': 'ISBN numarali bir kitap sistemde zaten mevcut',
                    'url': 'add/book/{}'.format(profile_id)
                }
                return render(request, '500-template.html', context)
            return render(request, 'success.html', context)
        else:
            context = {
                'body': 'ISBN okunamadı lütfen tekrar deneyiniz',
                'url': 'add/book/{}'.format(profile_id)
            }
            return render(request, '500-template.html', context)


@api_view(['GET', 'POST'])
def ManagerUserListView(request, profile_id):
    if request.method == 'GET':
        userbooks = UserBooks.objects.all()
        data = []
        for ub in userbooks:
            data.append({
                'username': ub.user.profile.username,
                'book_name': ub.book.name,
                'book_isbn': ub.book.isbn,
                'receiving_date': ub.receiving_date,
                'delivery_date': ub.delivery_date,
            })
        context = {
            'userbooks': data
        }
        return render(request, 'manager-user-list.html', context)


@api_view(['GET', 'POST'])
def MangerTimeJumpView(request, profile_id):
    if request.method == 'GET':
        context = {
            'profile_id': profile_id
        }
        return render(request, 'time-jump.html', context)
    if request.method == 'POST':
        if request.POST.get('time_jump'):
            time_jump = int(request.POST['time_jump'])
            check = TimeJumps.objects.create(day=time_jump)
            if check:
                context = {
                    'header': 'Success',
                    'body': 'Sistem zamani {} kadar degisti'.format(time_jump),
                    'url': 'giris/',
                    'backto': 'Girise geri don'

                }
                return render(request, 'success.html', context)
        elif request.POST.get('reset'):
            time_jump_value = int(request.POST['reset'])
            time_jump = TimeJumps.objects.last()
            if time_jump:
                time_jump.day = time_jump_value
                time_jump.save()
            else:
                TimeJumps.objects.create(day=time_jump_value)

            context = {
                'header': 'Success',
                'body': 'Sistem zamani sifirlandi',
                'url': 'giris/',
                'backto': 'Girise geri don'

            }
            return render(request, 'success.html', context)
