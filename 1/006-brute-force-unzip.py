#!/usr/bin/env python3

# preparations:
# mkdir 006a-folder
# echo 'goodbye cruel world' > 006a-folder/file.txt
# zip -re 006a-encrypted.zip 006a-folder
# pass: asdf
# pass: asdf
# rm -rf 006a-folder
#
# test archive with: unzip 006a-encrypted.zip
# rm -rf 006a-folder

import sys
import zipfile


def main():
    pf = open('006a-dictionary.txt', 'r')
    zf = zipfile.ZipFile("006a-encrypted.zip")
    for pw in pf:
        try:
            print(pw)
            # zf.setpassword(pwd=bytes(pw, 'utf-8'))
            zf.extractall(pwd=bytes(pw, 'utf-8'))
            print('[+] found pass: ' + pw)
            sys.exit(0)
        except:
            pass


if __name__ == '__main__':
    main()
