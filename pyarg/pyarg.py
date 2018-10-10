"""
pyarg
~~~~~~~~~~~~~~~~~~

argument management
"""

"""

Import extern module

"""
import sys
import os

"""

Import intern module

"""

"""

Internal Constant, Class, Function

"""

__CHAR_OPTION = '-'

__options = {}
__arguments = {}
__argumentsName = []


"""

Exported Constant, Class, Function

"""
name = os.path.basename(sys.argv[0])
argv = sys.argv[1:]
argc = len(argv)

def parse():
  """
  Parse the argument in argv
  """
  global __options
  global __arguments

  useNext = True
  otherArg = 0;
  nextArg = 1
  for arg in argv:
    if useNext == True:
      if arg[0] == __CHAR_OPTION:
        if not arg in __options:
          print(name + ": option '" + arg + "' not recognized")
        else:
          if nextArg < argc and argv[nextArg][0] != __CHAR_OPTION:
            __options[arg] = argv[nextArg]
            useNext = False
          elif __options[arg] == True:
            __options[arg] = None
          # end if
        # end if
      else:
        if len(__argumentsName) != 0:
          __arguments[__argumentsName.pop()] = arg
        else:
          __arguments[otherArg] = arg
          otherArg += 1
        # end if
      # end if
    else:
      useNext = True
    # end if
    nextArg += 1
  # end for
  for opt, arg in __options.items():
    if arg == None:
      print(name + ": error: missing require argument option: " + opt)
    # end if
  # end for
  for argName in __argumentsName:
    if not argName in __arguments:
      print(name + ": error: missing require argument: " + argName)
    # end if
  # end for

def get_args():
  """
  Get the arguments
  """
  args = (__arguments, __options)
  return args

def set_option(
    option,
    argument=False
    ):
  """
  Set a new option

  :param: option: option identifier
  :param: argument: (optional) if True, the option take one argument
  """
  global __options

  __options[option] = argument

def set_argument(
    argName
    ):
  """
  Set the argument expected

  :param: argName: the name use to identify the parameter expected
  """
  global __argumentsName

  __argumentsName.append(argName)

