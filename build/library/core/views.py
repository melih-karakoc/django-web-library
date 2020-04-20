from rest_framework.decorators import api_view
from django.shortcuts import render
from ..core.helpers import check_user_or_manager

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
        result = check_user_or_manager(username, password)
        if result.get('404') or result.get('401'):
            return render(request, '404-not-found.html')
        if result['profile_type'] == 'manager':
            return render(request, 'manager-main-page.html')
        if result['profile_type'] == 'user':
            return render(request, 'users/user-main-page.html')

        return render(request, 'test.html')
