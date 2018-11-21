import sys

args = {'command':sys.argv[1], 'args':dict([arg.split('=', maxsplit=1) for arg in sys.argv[2:]])}
print(args)