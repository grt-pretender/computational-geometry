# You are given an undirected weighted graph of n nodes (0-indexed), 
# represented by an edge list where edges[i] = [a, b] is an undirected edge 
# connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success 
# to go from start to end and return its success probability.
# If there is no path from start to end, return 0. 


import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = 0
        visited_nodes = set()

        # making adjacency list for each vertex i + i's neighbors + weights of the edges
        adjacency_list = collections.defaultdict(list)
        for i in range(len(edges)):
            origin, destination = edges[i][0], edges[i][1]
            adjacency_list[origin].append([destination, succProb[i]])
            adjacency_list[destination].append([origin, succProb[i]])
        
        # making priority queue: probability, position
        # Neetcode`s prompt - converting built-in python minheap to a maxheap
        priority_queue = [(-1, start_node)]

        while priority_queue:
            probability, current_position = heapq.heappop(priority_queue)
            visited_nodes.add(current_position)

            if current_position == end_node:
                # converting back
                return probability * -1
            
            for neighbour, edge_probability in adjacency_list[current_position]:
                if neighbour not in visited_nodes:
                    new_probability = probability * edge_probability
                    heapq.heappush(priority_queue, (new_probability, neighbour))

        return res




