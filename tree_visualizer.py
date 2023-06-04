from Tree_Generator import Tree
import tkinter as tk

def visualize_tree(node, canvas, x, y, x_dist, y_dist):
    # Recursive function to visualize the tree
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')  # Draw a node
    canvas.create_text(x, y, text=node.data)  # Label the node

    if node.left:
        x_left = x - x_dist
        y_left = y + y_dist

        canvas.create_line(x, y + 10, x_left, y_left - 10)  # Draw an edge
        visualize_tree(node.left, canvas, x_left, y_left, x_dist / 2, y_dist)

    if node.right:
        x_right = x + x_dist
        y_right = y + y_dist

        canvas.create_line(x, y + 10, x_right, y_right - 10)  # Draw an edge
        visualize_tree(node.right, canvas, x_right, y_right, x_dist / 2, y_dist)

def create_sample_tree():
    # Creating a sample tree structure
    root = Tree(10)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)
    root.insert(7)
    root.insert(2)
    root.insert(5)
    root.insert(33)
    root.insert(9)
    
    return root


def main():
    root_node = create_sample_tree()

    root = tk.Tk()
    root.title('Tree Visualization')
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    x_distance = 100  # Horizontal distance between nodes
    y_distance = 80  # Vertical distance between nodes

    visualize_tree(root_node, canvas, 400, 50, x_distance, y_distance)

    root.mainloop()


if __name__ == '__main__':
    main()