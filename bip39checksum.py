#!/usr/bin/python3


#   Copyright (C) 2019-2020 Denali Sàrl www.denali.swiss, Massimo Musumeci, @massmux
#
#   Bruteforce checking checksum of 24th words of a bip39 sequence
#
#   It is subject to the license terms in the LICENSE file found in the top-level
#   directory of this distribution.
#
#   No part of this software, including this file, may be copied, modified,
#   propagated, or distributed except according to the terms contained in the
#   LICENSE file.
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER


import mnemonic
import sys,argparse,os

APPDIR=sys.path[0]
wordsfile=APPDIR+"/english.txt"

""" parsing arguments """
def parseArguments():
    global args
    parser = argparse.ArgumentParser("bip39checksum.py")
    parser.add_argument("-s","--sequence", help="Specify sequence words file \
                        to check. Single line, words separed by a space", type=str, required=True)
    args = parser.parse_args()


def main():
  try:
    f=open(wordsfile)
    english = f.read().strip().split('\n')
    f.close()
  except:
    print("ERROR reading bip39 vocabulary")
    sys.exit()
    
  try:
    f=open(sequence)
    words = f.read().strip()
    f.close()
    if len(words.split(' ')) != 23:
        print("It seems not 23 words sequence")
        sys.exit()
  except:
    print("ERROR reading your 23 words bip39 sequence")
    sys.exit()

  m = mnemonic.Mnemonic('english')
  print("::Tested valid bip39 sequences::\n")
  for word in english:
    seq = "%s %s" % (words,word)
    if m.check(seq):
        print (seq)


if __name__ == "__main__":
    parseArguments()
    (sequence)=(args.sequence)
    main()

