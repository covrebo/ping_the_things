from typing import List, Dict

from models.modelbase import session_factory
from models.pinglog_models import PingLog


def print_results(report: List, batch: int):
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

    # print the changes
    changes = compare_ping_results(batch)

    print('-' * 80)
    print('| These hosts have changed to up:')
    if not changes["now_up"]:
        print(f"|\t No hosts have changed to up")
    else:
        for item in changes["now_up"]:
            print(f"|\t Host: {item[0]} which is {item[1]} is now UP!")
    print('-' * 80)
    print('| These hosts have changed to down:')
    if not changes["now_down"]:
        print(f"|\t No hosts have changed to down")
    else:
        for item in changes["now_down"]:
            print(f"|\t Host: {item[0]} which is {item[1]} is now DOWN!")
    print('-' * 80)
    print('| These hosts have not changed:')
    if not changes["no_change"]:
        print(f"|\t All hosts have changed status")
    else:
        for item in changes["no_change"]:
            print(f"|\t Host: {item[0]} which is {item[1]} has not changed!")
    print('-' * 80)
    print('| These hosts are new:')
    if not changes["new_host"]:
        print(f"|\t There are no new hosts")
    else:
        for item in changes["new_host"]:
            print(f"|\t Host: {item[0]} which is {item[1]} is new!")
    print('-' * 80)

    return None


def compare_ping_results(batch: int) -> Dict:
    batch_prev = batch - 1

    session = session_factory()

    # get the results from the previous batch and store in a dict
    results_prev = session.query(PingLog).filter_by(batch=batch_prev).all()

    dict_prev = {
        "up": [],
        "down": []
    }

    for row in results_prev:
        if row.status == True:
            dict_prev["up"].append((row.host, row.host_name))
        else:
            dict_prev["down"].append((row.host, row.host_name))

    # get the results of the current batch and store them in a dictionary
    results_cur = session.query(PingLog).filter_by(batch=batch).all()

    dict_cur = {
        "up": [],
        "down": []
    }

    for row in results_cur:
        if row.status == True:
            dict_cur["up"].append((row.host, row.host_name))
        else:
            dict_cur["down"].append((row.host, row.host_name))

    # create a dict of changes
    changes_dict = {
        "now_up": [],
        "now_down": [],
        "no_change": [],
        "new_host": []
    }

    for item in dict_cur["up"]:
        if item in dict_prev["up"]:
            changes_dict["no_change"].append(item)
        elif item in dict_prev["down"]:
            changes_dict["now_up"].append(item)
        else:
            changes_dict["new_host"].append(item)

    for item in dict_cur["down"]:
        if item in dict_prev["up"]:
            changes_dict["now_up"].append(item)
        elif item in dict_prev["down"]:
            changes_dict["no_change"].append(item)
        else:
            changes_dict["new_host"].append(item)

    return changes_dict
