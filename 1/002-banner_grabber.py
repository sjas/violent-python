#!/usr/bin/env python3

# def main()  ## create main function
# if __name__ == '__main__' ...
# pythonic stuff so main() will not run if script is imported somewhere else

import socket


def main():
    socket.setdefaulttimeout(2)
    s = socket.socket()
    # ip = "127.0.0.1"
    # port = 22
    file_name = "002a-iplist.txt"
    port = 22
    try:
        f = open(file_name, 'r')
        for i in f.readlines():
            ip = i.strip('\n')
            try:
                s.connect((ip, port))
                r = s.recv(1024)
                print('[+] banner grabbed at ' + ip + ':' + str(port))
                print(r)
                print()
            except Exception as e:
                print('[-] ERROR: ' + str(e))
    except Exception as e:
        print('[-] could not read ' + file_name)


if __name__ == '__main__':
    main()
