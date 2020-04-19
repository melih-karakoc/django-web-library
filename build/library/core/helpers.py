from datetime import datetime
from ..profiles.models import Profiles

def get_now_strftime():
    now = datetime.now()
    day = now.strftime('%d-%m-%Y')
    clock = now.strftime('%H-%M')


def check_user_or_manager(username, password):
    profile = Profiles.objects.filter(username=username)
    if not profile.exists():
        return {'404': 'user not found'}
    profile = profile.last()
    profile_type = getattr(profile, 'managers', 'user')
    if profile_type == 'user':
        if profile.password != password:
            return {'401': 'incorrect password'}
        data = {
            'profile_type': 'user',
            'user_obj': profile.users
        }
    else:
        if profile.password != password:
            return {'401': 'incorrect password'}
        data = {
            'profile_type': 'manager',
            'manager_obj': profile.managers
        }
    return data

