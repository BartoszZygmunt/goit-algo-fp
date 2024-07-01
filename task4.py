import networkx as nx
import matplotlib.pyplot as plt

# class Node:
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node

# def adding edges
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

# def draw_tree
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Collect node colors to display

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# This function inserts a new key into the binary heap while maintaining the heap property.
def insert_heap(root, key):
    new_node = Node(key)
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if not node.left:
            node.left = new_node
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right = new_node
            break
        else:
            queue.append(node.right)
    
    # Re-balance the heap
    return heapify_up(root, new_node)

# This function maintains the heap property by swapping the node with its parent if the parent is greater than the node.
def heapify_up(root, node):
    if not node or not root:
        return root
    parent = find_parent(root, node)
    while parent and parent.val > node.val:
        node.val, parent.val = parent.val, node.val
        node = parent
        parent = find_parent(root, node)
    return root

# This function finds the parent of a given node in the binary heap.
def find_parent(root, child):
    if not root or root == child:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left == child or node.right == child:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

# This function builds a binary heap from a list of elements.
def build_heap(elements):
    if not elements:
        return None
    root = Node(elements[0])
    for key in elements[1:]:
        insert_heap(root, key)
    return root

# Example usage
elements = [10, 20, 15, 30, 40, 50, 100, 25, 35, 2, 4]
heap_root = build_heap(elements)
draw_tree(heap_root)
