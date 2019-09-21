import random
                
aList = []

def setup():
    #create window size
    size(800, 500)
    
    #setting up list with random integer
    for a in range(width):
        aList.insert(a, random.randint(1, height))
    
    
    
def draw():
    #background color
    background(255)
    
    #bubble sort
    passnum = 0
    if passnum < len(aList):
        passnum += 1
        for i in range(len(aList) - passnum - 1):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
                
    else:
        print("finish")
        noLoop();
    
    #draw line according to list element
    for b in range(len(aList)):
        stroke(0);
        line(b, height, b, height - aList[b]);
        
    
    
