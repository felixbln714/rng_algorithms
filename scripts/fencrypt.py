#!/bin/python3.9

from cryptography.fernet import Fernet
import argparse

# set opt args
parser = argparse.ArgumentParser(description="Simple File Encryption Script")
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='Set path to file')
parser.add_argument('-g', '--generate-key', dest="generate_key", action="store_true", help="Generate new key or use existing")
parser.add_argument('-u', '--use-function', type=str, required="True", help="Choose to encrypt `e` or decrypt `d` a file") 
args = parser.parse_args()

# redefine arg variables
filename = args.file
generate_key = args.generate_key
use_function = args.use_function

def write_key():
    # generate key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write encrypted file data into file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write decrypted file data into file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    if generate_key:
        write_key()
    # load key
    key = load_key()

    if use_function == "e":
        print(f"encrypting {filename}...")
        encrypt(filename, key)
        print(f"{filename} has been encrypted successfully...")
    elif use_function == "d":
        print(f"decrypting {filename}...")
        decrypt(filename, key)
        print(f"{filename} has been decrypted successfully...")
    else: raise TypeError("Please specify wether you want to encrypt or decrypt the file")
