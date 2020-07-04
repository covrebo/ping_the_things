import os
import csv

# TODO implement support for Windows
# TODO improve reporting
# TODO email report
# TODO automate running the script

# get response wait time from user (optional)
# response_wait_time = input('How to to wait for ping response ( in milliseconds, recommend 250): ')

# comment out if prompting user for wait time
response_wait_time = 250

# a list of things to ping
hosts = []

# list of what is up and what is down
report = []

# open a local csv file to read in a list of hosts to check
with open('things.csv', 'r') as things_to_ping:
    # create the list of hosts
    for line in csv.DictReader(things_to_ping):
        try:
            # add a tuple for each host and hostname to the list of hosts
            hosts.append((line['Host'], line['Hostname']))
        except ValueError:
            continue

for host in hosts:
    # ping each host with one packet and wait up to 250 milliseconds for a response
    response = os.system(f'ping -W {response_wait_time} -c 1 {host[0]}')

    if response == 0:
        report.append([f'{host[0]} which is *{host[1]}* is UP!', 1])
    else:
        report.append([f'{host[0]} which is *{host[1]}* is DOWN!', 0])

# print the hosts that are down
print('-' * 80)

print('| These hosts are down:')
for result in report:
    if result[1] == 0:
        print(f'|\t {result[0]}')

# print the hosts that are up
print('-' * 80)

print('| These hosts are up:')
for result in report:
    if result[1] == 1:
        print(f'|\t {result[0]}')

print('-' * 80)