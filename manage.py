#!/usr/bin/env python

def main():
    import argparse
    from database.send_to_database import send_to_db
    from dedupe.dedupe import dedupe
    from join.join import join
    from parse.parse import parse

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    send_to_db_parser = subparsers.add_parser('send_to_db',
                                                    help='send list to database')
    send_to_db_parser.add_argument('--host', help='database host')
    send_to_db_parser.add_argument('--user', help='database user')
    send_to_db_parser.add_argument('--port', help='database port')
    send_to_db_parser.add_argument('--password', help='database password')
    send_to_db_parser.add_argument('--database', help='database name')

    dedupe_parser = subparsers.add_parser('dedupe', help='dedupe list')
    dedupe_parser.add_argument('--list', help='list to dedupe')

    join_parser = subparsers.add_parser('join', help='join lists')
    join_parser.add_argument('--dir', help='directory of lists to join')
    join_parser.add_argument('--type', help='file types "csv" or "txt"')

    parse_parser = subparsers.add_parser('parse', help='parse emails from directory of lists')


