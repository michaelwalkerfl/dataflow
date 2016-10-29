#!/usr/bin/python

import sys
import csv_splitter

def split(args):
    file_to_split = args.file
    with open(file_to_split, 'r') as f:
        csv_splitter.split(f);


if __name__ == '__main__':
    main()
