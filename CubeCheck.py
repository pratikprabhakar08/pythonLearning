#Author 
#Pratik Prabhakar

'''
Function named is_cube(n) which return True if the
integer is a perfect cube and False otherwise
'''
def is_cube(n):
    cuberoot = abs(n**(1/3))
    round_cuberoot = int(abs(n)**(1/3))
    if cuberoot == round_cuberoot:
        return True
    else:
        return False

