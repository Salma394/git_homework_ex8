
# This is a python module
# lines one and two are just comments
import sys

# pythons user system module sys is a sytem
argument_count = len(sys.argv)
print(argument_count)

# argument count is a variable. It is essential that variable names are understandable.

# sys.argv - these count the number of arguments (items) passed to the command line
# len is a function which counts the number of items or characters inside the variable

if argument_count > 0:
    # a conditional
    print('Too many inputs')
    # if the variable has  a value greater than one (in this case the number of items)
else:
    where = 'World'  # create a variable where and assign the value 'World' to it
#     print("Hello", where) #takes multiple arguments / parameters/ inputs
#     print ('one', 'two', 'three')
# print ('Goodbye from ' + sys.argv[0])
# Square brackets are a list

platform = sys.platform

print(platform)
