import importlib, traceback, sys, os
print('cwd', os.getcwd())
print('sys.path[0]', sys.path[0])
print('app folder exists', os.path.isdir(os.path.join(os.getcwd(), 'app')))
try:
    m = importlib.import_module('app')
    print('imported', m.__file__)
except Exception:
    traceback.print_exc()
