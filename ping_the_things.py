import argparse

from services import csv_services, ping_services, report_services, \
    host_services
from models import host_models, modelbase

# TODO write tests
# TODO implement support for Windows
# TODO email report
# TODO automate running the script
# TODO create users in database to receive emails

parser = argparse.ArgumentParser()
parser.add_argument("--load_from_csv", help="import hosts from a csv template to the db", action="store_true")
parser.add_argument("--setup", help="setup the db on first run")
parser.add_argument("--response_wait_time", help="How to to wait for ping response in milliseconds (recommend 250)")
args = parser.parse_args()
print(f'args={args}')
# print(args.echo)

# set response time for ping command
if args.response_wait_time:
    response_wait_time = args.response_wait_time
else:
    response_wait_time = 250

# if args.setup:
    # TODO: create db folder if not present
    # TODO: create workflow to add email recipients

if args.load_from_csv:
    # import a list of hosts from a csv
    hosts_to_import = csv_services.import_hosts_from_csv()

    # write the hosts to db
    host_services.write_hosts_to_db(hosts_to_import)

hosts = ping_services.get_host_list()

# list of what is up and what is down
report, batch = ping_services.ping_the_hosts(hosts, response_wait_time)

# print the results
report_services.print_results(report, batch)
