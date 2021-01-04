#!/usr/bin/python2
# Written by Felix Hellmich

import tarfile, zipfile, argparse

# set optional arguments
parser = argparse.ArgumentParser(description='Zip & Tar Cracker')
parser.add_argument('-t', '--type', type=str, metavar='', required=True, help='Set either ZIP or TAR as archive type')
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='Set path to target file')
parser.add_argument('-w', '--wordlist', type=str, metavar='', required=True, help='Set path to wordlist')
args = parser.parse_args()

# open wordlist as passwords
passwords = open(args.wordlist,"r").readlines()

# define ZIP crack function
def t_ZIP():
    for password in passwords:
        # remove '\n' from password
        passwd = password.rstrip()
        # try passwd
        try:
            # set args.file as target -> if match found: print match, else except and retry
            with zipfile.ZipFile(args.file) as target:
                target.extractall(pwd=passwd)
                print("[+] Password Match Found! %s" % passwd)
                break
        except:
            # no match found -> print status of no match found
            print("[-] No Match Found!")

# define TAR crack function
def t_TAR():
    for password in passwords:
        # remove '\n' from password
        passwd = password.rstrip()
        # try passwd
        try:
            # set args.file as target -> if match found: print match, else except and retry
            with tarfile.TarFile(args.file) as target:
                target.extractall(pwd=passwd)
                print("[+] Password Match Found! %s" % passwd)
                break
        except:
            # no match found -> print status of no match found
            print("[-] No Match Found!")

# define function that refs either ZIP or TAR
def handle():
        # try passwd with type: ZIP
        if args.type == 'zip'.lower():
            t_ZIP()
        # try passwd with type: TAR
        elif args.type == 'tar'.lower():
            t_TAR()
        # else: error
        else: print("zcrack: type: '%s': not supported or misstyped" % args.type)

# execute handler
handle()
