#!/usr/bin/env python3

# hashlib is not the right choice for encrypting passwords
# this seems to be the important part of 'use hashlib?' in the exercise
# import hashlib

import crypt


def testPass(pw):
    salt = pw[0:11]
    print('\n    hash: ' + salt)
    dict_file = open('005a-dictionary.txt', 'r')
    print('    orig: ' + pw + '\n')
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, salt)
        print("\"" + word + "\"")
        print('    test: ' + crypt_word)
        if crypt_word == pw:
            print('\n[+] found pw: ' + word + '\n')
            return
    print('\n[-] pw not found.')
    return


def main():
    pw_file = open('005a-password.txt', 'r')
    for line in pw_file.readlines():
        if ":" in line:
            split_line = line.split(':')
            user = split_line[0]
            crypt_pass = split_line[1].strip(' ')
            print('[*] cracking pass for user: ' + user)
            testPass(crypt_pass)


if __name__ == '__main__':
    main()
