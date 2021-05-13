import os
import platform

from typing import List, Tuple
from models.modelbase import session_factory
from models.host_models import Host
from models.pinglog_models import PingLog

# list of what is up and what is down
report = []
results = []


def ping_the_hosts(host_list: List, response_wait_time: int) -> Tuple[List, int]:
    for host in host_list:
        # ping each host with one packet and wait up to 250 milliseconds for a response
        print(platform.system())
        if platform.system() == 'Windows':
            response = os.system(f'ping -W {response_wait_time} -n 1 {host[0]}')
        else:
            response = os.system(f'ping -W {response_wait_time} -c 1 {host[0]}')

        if response == 0:
            report.append([f'{host[0]} which is *{host[1]}* is UP!', 1])
        else:
            report.append([f'{host[0]} which is *{host[1]}* is DOWN!', 0])

        results.append((host[0], host[1], response))

    # write results to the db
    session = session_factory()

    # get previous batch number
    batch_num = get_batch_num()
    # increment batch number
    batch_num = batch_num + 1

    for result in results:
        if result[2] == 0:
            status = 1
        else:
            status = 0
        log_entry = PingLog(batch=batch_num, host=result[0], host_name=result[1], status=status)
        session.add(log_entry)

    session.commit()
    session.close()

    return report, batch_num


def get_host_list() -> List:
    session = session_factory()

    # get a list of all the hosts in the db
    hosts = session.query(Host).all()

    # create a list of hosts to ping
    host_list = []
    for host in hosts:
        host_list.append((host.host, host.host_name))

    # clear the db session
    session.close()

    return host_list


def get_batch_num() -> int:
    session = session_factory()

    # check if there are any existing batches
    if session.query(PingLog).all():
        # get a list of all the hosts in the db
        batch_num = session.query(PingLog.batch).order_by(
            PingLog.id.desc()).first()
        batch_num = batch_num.batch
        session.close()
    else:
        batch_num = 0

    return batch_num
