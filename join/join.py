#!/usr/bin/python

import glob

# Change to *.txt if needed.
files = glob.glob( '*.csv' )

with open( 'joined.csv', 'w' ) as result:
    for file_ in files:
        for line in open( file_, 'r' ):
            result.write( line )
