'''
A function named play_one() to simulate a single run through
the dice game involving a single cube.
'''
import random
def play_one():
    throw_six = 0
    result = 0
    while throw_six < 2:
        result = result + 1
        throw = random.randint(1, 6)
        print(throw,",", end="")
        if throw == 6:
            throw_six = throw_six + 1
        else:
            throw_six = 0
        if throw_six == 2:
           break
    print()
    return result

'''
A function play_many(n) that simulates n executions of the above and
that returns the minimum, maximum and average game length observed.
'''
def play_many(n):
    minimum = total = maximum = play_one()
    for i in range(2,n+1):
        result = play_one()
        total = total + result
        if result < minimum:
            minimum = result
        elif result > maximum:
            maximum = result
    average = total/n
    return("Min: ",str(minimum),"Max: ",str(maximum),"Average: ",str(average))
