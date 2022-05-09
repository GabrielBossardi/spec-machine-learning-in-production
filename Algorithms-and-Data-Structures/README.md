# Implementation of Shortest Separation Degree in Social Network

Degrees of Separation in Social Networks: consider the graph of a social network, where each profile corresponds to a vertex, and there is an edge between two vertices only if the corresponding profiles are friends. We want to know the average degree of separation between two network profiles. That is, knowing how many edges have, on average, a shortest path connecting two profiles. To this end, we designed the following experiment.

We have a construction function that takes as input a # (number) of vertices, a # of edges, and that uses these parameters to randomly generate the graph of a network. We also have a tests function that receives the previously generated graph, performs a battery of 100 tests, calculates the average of the test results, and returns the average degree of separation found. In each of the 100 iterations, the tests function randomly selects two profiles (vertices) from the network and calls a search function to calculate the degree of separation of the selected vertices.

However, this search function is not implemented. Your mission is to implement it, perform the tests for each pair (# of vertices, # of edges) indicated in the following table, and fill each cell of the table with the average value of the degrees of separation found. Note that the # of edges per vertex are indicated in the table, but the construction function receives the total number. With the table filled, briefly analyze how the average degree of separation grows as a function of the # of vertices and edges of the graph.


| Vértices ( n ) | n * 5 | n * raíz ( n ) | n * n / 5 |
| :---: | :---: | :---: | :---: |
| 100 |
| 1000 |
| 10000 |
| 100000 |

After carrying out the previous tests, we have one more challenge. Now consider the alternating version of the degree of separation (distance) between two network profiles. In the alternating version, only paths in which a male profile follows a female profile are considered and vice versa. Make a new version of your search function to consider only alternate paths, retest using this new function and fill in the next table with the average degrees of separation found. How did this version of the problem affect degrees of separation?
