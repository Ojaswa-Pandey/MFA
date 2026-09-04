import math

def eigenValues(x):
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

    return [root1, root2, root3]



A=[[9.066964285714283, -10.076785714285714, -0.726785714285712],
[-10.076785714285714, 159.125, 123.05357142857143],
[-0.726785714285712, 123.05357142857143, 684.6964285714286]]

eigenvalues= eigenValues(A)
for x in eigenvalues:
    print("\nEigenvalue:", x)

    M = [
        [A[0][0]-x,      A[0][1],        A[0][2]],
        [A[1][0],        A[1][1]-x,      A[1][2]],
        [A[2][0],        A[2][1],        A[2][2]-x]
    ]

    v1 = M[0][1] * M[1][2] - M[0][2] * M[1][1]
    v2 = M[0][2] * M[1][0] - M[0][0] * M[1][2]
    v3 = M[0][0] * M[1][1] - M[0][1] * M[1][0]

    length = math.sqrt(v1**2 + v2**2 + v3**2)
    v1 = v1 / length
    v2 = v2 / length
    v3 = v3 / length

    print("Eigenvector:", [v1, v2, v3])


'''OUTPUT is:
Eigenvalue: 8.296231759185172
Eigenvector: [-0.9969322675670309, -0.07718683874009853, 0.012970960217664607]

Eigenvalue: 712.0924664370984
Eigenvector: [-0.004123595849336822, 0.2172893862655685, 0.976098518887107]

Eigenvalue: 132.4996946608593
Eigenvector: [-0.07816041095675967, 0.9730506228052282, -0.21694108789583408]'''
