'''
Create program with staircase pattern
example :
input : 5
output : 
    #
   ##
  ###
 ####
#####
'''


# n for num of stairs or rows
def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)

n = int(input("Enter num of stairs : "))
staircase(n)
