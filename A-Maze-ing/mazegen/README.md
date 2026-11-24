# mazegen

Reusable Python 3.10+ maze generation and shortest-path solving, with no runtime
dependencies. Licensed under the MIT License by aryaprak and yaydilek.

Install with `python3 -m pip install mazegen-1.0.0-py3-none-any.whl`.

```python
from mazegen import MazeGenerator

maze = MazeGenerator(width=20, height=15, seed=42)
maze.generate()  # Perfect maze.
path = maze.solve(entry=(0, 0), exit_position=(19, 14))
print(maze.grid)  # Access cells as maze.grid[y][x].
print(path)       # Ordered (x, y) pairs, including both endpoints.

maze.generate_playable()  # Alternative: loops and at most two dead ends.
path = maze.solve((0, 0), (19, 14))
```

Coordinates start at the top left; x increases rightwards and y downwards.
Each integer encodes closed walls: North=1, East=2, South=4, West=8.
The 7x7 closed-cell 42 pattern is included when width and height are at least 9.
`get_pattern_cells()` returns its coordinates; endpoints must avoid these cells.
The CLI warns when the pattern cannot fit. The class itself does not print.

`generate_playable()` generates a DFS tree, then opens safe extra passages.
It requires at least two independent loops, reachable corners and centre,
at most two dead ends, and no fully open 3x3 area. It raises ValueError when
the constraints cannot be achieved within its attempt limit. Very small or
narrow boards cannot meet these constraints.

The same seed and sequence of calls reproduce the generation sequence within
the same Python environment. Repeated generation on one instance advances its
random generator rather than restarting its seed.

Other methods: `get_accessible_neighbors(x, y)`, `get_dead_ends()`,
`count_loops()`, and `has_open_3x3()`. Analysis methods assume a generated maze
whose normal cells are connected. `solve()` raises ValueError for out-of-bounds
endpoints or when no route exists. The grid is mutable; callers modifying it
must maintain shared walls and connectivity.

Build from the repository root:

```sh
python3 -m pip install build
python3 -m build
```

Both generator and BFS solver are included in the resulting package.
