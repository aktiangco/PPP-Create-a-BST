

#Part 1: Create a BSTNode class
class BSTNode:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
    # To allow the nodes to be printed
  def __str__(self):
    return str(self.data)
  def __repr__(self):
    return str(self.data)

# TODO Part 2: Create a BST class



# TODO Part 3: Add functionality to your BST class



#* test code
node1 = BSTNode(3)
print(node1) #3

node2 = BSTNode(4, left=node1)
print(node2) #4

node3 = BSTNode()
print(node3) #None
node3.data = 5
print(node3) #5