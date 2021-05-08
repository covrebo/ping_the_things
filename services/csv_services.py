import csv
from typing import List

hosts = []

# open a local csv file to read in a list of hosts to check
def import_hosts_from_csv() -> List:
    with open('data/things.csv', 'r') as things_to_ping:
        # create the list of hosts
        for line in csv.DictReader(things_to_ping):
            try:
                # add a tuple for each host and hostname to the list of hosts
                hosts.append((line['Host'], line['Hostname']))
            except ValueError:
                continue

    return hosts