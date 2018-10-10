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
__set_options = {}
__arguments = {}
__set_arguments = []


"""

Exported Constant, Class, Function

"""
name = os.path.basename(sys.argv[0])
argv = sys.argv[1:]
argc = len(argv)

class ArgError(Exception):

  message = ''

  def __init__(self, msg):

    super(ArgError, self).__init__(msg)

    self.message = msg


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
        if not arg in __set_options:
          raise ArgError("option '" + arg + "' not reconized")
        else:
          if __set_options[arg] == True:
            if nextArg < argc and argv[nextArg][0] != __CHAR_OPTION:
              __options[arg] = argv[nextArg]
              useNext = False
            else:
              __options[arg] = None
            # end if
          else:
            __options[arg] = False
          # end if
        # end if
      else:
        if len(__set_arguments) != 0:
          __arguments[__set_arguments.pop()] = arg
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
      raise ArgError("missing require argument option: " + opt)
    # end if
  # end for
  for argName in __set_arguments:
    if not argName in __arguments:
      raise ArgError("missing require argument: " + argName)
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
  global __set_options

  __set_options[option] = argument

def set_argument(
    argName
    ):
  """
  Set the argument expected

  :param: argName: the name use to identify the parameter expected
  """
  global __set_arguments

  __set_arguments.append(argName)

