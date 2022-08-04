#!/usr/bin/env python3

import sys
import argparse
import sys
import re
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("commit_msg_filepath")
    parser.add_argument(
        '-r', '--regexp', default=".*",
        help='Regular extention for validate',
    )
    args = parser.parse_args()
    regexp = args.regexp
    branch = ""

    try:
        branch = subprocess.check_output(["git","symbolic-ref", "--short", "HEAD"], universal_newlines=True).strip()
    except Exception as e:
        print(e)

    if re.match(regexp, branch):
        print(f"Branch name is ok: {branch}")
        sys.exit(0)
    else:
        print(f"Branch name is incorrect: {branch}")
        sys.exit(1)


if __name__ == "__main__":
    exit(main())
