#!/usr/bin/python

import sys
import csv_splitter


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        csv_splitter.split(f);
