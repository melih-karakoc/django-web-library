from datetime import datetime
from ..managers.models import Managers
from ..users.models import Users

def get_now_strftime():
    now = datetime.now()
    day = now.strftime('%d-%m-%Y')
    clock = now.strftime('%H-%M')


def check_user_or_manager(email):


