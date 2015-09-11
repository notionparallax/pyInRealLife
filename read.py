import math
#open a file to read from it
someUsefulFile = open("myPoints.txt" , "rw") 
for shazza in someUsefulFile:
    x,y,name = shazza.split(",")
    distance = math.sqrt(pow(float(x),2)+pow(float(y),2))
    print "distance:", distance,name

someUsefulFile.close();
