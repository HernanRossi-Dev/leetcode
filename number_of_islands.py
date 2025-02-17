import unittest
from typing import List, Dict, Tuple


class NumberOfIslands:
    grid: List[List[str]]
    grid_length: int
    grid_height: int
    visited_nodes: Dict[Tuple[int, int], bool] = {}

    def get_neighbours(self, x: int, y: int) -> List[Tuple[int, int]]:
        # top neighbour
        neighbours = []
        if y + 1 < self.grid_height:
            if self.grid[x][y + 1] == "1":
                neighbours.append((x, y + 1))
        if y - 1 >= 0:
            if self.grid[x][y - 1] == "1":
                neighbours.append((x, y - 1))
        if x - 1 >= 0:
            if self.grid[x - 1][y] == "1":
                neighbours.append((x - 1, y))
        if x + 1 < self.grid_length:
            if self.grid[x + 1][y] == "1":
                neighbours.append((x + 1, y))
        return neighbours

    def num_islands(self, grid: List[List[str]]) -> int:
        """Go through the entire grid and make a graph for all adjacent islands
        {
            (0, 0) : [(0, 1), (1, 0)],
            (0, 1) : [(0, 0), (0, 2), (1, 1)],
            ...
        """
        if not grid or not grid[0]:
            return 0
        self.grid = grid
        self.grid_length = len(grid[0]) - 1
        self.grid_height = len(grid) - 1
        island_graph: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
        for r_idx, row in enumerate(grid):
            for c_idx, val in enumerate(row):
                if val == "1":
                    neighbours = self.get_neighbours(r_idx, c_idx)
                    island_graph[(r_idx, c_idx)] = neighbours
        print(f"Island Graph: {island_graph}")
        # Now that we have a graph we will go through it and do a breath first search, start with the first node and queue up its neighbours once we have checked all the neighbours we have found an island. If there is another node left do a another bfs keep going until we don't have any nodes left in the island_graph
        island_count: int = 0
        while island_graph:
            queue = []
            check_node = next(iter(island_graph))
            graph_n = island_graph[check_node]
            queue.extend(graph_n)
            del island_graph[check_node]
            # Do BFS
            self.visited_nodes[check_node] = True
            while queue:
                check_node = queue.pop(0)
                if self.visited_nodes.get(check_node):
                    continue
                self.visited_nodes[check_node] = True
                graph_n = island_graph[check_node]
                queue.extend(graph_n)
                del island_graph[check_node]
            island_count += 1
        return island_count - 1


class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.instance = NumberOfIslands()

    def test_one_island(self):
        test = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        result = self.instance.num_islands(test)
        self.assertEqual(result, 1)

    def test_three_islands(self):
        test = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        result = self.instance.num_islands(test)
        self.assertEqual(result, 3)

    def test_four_islands(self):
        test = [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        result = self.instance.num_islands(test)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
