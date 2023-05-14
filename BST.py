
# * Part 1: Create a BSTNode class
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

# * Part 2: Create a BST class
class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []
    
  def __str__(self):
    # If the tree is empty, return a message indicating that
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
  
  def __repr__(self):
    # If the tree is empty, return a message indicating that
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output
    
  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)  # Recursively traverse the right subtree
      # Add the current node's data to the output with proper indentation
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)  # Recursively traverse the left subtree

#* Part 3: Add functionality to your BST class
  def add(self, node):
    # Check if the input node is of type int or BSTNode
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("Need int or BSTNode")

    # If the input node is of type int, convert it to a BSTNode
    if type(node) == int:
      node = BSTNode(node)

    # Check if the node's data already exists in the tree
    if node.data in self.contents:
      return

    # If the tree is empty, set the input node as the root and add its data to the contents list
    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return
    
    self.add_node(self.root, node)
 
  def add_node(self, c_node, n_node):
    # If the data of the new node is greater than the current node's data
    if n_node.data > c_node.data:
      # If there is no right child of the current node
      if c_node.right == None:
        # Set the new node as the right child of the current node
        c_node.right = n_node
        self.contents.append(n_node.data)  # Add the new node's data to the contents list
        return
      else:
        # Recursively call the add_node method with the current node's right child as the new current node
        self.add_node(c_node.right, n_node)
    else:
      # If the data of the new node is less than or equal to the current node's data
      # If there is no left child of the current node
      if c_node.left == None:
        # Set the new node as the left child of the current node
        c_node.left = n_node
        self.contents.append(n_node.data)  # Add the new node's data to the contents list
        return
      else:
        # Recursively call the add_node method with the current node's left child as the new current node
        self.add_node(c_node.left, n_node)



#* Testing code Part 1: Writing a BSTNode Class
node1 = BSTNode(3)
print(node1)  # 3

node2 = BSTNode(4, left=node1)
print(node2)  # 4

node3 = BSTNode()
print(node3)  # None
node3.data = 5
print(node3)  # 5



#* Testing code Part 2: Writing a BST Class
bst = BST()
print(bst)  # The tree is empty

bst.root = node2
print(bst)  # -> 4

node2.right = node3
print(bst)  #   -> 5
            # -> 4
            #    -> 3

# * Testing code Part 3: Add Functionality to the BST Class
#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)

print(bst)
