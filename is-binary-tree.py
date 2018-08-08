# Given a subset of node relationships in a graph, 
# determine if the relationships can be represented as a binary tree.


# Relationships will be represented as a list of tuple pairs where the
# parent is the first element and the child is the second.

# eg. [(parent_1, child_1), (parent_2, child_2), ... (parent_n, child_n)]


def is_binary(node_pairs):




"""
Given a list of tuples indicating node connections, determine if the
tuples can be represented as a linked list.

eg. [(1,2), (2,3)] >>> True
explanation: 1 -> 2 -> 3

eg. [(1,2), (3, 4)] >>> False
explanation: 1 -> 2  3 -> 4

"""