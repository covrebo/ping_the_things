import sys
from typing import List, Optional
from models.modelbase import session_factory
from models.host_models import Host

############################
###  MANAGING HOSTS CLI  ###
############################

def manage_hosts():
    while True:
        task = input(
            f'How do you want to manage hosts? [L]ist hosts, [A]dd host, [R]emove host, or [Q]uit: ')
        if task.lower() == 'q':
            sys.exit("Goodbye")
        if task.lower() == 'l':
            host_list = get_all_hosts()
            if host_list:
                print(f'-' * 5)
                for row in host_list:
                    print(f'| ID: {row.id}')
                    print(f'| Host: {row.host}')
                    print(f'| Host name: {row.host_name}')
                    print('-' * 5)
        if task.lower() == 'a':
            new_host = []
            new_host.append(input(f'Host IP or address: '))
            new_host.append(input(f'Host name: '))
            add_host(new_host)
        if task.lower() == 'r':
            id = input(f'Enter ID of host to remove or [L]ist current hosts: ')

            if id.lower() == 'l':
                host_list = get_all_hosts()
                if host_list:
                    print('-' * 5)
                    for row in host_list:
                        print(f'| ID: {row.id}')
                        print(f'| Host: {row.host}')
                        print(f'| Host name: {row.host_name}')
                        print('-' * 5)
            else:
                try:
                    id = int(id)
                except:
                    print(f'ID not recognized, please enter valid ID number.')
            remove_host(id)
        else:
            print(f'Input not recognized. Expected input: L, A, R, or Q')
    return None


####################
###  DB METHODS  ###
####################

# write the list of hosts from a csv import to the db
def write_hosts_to_db(host_list: List):
    session = session_factory()

    for host in host_list:
        new_host = Host(host=host[0], host_name=host[1])
        session.add(new_host)

    session.commit()
    session.close()

    return None

# get a list of all hosts in the db
def get_all_hosts() -> List[Host]:
    session = session_factory()
    hosts = session.query(Host).all()
    session.close()

    return hosts

# method to add new host to db
def add_host(host: List) -> bool:
    session = session_factory()

    # check for duplicate email
    if get_host_by_address(host[0]):
        print(f'This host already exists')
        return True

    new_host = Host(host=host[0], host_name=host[1])
    session.add(new_host)

    session.commit()
    session.close()

    sys.exit(f"New host {host[1]} created.")

# remove a host from db by id
def remove_host(id: int):
    session = session_factory()

    host = get_host_by_id(id)
    # check if user id exists
    if not host:
        print(f'Host ID {id} not found in db. Please try again.')
        return True

    session.delete(host)
    session.commit()
    session.close()

    return True

# retrieve a host by address
def get_host_by_address(address: str) -> Optional[Host]:
    session = session_factory()
    host = session.query(Host).filter_by(host=address).first()
    session.close()
    return host

# retrieve a host by id
def get_host_by_id(id: int) -> Optional[Host]:
    session = session_factory()
    host = session.query(Host).filter_by(id=id).first()
    session.close()
    return host
