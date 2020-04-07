#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Merge text files in input path.

usage: merge_files.py [-h] [-o OUTPUT] input

positional arguments:
  input                 input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file name
'''

from argparse import ArgumentParser
from os import walk
from shutil import copyfileobj

def merge_files(input_name, output_name = None):
    '''
    Merge files in folder through byte reading.
    Allows UNIX wildcards as input name, being
    a . (dot) for merging files in the current
    path or an * (asterisk) for all subfolders.
    '''
    merge_subfolders = False

    if input_name == '*':
        merge_subfolders = True
        input_name = '.'

    if not output_name:
        output_name = input_name + '_MERGED'

    if not file_list:
        for path, folders, files in walk(input_name):
            if path == input_name or merge_subfolders:
                for f in files:
                    if not (f == output_name and path == input_name):
                        file_list.append(path + '/' + f)

    int_total = len(file_list)
    print('Merging %d files...' % int_total)

    if int_total > 0:
        with open(output_name, 'wb') as wfd:
            for f in file_list:
                print('%d/%d: %s...' % (str(file_list.index(f)+1), str(int_total), f))
                with open(f,'rb') as fd:
                    copyfileobj(fd, wfd)#, 1024*1024*10)

if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('input', action='store', help='input file name')
    parser.add_argument('-o', '--output', action='store', help='output file name')

    args = parser.parse_args()

    merge_files(args.input,
                args.output)