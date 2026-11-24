"""BFS ile giristen cikisa en kisa yolu bulma islemleri."""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .generator import MazeGenerator


# en kısa yol için bfs algoritması en yakın hücreler araştırılacak
def solve_maze(
    maze: MazeGenerator,
    entry: tuple[int, int],
    exit_position: tuple[int, int],
) -> list[tuple[int, int]]:
    """Find a shortest path between entry and exit using BFS."""
    for x, y in (entry, exit_position):
        if not (0 <= x < maze.width and 0 <= y < maze.height):
            raise ValueError(
                "Solution endpoints must be inside the maze."
            )

    queue = deque([entry])

    # parents “Bu komşuyu, mevcut hücreden gelerek keşfettim” bilgisini
    # kaydeder.hücre: geldiğimiz hücre bu yüzden dict
    parents: dict[
        tuple[int, int], tuple[int, int] | None
        # başlangıcın önceki hücresi olmadığı için none
    ] = {entry: None}

    while queue:
        # Böylece hücreleri keşfedilme sırasıyla araştırıyoruz. DFS’de son
        # eklediğimiz hücreye ilerliyorduk; BFS’de en önce eklenmiş hücreyi
        # işliyoruz.
        current = queue.popleft()

        if current == exit_position:
            break

        x, y = current

        for neighbor in maze.get_accessible_neighbors(x, y):
            if neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)

    if exit_position not in parents:
        raise ValueError("No path exists between entry and exit.")

    path: list[tuple[int, int]] = []
    position: tuple[int, int] | None = exit_position

    while position is not None:
        path.append(position)
        position = parents[position]

    # yolu çıkıştan başlayıp parents üzerinden başlangıca doğru topluyoruz
    path.reverse()
    return path
