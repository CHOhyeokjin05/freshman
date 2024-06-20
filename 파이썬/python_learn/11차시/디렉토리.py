import os
files = os.getcwd()
print(dir)
for name in files : 
    if os.path.isfile(name):
        if name.endswith('.py'):
            print(name)