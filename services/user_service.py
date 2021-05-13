import sys
from typing import List, Optional

from models.modelbase import session_factory
from models.user_models import User

##########################
###  MANAGE USERS CLI  ###
##########################

# CLI method to list, add, or remove users
def manage_users():
    while True:
        task = input(f'How do you want to manage users? [L]ist users, [A]dd user, [R]emove user, or [Q]uit: ')
        if task.lower() == 'q':
            sys.exit("Goodbye")
        if task.lower() == 'l':
            user_list = list_users()
            if user_list:
                for row in user_list:
                    print(f'ID:\t{row.id}')
                    print(f'Name:\t{row.f_name} {row.l_name}')
                    print(f'Email:\t{row.email}\n')
        if task.lower() == 'a':
            new_user = []
            new_user.append(input(f'User first name: '))
            new_user.append(input(f'User last name: '))
            new_user.append(input(f'User email: '))
            add_user(new_user)
        if task.lower() == 'r':
            id = input(f'Enter ID of user to remove or [L]ist current users: ')

            if id.lower() == 'l':
                user_list = list_users()
                if user_list:
                    for row in user_list:
                        print(f'ID:\t{row.id}')
                        print(f'Name:\t{row.f_name} {row.l_name}')
                        print(f'Email:\t{row.email}\n')
            else:
                try:
                    id = int(id)
                except:
                    print(f'ID not recognized, please enter ID number.')
            remove_user(id)
        else:
            print(f'Input not recognized. Expected input: L, A, R, or Q')
    return None

####################
###  DB Methods  ###
####################

def add_user(user: List) -> bool:
    session = session_factory()

    # check for duplicate email
    if get_user_by_email(user[2]):
        print(f'This email already exists')
        return True

    new_user = User(f_name=user[0], l_name=user[1], email=user[2])
    session.add(new_user)

    session.commit()
    session.close()

    sys.exit(f"New user {user[0]} {user[1]} created.")

# remove a user from db by id
def remove_user(id: int):
    session = session_factory()

    user = get_user_by_id(id)
    # check if user id exists
    if not user:
        print(f'User ID {id} not found in db. Please try again.')
        return True

    session.delete(user)
    session.commit()
    session.close()

    return True

# retrieve a list of users ordered by id
def list_users() -> List[User]:
    session = session_factory()
    user_list = session.query(User).order_by(User.id.desc()).all()
    session.close()
    return user_list

# retrieve a user by id
def get_user_by_id(id: int) -> Optional[User]:
    session = session_factory()
    user = session.query(User).filter_by(id=id).first()
    session.close()
    return user

# retrieve a user by email
def get_user_by_email(email: str) -> Optional[User]:
    session = session_factory()
    user = session.query(User).filter_by(email=email).first()
    session.close()
    return user
