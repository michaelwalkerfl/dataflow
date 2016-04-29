#!/usr/bin/env python

from sys import argv

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        flist = f.readlines()
        deduped = list(set(flist))

        with open('deduped_file.txt', 'w') as result:
            for line in deduped:
                result.write(line)
