# bip39checksum

bip39 checksum word finder

 tests 23 words bip39 sequence in order to find all the valid checksums. The test is made by bruteforce check against all the possible bip39 words of english dictionary.

## dependencies

```
pip3 install mnemonic
```

## how to run

 fill a file with the 23 words sequence (single line, words separed by a space) you want to test. Then just run the script. You will get a list of valid 24 words bip39 sequence as checked valid.


```
usage: bip39checksum.py [-h] -s SEQUENCE

optional arguments:
  -h, --help            show this help message and exit
  -s SEQUENCE, --sequence SEQUENCE
                        Specify sequence words file to check. Single line, words separed by a space
```


