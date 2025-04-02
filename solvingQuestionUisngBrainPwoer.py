

a=[[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]

currentIndex = 0
points=0
while currentIndex < len(a):
    doingThis = 0
    skipingThis = 0 

    skipingThisIndex = 0
    
    skipingThisIndex = currentIndex+1
    doingThisIndex = currentIndex
    
    currentIndexForChecking = currentIndex

    skipWillCheckAt = skipingThisIndex
    doingWillCheckAt = doingThisIndex
    while currentIndexForChecking < len(a):
        if currentIndexForChecking == doingThisIndex:
            doingThis+=a[currentIndexForChecking][0]
            doingThisIndex += a[currentIndexForChecking][1]+1
            print("doing  poits: ",doingThis,"next doing this ",doingThisIndex)
        elif skipingThisIndex == currentIndexForChecking:
            skipingThis+= a[currentIndexForChecking][0]
            skipingThisIndex+=a[currentIndexForChecking][1]+1
            print("skiping  poits: ",skipingThis,"next skipng this ",skipingThisIndex)
        currentIndexForChecking+=1
    
    if doingThis >= skipingThis:
        print("doing win at ",currentIndex)
        points+=a[currentIndex][0]
        currentIndex += a[currentIndex][1] + 1
        
    elif doingThis < skipingThis:
        print("skiping win at",currentIndex)
        points+= a[currentIndex+1][0]
        currentIndex += a[currentIndex+1][1] +1
        


# FUCKED