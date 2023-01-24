# This is a python module
import sys

# argc is a variable and the len (built in function that checks the length)
# import sys is a module
argument_count = len(sys.argv)
# conditional statement. If first condition is not satisfied it will go to the next condition.
if argument_count > 1:
    print('Too many args')

else:
    where = 'World'
    print("Hello", where)

# This output will be printed regardless of the conditional statements as it is outside the block
print('Goodbye from' + sys.argv[0])

