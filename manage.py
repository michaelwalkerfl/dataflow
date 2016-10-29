#!/usr/bin/env python
import sys


def main():
    import argparse
    from database.send_to_database import send_to_db
    from dedupe.dedupe import dedupe
    from join.join import join
    from parse.parse import parse
    from randomize.randomize import randomize
    from scrub.scrub import scrub
    from split.split import split

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    send_to_db_parser = subparsers.add_parser('send_to_db',
                                                    help='send list to database')
    send_to_db_parser.add_argument('--host', help='database host')
    send_to_db_parser.add_argument('--user', help='database user')
    send_to_db_parser.add_argument('--port', help='database port')
    send_to_db_parser.add_argument('--password', help='database password')
    send_to_db_parser.add_argument('--database', help='database name')
    send_to_db_parser.set_defaults(command=send_to_db)

    dedupe_parser = subparsers.add_parser('dedupe', help='dedupe list')
    dedupe_parser.add_argument('--list', help='list to dedupe')
    dedupe_parser.set_defaults(command=dedupe)

    join_parser = subparsers.add_parser('join', help='join lists')
    join_parser.add_argument('--dir', help='directory of lists to join')
    join_parser.add_argument('--type', help='file types "csv" or "txt"')
    join_parser.set_defaults(command=join)

    parse_parser = subparsers.add_parser('parse', help='parse emails from directory of lists')
    parse_parser.set_defaults(command=parse)

    randomize_parser = subparsers.add_parser('randomize', help='randomize list')
    randomize_parser.add_argument('--list', help='list to randomize')
    randomize_parser.set_defaults(command=randomize)

    scrub_parser = subparsers.add_parser('scrub', help='scrub list against list')
    scrub_parser.add_argument('--emails', help='list of emails to clean')
    scrub_parser.add_argument('--blacklist', help='list of emails to remove from list')
    scrub_parser.set_defaults(command=scrub)

    split_parser = subparsers.add_parser('split', help='split list')
    split_parser.add_argument('--file', help='file to split')
    split_parser.set_defaults(command=split)
    args = parser.parse_args()

    try:
        cmd = args.command
    except AttributeError:
        parser.print_help()
        return

    try:
        cmd(args)
    except KeyboardInterrupt:
        print('')
        sys.exit(1)


if __name__ == '__main__':
    main()
