import argparse
import sys

from services import csv_services, ping_services, report_services, \
    host_services, user_services, setup_services
from models import host_models, modelbase

# TODO write tests
# TODO email report
# TODO automate running the script
# TODO historic reports
# TODO create alert levels/report format
# TODO add logging

##################
###  ARGPARSE  ###
##################

parser = argparse.ArgumentParser()
parser.add_argument("--load_from_csv",
                    help="import hosts from a csv template to the db",
                    action="store_true")
parser.add_argument("--setup", help="setup the db on first run", action="store_true")
parser.add_argument("--response_wait_time",
                    help="How to to wait for ping response in milliseconds (default is 250)")
parser.add_argument("--add_user", nargs=3,
                    help="3 parameters <first name> <last name> <email> to add an email recipient to the db")
parser.add_argument("--manage_users",
                    help="view a list of email recipients, add new users, or remove users",
                    action="store_true")
parser.add_argument("--manage_hosts",
                    help="view a list of hosts, add new hosts, or remove hosts",
                    action="store_true")
# TODO: add argument to only report changes
# TODO: add argument to minimize the app to run without any dependencies
args = parser.parse_args()

if args.setup:
    setup_services.check_for_db_directory()
    sys.exit("Setup complete.")

# set response time for ping command
if args.response_wait_time:
    response_wait_time = args.response_wait_time
else:
    response_wait_time = 250

# import hosts from a csv template
if args.load_from_csv:
    # import a list of hosts from a csv
    hosts_to_import = csv_services.import_hosts_from_csv()

    # write the hosts to db
    host_services.write_hosts_to_db(hosts_to_import)

# add new user to the email list db table
if args.add_user:
    user_services.add_user(args.add_user)
    sys.exit('New user created')

# manage users
if args.manage_users:
    user_services.manage_users()

# manage hosts
if args.manage_hosts:
    host_services.manage_hosts()

########################
###  PING THE HOSTS  ###
########################

# retrieve a list of hosts to ping from the db
hosts = ping_services.get_host_list()

# list of what is up and what is down
report, batch = ping_services.ping_the_hosts(hosts, response_wait_time)

# print the results
report_services.print_results(report, batch)
