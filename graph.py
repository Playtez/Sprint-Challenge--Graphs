"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #  If they're both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        # Keep track of visited nodes
        visited = set()
        # Repeat until queue is empty
        while q.size() > 0:
            # Dequeue first vertex
            v = q.dequeue()
            # If it's not visited:
            if v not in visited:
                print(v)
                # Mark visited
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        # keep track of visited
        visited = set()
        # Repeated until stack is empty
        while s.size() > 0:
            v = s.pop()
            # if v meaning the value is not in visiteed then execute
            if v not in visited:
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # keeping track of visited

        if visited is None:
            visited = set()

        if vertex in visited:
            # add the starting vertex to set
            return
        # i want to add
        visited.add(vertex)
        print(vertex)

        for neighbor in self.get_neighbors(vertex):
            self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # path = []
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # path.append(starting_vertex)
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        #
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # print(path, "**********")
            current_vertex = path[-1]
            # Grab the last vertex from the PATH
            # If that vertex has not been visited..
            if current_vertex not in visited:
                visited.add(current_vertex)
                #     # CHECK IF IT'S THE TARGET aka destination_vertex
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor == destination_vertex:
                        # same thing as path.append(neighbor)
                        # append mutates
                        return path+[neighbor]
                    else:
                        q.enqueue(path+[neighbor])

                #     #   IF SO, RETURN PATH
                #     # Mark it as visited...
                #     # Then add A PATH TO its neighbors to the back of the queue
                #     #   _COPY_ THE PATH
                #     #   APPEND THE NEIGHOR TO THE BACK
                # pass

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        #
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # print(path, "**********")
            current_vertex = path[-1]
            # Grab the last vertex from the PATH
            # If that vertex has not been visited..
            if current_vertex is not visited:
                visited.add(current_vertex)
                #     # CHECK IF IT'S THE TARGET aka destination_vertex
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor == destination_vertex:
                        # same thing as path.append(neighbor)
                        # append mutates
                        return path+[neighbor]
                    else:
                        s.push(path+[neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        # base case
        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
