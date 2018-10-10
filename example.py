#!/usr/bin/python3

import pyarg

pyarg.set_argument('path')
pyarg.set_option('-v')
pyarg.set_option('-d', True)

pyarg.parse()

args, option = pyarg.get_args()

print(args)
print(option)

