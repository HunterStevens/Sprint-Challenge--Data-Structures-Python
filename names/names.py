import time
class BSTNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value > self.value:
            if self.right:
                # print(f"self.right has value: {self.right}")
                self.right.insert(value)
            else:
                # print("self.right has no value")
                self.right = BSTNode(value)
        else:
            if self.left:
                # print(f"self.left has value: {self.left}")
                self.left.insert(value)
            else:
                # print("self.left has no value")
                self.left = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target, duplicates):
        if self.value in target:
            # print(f"self.value: {self.value} == target {target}")
            duplicates.append(self.value)        
            # print(f"self.value: {self.value} > target {target}")
        if self.right:
            self.right.contains(target, duplicates)
            # print(f"self.value: {self.value} < target {target}")
        if self.left:
            self.left.contains(target, duplicates)
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [] # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
names_bst = BSTNode(names_1[0])
for i in names_1:
    names_bst.insert(i)
names_bst.contains(names_2, duplicates)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''