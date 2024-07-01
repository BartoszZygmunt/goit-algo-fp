import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  # Saving a node color in a graph
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, ax, title):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Collect node colors to display

    ax.clear()
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors, ax=ax)
    ax.set_title(title)
    plt.draw()
    plt.pause(0.5)

def build_heap_tree(array):
    """
    Builds a binary heap from the given array and returns the root of the heap.
    """
    if not array:
        return None

    nodes = [Node(key) for key in array]
    
    for i in range(len(array)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(array):
            nodes[i].left = nodes[left_index]
        if right_index < len(array):
            nodes[i].right = nodes[right_index]

    return nodes[0]

def color_gradient(n):
    """
    Generate a gradient of n colors from dark to light shades.
    """
    colors = list(mcolors.CSS4_COLORS.keys())
    step = len(colors) // n
    return [colors[i * step] for i in range(n)]

def dfs_visualize(node, colors, ax, index=0):
    if node:
        node.color = colors[index]
        draw_tree(root, ax, "DFS Traversal")
        index += 1
        index = dfs_visualize(node.left, colors, ax, index)
        index = dfs_visualize(node.right, colors, ax, index)
    return index

def bfs_visualize(node, colors, ax):
    queue = deque([node])
    index = 0
    while queue:
        current = queue.popleft()
        current.color = colors[index]
        draw_tree(root, ax, "BFS Traversal")
        index += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Example usage
if __name__ == "__main__":
    array = [10, 9, 7, 8, 6, 5, 3, 0, 4, 2, 1]
    root = build_heap_tree(array)

    fig, ax = plt.subplots(figsize=(8, 5))
    plt.ion()  # Turn on interactive mode for visualization
    colors = color_gradient(len(array))

    # DFS visualization
    print("DFS Traversal Visualization")
    dfs_visualize(root, colors, ax)

    # Reset tree colors
    root = build_heap_tree(array)

    # BFS visualization
    print("BFS Traversal Visualization")
    bfs_visualize(root, colors, ax)
    
    plt.ioff()  # Turn off interactive mode
    plt.show()
