x=5
foundRoot = 0
currenrate =  1
accuracy = 0.0005
while not (x - (foundRoot*foundRoot)) < accuracy:

    if foundRoot*foundRoot > x:
        currenrate=currenrate/2
        
    if foundRoot*foundRoot < x:
        print(currenrate)
        foundRoot+=currenrate
    print(foundRoot, foundRoot*foundRoot)

print(foundRoot)