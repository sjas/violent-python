#!/usr/bin/env python3

import crypt


def testPass(pw):
    salt = pw[0:2]
    dict_file = open('005a-dictionary.txt', 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, salt)
        if crypt_word == pw:
            print('[+] found pw: ' + word + '\n')
            return
    print('[-] pw not found.')
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
