'''
Created on Jan 10, 2017

@author: jfinn
'''

def paths_through_lattice(grid_size):

    # Problem defines the grid size as the number of squares.  Add one to get the number of intersections.
    grid_size += 1
    
    # We'll track the number of different paths that may be taken to get to each node
    nodes = [ [ 0 for col in range(grid_size) ] for row in range(grid_size) ]
    
    # Always 1 path to the first node (we start there)
    nodes[0][0] = 1
    
    # For each path to a given node, that many paths are added to any node reachable from there
    for row in range(grid_size):
        for col in range(grid_size):
            if row < grid_size - 1:
                nodes[row+1][col] += nodes[row][col]
            if col < grid_size - 1:
                nodes[row][col+1] += nodes[row][col]
                
    return nodes[-1][-1]

print(paths_through_lattice(1))
print(paths_through_lattice(2))
print(paths_through_lattice(20))