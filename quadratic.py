import cmath 
print("QUADRATIC EQUATION - ax^2 + bx + c")
a = float(input("Enter the value of 'a' : "))
b = float(input("Enter the value of 'b' : "))
c = float(input("Enter the value of 'c' : "))
x1 = (((-b) + cmath.sqrt((b*b)-(4*a*c)))/2*a)
x2 = (((-b) - cmath.sqrt((b*b)-(4*a*c)))/2*a)
print("Solution is : ", x1, " and ", x2)
