
''' 
Algorithm to print the least two common parent node between 2 nodes of a binary tree for given 2 key values which are present in binary tree.

Step1: A binary tree node,Constructor to create a new binary node.
Step2: Finds the path from root node to given root of the tree.
       Stores the path in a list path[], returns true if path exists otherwise false.
Step3: Store this node is path vector. The node will be 
       removed if not in path from root to k.
Step4: See if the k is same as root's key.
Step5: Check if k is found in left or right sub-tree.
       If not present in subtree rooted with root, remove 
       root from path and return False.
Step6: Returns LCA if node n1 , n2 are present in the given 
       binary tre otherwise return -1.
Step7: To store paths to n1 and n2 fromthe root.
Step8: Find paths from root to n1 and root to n2.
       If either n1 or n2 is not present , return -1.
Step9: Compare the paths to get the first different value.
Step10: Creation of binary tree as shown in the diagram.
        Get the output.
    '''

class Node:       
    
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None

def findLCA(root, n1, n2): 
      
     
    if root is None: 
        return None
     
    if root.key == n1 or root.key == n2: 
        return root  
    
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
    
    if left_lca and right_lca: 
        return root     
    return left_lca if left_lca is not None else right_lca 
  

root = Node(2) 
root.left = Node(1) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5) 
root.right.right.right = Node(6) 
print ("LCA(1,5) = ", findLCA(root, 1, 5).key) 
print ("LCA(3,6) = ", findLCA(root, 3, 6).key) 
print ("LCA(4,6) = ", findLCA(root, 4, 6).key) 
 