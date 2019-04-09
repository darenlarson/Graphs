import random
import queue

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


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        - Takes a number of users and an average number of friendships
        as arguments.
        - Creates that number of users and a randomly distributed friendships
        between those users.
        - The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}")

        # Create friendships
        # Generate all possible friendship combinations
        possibleFriendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Shuffle the possible friendships
        random.shuffle(possibleFriendships)


        # Create friendships for the first X pairs of the list
        # X is determined by the formula: numUsers * avgFriendships // 2
        # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range(numUsers * avgFriendships // 2):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])


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
                for friend in self.friendships[v]:
                    # Create a copy of the path
                    new_path = list(path)

                    # Add one of the next verts to the path
                    new_path.append(friend)

                    # Add this path to the queue
                    q.enqueue(new_path)

        return None


    def getAllSocialPaths(self, userID):
        visited = {}

        for i in range(1, len(self.friendships) + 1):
            print("friendships:", self.friendships)
            visited[i] = self.bfs(userID, i)
            print(visited)
        
        return {key: value for key, value in visited.items() if value is not None}




# Test Social Graph created using populateGraph method
# sg = SocialGraph()
# sg.populateGraph(10,2)
# print(sg.friendships)

# Test Social Graph I created
sg = SocialGraph()
sg.addUser("daren") #1
sg.addUser("mike") #2
sg.addUser("bill") #3
sg.addUser("kendrick") #4
sg.addUser("noi") #5
sg.addUser("kelley") #6
sg.addUser("chrissy") #7
sg.addUser("ashley") #8
sg.addFriendship(1,2)
sg.addFriendship(1,3)
sg.addFriendship(1,4)
sg.addFriendship(2,6)
sg.addFriendship(3,7)
sg.addFriendship(5,8)

# print("*** sg:", sg)
# print("*** sg.users:", sg.users)
# print("*** sg.friendships:", sg.friendships)
print(sg.getAllSocialPaths(1))


# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populateGraph(10, 2)
#     print(sg.friendships)
#     connections = sg.getAllSocialPaths(1)
#     print(connections)
