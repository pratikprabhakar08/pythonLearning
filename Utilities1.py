def average_word(filename):
    count_char = 0
    with open(filename,"r") as fileOpen:
        for fileContent in fileOpen:
            wordSplit = fileContent.split()
            print(wordSplit)
            count_char = count_char + len(wordSplit)
        return len(fileContent)/count_char

#To reverse each word of a string 
def reverse(s):
    return ' '.join([word[::-1] for word in s.split()])
    #for i in s:
     #   list_s = s[::-1]

#To reverse the string backwards
def reverseback(s):
    list_s = s.split()
    list_s.reverse()
    reverse_string = " ".join(list_s)
    return reverse_string

#print(reverse("The quick brown fox jumped over the lazy dog"))
#print(reverseback("The quick brown fox jumped over the lazy dog"))

def is_palindrome(s):
    s = s.replace(" ","")
    s_lower = s.lower()
    s_reverse = s[::-1]
    if s_lower == s_reverse:
        return True
    else:
        return False
    
#print(is_palindrome("some men interpret nine memos"))

def fib(n):
    a,b = 1,1
    for i in range(0,n-1):
        a,b=b, a+b
    return a

#for i in range(1,10):
 #   print(fib(i))


num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


def IsStairs(s):
    #list_split = s.split()
    length = len(s)
    for i in range(0,length-1):
        if s[i] < s[i+1] or s[i+1] > s[i]:
            return True
        else:
            return False

print(IsStairs([2,4,4,6]))
