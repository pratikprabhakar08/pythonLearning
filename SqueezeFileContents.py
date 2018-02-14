#Author 
#Pratik Prabhakar

'''
A python function named squeeze(filename) which
input the file filename and output each line of this file which differs from the previous
line (its first line is always written); each output line should be prefixed with its line
number in the input file.
'''
def squeeze(filename):
    repeatLine = ""
    count = 1
    with open(filename, "r") as fileOpen:
        for line in fileOpen:
            if repeatLine != line:
                count = count+1
                print("", count, "-", line)
            repeatLine = line


