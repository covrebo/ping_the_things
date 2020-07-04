import os

# TODO implement file i/o into list of namedtuples or dictionary?
# TODO implement support for Windows
# TODO improve reporting
# TODO email report
# TODO automate running the script

hosts = ['192.168.1.1', 'google.com']
report = []

for host in hosts:
    response = os.system(f'ping -c 1 {host}')

    if response == 0:
        report.append([f'{host} is up!', 1])
    else:
        report.append([f'{host} is down!', 0])

print('-' * 40)

print('These hosts are down:')
for result in report:
    if result[1] == 0:
        print(f'\t {result[0]}')

print('-' * 40)

print('These hosts are up:')
for result in report:
    if result[1] == 1:
        print(f'\t {result[0]}')

print('-' * 40)