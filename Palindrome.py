'''
Python function named palindrome(s) that takes a single string parameter 
representing a word and that returns True if the letters within the word
read the same left to right as they do right to left and False otherwise.
This function checks palindrome regardless of cases of word
'''
def is_palindrome(s):
    uppercase_word = s.upper()
    lowercase_word = s.lower()
    s = lowercase_word
    s = uppercase_word
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
