#!/usr/bin/env python3

import os
import sys
import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    exit_code = 0
    autoindex_pattern = re.compile(r".*<autoindex>.*")

    for file in args.files:
        with open(file, 'r+') as f:
            # Get second string
            first_line = f.readline()
            second_line = f.readline()
            if not autoindex_pattern.match(second_line):
                continue

            print(f"Generate autoindex in file: {file}")
            f.seek(0)
            f.truncate(0)
            f.write(first_line)
            f.write(second_line)
            f.write("\n")

            dirlist = [directory
            for directory in os.listdir(os.path.join(os.getcwd() ,os.path.dirname(file)))
            if os.path.isdir(os.path.join(".",directory))
            if not directory.startswith('.')]

            filelist = [file
            for file in os.listdir(os.path.join(os.getcwd() ,os.path.dirname(file)))
            if os.path.isfile(os.path.join(".",file))
            if not file.startswith('.') and file.endswith('.md') and file != "README.md"]

            for directory in dirlist:
                f.write(f"* **[{directory}/]({directory}/README.md)**\n")

            if len(filelist) > 0:
                f.write("<br/>\n")
                f.write("\n")

            for file in filelist:
                f.write(f"* [{file}]({file})\n")

    sys.exit(exit_code)

if __name__ == "__main__":
    exit(main())
