import argparse

from services import csv_services, ping_services, report_services, \
    host_services
from models import host_models, db_base

# TODO write tests
# TODO implement support for Windows
# TODO improve reporting
# TODO email report
# TODO automate running the script

parser = argparse.ArgumentParser()
parser.add_argument("--import", help="import hosts from a csv template to the db")
args = parser.parse_args()
print(f'args={args}')
# print(args.echo)

# create the db
db_base.create_db()

# get response wait time from user (optional)
# response_wait_time = input('How to to wait for ping response ( in milliseconds, recommend 250): ')

# comment out if prompting user for wait time
response_wait_time = 250

if "import" in args:
    # import a list of hosts from a csv
    hosts_to_import = csv_services.import_hosts_from_csv()

    # write the hosts to db
    host_services.write_hosts_to_db(hosts_to_import)

hosts = ping_services.get_host_list()

# list of what is up and what is down
report = ping_services.ping_the_hosts(hosts, response_wait_time)

# print the results
report_services.print_results(report)
