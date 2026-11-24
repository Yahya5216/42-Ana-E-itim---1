"""Bir bitin 1 olması, o yönde duvar bulunduğunu gösterir. Dolayısıyla 15,
dört duvarı da kapalı bir hücredir.

Örneğin doğu duvarı açık, diğerleri kapalıysa:
Kuzey + Güney + Batı = 1 + 4 + 8 = 13
Bu hücrenin hexadecimal gösterimi D olur
"""

# Provide a reusable maze generator.

import random
from .solver import solve_maze


NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

ALL_WALLS = NORTH | EAST | SOUTH | WEST

PATTERN_42 = (
    "#.#.###",
    "#.#...#",
    "#.#...#",
    "###.###",
    "..#.#..",
    "..#.#..",
    "..#.###",
)


class MazeGenerator:
    """Store the maze grid and its random number generator."""

    def __init__(
        self,
        width: int,
        height: int,
        seed: int | None = None,
    ) -> None:
        """Initialize a grid with all walls closed."""
        # Boyutları parser’da da kontrol etmiştik. Burada tekrar kontrol
        # etmemizin nedeni, MazeGenerator sınıfının parser kullanılmadan başka
        # bir projeden de çağrılabilecek olması.
        if width <= 0 or height <= 0:
            raise ValueError(
                "Maze dimensions must be greater than zero."
            )

        self.width = width
        self.height = height
        self.rng = random.Random(seed)

        self.grid: list[list[int]] = [
            [ALL_WALLS for _ in range(width)]
            for _ in range(height)
        ]

    def has_wall(self, x: int, y: int, direction: int) -> bool:
        """Return whether a cell has a wall in the given direction."""
        return bool(self.grid[y][x] & direction)
    #
    # Hücre:  1101
    # EAST:   0010
    # ────
    # Sonuç:  0000 → 0 → bool(0) = False
    # Doğu duvarı yok; o yön açık.
    #

    def open_passage(
        self,
        x: int,
        y: int,
        next_x: int,
        next_y: int,
    ) -> None:
        """Open the shared wall between two adjacent cells."""
        if not (
            0 <= x < self.width
            and 0 <= y < self.height
            and 0 <= next_x < self.width
            and 0 <= next_y < self.height
        ):
            raise ValueError("Both cells must be inside the maze.")

        dx = next_x - x
        dy = next_y - y

        if dx == 1 and dy == 0:
            direction, opposite = EAST, WEST
        elif dx == -1 and dy == 0:
            direction, opposite = WEST, EAST
        elif dx == 0 and dy == 1:
            direction, opposite = SOUTH, NORTH
        elif dx == 0 and dy == -1:
            direction, opposite = NORTH, SOUTH
        else:
            raise ValueError("Cells must be directly adjacent.")

        self.grid[y][x] &= ~direction
        self.grid[next_y][next_x] &= ~opposite
        # Bu iki satırın amacı iki komşu hücre arasındaki duvarı iki taraftan
        # da kaldırmak.
        #
        # Örneğin yan yana iki hücre olsun:
        # Sol hücre  │  Sağ hücre
        # ↑
        # Açacağımız geçit
        # Soldaki hücrenin doğu, sağdaki hücrenin batı duvarını kaldıracağız:
        # Batı Güney Doğu Kuzey
        # Başlangıç:          1    1    1    1    → 15
        # Doğuyu kaldır:
        # 1    1    0    1    → 13
        # Batı Güney Doğu Kuzey
        # Başlangıç:          1    1    1    1    → 15
        # Batıyı kaldır:      0    1    1    1    → 7

    # Fiziksel olarak yanındaki hücreleri verir; duvara bakmaz.
    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        """Return the coordinates of neighboring cells inside the maze."""
        neighbors: list[tuple[int, int]] = []

        # offset mevcut hücreden komşuya gitmek için koordinatlara eklenecek
        # farkları tutuyor
        offsets = (
            # kuzey
            (0, -1),
            # doğu
            (1, 0),
            # güney
            (0, 1),
            # batı
            (-1, 0),
        )

        for dx, dy in offsets:
            next_x = x + dx
            next_y = y + dy

            if (
                0 <= next_x < self.width
                and 0 <= next_y < self.height
            ):
                neighbors.append((next_x, next_y))

        return neighbors

    # rastgele yollar oluşturan algoritmayıoluşturuyoux dfs ile geri izleme
    # yöntemini kullanacağız
    def generate(self) -> None:
        """Başlangıç hücresini ziyaret edilmiş olarak işaretle.
        Ziyaret edilmemiş komşularından birini rastgele seç.
        Aradaki duvarı kaldır ve o hücreye ilerle.
        Gidilecek yeni komşu kalmadığında bir önceki hücreye dön.
        Bütün seçenekler bitene kadar devam et.
        """
        # Önce neden tabloyu yeniden oluşturuyoruz?generate() tekrar çağrılırsa
        # eski yolların üzerine ekleme yapmak yerine bütün duvarları kapatıp
        # yeni üretime başlamak için.
        self.grid = [
            [ALL_WALLS for _ in range(self.width)]
            for _ in range(self.height)
        ]
        pattern_cells = self.get_pattern_cells()

        # aynı hücreye tekrar yeni bir geçit açmamız engellemke için
        visited: set[tuple[int, int]] = {(0, 0)}
        # ilerlediğimiz yolun kaydı, çıkmazda buradan geri döneriz
        stack: list[tuple[int, int]] = [(0, 0)]

        # liste boş olmadığı sürece devam et
        while stack:
            x, y = stack[-1]
            candidates: list[tuple[int, int]] = []

            for neighbor in self.get_neighbors(x, y):
                if (
                    neighbor not in visited
                    and neighbor not in pattern_cells
                ):
                    candidates.append(neighbor)

            if not candidates:
                # bi sonraki turda tekrar son elemanda oluruz,onun visited
                # edilmemiş komşularını ararız
                stack.pop()
                continue

            next_x, next_y = self.rng.choice(candidates)

            self.open_passage(x, y, next_x, next_y)
            visited.add((next_x, next_y))
            stack.append((next_x, next_y))
        # dfs nin desen dışındaki bütün hücrelere ulaştığını kontrol ediyoruz
        # Toplam hücre:       9 × 7 = 63
        # Desen hücreleri:            20
        # Ulaşılması gereken: 63 − 20 = 43    ziyaret edilen expected counta
        # eşit olmalı
        expected_count = (
            self.width * self.height - len(pattern_cells)
        )

        if len(visited) != expected_count:
            raise ValueError(
                "The 42 pattern leaves unreachable maze cells."
            )

    # # işaretlerinin labirentte hangi koordinatlara denk geldiğini bulma
    def get_pattern_cells(self) -> set[tuple[int, int]]:
        """Return centered pattern coordinates, or an empty set."""
        pattern_width = len(PATTERN_42[0])
        pattern_height = len(PATTERN_42)

        if (
            # kontrol deseninin çevresinde en az 1 tane boşluk bırakır
            self.width < pattern_width + 2
            or self.height < pattern_height + 2
        ):
            return set()
        # bunlar desenin sol üst köşesini belirtir
        start_x = self.width // 2 - 3
        start_y = (self.height - pattern_height) // 2

        cells: set[tuple[int, int]] = set()

        # her elemanın sıra numarasını almak için enumerate kullandık
        for row_index, row in enumerate(PATTERN_42):
            for column_index, character in enumerate(row):
                if character == "#":
                    cells.add(
                        (start_x + column_index, start_y + row_index)
                    )

        return cells

    # Arada duvar olmadan geçebildiklerini verir.
    def get_accessible_neighbors(
        self,
        x: int,
        y: int,
    ) -> list[tuple[int, int]]:
        """Return neighboring cells reachable through open passages."""
        accessible: list[tuple[int, int]] = []

        directions = (
            (0, -1, NORTH),
            (1, 0, EAST),
            (0, 1, SOUTH),
            (-1, 0, WEST),
        )

        for dx, dy, direction in directions:
            next_x = x + dx
            next_y = y + dy

            if (
                0 <= next_x < self.width
                and 0 <= next_y < self.height
                and not self.has_wall(x, y, direction)
            ):
                accessible.append((next_x, next_y))

        return accessible

    def get_closed_neighbors(
        self,
        x: int,
        y: int,
    ) -> list[tuple[int, int]]:
        """Return non-pattern neighbors separated by a closed wall."""
        pattern_cells = self.get_pattern_cells()

        if (x, y) in pattern_cells:
            return []

        accessible = set(self.get_accessible_neighbors(x, y))
        candidates: list[tuple[int, int]] = []

        for neighbor in self.get_neighbors(x, y):
            if (
                neighbor not in pattern_cells
                and neighbor not in accessible
            ):
                candidates.append(neighbor)

        return candidates

    def solve(
        self,
        entry: tuple[int, int],
        exit_position: tuple[int, int],
    ) -> list[tuple[int, int]]:
        """Return a shortest path using the BFS solver."""
        return solve_maze(self, entry, exit_position)

    def get_dead_ends(self) -> list[tuple[int, int]]:
        """Return corridor cells with exactly one accessible neighbor."""
        dead_ends: list[tuple[int, int]] = []

        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.get_accessible_neighbors(x, y)

                # yalnızca bir komsusu varsa çıkmaz sokaktır
                if len(neighbors) == 1:
                    dead_ends.append((x, y))

        return dead_ends

    def has_open_3x3(self) -> bool:
        """Return whether any 3x3 area has no internal walls."""
        for start_y in range(self.height - 2):
            for start_x in range(self.width - 2):
                has_internal_wall = False

                for y in range(start_y, start_y + 3):
                    for x in range(start_x, start_x + 3):
                        if (
                            x < start_x + 2
                            and self.has_wall(x, y, EAST)
                        ):
                            has_internal_wall = True

                        if (
                            y < start_y + 2
                            and self.has_wall(x, y, SOUTH)
                        ):
                            has_internal_wall = True

                if not has_internal_wall:
                    return True

        return False

    def try_open_passage(
        self,
        x: int,
        y: int,
        next_x: int,
        next_y: int,
    ) -> bool:
        """Open a closed passage unless it creates an open 3x3 area."""
        if (next_x, next_y) not in self.get_closed_neighbors(x, y):
            return False

        original_cell = self.grid[y][x]
        original_neighbor = self.grid[next_y][next_x]

        self.open_passage(x, y, next_x, next_y)

        if self.has_open_3x3():
            self.grid[y][x] = original_cell
            self.grid[next_y][next_x] = original_neighbor
            return False

        return True

    # Bir çıkmaz bul, kapalı komşularını rastgele sırayla dene, uygun bir
    # ikinci geçit açabilirsen o hücreyi bırak
    def braid(self) -> None:
        """Reduce dead ends by opening additional safe passages."""
        dead_ends = self.get_dead_ends()
        self.rng.shuffle(dead_ends)

        for x, y in dead_ends:
            if len(self.get_accessible_neighbors(x, y)) != 1:
                continue

            candidates = self.get_closed_neighbors(x, y)
            self.rng.shuffle(candidates)

            for next_x, next_y in candidates:
                if self.try_open_passage(x, y, next_x, next_y):
                    break

    # labirentte kaç bağımsız döngü olduğunu hesaplayacağız. Çünkü
    # PERFECT=False için yalnızca bir döngü yeterli değil; en az iki tane
    # gerekiyor
    def count_loops(self) -> int:
        """Count independent cycles in the connected corridor graph."""
        pattern_cells = self.get_pattern_cells()
        cell_count = self.width * self.height - len(pattern_cells)
        passage_count = 0

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in pattern_cells:
                    continue

                if (
                    x + 1 < self.width
                    and not self.has_wall(x, y, EAST)
                ):
                    passage_count += 1

                if (
                    y + 1 < self.height
                    and not self.has_wall(x, y, SOUTH)
                ):
                    passage_count += 1

        return passage_count - cell_count + 1
    # Neden yalnızca doğu ve güney geçitlerini sayıyoruz?
    # Bir geçit iki hücre tarafından görülür. Hem doğuyu hem batıyı
    # saysaydık aynı geçidi iki kez sayardık. Doğu ve güney yönlerini saymak,
    # her geçidi bir kez saymamızı sağlar.
    # Formül neden çalışıyor
    # Döngü içermeyen, bağlantılı bir yapıda n hücreyi bağlamak
    # için n - 1 geçit vardır. Bu yapı üzerine eklenen her yeni geçit
    # bir bağımsız döngü ekler

    def ensure_minimum_loops(self, minimum: int = 2) -> None:
        """Add safe passages until the required cycle count is reached."""
        if minimum < 0:
            raise ValueError("Minimum loop count cannot be negative.")

        loop_count = self.count_loops()

        if loop_count >= minimum:
            return

        candidates: list[tuple[int, int, int, int]] = []

        for y in range(self.height):
            for x in range(self.width):
                for next_x, next_y in self.get_closed_neighbors(x, y):
                    if next_x > x or next_y > y:
                        candidates.append((x, y, next_x, next_y))

        self.rng.shuffle(candidates)

        for x, y, next_x, next_y in candidates:
            if self.try_open_passage(x, y, next_x, next_y):
                loop_count += 1

                if loop_count >= minimum:
                    return

        raise ValueError(
            f"Could not create at least {minimum} independent loops "
            "with the current maze and constraints."
        )
    # PERFECT=False modunda merkez yürünebilir olmalı, ancak ortaladığımız 42
    # deseni bazı boyutlarda merkezi kapatabilir

    def validate_playable_cells(self) -> None:
        """Check that corners and the center are corridor cells."""
        required_cells = (
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
            (self.width // 2, self.height // 2),
        )

        for x, y in required_cells:
            if not self.get_accessible_neighbors(x, y):
                raise ValueError(
                    f"Required playable cell ({x},{y}) has no passage."
                )

    def generate_playable(self) -> None:
        """Try to generate a playable maze with at most two dead ends."""
        max_attempts = 50

        for _ in range(max_attempts):
            self.generate()
            self.braid()
            self.ensure_minimum_loops()
            self.validate_playable_cells()

            if len(self.get_dead_ends()) <= 2:
                return

        raise ValueError(
            "Could not generate a playable maze with at most "
            f"two dead ends after {max_attempts} attempts."
        )
        # 1. DFS ile bağlantılı temel labirenti oluşturuyoruz.
        # 2. Çıkmazları azaltıyoruz.
        # 3. En az iki bağımsız döngü sağlıyoruz.
        # 4. Köşeleri ve merkezi kontrol ediyoruz.
        # 5. Kalan çıkmaz sayısını kontrol ediyoruz.
        # Subject “birkaç çıkmaz tolere edilir” diyor; en fazla iki sınırı
        # bizim uygulama tercihimiz. Bu denemede sağlanamazsa geçersiz sonucu
        # kabul etmek yerine hata veriyoruz.
