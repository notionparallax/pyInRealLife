import os
import random

someWords = ("Pineapple", "Pinnacle", "Pine nut", "Pumpkin", "Peanut",  "Pumpernickel")

#open a file to write to it
someUsefulFile = open("myPoints.txt" , "w") 
#list of access modes here: http://www.tutorialspoint.com/python/python_files_io.htm
for i in range(10):
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    name = random.choice(someWords)
    localPoint = {'x': x, 'y': y, 'name': name}
    someUsefulFile.write("point is at {x:.2f}, {y:.6f} and is called {name}\n".format(**localPoint))

someUsefulFile.close();

#open a file to read from it
someUsefulFile = open("myPoints.txt" , "r") 
for i in range(10):
    print someUsefulFile.read()

someUsefulFile.close();
