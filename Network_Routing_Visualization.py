import pygame 
"""For gui"""
import sys 
"""Standard Library for system specific parameters"""
import heapq 
"""Priority queue"""
from collections import defaultdict
"""Provides default values in dictionary based adjacency lists"""
pygame.init() 
"""Initializes the display"""
WIDTH, HEIGHT = 800, 600 
"""Dimensions of display screen"""
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
""""""
pygame.display.set_caption("Network Packet Routing - Bellman-Ford & Dijkstra Algorithms")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 24)
class NetworkGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.adj_list = defaultdict(list)
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
    def bellman_ford(self, source):
        distance = {v: float('inf') for v in range(self.vertices)}
        distance[source] = 0
        predecessor = {v: None for v in range(self.vertices)}
        visited = set()
        priority_queue = [(0, source)]
        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)
            if u in visited:
                continue
            visited.add(u)
            for v, weight in self.adj_list[u]:
                if v not in visited and current_dist + weight < distance[v]:
                    distance[v] = current_dist + weight
                    predecessor[v] = u
                    heapq.heappush(priority_queue, (distance[v], v))
        return distance, predecessor
    def dijkstra(self, source):
        distance = {v: float('inf') for v in range(self.vertices)}
        distance[source] = 0
        predecessor = {v: None for v in range(self.vertices)}
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
        for u, v, weight in self.edges:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")
        return distance, predecessor
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])
class NetworkGUI:
    def __init__(self, graph):
        self.graph = graph
        self.node_positions = {}
        self.source_node = None
        self.shortest_paths = None
        self.predecessor = None
        self.algorithm = None
        self.nodes_added = 0
        self.edge_added = 0
    def draw_network(self, highlight_path=None):
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (50, 50, 200, 40))
        draw_text("Select Bellman-Ford", font, WHITE, 60, 55)
        pygame.draw.rect(screen, BLACK, (300, 50, 200, 40))
        draw_text("Select Dijkstra", font, WHITE, 370, 55)
        for node, pos in self.node_positions.items():
            color = BLUE if highlight_path is None or node not in highlight_path else YELLOW
            pygame.draw.circle(screen, color, pos, 20)
            draw_text(str(node), font, BLACK, pos[0] - 10, pos[1] - 10)
        for u, v, weight in self.graph.edges:
            color = BLACK
            if highlight_path and (u in highlight_path and v in highlight_path):
                color = GREEN
            pygame.draw.line(screen, color, self.node_positions[u], self.node_positions[v], 2)
            mid_x = (self.node_positions[u][0] + self.node_positions[v][0]) // 2
            mid_y = (self.node_positions[u][1] + self.node_positions[v][1]) // 2
            draw_text(str(weight), font, RED, mid_x, mid_y)
        pygame.display.update()
    def add_node(self, pos):
        if self.nodes_added < self.graph.vertices:
            self.node_positions[self.nodes_added] = pos
            print(f"Node {self.nodes_added} added at {pos}")
            self.nodes_added += 1
    def set_edge_count(self):
        while True:
            try:
                self.edge_count = int(input("Enter the number of edges to add: "))
                break
            except ValueError:
                print("Please enter a valid integer for the number of edges.")
    def add_edge(self, u, v, weight):
        while True:
            try:
                if u in self.node_positions and v in self.node_positions:
                    self.graph.add_edge(u, v, weight)
                    self.edge_added += 1
                    break
                else:
                    print("Invalid nodes. Choose nodes within the existing network.")
            except ValueError:
                print("Please enter valid integer values for nodes and weight.")
    def select_algorithm(self, mouse_pos):
        if 50 <= mouse_pos[0] <= 250 and 50 <= mouse_pos[1] <= 90:
            self.algorithm = "bellman_ford"
            print("Algorithm selected: Bellman-Ford")
        elif 300 <= mouse_pos[0] <= 500 and 50 <= mouse_pos[1] <= 90:
            self.algorithm = "dijkstra"
            print("Algorithm selected: Dijkstra")
    def run_algorithm(self, source):
        if self.algorithm == "bellman_ford":
            try:
                self.shortest_paths, self.predecessor = self.graph.bellman_ford(source)
                print(f"Shortest distances from node {source} using Bellman-Ford: {self.shortest_paths}")
            except ValueError as e:
                print(e)
        elif self.algorithm == "dijkstra":
            self.shortest_paths, self.predecessor = self.graph.dijkstra(source)
            print(f"Shortest distances from node {source} using Dijkstra: {self.shortest_paths}")
    def animate_packet(self, source, destination):
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = self.predecessor[current]
        path.reverse()
        for i in range(len(path) - 1):
            start_pos = self.node_positions[path[i]]
            end_pos = self.node_positions[path[i + 1]]
            steps = 20
            for step in range(steps):
                intermediate_x = start_pos[0] + (end_pos[0] - start_pos[0]) * step / steps
                intermediate_y = start_pos[1] + (end_pos[1] - start_pos[1]) * step / steps
                self.draw_network(highlight_path=path[:i + 2])
                pygame.draw.circle(screen, RED, (int(intermediate_x), int(intermediate_y)), 5)
                pygame.display.update()
                pygame.time.delay(50)
    def get_closest_node(self, mouse_pos):
        closest_node = None
        min_distance = float('inf')
        for node, pos in self.node_positions.items():
            distance = ((mouse_pos[0] - pos[0]) ** 2 + (mouse_pos[1] - pos[1]) ** 2) ** 0.5
            if distance < min_distance and distance < 20:
                min_distance = distance
                closest_node = node
        return closest_node
def main():
    clock = pygame.time.Clock()
    vertices = int(input("Enter number of nodes: "))
    graph = NetworkGraph(vertices)
    gui = NetworkGUI(graph)
    node_selection_mode = True
    running = True
    source_selected = False
    destination_selected = False
    source_node = None
    destination_node = None
    while running:
        gui.draw_network()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if node_selection_mode:
                    gui.add_node((mouse_x, mouse_y))
                    if gui.nodes_added == vertices:
                        node_selection_mode = False
                        edges = int(input("Enter number of edges: "))
                        gui.max_edges = edges
                        print("Click on nodes to add edges and specify weights")
                else:
                    gui.select_algorithm((mouse_x, mouse_y))
                    if gui.edge_added < gui.max_edges:
                        u = int(input("Enter the first node for the edge: "))
                        v = int(input("Enter the second node for the edge: "))
                        weight = int(input(f"Enter weight for edge between {u} and {v}: "))
                        gui.add_edge(u, v, weight)
                    elif gui.edge_added == gui.max_edges:
                        print("All edges have been added.")
                    if gui.algorithm and gui.edge_added == gui.max_edges:
                        if not source_selected:
                            closest_node = gui.get_closest_node((mouse_x, mouse_y))
                            if closest_node is not None:
                                source_node = closest_node
                                source_selected = True
                                print(f"Source node selected: {source_node}")
                        elif source_selected and not destination_selected:
                            closest_node = gui.get_closest_node((mouse_x, mouse_y))
                            if closest_node is not None:
                                destination_node = closest_node
                                destination_selected = True
                                print(f"Destination node selected: {destination_node}")
                                gui.run_algorithm(source_node)
                                gui.animate_packet(source_node, destination_node)
                            if source_selected and destination_selected:
                                source_selected = False
                                destination_selected = False
        clock.tick(30)
if __name__ == "__main__":
    main()