#!/usr/bin/env python3

import inspect
import sys


def usage():
    fn = inspect.stack()[0][1]
    print()
    print('usage: ' + fn + " first_string second_string")


def main():
    try:
        if not len(sys.argv) == 3:
            usage()
        else:
            print('[+] ' + sys.argv[1] + " " + sys.argv[2])
    except Exception as e:
        print('[-] ' + e)


if __name__ == '__main__':
    main()
