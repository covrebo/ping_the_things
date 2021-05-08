import os
from typing import List

# list of what is up and what is down
report = []

def ping_the_hosts(host_list: List, response_wait_time: int) -> List:
    for host in host_list:
        # ping each host with one packet and wait up to 250 milliseconds for a response
        response = os.system(f'ping -W {response_wait_time} -c 1 {host[0]}')

        if response == 0:
            report.append([f'{host[0]} which is *{host[1]}* is UP!', 1])
        else:
            report.append([f'{host[0]} which is *{host[1]}* is DOWN!', 0])

    return report