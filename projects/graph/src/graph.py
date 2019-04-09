"""
Simple graph implementation
"""
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop() 
        else:
            return None
    def size(self):
        return (len(self.stack))



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
        
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")
            
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")


    # Breadth-Fist Travesal
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()

        # Create a set to store vertices that have been visited
        visited = set()

        # Enqueue the starting vertex to the queue
        q.enqueue(starting_vertex_id)

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first element from the queue
            v = q.dequeue()

            # Check if it has been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)

                # Put all of its neighbors in the back of the queue
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)


    # Breadth-First Search
    def bfs(self, starting_vertex_id, target_value):
        # Create an empty queue
        q = Queue()

        # Enqueue the [path] to the starting vertex
        q.enqueue([starting_vertex_id])

        # Create a set to store vertices that have been visited
        visited = set()

        # While the queue is not empty
        while q.size() > 0:

            # Dequeue the first [path] from the queue
            path = q.dequeue()
            v = path[-1]

            # Check if it has been visited. If it hasn't been visited...
            if v not in visited:
                # Check to see if v is our target value. Return the path if it is. This will be the final return statement if the target value is in the graph.
                if v == target_value:
                    return path
                
                # Otherwise, add v to visited
                visited.add(v)

                # Loop over all the verts that v is connected to. Each time this loops, this will add only one next_vert and add it to the queue, then reset to the current path and do it again, and add another vert.
                for next_vert in self.vertices[v]:
                    # Create a copy of the path
                    new_path = list(path)

                    # Add one of the next verts to the path
                    new_path.append(next_vert)

                    # Add this path to the queue
                    q.enqueue(new_path)

        return None


    # Depth-First Traversal
    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()

        # Create a set to store vertices
        visited = set()

        # Put the starting vertex in our stack
        s.push(starting_vertex_id)

        # While the stack is not empty
        while s.size() > 0:
            # Pop the top vertex from the stack
            v = s.pop()

            # If that vertex hasn't been visted
            if v not in visited:
                # mark it as visited
                visited.add(v)
                print(v)

                for next_vert in self.vertices[v]:
                    s.push(next_vert)


    # Depth-First Search
    def dfs(self, starting_vertex_id, target_value):
        # Create an empty stack
        s = Stack()

        # Create a set to store vertices that have been visited
        visited = set()

        # Put the starting vertex in our stack
        s.push(starting_vertex_id)

        # While the stack is not empty
        while s.size() > 0:

            # Pop the top [path] from the stack
            path = s.pop()
            v = path[-1]

            # Check if it has been visited. If it hasn't been visited...
            if v not in visited:
                # Check to see if v is our target value. Return the path if it is. This will be the final return statement if the target value is in the graph.
                if v == target_value:
                    return path
                
                # Otherwise, add v to visited
                visited.add(v)

                # Loop over all the verts that v is connected to. Each time this loops, this will add only one next_vert and add it to the stack, then reset to the current path and do it again, and add another vert.
                for next_vert in self.vertices[v]:
                    # Create a copy of the path
                    new_path = list(path)

                    # Add one of the next verts to the path
                    new_path.append(next_vert)

                    # Add this path to the stack
                    s.push(new_path)

        return None


    # Depth-First Search Recursion
    def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
        # If visited is none, create an empty set()
        if visited is None:
            visited = set()
        
        # If path is None, create an empty list
        if path is None:
            path = []
        
        # Add the current vert to visited
        visited.add(start_vert)

        # Add the current vert to the path that is being built
        path = path + [start_vert]

        # Check if current vert is the target value. If it is, return the path. This is what we're looking for.
        if start_vert == target_value:
            return path

        # Otherwise, loop over each vert that is connected to the current vert
        for child_vert in self.vertices[start_vert]:
            # If this child vert hasn't been visited yet...
            if child_vert not in visited:
                # Recursively call dfs_r_path on each child vert in the loop
                new_path = self.dfs_r_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None




graph = Graph()  # Instantiate your graph
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)

graph.add_directed_edge(1, 2)
graph.add_directed_edge(2, 3)
graph.add_directed_edge(2, 4)
graph.add_edge(3, 5)
graph.add_directed_edge(4, 7)
graph.add_directed_edge(4, 6)
graph.add_directed_edge(6, 3)
graph.add_directed_edge(7, 6)
graph.add_directed_edge(7, 1)


# print(graph.vertices)
print(graph.bfs(1,5))