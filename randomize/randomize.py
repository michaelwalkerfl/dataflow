#!/usr/bin/python

import sys
import random

def randomize(args):
    file_list = args.list
    with open(file_list, 'r') as f:
        flist = f.readlines()
        random.shuffle(flist)

        for line in flist:
            print line.strip()

if __name__ == '__main__':
    main()
