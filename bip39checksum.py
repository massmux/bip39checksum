#!/usr/bin/python3


import argparse
import sys

import mnemonic
import os

wordsfile = f"{sys.path[0]}/english.txt"


""" parsing arguments """
def parse_arguments():
    global args
    parser = argparse.ArgumentParser("bip39checksum.py")
    parser.add_argument("-s", "--sequence", help="Specify sequence words file \
                        to check. Single line, words separated by a space", type=str, required=True)
    args = parser.parse_args()


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def main():
    try:
        f = open(wordsfile)
        english = f.read().strip().split('\n')
        f.close()
    except:
        print("ERROR reading bip39 vocabulary")
        sys.exit()

    try:
        f = open(sequence)
        words = f.read().strip()
        f.close()
        if len(words.split(' ')) != 23:
            print("ERROR: it does not seem 23 words sequence")
            sys.exit()
    except:
        print("ERROR: error while reading your 23 words bip39 sequence")
        sys.exit()

    m = mnemonic.Mnemonic('english')
    clear()
    print("::Tested valid bip39 sequences::\n")
    for word in english:
        seq = "%s %s" % (words, word)
        if m.check(seq):
            print(seq)


if __name__ == "__main__":
    parse_arguments()
    sequence = args.sequence
    main()
