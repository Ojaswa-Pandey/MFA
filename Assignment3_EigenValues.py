import math
x=[[9.066964285714283, -10.076785714285714, -0.726785714285712],
[-10.076785714285714, 159.125, 123.05357142857143],
[-0.726785714285712, 123.05357142857143, 684.6964285714286]]

#sumOfDiagonal
a=x[0][0]+x[1][1]+x[2][2]

#sumOfDiagonalMinors
b=((x[1][1]*x[2][2])-(x[1][2]*x[2][1])) + ((x[0][0]*x[2][2])-(x[0][2]*x[2][0])) + ((x[0][0]*x[1][1])-(x[0][1]*x[1][0]))

#determinant
c= x[0][0]*((x[1][1]*x[2][2])-(x[1][2]*x[2][1])) - x[0][1]*((x[1][0]*x[2][2])-(x[1][2]*x[2][0])) + x[0][2]*((x[1][0]*x[2][1])-(x[1][1]*x[2][0]))
#print(f"λ^3 - {a}λ^2 + {b}λ - {c} = 0")

def f(value):
    return value**3 - a*value**2 + b*value - c
def derivative(value):
    return 3*value**2 - 2*a*value + b

root=0
for i in range(100):
    new_root= root - f(root)/derivative(root)
    if abs(new_root - root)<0.000001:
        break #new_root is the first root
    root=new_root
root1= new_root    

#Divide by (λ - root1)
b1 = -a + root1
b2 = b + root1 * b1
#print(f"λ^2 + ({b1})λ + ({b2}) = 0")

D = b1**2 - 4*b2
root2 = (-b1 + math.sqrt(D)) / 2
root3 = (-b1 - math.sqrt(D)) / 2

print("\nEigenValues :")
print("λ1 =", root1)
print("λ2 =", root2)
print("λ3 =", root3)


'''OUTPUT is:
EigenValues :
λ1 = 8.296231759185172
λ2 = 712.0924664370984
λ3 = 132.4996946608593'''
