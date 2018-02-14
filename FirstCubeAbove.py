'''
Function named first_cube_above(n) which return the smallest
cube which exceeds the non-negative integer n.
'''
import math
def first_cube_above(n):
    cube_above = 0
    cuberoot = math.ceil(n**(1/3))
    if is_cube(n):
        cube_above = (cuberoot+1)**3
    else:
        cube_above = cuberoot**3
    return cube_above
