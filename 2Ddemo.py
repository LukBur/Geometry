import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the Euclidean distance between two points
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate the circumcenter of a triangle
def circumcenter(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / d
    uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / d
    return ux, uy

# Function to check if a point lies inside the circumcircle of a triangle
def in_circle(p1, p2, p3, test):
    ux, uy = circumcenter(p1, p2, p3)
    r = distance((ux, uy), p1)
    return distance((ux, uy), test) < r

# Function to perform the sweep line algorithm for Delaunay triangulation
def delaunay_triangulation(points):
    # Sort points by x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])
    n = len(sorted_points)
    # Initialize an empty list to store triangles
    triangles = []
    # Initialize a list to store active edges
    active_edges = []
    # Sweep line starts from the leftmost point
    sweep_line_x = sorted_points[0][0]

    # Process each point one by one
    for i in range(n):
        # Update the sweep line position
        sweep_line_x = sorted_points[i][0]
        # Remove edges that are no longer active
        active_edges = [edge for edge in active_edges if edge[1] > sweep_line_x]
        # Add new edges formed by the current point
        for edge in active_edges:
            if in_circle(edge[0], edge[1], sorted_points[i], sorted_points[edge[2]]):
                triangles.append((edge[0], edge[1], sorted_points[i]))
        # Find new edges
        for j in range(i+1, n):
            if sorted_points[j][0] - sweep_line_x > 2 * np.spacing(1):
                break
            if i != j and j != n-1:
                active_edges.append((sorted_points[i], sorted_points[j], j))
            elif i != j:
                active_edges.append((sorted_points[i], sorted_points[j], -1))
        # Sort active edges by y-coordinate of the right endpoint
        active_edges.sort(key=lambda edge: edge[1][1])

    return triangles

# Generate random points
np.random.seed(0)
num_points = 20
points = np.random.rand(num_points, 2)

# Perform Delaunay triangulation using the sweep line algorithm
triangles = delaunay_triangulation(points)

# Plot the triangulation
plt.triplot(points[:,0], points[:,1], np.array(triangles))
plt.plot(points[:,0], points[:,1], 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Delaunay Triangulation (Sweep Line Algorithm)')
plt.show()
