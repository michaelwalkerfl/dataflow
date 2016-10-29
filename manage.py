#!/usr/bin/env python

def main():
    import argparse
    from database.send_to_database import send_to_db

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    send_to_db_parser = subparsers.add_parser('send_to_db',
                                                    help='send list to database')
    send_to_db_parser.add_argument('--host', help='database host')
    send_to_db_parser.add_argument('--user', help='database user')
    send_to_db_parser.add_argument('--port', help='database port')
    send_to_db_parser.add_argument('--password', help='database password')
    send_to_db_parser.add_argument('--database', help='database name')
