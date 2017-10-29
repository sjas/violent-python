#!/usr/bin/env python3

import inspect
import sys
import os


def usage():
    fn = inspect.stack()[0][1]
    print()
    print('usage: ' + fn + ' OPTION file_name')
    print()
    print('OPTIONs:')
    print(' - exists')
    print(' - readable')
    print(' - writable')
    print(' - executable')


def check_argument_count():
    if not len(sys.argv) == 3:
        usage()
        sys.exit(1)


def check_if_file_exists(fn):
    return os.path.isfile(fn)


def check_if_file_is_readable(fn):
    return os.access(fn, os.R_OK)


def check_if_file_is_writable(fn):
    return os.access(fn, os.W_OK)


def check_if_file_is_executable(fn):
    return os.access(fn, os.X_OK)


def main():
    check_argument_count()

    opt = sys.argv[1]
    fn = sys.argv[2]

    if opt == 'exists':
        if check_if_file_exists(fn):
            print(fn + ' exists.')
        else:
            print(fn + ' does not exist.')
    elif opt == 'readable':
        if check_if_file_is_readable(fn):
            print(fn + ' is readable.')
        else:
            print(fn + ' is not readable.')
    elif opt == 'writable':
        if check_if_file_is_writable(fn):
            print(fn + ' is writable')
        else:
            print(fn + ' is not writable.')
    elif opt == 'executable':
        if check_if_file_is_executable(fn):
            print(fn + ' is executable.')
        else:
            print(fn + ' is not executable.')


if __name__ == '__main__':
    main()
