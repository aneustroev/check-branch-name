#!/usr/bin/env python3

import sys
import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    exit_code = 0
    acl_pattern = re.compile(r"^@ACL .*")

    for file in args.files:
        with open(file, 'r') as f:
            first_line = f.readline().strip()
            if not acl_pattern.match(first_line):
                print(f"Missing or incorrect @ACL annotation in file: {file}")
                exit_code = 1

    sys.exit(exit_code)

if __name__ == "__main__":
    exit(main())
