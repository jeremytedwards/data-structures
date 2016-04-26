

# data-structures

## This project contains sample code for implementing the following structures:

### Trie
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=trie)](https://travis-ci.org/jeremytedwards/data-structures)

A Trie, also called digital tree and sometimes radix tree or prefix tree (as they can 
be searched by prefixes), is an ordered tree data structure that is used to store a 
dynamic set or associative array where the keys are usually strings. Unlike a 
binary search tree, no node in the tree stores the key associated with that node; 
instead, its position in the tree defines the key with which it is associated. 
All the descendants of a node have a common prefix of the string associated with 
that node, and the root is associated with the empty string. Values are not necessarily 
associated with every node. Rather, values tend only to be associated with leaves, 
and with some inner nodes that correspond to keys of interest. 


### Radix Sort: Testing
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=sort-radix)](https://travis-ci.org/jeremytedwards/data-structures)

Radix sort is a non-comparative integer sorting algorithm that sorts data with integer 
keys by grouping keys by the individual digits which share the same significant 
position and value. A positional notation is required, but because integers can 
represent strings of characters (e.g., names or dates) and specially formatted 
floating point numbers, radix sort is not limited to integers. 

Radix sort dates back as far as 1887 to the work of Herman Hollerith on tabulating machines.

By running the following code in your console you'll see some TimeIt results
for running an Radix Sort on a random, ordered, and reversed list of
integers from 1 to 10,000.

```$ python sort_radix.py```


### Quick Sort: Testing
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=sort-quick)](https://travis-ci.org/jeremytedwards/data-structures)

Quicksort is a divide and conquer algorithm. Quicksort first divides a large array 
into two smaller sub-arrays: the low elements and the high elements. Quicksort can 
then recursively sort the sub-arrays.

The steps are:

1) Pick an element, called a pivot, from the array.

2) Partitioning: reorder the array so that all elements with values less than 
the pivot come before the pivot, while all elements with values greater than 
the pivot come after it (equal values can go either way). 

After this partitioning, the pivot is in its final position. This is called 
the partition operation.

3) Recursively apply the above steps to the sub-array of elements with smaller 
values and separately to the sub-array of elements with greater values.

The base case of the recursion is arrays of size zero or one, which never need to be sorted.

The pivot selection and partitioning steps can be done in several different ways; the choice of specific implementation schemes greatly affects the algorithm's performance.

By running the following code in your console you'll see some TimeIt results
for running an Quick Sort on a random, ordered, and reversed list of
integers from 1 to 1,000. 

(Beware for larger sets the recursion can exceed memory)


```$ python sort_quick.py```


### Merge Sort: Testing
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=sort-merge)](https://travis-ci.org/jeremytedwards/data-structures)

Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. 
Most implementations produce a stable sort, which means that the implementation 
preserves the input order of equal elements in the sorted output. Merge sort 
is a divide and conquer algorithm that was invented by John von Neumann in 1945.

By running the following code in your console you'll see some TimeIt results
for running an Merge Sort on a random, ordered, and reversed list of
integers from 1 to 10,000.


```$ python sort_merge.py```


### Insertion Sort: Testing
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=sort-insertion)](https://travis-ci.org/jeremytedwards/data-structures)

Insertion sort iterates, consuming one input element each repetition, and 
growing a sorted output list. Each iteration, insertion sort removes one 
element from the input data, finds the location it belongs within the sorted 
list, and inserts it there. It repeats until no input elements remain.

Sorting is typically done in-place, by iterating up the array, growing the sorted list behind it. At each array-position, it checks the value there against the largest value in the sorted list (which happens to be next to it, in the previous array-position checked). If larger, it leaves the element in place and moves to the next. If smaller, it finds the correct position within the sorted list, shifts all the larger values up to make a space, and inserts into that correct position.

By running the following code in your console you'll see some TimeIt results
for running an Insertion Sort on a random, ordered, and reversed list of
integers from 1 to 10,000.


```$ python sort_insertion.py```


### Hash Table
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=hash-table)](https://travis-ci.org/jeremytedwards/data-structures)

This data structure, a hash table, is used to implement an associative 
array, a structure that can map keys to values. A hash table uses a hash 
function to compute an index into an array of buckets or slots, from 
which the desired value can be found.

ht.get(key) - Returns the value stored with the given key
ht.set(key, val) - Stores the given val using the given key


### Binary Search Tree (BST)
[![Build Status](https://travis-ci.org/jeremytedwards/data-structures.svg?branch=bst)](https://travis-ci.org/jeremytedwards/data-structures)

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
