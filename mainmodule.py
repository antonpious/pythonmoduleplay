from dotenv import load_dotenv
# loading variables from .env file
load_dotenv() 

from pythonmoduleplay.submodule1 import submodule11 


from pythonmoduleplay.submodule1.submodule11 import _funcsubmodule12


from pythonmoduleplay import submodule1



print("This is the main module")

print("Calling Sub Module 11")
submodule11.funcsubmodule11()

print("Calling Sub Module 12")
submodule11._funcsubmodule12()

print("Directly calling Submodule 12")
_funcsubmodule12()

print("From Init File. The Submodule 11 is removed and can be directly accessed")
submodule1.funcsubmodule11()

print("This would throw error")
submodule1.funcsubmodule12()