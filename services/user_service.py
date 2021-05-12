import sys
from typing import List

from models.modelbase import session_factory
from models.user_models import User


def add_user(user: List) -> bool:
    session = session_factory()

    new_user = User(f_name=user[0], l_name=user[1], email=user[2])
    session.add(new_user)

    session.commit()
    session.close()

    sys.exit(f"New user {user[0]} {user[1]} created.")