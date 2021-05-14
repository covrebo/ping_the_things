import os.path

# check if the db directory exists during setup process
def check_for_db_directory():
    if not os.path.isdir('./db'):
        os.mkdir('./db')
    else:
        print('The directory exists.')
    return None