import sys 


def parseFile():
    tree = {}
    file = open('merkle.tree', 'r')
    for line in file: 
        lineArray = line.split(' ')
        tree[lineArray[3]] = lineArray[8]
    return tree

def checkInclusion(inputString, tree):
    op = []
    for key, value in tree.items():
        if inputString == key: 
            op.append(value)
            inputString = value
    return op


inputString = sys.argv[1]

tree = parseFile()

op = checkInclusion(inputString,tree)
if(len(op)> 0):
    print("yes",op)
else:
    print("no")
        
