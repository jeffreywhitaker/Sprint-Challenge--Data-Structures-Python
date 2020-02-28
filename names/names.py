import time

# add binary search tree


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, passed_in_value):
        # if the passed in value is less than the node
        if passed_in_value < self.value:
            # if there is no less than node
            if self.left == None:
                # make a node
                self.left = BinarySearchTree(passed_in_value)
            # if there is a node there
            else:
                # be recursive
                self.left.insert(passed_in_value)
        # if the passed in value is greater than the node
        else:
            # if there is no greater than node
            if self.right == None:
                # make a node
                self.right = BinarySearchTree(passed_in_value)
            # if a node already exists
            else:
                # be recursive
                self.right.insert(passed_in_value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if current value is right, return true
        if target == self.value:
            return target
        # if target is less than current value
        elif target < self.value:
            # if there is no left node, return false
            if self.left == None:
                return None
            # if there is a left node
            else:
                return self.left.contains(target)

        # if target is greater than current value
        else:
            # if there is no right node, return false
            if self.right == None:
                return None
            # if there is a right node
            else:
                return self.right.contains(target)

###


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# the below starter code has time complexity of O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# begin my code here

my_bst = BinarySearchTree('Generic String')

for name in names_1:
    my_bst.insert(name)

for name in names_2:
    match = my_bst.contains(name)
    if (match is not None):
        duplicates.append(match)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# trying with binary search tree
# seems a bit faster


def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

names_1.sort()

for name in names_2:
    match = binarySearch(names_1, 0, 9999, name)
    if match != -1:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# trying with set and intersection function
# seems to be the fastest version

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

s1 = set(names_1)
s2 = set(names_2)

duplicates = s1.intersection(s2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
