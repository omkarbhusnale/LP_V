#PR 1 : Parallel BFS and DFS

import numpy as np
import queue
import time
import openmp

# Parallel Breadth First Search (BFS)
def parallel_bfs(graph, start_node):
    num_nodes = len(graph)
    visited = np.zeros(num_nodes, dtype=bool)
    visited[start_node] = True
    bfs_queue = queue.Queue()
    bfs_queue.put(start_node)

    while not bfs_queue.empty():
        current_node = bfs_queue.get()
        print("Visiting node:", current_node)
        
        # Use OpenMP parallelism for expanding neighbors
        with openmp.parallel(num_threads=4):
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    bfs_queue.put(neighbor)

# Parallel Depth First Search (DFS)
def parallel_dfs(graph, start_node):
    num_nodes = len(graph)
    visited = np.zeros(num_nodes, dtype=bool)
    visited[start_node] = True
    dfs_stack = [start_node]

    while dfs_stack:
        current_node = dfs_stack.pop()
        print("Visiting node:", current_node)

        # Use OpenMP parallelism for exploring neighbors
        with openmp.parallel(num_threads=4):
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs_stack.append(neighbor)

# Example usage
if __name__ == '__main__':
    # Example graph represented as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 6],
        5: [2],
        6: [4]
    }

    start_node = 0

    print("Parallel BFS:")
    start_time = time.time()
    parallel_bfs(graph, start_node)
    end_time = time.time()
    print("Time taken:", end_time - start_time)

    print("\nParallel DFS:")
    start_time = time.time()
    parallel_dfs(graph, start_node)
    end_time = time.time()
    print("Time taken:", end_time - start_time)

