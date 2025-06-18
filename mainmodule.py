from pythonmoduleplay.submodule1 import submodule11 


from pythonmoduleplay.submodule1.submodule11 import _funcsubmodule112


from pythonmoduleplay import submodule1



print("This is the main module")

print("Calling Sub Module 1-1-1")
submodule11.funcsubmodule111()

print("Calling Sub Module 1-1-2")
submodule11._funcsubmodule112()

print("Directly calling Submodule 1-1-2")
_funcsubmodule112()

print("From Init File. The Submodule 11 is removed and can be directly accessed")
submodule1.funcsubmodule111()

print("From Init File. The Submodule 12 is removed and can be directly accessed")
submodule1.funcsubmodule121()

print("This would throw error as the method is not exposed")

try:
    submodule1.funcsubmodule112()
except Exception as ex:
    print(ex)
 