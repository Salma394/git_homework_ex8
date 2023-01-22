# This is a python module
import sys

# argc is a variable and the len (built in function that checks the length)
# import sys is a module that can show file path
argument_count = len(sys.argv)
if argument_count > 1:
    print('Too many args')

else:
    where = 'World'
    print("Hello", where)

print('Goodbye from' + sys.argv[0])

