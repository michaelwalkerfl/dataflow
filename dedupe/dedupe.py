#!/usr/bin/env python


    def dedupe(args):
        '''
        Python is not a good solution for deduping larger files, awk is much faster.
        awk '!x[$0]++' /path/to/file > /path/to/deduped_file
        '''
        from sys import argv

        email_list = args.list
        with open(email_list, 'r') as f:
            flist = f.readlines()
            deduped = list(set(flist))

            with open('deduped_file.txt', 'w') as result:
                for line in deduped:
                    result.write(line)
        return dedupe


if __name__ == '__main__':
    main()
