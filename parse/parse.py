#!/usr/bin/env python

import os, subprocess
import re
import csv

def parse():
    '''
    This script sorts through lists in a given directory and output into a single text file used for easy importing.
    '''

    regex = re.compile((r"([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                        r"{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                        r"\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))


    #regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    d = raw_input('What directory would you like to parse emails from?')

    dircontent = os.listdir(d)
    for filename in dircontent:
        print filename
        file1 = open(d + filename)
        for line in file1:
            email = re.findall(regex, line)
            with open('emailsonly.txt', 'a') as n:
                email = str(email).replace("[('", "")
                email = str(email).replace("', '@', '.')]", "")
                email = str(email).replace("', '@', '.'), (", "")
                email = str(email).replace("'", "\n")
                if email != '[]':
                    n.write(email + '\n')

    file1.close()
    n.close()


if __name__ == '__main__':
    main()
