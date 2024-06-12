a = input('Enter the value of A = ')
b = input('Enter the value of B = ')
x=input('Enter the operation = ')
sum = int(a)+int(b)
sub = int(a)-int(b)
mul = int(a)*int(b)
div = int(a)/int(b)
if x=='+':
    print(sum)
elif x=='-':
    print(sub)
elif x=='*':
    print(mul)
elif x=='/':
    print(div)