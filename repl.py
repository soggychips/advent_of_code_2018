import readline
import code
from helpers import *

vars = globals().copy()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()

