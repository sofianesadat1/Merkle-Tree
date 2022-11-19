import hashlib, sys 

class MerkleTreeNode:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.value = value 
        self.hashValue = hashlib.sha256(self.value.encode('utf-8')).hexdigest() 

def buildTree(leaves, f): 
    nodes = []

    for i in leaves: 
        nodes.append(MerkleTreeNode(i))

    while len(nodes) != 1:
        temp = []
        for i in range(0, len(nodes), 2):
            node1 = nodes[i]
            if i + 1 < len(nodes):
                node2 = nodes[i+1]
            else : 
                temp.append(nodes[i])
                break
            concat = node1.hashValue + node2.hashValue
            parent = MerkleTreeNode(concat)
            parent.left = node1
            parent.right = node2 
            f.write('left value : ' + node1.value + ' | left hashValue : ' + node1.hashValue + ' \n')            
            f.write('right value : ' + node2.value + ' | right hashValue : ' + node2.hashValue + ' \n')
            f.write('parent value : ' + parent.value + ' | parent hashValue : ' + parent.hashValue + ' \n')
            temp.append(parent)
        nodes = temp
    return nodes[0]

leaves = sys.argv[1:]
f = open("merkle.tree", "w")
root = buildTree(leaves,f)
f.close()
