"""
@author: Pratik Prabhakar
Mode using dictionary from list of values
"""

def mode(lst):
    modeDict = {}
    for i in lst:
        if i not in modeDict:
            modeDict[i] = 1
        else:
            modeDict[i] = modeDict[i]+1
    print(max(modeDict,key=modeDict.get))
        