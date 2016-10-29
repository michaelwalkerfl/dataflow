# dataflow
A collection of python utilities for your email data management needs.

- Send your email list to MySQL database.
- Parse all emails from files within a given directory.
- Randomize your email list.
- Remove duplicate emails from within a given list.
- Split large email lists for easier management.
- Combine multiple lists into one.
- Remove emails from list if contained on another list.

# Usage:
`./manage.py send_to_db --host=localhost --user=dbuser --port=3306
--password=dbpassword --db=dbname`
`./manage.py dedupe --list=file.txt`
`./manage.py join --dir=/downloads/email/ --type=csv`
`./manage.py randomize --list=file.txt`
`./manage.py scrub --emails=emails.txt --blacklist=blacklist.txt`
`./manage.py split --file=email_list.csv`
