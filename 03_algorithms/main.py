import heapq
import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Union


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


@dataclass(order=True)
class PriorityQueueNode:
    priority: int
    point: Point = field(compare=False)


class CellType(Enum):
    WATER = "W"
    LAND = "L"


def generate_map(width: int, height: int, land_ratio: float = 0.3) -> list[list[CellType]]:
    total_cells = width * height
    land_cells = int(total_cells * land_ratio)
    water_cells = total_cells - land_cells

    cells = [CellType.WATER] * water_cells + [CellType.LAND] * land_cells

    random.shuffle(cells)
    map_grid = [cells[index * width: (index + 1) * width] for index in range(height)]
    return map_grid


def print_map(map_grid: list[list[CellType]]):
    for row in map_grid:
        print("".join(map(lambda cell: cell.value, row)))


def is_valid(point: Point, width, height):
    return 0 <= point.x < width and 0 <= point.y < height


def heuristic(start: Point, end: Point):
    return abs(start.x - end.x) + abs(start.y - end.y)


def a_star(map_grid: list[list[CellType]], start: Point, end: Point) -> Union[list[Point], int]:
    height = len(map_grid)
    width = len(map_grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    open_list: list[PriorityQueueNode] = []
    heapq.heappush(open_list, PriorityQueueNode(0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_list:
        current = heapq.heappop(open_list).point

        if current == end:
            return reconstruct_path(came_from, current)

        for dx, dy in directions:
            neighbor = Point(current.x + dx, current.y + dy)

            if is_valid(neighbor, width, height) and map_grid[neighbor.x][neighbor.y] == CellType.WATER:
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_list, PriorityQueueNode(f_score[neighbor], neighbor))

    return -1  # Path not found


def reconstruct_path(came_from: dict[Point, Point], current: Point) -> list[Point]:
    total_path = [current]

    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()

    return total_path


M, N = 10, 10  # Size of map

# Debug version
# generated_map = generate_map(M, N, land_ratio=0.0)

generated_map = generate_map(M, N)
print_map(generated_map)

start_point = Point(0, 0)
end_point = Point(M - 1, N - 1)

if generated_map[start_point.x][start_point.y] != CellType.WATER or generated_map[end_point.x][end_point.y] != CellType.WATER:
    print("Start or end point is not water. Adjust the points or regenerate the map.")
else:
    path = a_star(generated_map, start_point, end_point)
    if path != -1:
        print(f"The shortest path from {start_point} to {end_point} is {len(path) - 1} steps.")
        print("Path:", path)
    else:
        print("No path found from start to end.")
