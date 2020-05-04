#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Merge all files in input path.

usage: merge_files [-h] [-o OUTPUT] [-e EXTENSIONS] [-b MB] input

positional arguments:
  input                 input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file name
  -e EXTENSIONS, --extensions EXTENSIONS
                        allowed file extensions (comma separated)
  -b MB, --buffer-length MB
                        default to 10 megabytes
'''

from argparse import ArgumentParser
from os import walk
from shutil import copyfileobj

BUFFER_LENGTH = 10 # megabytes

def merge_files(input_name, output_name=None,
    extensions=[], buffer_length=BUFFER_LENGTH):
    '''
    Merge files in folder through byte reading.

    Allows UNIX wildcards as input name, being
    a . (dot) for merging files in the current
    path or an * (asterisk) for all subfolders.
    '''
    file_list = []
    merge_subfolders = False

    if input_name == '*':
        merge_subfolders = True
        input_name = '.'

    if not output_name:
        output_name = (input_name if input_name != '.' else 'output') + '.MERGED'

    if isinstance(extensions, str):
        extensions = extensions.replace(', ', ',').split(',')

    for path, folders, files in walk(input_name):
        if path == input_name or merge_subfolders:
            for f in files:
                cond1 = (extensions == [])
                cond2 = (any(f.endswith(x) for x in extensions))
                cond3 = (f == output_name and path == input_name)
                if (cond1 or cond2) and not cond3:
                    file_list.append(path + '/' + f)

    int_total = len(file_list)
    print('Merging %d files...' % int_total)

    if int_total > 0:
        with open(output_name, 'wb') as wfd:
            for f in file_list:
                print('%s/%s: %s...' % (file_list.index(f)+1, str(int_total), f))
                with open(f, 'rb') as fd:
                    copyfileobj(fd, wfd, 1024*1024*buffer_length)

if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('input', action='store', help='input file name')
    parser.add_argument('-o', '--output', action='store', help='output file name')
    parser.add_argument('-e', '--extensions', action='store', default=[], help='allowed file extensions (comma separated)')
    parser.add_argument('-b', '--buffer-length', action='store', type=int, help='default to 10 megabytes', dest='MB', default=BUFFER_LENGTH)

    args = parser.parse_args()

    merge_files(args.input,
                args.output,
                args.extensions,
                args.MB)