*This project has been created as part of the 42 curriculum by aryaprak, yaydilek.*

# A-Maze-ing

## Description

A Python 3.10+ maze generator with an interactive terminal display, reproducible
random generation, BFS shortest paths, hexadecimal file export, and a reusable
`mazegen` package. The application has no third-party runtime dependencies.

Two modes are available:

- `PERFECT=True`: iterative randomized DFS builds a connected, loop-free maze.
- `PERFECT=False`: DFS followed by braiding creates at least two independent
  loops, keeps at most two dead ends, and checks reachable corners and centre.

Both modes preserve matching shared walls, closed outside borders, and a visible
42 made from fully closed cells. Normal cells are connected; the closed pattern
is deliberately excluded. No fully open 3x3 area is allowed.

## Instructions

Use Linux or WSL with Python 3.10+, pip, GNU Make, and a UTF-8 terminal supporting
ANSI colours and Unicode box-drawing characters. MLX is not needed: the project
uses the terminal display option allowed by the subject.

```sh
python3 -m venv .venv
source .venv/bin/activate
make install
make run
```

Direct execution and a custom configuration file:

```sh
python3 a_maze_ing.py config.txt
make run CONFIG=config.txt
```

Exactly one argument is required. Invalid settings and filesystem errors produce
an explanatory message on stderr and a non-zero exit status. Quit normally with
`q`; Ctrl+C and end-of-input also exit cleanly while waiting for commands.

| Command | Action |
| --- | --- |
| `r` + Enter | Generate another maze, recompute its solution, update output |
| `p` + Enter | Show or hide the shortest path |
| `c` + Enter | Cycle wall colours |
| `q` + Enter | Quit |

`S` marks the entry, `E` the exit, yellow dots the visible solution, and shaded
cyan cells the 42 pattern. Hiding the solution affects only the display: the
exported file always includes it.

Development commands:

```sh
make lint
make lint-strict
make debug
make clean
```

`make lint` runs flake8 and the subject's required mypy flags. `make clean`
removes Python/type-check caches outside `.venv`; it preserves source files and
the root delivery archives. Override the interpreter with `make PYTHON=python3`.

## Configuration

The repository includes `config.txt`. Each non-empty, non-comment line contains
one `KEY=VALUE` pair. Lines starting with `#` are comments. Surrounding whitespace
is ignored; key names and boolean values are case-insensitive. Duplicate keys,
empty values and malformed lines are rejected. Extra keys are currently ignored.

```text
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=False
SEED=42
```

| Key | Required | Meaning |
| --- | --- | --- |
| `WIDTH` | Yes | Positive integer number of columns |
| `HEIGHT` | Yes | Positive integer number of rows |
| `ENTRY` | Yes | Two integers `x,y`, inside the maze |
| `EXIT` | Yes | Two integers `x,y`, different from entry |
| `OUTPUT_FILE` | Yes | Output path, relative to the working directory |
| `PERFECT` | Yes | `True` or `False`; supplied default configuration is False |
| `SEED` | No | Integer seed; omission uses a non-fixed random initialization |

Coordinates start at `(0,0)` in the top left; x increases to the right and y
downwards. Entry and exit must not overlap the closed 42 pattern. Its 7x7 shape
needs at least a 9x9 maze including margins; smaller boards omit it with a
console message. The centre is defined as `(WIDTH // 2, HEIGHT // 2)` and lies
in the gap between the digits. For even sizes this selects the lower/right
central cell.

Small or narrow boards may be valid in perfect mode but unable to satisfy
non-perfect constraints. Such requests are rejected with an explanation.
Non-perfect generation allows up to 50 attempts to reduce dead ends; a failed
attempt limit is reported rather than exporting a board that fails the rules.

## Algorithms and technical choices

**Randomized iterative DFS:** start at `(0,0)`, mark it visited, randomly choose
an unvisited non-pattern neighbour, and open the shared wall in both cells.
A stack records the current exploration branch. Pop when no unvisited neighbour
remains. Each new cell adds one edge, producing a spanning tree without loops.
The iterative form avoids Python's recursion-depth limit. DFS was chosen for its
small, explainable implementation and direct perfect-maze guarantee.

**Braiding:** find cells with one open passage and try opening an additional
wall to a non-pattern neighbour. Save the original wall values, tentatively
open the passage, and undo it if a fully open 3x3 area appears. Add further safe
passages if necessary to reach two independent loops. For a connected corridor
graph, the cycle count is `edges - vertices + 1`; closed pattern cells are
excluded. Right/down passage counting avoids counting an edge twice.

**BFS:** explore accessible neighbours with a FIFO `deque`. Record each cell's
predecessor in a dictionary. Reconstruct from exit to entry, then reverse the
list. BFS gives a shortest path because every passage has equal unit cost.

**Wall encoding:** each cell is an integer bit mask: North=1, East=2, South=4,
West=8. `15` (`F`) means all walls closed. The internal grid is indexed
`grid[y][x]`. Bit clearing opens shared walls symmetrically. A separate random
generator per instance keeps unrelated random calls from affecting generation.

The same seed and sequence of method calls reproduce the same results in the
same Python environment. Regeneration advances the instance's random state.

## Output format

The output contains HEIGHT rows of WIDTH hexadecimal characters, a blank line,
entry coordinates, exit coordinates, and a shortest path using `N`, `E`, `S`,
`W`. Every line ends with LF (`\n`). Example for a 2x2 perfect maze:

```text
D3
D6

0,0
0,1
ESW
```

If the subject's analyzer is available, run it against a freshly generated file:

```sh
python3 /path/to/maze_analyzer.py maze.txt
```

Check its verdict against the requested mode; the script can report either
perfect or playable mazes successfully. It is an independent aid, not a
replacement for checking all subject requirements.

## Reusable module

The package contains `mazegen/generator.py` and `mazegen/solver.py`. It depends
only on the standard library and includes its own usage documentation.

```python
from mazegen import MazeGenerator

maze = MazeGenerator(width=20, height=15, seed=42)
maze.generate()  # Or maze.generate_playable() for non-perfect mode.
structure = maze.grid
solution = maze.solve((0, 0), (19, 14))
print(structure[0][0])
print(solution)
```

The solution is an ordered list of `(x, y)` pairs including both endpoints.
`maze.get_pattern_cells()` exposes the blocked coordinates. Do not choose these
as endpoints. Invalid or unreachable endpoints raise ValueError. See
[package documentation](mazegen/README.md) for the API and assumptions.

Rebuild the package from source:

```sh
make install
make package
```

This creates `.whl` and `.tar.gz` archives in `dist/` and copies them to the
repository root, as required for submission. To build with standard tooling
directly, use `python3 -m build`.

Test an installation outside the source tree so imports cannot accidentally use
the working copy:

```sh
python3 -m venv /tmp/amazegen-check
/tmp/amazegen-check/bin/python -m pip install ./mazegen-1.0.0-py3-none-any.whl
cd /tmp
/tmp/amazegen-check/bin/python -c "from mazegen import MazeGenerator; m = MazeGenerator(20, 15, 42); m.generate(); print(m.solve((0, 0), (19, 14)))"
```

To test the CLI against that installed package, copy `a_maze_ing.py`,
`config_parser.py`, `maze_writer.py`, `renderer.py`, and `config.txt` to another
directory without the local `mazegen/` folder, and run it with that environment.

## Team and project management

The responsibility split is balanced by work area, with shared integration and
review. It does not imply equal line counts or separate ownership of the code.

| Member | Main responsibilities |
| --- | --- |
| **aryaprak** | DFS generation, wall bit masks, BFS solving, braiding, cycle counting, connectivity and 3x3 checks, seed reproducibility |
| **yaydilek** | Configuration parsing and error messages, CLI interactions, terminal rendering and colours, hexadecimal export, Makefile and package integration |
| **Both** | Design discussions, integration checks, analyzer results, documentation review, and defence preparation |

The intended sequence was configuration, basic generation, solving/export,
display/interactions, non-perfect rules, then packaging and verification.
During implementation BFS moved into its own package module to keep generation
readable. The original 42 shape caused unavoidable dead ends; its geometry was
revised and tested. A larger visual version was reduced to a compact 7x7 shape.

Small implementation steps and executable examples helped relate bit operations
to visible passages. Shared-wall checks and the supplied analyzer made logical
errors easier to identify. Earlier validation of pattern geometry and earlier
lint runs would have avoided rework. Future improvements could include faster
local 3x3 checks and broader automated regression coverage.

Tools: Python, VS Code, WSL/terminal, Git, flake8, mypy, pip/venv, setuptools,
build, GNU Make, and the subject-provided maze analyzer.

## Resources

- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Python random](https://docs.python.org/3/library/random.html)
- [Python collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
- [Python integer bitwise operations](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)
- [Princeton: depth-first paths](https://algs4.cs.princeton.edu/41graph/DepthFirstPaths.java.html)
- [Princeton: breadth-first paths](https://algs4.cs.princeton.edu/41graph/BreadthFirstPaths.java.html)
- [Python packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- Project subject v2.3, the supplied evaluation scale and `maze_analyzer.py`.

AI assistance was used for the initial file structure, step-by-step explanations
of Python and graph algorithms, implementation suggestions, debugging pattern
placement, renderer changes, separating BFS, lint/type-check diagnostics,
packaging and documentation. Both code and suggested approaches required review
and execution; unsuitable pattern designs were revised after testing. Learning
comments remain in the source for defence preparation.

## License

[MIT](LICENSE.md), allowing reuse, modification and redistribution of the maze
generator with the copyright and license notice preserved.
