Without setting up the path you would get the following error

`
Traceback (most recent call last):
  File "/Users/anton/Documents/projects/pythonprojects/pythonmoduleplay/mainmodule.py", line 1, in <module>
    from pythonmoduleplay.submodule1 import funcsubmodule11
ModuleNotFoundError: No module named 'pythonmoduleplay'

export PYTHONPATH=/Users/anton/Documents/projects/pythonprojects/



Only if you do this it won't import methods with _ else it would import

from pythonmoduleplay.submodule1.submodule11 import *

Traceback (most recent call last):
  File "/Users/anton/Documents/projects/pythonprojects/pythonmoduleplay/mainmodule.py", line 22, in <module>
    _funcsubmodule12()
    ^^^^^^^^^^^^^^^^
NameError: name '_funcsubmodule12' is not defined. Did you mean: 'funcsubmodule11'?