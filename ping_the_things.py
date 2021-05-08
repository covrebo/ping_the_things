from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base
from services import csv_services, ping_services, report_services
from models import host_models, db_base

# TODO write tests
# TODO implement support for Windows
# TODO improve reporting
# TODO email report
# TODO automate running the script

# get response wait time from user (optional)
# response_wait_time = input('How to to wait for ping response ( in milliseconds, recommend 250): ')

# comment out if prompting user for wait time
response_wait_time = 250

# import a list of hosts from a csv
hosts = csv_services.import_hosts_from_csv()

# list of what is up and what is down
report = ping_services.ping_the_hosts(hosts, response_wait_time)

# print the results
report_services.print_results(report)

db_base.create_db()
# engine = create_engine("sqlite+pysqlite:///db/app.db", echo=True, future=True)
# # meta = MetaData()
#
# Base = declarative_base()
#
# class Host(Base):
#     __tablename__ = "host_table"
#
#     id = Column(Integer, primary_key=True)
#     host = Column(String)
#     host_name = Column(String)
#
#     def __repr__(self):
#         return f"Host(id={self.id}, host={self.host}, host_name={self.host_name})"
#
# Base.metadata.create_all(engine)
