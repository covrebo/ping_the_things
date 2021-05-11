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

    compare_ping_results(batch)

    return None

def compare_ping_results(batch: int) -> Dict:
    batch_prev = batch - 1

    session = session_factory()

    results_prev = session.query(PingLog).filter_by(batch=batch_prev).all()

    results_cur = session.query(PingLog).filter_by(batch=batch).all()

    return None