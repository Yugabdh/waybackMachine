#!/usr/bin/env python3
import argparse

from scripts.main import WayBackMachine


if __name__ == '__main__':
    wayback_parser = argparse.ArgumentParser(
        description='List all the endpoints for given domain',
        usage='python3 waybackMachine.py example.com'
    )

    wayback_parser.add_argument(
        'domain_name',
        type=str,
        help='Domain name'
    )

    wayback_parser.add_argument(
        '-f', '--fyear',
        type=int,
        metavar='',
        help='Results from year'
    )

    wayback_parser.add_argument(
        '-t', '--tyear',
        type=int,
        metavar='',
        help='Results to year'
    )

    args = wayback_parser.parse_args()
    wbm = WayBackMachine(
        domain=args.domain_name,
        start_year=args.fyear,
        stop_year=args.tyear
    )

    url_list = wbm.get_urls()

    for row in url_list[1:]:
        print(row[0])
