#!/usr/bin/python


def join(args):
    import os

    directory = args.dir
    dircontent = os.listdir(directory)
    with open('joined.csv', 'w') as result:
        for filename in dircontent:
            file1 = open(directory + filename)
            for line in file1:
                result.write(line)

    file1.close()
    result.close()
    return join
    #file_type = args.type
    # Change to *.txt if needed.
    #files = glob.glob('{0}/*.{1}').format(directory, file_type)
    #files = glob.glob('{0}/*.csv').format(directory)
    #with open( 'joined.csv', 'w' ) as result:
    #    for file_ in files:
    #        for line in open( file_, 'r' ):
    #            result.write( line )

    #return join


if __name__ == '__main__':
    main()
