# Network Packet Routing Simulation

A Python-based interactive visualization tool for network routing algorithms, demonstrating how packets find their way through networks using Bellman-Ford and Dijkstra's algorithms.

## Features

- Interactive network topology creation
- Implementation of Bellman-Ford and Dijkstra's routing algorithms
- Real-time packet routing visualization
- Custom edge weight configuration
- Path highlighting and animation
- User-friendly GUI interface

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.x
- Pygame library
- sys (included in Python standard library)
- heapq (included in Python standard library)
- collections (included in Python standard library)

## Installation

1. Clone the repository or download the source code:
```bash
git clone [repository-url]
```

2. Install the required Pygame library:
```bash
pip install pygame
```

## Usage

1. Run the program:
```bash
python Network_part5.py
```

2. Follow the interactive steps:

   a. **Create Network Nodes:**
   - Enter the number of nodes when prompted
   - Click on the screen to place each node
   
   b. **Add Network Edges:**
   - Enter the number of edges to create
   - For each edge:
     - Enter the first node number
     - Enter the second node number
     - Enter the edge weight (cost/distance)
   
   c. **Select Routing Algorithm:**
   - Click "Select Bellman-Ford" or "Select Dijkstra"
   
   d. **Choose Route:**
   - Click source node
   - Click destination node
   - Watch the packet animation

## Algorithm Details

### Bellman-Ford Algorithm
- Supports negative edge weights
- Detects negative cycles
- Time complexity: O(VE)
- V = number of vertices, E = number of edges

### Dijkstra's Algorithm
- More efficient for non-negative weights
- Finds shortest path tree
- Time complexity: O(V log V + E)
- Uses priority queue for optimization

## Controls

- **Left Mouse Click:**
  - Place nodes
  - Select algorithm
  - Choose source/destination nodes
- **Close Window:**
  - Exit application

## Technical Implementation

The project consists of three main components:

1. **NetworkGraph Class:**
   - Graph data structure
   - Routing algorithm implementations
   - Path calculations

2. **NetworkGUI Class:**
   - Visualization handling
   - User interaction management
   - Animation control

3. **Main Program:**
   - Program flow control
   - Event handling
   - User input processing

## Visualization Color Codes

- **Blue:** Regular nodes
- **Yellow:** Nodes in current path
- **Green:** Active path edges
- **Red:** Edge weights and moving packet
- **Black:** Regular edges

## Limitations

- Nodes must be placed with sufficient spacing
- Edge weights must be integers
- Screen size fixed at 800x600 pixels
- All edges are undirected (bidirectional)

## Troubleshooting

1. If Pygame installation fails:
```bash
python -m pip install --upgrade pip
python -m pip install pygame
```

2. If nodes aren't appearing:
- Ensure clicks are within window bounds
- Check if correct number of nodes was entered

3. If path animation isn't showing:
- Verify all edges are properly connected
- Ensure source and destination nodes are valid

## Contributing
Contributors - Aditya-Codes-247 , Devansh3212

Feel free to fork the project and submit pull requests. Areas for potential improvement:
- Add directed edges support
- Implement additional routing algorithms
- Add save/load functionality for networks
- Enhance visualization features

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Pygame community for graphics support
- Network routing algorithm implementations based on standard graph theory
- Educational resources on network routing protocols

