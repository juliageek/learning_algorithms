import functools

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [
            [0 for column in range(vertices)]
            for row in range(vertices)
        ]

    def __str__(self):
        return f'graph is: {self.graph}'

    def convert_graph_to_hash_map(self):
        # look in neighbour for edge different than 0
        # take the value and sum it up on all edges of the current node except previous neighbour's index and current index
        graph_hash_map = {}
        for idxi, i in enumerate(self.graph):
            graph_hash_map[idxi+1] = {}
            for idxj, j in enumerate(i):
                if idxi == 0: # not first node
                    graph_hash_map[idxi + 1][idxj + 1] = j
                else:
                    if graph_hash_map[idxi][idxi + 1] != 0 and j != 0 and idxj+1 >= idxi + 1:
                        graph_hash_map[idxi + 1][idxj + 1] = graph_hash_map[idxi][idxi + 1] + j
                    else:
                        graph_hash_map[idxi + 1][idxj + 1] = j
        print(graph_hash_map)


    def compute_cumulated_distances_based_on_matrix(self, node: int):
        neighbour_values = []
        for idx, i in enumerate(range(0, node)):
            neighbour_values.append(self.graph[i][idx-1])
        return sum(neighbour_values)


    def dijkstra(self):
        # traverse every node in matrix, but eliminate edges <= current edge
        # if there is already a key in the dictionary for that node, do min(saved_distance, current_edge_distance + cumulated distance)
        self.convert_graph_to_hash_map()
        smallest_distances = {}

        for idxi, i in enumerate(self.graph):
            for idxj, j in enumerate(i):
                # we get to the current node's distance
                if j != 0:
                    if idxj + 1 not in smallest_distances.keys():
                        smallest_distances[idxj+1]=self.compute_cumulated_distances_based_on_matrix(idxi+1) + j
                    else:
                        smallest_distances[idxj + 1] = min(
                            self.compute_cumulated_distances_based_on_matrix(idxi+1) + j,
                            smallest_distances[idxj + 1]
                        )

        print(smallest_distances)

        distance_to_neighbours = {
            2: (1, 4),
            3: (2, 12),
            4: (3, 19),
            5: (3, 21),
            6: (3, 16),
            7: (8, 16),
            8: (2, 15),
            9: (3, 14)
        }


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [
        #1, 2, 3, 4, 5, 6, 7, 8, 9
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],# 4
        [0, 8, 0, 7, 0, 4, 0, 0, 2], # 8 + 4
        [0, 0, 7, 0, 9, 14, 0, 0, 0], # 4 + 8 + 7
        [0, 0, 0, 9, 0, 10, 0, 0, 0], # 9 + 7 + 8 + 4
        [0, 0, 4, 14, 10, 0, 2, 0, 0], # 10 + 9 + 7 + 8 + 4
        [0, 0, 0, 0, 0, 2, 0, 1, 6], # 2 + 10 + 9 + 7 + 8 + 4
        [8, 11, 0, 0, 0, 0, 1, 0, 7], # 1 + 2 + 10 + 9 + 7 + 8 + 4
        [0, 0, 2, 0, 0, 0, 6, 7, 0]

        # compute cumulated sum => add that to all other non-0 edges in the array
        # don't compare
    ]

    g.compute_cumulated_distances_based_on_matrix(4)
    g.dijkstra()
