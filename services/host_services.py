from typing import List
from models.db_base import session
from models.host_models import Host

def write_hosts_to_db(host_list: List):
    for host in host_list:
        new_host = Host(host=host[0], host_name=host[1])

        session.add(new_host)

    session.commit()

    return None