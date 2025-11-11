def hughes_hartogs_algorithm(graph):
    # Initialize the data structures needed for the algorithm
    visited = set()  # To keep track of visited nodes
    stack = []  # To simulate the recursive calls

    # A helper function to explore the graph using Depth-First Search approach
    def dfs(node):
        visited.add(node)
        stack.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.pop()

    # Run DFS from each node to ensure all components are covered
    for start_node in graph:
        if start_node not in visited:
            dfs(start_node)

    # Return the stack of nodes which represent the Hughes-Hartogs order
    return stack

# Example usage
if __name__ == '__main__':
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    result = hughes_hartogs_algorithm(example_graph)
    print("Order of nodes as per Hughes-Hartogs Algorithm:", result)