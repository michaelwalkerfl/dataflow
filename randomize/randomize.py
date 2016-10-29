#!/usr/bin/python

import sys
import random

def randomize(args):
    file_list = args.list
    with open(file_list, 'r') as f, open('randomized.txt', 'a') as clean:
        flist = f.readlines()
        random.shuffle(flist)

        for line in flist:
            clean.write(line.strip() + "\n")

    return randomize

if __name__ == '__main__':
    main()
