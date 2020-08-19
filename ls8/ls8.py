#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# def main(argv):
#     print('ARGV', argv)
#     if len(argv) == 0:
#         return 0
#     if len(argv) >= 1:
#         cpu = CPU()
#         # print(sys.argv[0], 'PRINT STATEMENT')
#         cpu.load()
#         # breakpoint
#         cpu.run()
if len(sys.argv) <= 1:
    print(' please provide program file')
elif len(sys.argv) > 1:
    file_name = sys.argv[1]
    print('File name in ls8.py', file_name)
    cpu = CPU()
    cpu.load(file_name)
    cpu.run()
# main()