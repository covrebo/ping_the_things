import csv
from typing import List

from services import host_services

# open a local csv file to read in a list of hosts to check
def import_hosts_from_csv() -> List:
    hosts = []

    # get a list of hosts from the db to check for duplicates
    hosts_cur = []
    for row in host_services.get_all_hosts():
        hosts_cur.append(row.host)

    with open('data/things.csv', 'r') as things_to_ping:
        # create the list of hosts
        for line in csv.DictReader(things_to_ping):
            if line['Host'] in hosts_cur:
                print(f"{line['Host']} is already in the db and will not be added")
            else:
                try:
                    # add a tuple for each host and hostname to the list of hosts
                    hosts.append((line['Host'], line['Hostname']))
                except ValueError:
                    continue

    return hosts