# Traveling-Sales-Man-Problem-TSP-Algeria
This GitHub repository contains implementations of four different algorithms to solve the Traveling Salesman Problem (TSP). The TSP is a classic problem in computer science and operations research, aiming to find the shortest possible route that a salesman can take to visit a set of cities and return to the starting point.

The implemented algorithms in this repository are as follows:
1. **Christofides** : The Christofides algorithm is an approximation algorithm that guarantees a solution within a factor of 3/2 of the optimal solution.The Networkx implementation is used . the resulting graph contains cycles but nonethless it provides a good solution.
1. **Kruskal+DFS** : This algorithm combines Kruskal's minimum spanning tree algorithm with Depth-First Search (DFS) to find an approximate solution for the TSP. It constructs a minimum spanning tree and then performs a DFS traversal to find a Hamiltonian cycle.it provides very good results , but doesn't respect the cities connections contraints as the graph is supposedly incomplete.
1. **Nearest Neighbor** :  The algorithm starts from a randomly chosen city and repeatedly selects the nearest unvisited city until all cities have been visited, forming a Hamiltonian cycle, It is the the second best algorithm in term of results,tho may produce inexisting connections.
1. **Concorde** :  Concorde is a well-known TSP solver developed by the Operations Research Group at Carnegie Mellon University. It utilizes a variety of sophisticated techniques, including linear programming and branch-and-cut, to find an optimal or near-optimal solution to the TSP.By far the best algorithm in terms of results,execution time and respecting connection constraints .

## Data Files
Algeria can be modeled as an incomplete graph of 58 nodes representing the main city of the given province and 144 edges representing the shortest road connecting the two .

![AlgeriaMap](https://github.com/bensalem14/Traveling-Sales-Man-Problem-TSP-Algeria/assets/104575447/4e7bc22f-9d87-4ace-9637-f554724d1e00)


The csv file **'AlgeriaCities.csv'** contains four columns the **City** representing the main city of a given province while the **Adjacent province** represents the main city of the adjacent province, the **Distance** represents the shortest road distance between the cities and **Route** represents the route name.

The csv file **'Cities.csv'** contains the cities and the geographic coordinantes. the coordinantes are approximative and the folium library may occasionally print far away points.

The data was inserted manually and taken from GoogleMaps meaning possible mistakes in the connections or distances.

## Results
The results will be displayed in an html file containing the folium map under the naming convention of **'Algorithm_map.html'**.the paths and cost of the path will be rpinted on the console , as for concorde it will print it's own cost so no need to calculate it.

## Contributing
Contributions to this repository are welcome. If you have any improvements, bug fixes, or additional algorithms to propose, please feel free to submit a pull request.If you encounter any issues or have suggestions, please open an issue in the GitHub repository, and I'll be happy to assist you.

## License
This repository is licensed under the MIT License. You are free to use, modify, and distribute the code and resources provided in this repository.
