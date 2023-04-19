## What is a Graph?

A graph is a non-linear data structure composed of **vertices** and **edges**.

### Vertices

**Vertices** or **nodes** are the fundamental units of the graph. Every node/vertex can be labeled or unlabelled.

### Edges

**Edges** or **arcs** are drawn or used to connect two nodes of the graph. It can be an ordered pair of nodes in a directed graph. 
Edges can connect any two nodes in any possible way. They can also be labelled or unlabelled.

## Tree vs Graph
Trees are restricted types of graphs, just with some more rules. Every tree will always be a graph but not all graphs will be trees. 
**Linked lists**, **trees**, and **heaps** all are special cases of graphs.

## Representation of Graphs
There are two ways to store a graph:
* adjacency matrix
* adjacency list

### Adjacency matrix
In this method, the graph is stored in the form of the 2D matrix where rows and columns denote vertices.
Each entry in the matrix represents the weight of the edge between those vertices.

### Adjacency list

This graph is represented as a collection of linked lists.
There is an array of pointer which points to the edges connected to that vertex.

### Basic Operations on Graphs
Below are the basic operations on the graph:

* insertion of nodes/edges in the graph
* deletion of nodes/edges in the graph
* searching on graphs – search an entity in the graph
* traversal of graphs – traversing all the nodes in the graph

### Usage of graphs
Maps can be represented using graphs and then can be used by computers to provide various services like _the shortest path between two cities_.

When various tasks depend on each other, this situation can be represented using a **directed acyclic graph** 
and we can find the order in which tasks can be performed using **topological sort**.

**State transition diagram** represents what can be the legal moves from current states. This can be used in a game of tic-tac-toe.


