"""
@author: Pratik Prabhakar
Greatest common divisor of two numbers
"""

def gcd(a,b):
	if b == 0:
		return a
	else:
		c = a%b
		return gcd(b,c)