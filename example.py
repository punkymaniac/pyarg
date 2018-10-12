#!/usr/bin/python3

import pyarg

pyarg.set_argument('path')
pyarg.set_option('-v', alone=True)
pyarg.set_option('-i')
pyarg.set_option('-d', True)

try:
  pyarg.parse()
except pyarg.ArgError as err:
  print(pyarg.name + ": error: " + err.message)
else:
  args, option = pyarg.get_args()
  if '-v' in option:
    print("version: 0.0.1")
  if args:
    path = args['path']
    if '-i' in option:
      print("My path: " + path)
    else:
      print(path)

