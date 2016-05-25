# data-structures

## This project contains sample code for implementing the following structures:

### Hash Table

This data structure, a hash table, is used to implement an associative 
array, a structure that can map keys to values. A hash table uses a hash 
function to compute an index into an array of buckets or slots, from 
which the desired value can be found.

This implementation returns 'None' if you ask for a key that is not available.

This implementation uses the "Additive Hash," the simplest algorithm for hashing. 
It take a sequence of integral values (such as a string), it adds all of the characters 
ordinal values together and then uses remainder of division (%Modulo) to find a 
position in a fixed size data structure.

ht.get(key) - Returns the value stored with the given key
ht.set(key, val) - Stores the given val using the given key


### Binary Search Tree (BST)

This data structure, a binary tree, is a tree data structure in which each 
node has at most two children, which are referred to as the left child 
and the right child.

Supports:

bst.find_node(value) - Finds a node by value in a tree.
bst.delete(value) - Deletes a node by value in a tree.
bst.insert(value) - Will insert the value val into the BST. If val is 
already present, it will be ignored.
bst.contains(value) - Will return True if val is in the BST, False if not.
bst.size() - Will return the integer size of the BST (equal to the total 
number of values stored in the tree). It will return 0 if the tree is empty.
bst.depth() - Will return an integer representing the total number of 
levels in the tree. If there is one value, the depth should be 1, if two 
values it will be 2, if three values it may be 2 or three, depending, etc.
bst.balance() - Will return an integer, positive or negative that 
represents how well balanced the tree is. Trees which are higher on the 
_left than the _right should return a positive value, trees which are 
higher on the _right than the _left should return a negative value. An 
ideally-balanced tree should return 0.
bst.in_order() - Returns the data of all nodes in-order (all left, me, all right)
bst.pre_order() - Returns the data of all nodes in pre-order (me, all left, all right)
bst.post_order() - Returns the data of all nodes in post-order (all left, all right, me)
bst.breadth_order() - Returns the data of all nodes in breadth-order (height=0, 1, 2, ...)

### Graph

Graphs(g) are used to record relationships between things. Popular uses of 
graphs are mapping, social networks, chemical compounds and electrical 
circuits.

Supports:

g.depth_first_traversal(start): Perform a full depth-first traversal of 
the graph beginning at start. Return the full visited path when traversal 
is complete.

g.breadth_first_traversal(start): Perform a full breadth-first traversal 
of the graph, beginning at start. Return the full visited path when 
traversal is complete.

### WeightedGraph

A subclass of the above which can optionally store and provide weights for each
edge. This class also supports shortest-path traversals for graphs with and without
negative edge weights.

g.dijkstra_traversal(start, end): An algorithm for finding the shortest 
paths between nodes in a graph, which may represent, for example, road networks.

g.bellman_ford(node): An algorithm that computes shortest paths from a 
single source node to all of the other nodes in the graph. Slower than Dijkstra's 
algorithm for the same graph, but more versatile, as it is capable of handling graphs
in which some of the edge weights are negative numbers. 

This example walks a graph from a set vertex and sets each vertex
with a previous vertex and weight. It then returns a dictionary of all the 
vertices that you can then use to walk back to the provided vertex along the
smallest weighted path.

### Binary Heap

This data structure, Heap, is a specialized tree-based data structure that 
satisfies the heap property: If A is a parent node of B then the key of 
node A is ordered with respect to the key of node B with the same ordering 
applying across the heap. Fills from left to right. There are minHeap 
and maxHeap alternatives.

### Priority Queue

This data structure, a priority queue, is an abstract data type which is 
like a regular queue or stack data structure, but where additionally each 
element has a "priority" associated with it.

### Deque

This data structure, Deque (usually pronounced like "deck"), is an irregular acronym of double-ended 
queue. Double-ended queues are sequence containers with dynamic sizes that can be expanded or 
contracted on both ends (either its FRONT(head) or REAR(tail)).

### Queue

This data structure, a Queue, is an abstract data type or a linear data structure, in which the first element is 
inserted from one end called REAR(or tail), and the deletion of existing element takes place from the other end 
called as FRONT(or head).

### Doubly Linked List

This data structure is a linked data structure that consists of a set of sequentially linked records called nodes. Each 
node contains two fields, called _next and _prev, that are references to the previous(_prev) and to the next(_next) node 
in the sequence of nodes.

### Stack

This data structure that allows for a Last In First Out (LIFO) access to a collection of objects (nodes), each containing
a link to its successor and a piece of data. Access is given through the methods push(), adding an item to the stack,
or pop(), removing an item from the stack.


### Linked List

This data structure has an ordered set of data elements (nodes), each containing a link to its successor and a piece of data.

## *Interview Challenge: Proper Parenthetics*

Takes a unicode string proper_paren(text) as input and returns one of three possible values:

> Return 1 if the string is “open” (there are open parens that are not closed)
> Return 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
> Return -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)
