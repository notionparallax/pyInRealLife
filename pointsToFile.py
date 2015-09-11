import os
import random

someWords = ("Pineapple", "Pinnacle", "Pine nut", 
	         "Pumpkin", "Peanut",  "Pumpernickel")

#open a file to write to it
someUsefulFile = open("myPoints.txt", "w") 
#list of access modes here: http://www.tutorialspoint.com/python/python_files_io.htm
for i in range(10):
    x = random.randint(1,1000) #I think this is the same: random.choice(range(1001))
    y = random.randint(1,1000)
    name = random.choice(someWords) #nicer than name = someWords[random.randint(0,5)]
    localPoint = {'x': x, 'y': y, 'name': name}
    # template = "point is at {x:.4f}, {y:.4f} and is called {name}\n"
    template = "{x:.4f}, {y:.4f}, {name}\n"
    someUsefulFile.write(template.format(**localPoint))

someUsefulFile.close();