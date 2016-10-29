#!/usr/bin/env python
import re
from sys import argv


def scrub(args):
    emails_file = args.emails
    blacklist_file = args.blacklist

    with open(blacklist_file) as f:
        blacklist_re = re.compile('|'.join(line.strip() for line in f))

    with open(emails_file) as emails, open('removed.txt', 'w') as removed, open('good.txt', 'w') as good:
        for email in emails:
            if blacklist_re.search(email):
                removed.write(email + '\n')
                print email, "is in Blacklist"
            else:
                good.write(email + '\n')
                print email, "is Good"

    return scrub


if __name__ == '__main__':
    main()
