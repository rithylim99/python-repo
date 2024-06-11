import sys #to use check the size of the variable
a = 3.0
message = "welcome"
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
s = sys.getsizeof(message)
# to check the data type of the variable, we can use the cammand (type)
print(message)
print(type(message))
print(s, "byte")