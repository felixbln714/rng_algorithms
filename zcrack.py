#!/usr/bin/python2

# import
import zipfile, argparse

# set optional arguments
parser = argparse.ArgumentParser(description='ZIP Archive Cracker')
parser.add_argument('-t', '--target', type=str, metavar='', required=True, help='Path to target ZIP archive')
parser.add_argument('-w', '--wordlist', type=str, metavar='', required=True, help='Path to wordlist')
args = parser.parse_args()

# open wordlist and set line_log
passwords = open(args.wordlist,"r").readlines()
# use wordlist to bruteforce the password
for password in passwords:
    passwd = password.rstrip()
    # use passwd, try passwd
    try:
        # set args.target as target and if match found print match
        with zipfile.ZipFile(args.target) as target:
            target.extractall(pwd=passwd)
            print("[*] Password Match Found! %s" % passwd)
            break
    except:
        # no match found, print no print no match found
        print("[I] No Match Found!")




