#compute the area of a triangle given the
#length of its three sides 
#Pratik Prabhakar

side1 = int(input("Enter the first side of triangle: "))
side2 = int(input("Enter the second side of triangle: "))
side3 = int(input("Enter the third side of triangle: "))
totalsides = (side1+side2+side3)/2
area=totalsides*(totalsides-side1)*(totalsides-side2)*(totalsides-side3)
sqrtarea = area ** 0.5
print("The area of triangle with sides",side1, "m",side2, "m",side3,"m is: ", sqrtarea ,"sqmts")
