import re
from sys import argv
 
emails_file = argv[0]
blacklist_file = argv[1]
 
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
