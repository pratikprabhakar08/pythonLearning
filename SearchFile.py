#Author 
#Pratik Prabhakar

'''
A python function named search_file(filename, target) which
outputs each line in file containing string target,
preceded by its line number.
'''
def search_file(filename, target):
    with open(filename,"r") as myFile:
        for num, line in enumerate(myFile, 1):
            if target in line:
                print("", num,"-", line)


