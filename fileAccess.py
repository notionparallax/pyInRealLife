import os

print os.getcwd()

#open a file to write to it
someUsefulFile = open("theFileIWantToWriteTo.txt" , "w") 
#list of access modes here: http://www.tutorialspoint.com/python/python_files_io.htm
for i in range(10):
    someUsefulFile.write(str(i)+"\n")

someUsefulFile.close();

#open a file to read from it
someUsefulFile = open("theFileIWantToWriteTo.txt" , "r") 
for i in range(10):
    print someUsefulFile.read()

someUsefulFile.close();
