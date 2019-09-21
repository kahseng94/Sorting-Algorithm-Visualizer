import random

aList = []
passnum = 0
def setup():
    #create window size
    size(800, 500)
    
    #setting up list with random integer
    for a in range(width):
        aList.insert(a, random.randint(1, height))
        
passnum = 1    
def draw():
    #background color
    background(255)
    
    #insertion sort 
    global passnum
    if passnum < len(aList):
        curr = aList[passnum]
        pos = passnum
        while pos > 0 and aList[pos - 1] > curr:
            aList[pos] = aList[pos - 1]
            pos-=1
        aList[pos] = curr
    else:
        print("finish")
        noLoop();
    passnum += 1
    
    #draw line according to list element
    for b in range(len(aList)):
        stroke(0);
        line(b, height, b, height - aList[b]);
