#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
from examples import *

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
cpu = CPU()
cpu.load(sys.argv[1])
cpu.run()
# main('examples/print8.ls8')