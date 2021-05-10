from typing import List


def print_results(report):
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

    return None