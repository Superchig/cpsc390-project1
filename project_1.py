# Can use deque for queue

# Using https://www.geeksforgeeks.org/deque-in-python/

from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.successors = {}

    # Using https://www.educative.io/edpresso/what-is-the-str-method-in-python
    def __str__(self):
        return self.name

    # https://www.pythoncontent.com/understanding-__repr__-in-python/
    def __repr__(self):
        return self.__str__()

s = Node('S')
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
g = Node('G')

s.successors[a] = 3
s.successors[b] = 1
s.successors[c] = 8

a.successors[d] = 3
a.successors[e] = 7
a.successors[g] = 15

b.successors[g] = 20

c.successors[g] = 5

# Returns the path from initial_node to target_node, including both nodes.
def depth_first_search(initial_node, target_node):
    frontier = [initial_node]
    path = []
    expanded_nodes = []

    while len(frontier) > 0:
        node = frontier.pop()
        path.append(node)
        expanded_nodes.append(node)

        if node is target_node:
            return (path, expanded_nodes)

        # Using https://linuxize.com/post/python-list-reverse/
        # Push the "right-most" successor onto the frontier stack first, so that
        # the "left-most" successor will be the next node
        for child in reversed(node.successors):
            frontier.append(child)

        if len(node.successors) <= 0:
            path.pop()

    return None

# Simple test cases
assert depth_first_search(s, s) == ([s], [s])
assert depth_first_search(s, g) == ([s, a, g], [s, a, d, e, g])
assert depth_first_search(s, Node('Z')) == None

(solution_path, expanded_nodes) = depth_first_search(s, g)

print('Solution path:')
for node in solution_path:
    print(node)

print()

print('Expanded nodes:')
for node in expanded_nodes:
    print(node)
