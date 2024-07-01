import matplotlib.pyplot as plt
import numpy as np

def draw_pythagorean_tree(ax, x, y, angle, depth, size):
    """
    Draws the Pythagorean tree fractal.
    
    Parameters:
    ax (matplotlib.axes.Axes): The axes on which to draw.
    x (float): The x-coordinate of the starting point.
    y (float): The y-coordinate of the starting point.
    angle (float): The angle of the branch.
    depth (int): The current recursion depth.
    size (float): The length of the branch.
    """
    if depth == 0:
        return
    
    x0 = x + size * np.cos(angle)
    y0 = y + size * np.sin(angle)
    x1 = x0 - size * np.sin(angle)
    y1 = y0 + size * np.cos(angle)
    x2 = x1 + size * np.cos(angle)
    y2 = y1 + size * np.sin(angle)
    
    ax.plot([x, x0], [y, y0], color='brown')
    ax.plot([x0, x1], [y0, y1], color='brown')
    ax.plot([x1, x2], [y1, y2], color='brown')
    ax.plot([x2, x], [y2, y], color='brown')
    
    draw_pythagorean_tree(ax, x2, y2, angle - np.pi / 4, depth - 1, size / np.sqrt(2))
    draw_pythagorean_tree(ax, x1, y1, angle + np.pi / 4, depth - 1, size / np.sqrt(2))

def main():
    recursion_level = int(input("Enter the recursion level: (I suggests max 12): "))
    if recursion_level < 1:
        print("Recursion level must be integer > 0 and < 13.")
        return
    if recursion_level > 12:
        print("Recursion level must be less than or equal to 12.")
        return
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    draw_pythagorean_tree(ax, 0, 0, np.pi / 2, recursion_level, 1)
    
    plt.show()

if __name__ == "__main__":
    main()
