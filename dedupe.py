#!/usr/bin/env python

'''
Python is not a good solution for splitting larger files, awk is much faster.
awk '!x[$0]++' /path/to/file > /path/to/deduped_file
'''

from sys import argv

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        flist = f.readlines()
        deduped = list(set(flist))

        with open('deduped_file.txt', 'w') as result:
            for line in deduped:
                result.write(line)
