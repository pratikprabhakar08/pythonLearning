'''
A python function named join_files(inputfilenames, outputfilename) which
Copy all files in the list inputfilenames to the file outputfilename.
'''
def join_files(inputfilenames, outputfilename):
    with open(outputfilename,"w") as outputfile
    for files in range(len(inputfilenames)):
        listfiles = open(inputfilenames[files],"r")
        listfiles.seek(0)
        fileContent = listfiles.read()
        outputfile.write(fileContent+"\n")

