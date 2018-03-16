#Pratik Prabhakar

'''
A function identifiers(pyprog) that takes in a string representing the code of a
Python function and returns a list of all the identifi
ers mentioned in the code. 
The value returned should be a list of strings in alphabetical order. 
Each identi
er should appear exactly once however many times it features in the code.
'''
import keyword
import re

def identifiers(pyprog):
    identifiers = []
    keyword_list  = keyword.kwlist
    pyprog = re.sub(re.compile("#.*?\n"), "", pyprog)
    ident = re.compile(r'[^\d\W]\w*', re.UNICODE)
    for klist in pyprog.split():
        ident1 = re.match(ident, klist)
        if ident1 != None:
            if klist not in keyword_list:
                identifiers.append(ident1.group())
    return sorted(list(set(identifiers)))