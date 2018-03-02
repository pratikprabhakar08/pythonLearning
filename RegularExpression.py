#Pratik Prabhakar
#117220752

import re
'''
A function multivowel that takes a string as its argument and 
that returns a list of all words that contain two or more vowels
'''
def multivowel(string):
    vowels = "[aeiouAEIOU]"
    check = []
    result_words = []
    for word in string.split():
        check = re.findall(vowels, word)
        if len(check) >= 2:
            result_words.append(word)
    return " ".join(result_words)

'''
A function moolah that takes a string as its argument and 
that returns a list every Euro amount (as a string) 
that is mentioned in the text.
'''    
def moolah(string):
    regexp1 = re.compile(r"EUR(\d+(\.\d+)?)")
    regexp2 = re.compile(r"EUR (\d+(\.\d+)?)")
    match_word1 = regexp1.search(string)
    match_word2 = regexp2.search(string)
    if match_word1:
        num1 = match_word1.group()
        return num1
    elif match_word2:
        num2 = match_word2.group()
        return num2
    else:
        return "No amount found"

'''
A function bleep that takes a string as its argument and 
that returns a modi
fied copy of the text in which all 
four-letter words are replaced by ****.
'''    
def bleep(string):
    encrypt_word = re.sub(r'\b[\w]{4}\b', '****', string)
    return encrypt_word

'''
A function to_english that takes a string as its argument 
and that returns a modifi
ed copy of the text in which all 
numbers appearing in the original are spelled out in English.
'''
def to_english(string):
    word = []
    result = ""
    number_list=["zero","one","two","three","four","five","six","seven","eight","nine"]
    regexp = re.findall(r"\d+", string)        
    regexp = list(set(regexp))
    for number in regexp:
        for conversion in number:
            word.append(number_list[int(conversion)])
    result =  "("+" ".join(word)+")"
    for digit in regexp:
        string = re.sub(digit, digit + result , string)
    return string