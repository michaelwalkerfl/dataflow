#!/usr/bin/python


def join(args):
    import glob

    directory = args.dir
    file_type = args.type
    # Change to *.txt if needed.
    files = glob.glob('{0}/*.{1}').format(directory, file_type)

    with open( 'joined.csv', 'w' ) as result:
        for file_ in files:
            for line in open( file_, 'r' ):
                result.write( line )


if __name__ == '__main__':
    main()
