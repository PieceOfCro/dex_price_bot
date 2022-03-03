from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.nodes = set()
        self.adjacency_list = defaultdict(set)
        self.edges = {}

    def add_node(self, node: str):
        self.nodes.add(node)

    def add_edge(self, node_1: str, node_2: str, edge: str):
        assert node_1 != node_2
        self.edges[tuple(sorted([node_1, node_2]))] = edge
        self.adjacency_list[node_1].add(node_2)
        self.adjacency_list[node_2].add(node_1)

    def find_path(self, source: str, destination: str):
        used = {destination: None}
        queue = deque()
        queue.append(destination)
        while queue:
            dst = queue.popleft()
            for neighbour in self.adjacency_list[dst]:
                if neighbour in used:
                    continue
                used[neighbour] = dst
                queue.append(neighbour)
                if neighbour == source:
                    break
        path = deque()
        half_pair = source
        while used[half_pair]:
            path.appendleft((used[half_pair], half_pair))
            half_pair = used[half_pair]
        return path
