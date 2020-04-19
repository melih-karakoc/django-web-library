from rest_framework.decorators import api_view
from django.shortcuts import render


@api_view(['GET'])
def test(request):
    return render(request, 'test.html')


@api_view(['GET', 'POST'])
def MainEnterPageView(request):
    if request.method == 'GET':
        return render(request, 'main_entrance.html')
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        print(username)
        print(password)
        return render(request, 'test.html')
