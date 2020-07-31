from collections import deque



"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""



class BSTNode:
    def __init__(self, value):
        # current node's value
        self.value = value

        self.left = None
        self.right = None

        # Insert the given value into the tree
    def insert(self, value):
        # check whether new node's value is less than current node's value
        if value < self.value:
            if not self.left: # if there is no node on the left the n create a new node
                self.left = BSTNode(value)
            else: # if there is a node on the left start the function over 
                self.left.insert(value)
        # check whether new node's value is greater than or equal to curr node's val
        elif value >= self.value:
            if not self.right: # if there is no node on the right the n create a new node
                self.right = BSTNode(value)
            else: # if there is a node on the right start the function over
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check whether curr node matches target
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:  #if there is no node left 
                return False
            else:   # if there node on the left then repeat the function
                return self.left.contains(target)
        else:
            if not self.right: #if there is no node on the right
                return False
            else: # if there node on the right then repeat the function
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        # self.left.value will always be smaller than the root
        # so we have to check only the self.right path
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function
        fn(self.value)
        print(self.value)
        # go to the left node if any
        if self.left:
            print('left')
            self.left.for_each(fn)
        # go to the right node if any
        if self.right:
            print('right')
            self.right.for_each(fn)

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return 

        # left -> root -> right
        if self.left:
            self.left.in_order_print()
        
        print(self.value)

        if self.right:
            self.right.in_order_print()

        

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #1. define deque
        # 2. add self todeque
        # 3. iterate : while there are items in the deque
        # 4. deque/pop from deque,point to result and print
        # 5.add left and right  children deque

        qq = deque()
        qq.append(self)

        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = []
        s.append(self)

        while len(s) > 0:
            current = s.pop()
            print(current.value)

            if current.left:
                s.append(current.left)

        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # check self
        # 1. print self
        # root-->left--->right
        # 2. recurse to the left
        # 3. recurse to the right
        pass
    # Print Post-order recursive DFT
    def post_order_dft(self):
         # check self
        # left--->right--->root
        # 2. recurse to the left
        # 3. recurse to the right
        # print self
        pass
"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
