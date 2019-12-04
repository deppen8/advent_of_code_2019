from typing import List, Dict, NamedTuple
import csv


class Vertex(NamedTuple):
    x: int
    y: int


def get_vertices(path: List[str]) -> Dict[Vertex, int]:
    vertices = {}
    x = 0
    y = 0
    steps_visited = 0
    for turn in path:
        direction = turn[0]
        dist = int(turn[1:])
        for i in range(dist):
            steps_visited += 1
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            vert = Vertex(x, y)
            if vert not in vertices.keys():
                vertices[vert] = steps_visited
    return vertices


def get_overlap(verts0: Dict[Vertex, int], verts1: Dict[Vertex, int]) -> List[Vertex]:
    return [vert for vert in verts0.keys() if vert in verts1.keys()]


def min_dist_from_origin(shared_verts: List[Vertex]) -> int:
    return min([abs(vert[0]) + abs(vert[1]) for vert in shared_verts])


def manhattan_wires(list0, list1):
    verts0 = get_vertices(list0)
    verts1 = get_vertices(list1)
    overlap = get_overlap(verts0, verts1)
    return min_dist_from_origin(overlap)


def minimal_combined_steps(list0, list1):
    verts0 = get_vertices(list0)
    verts1 = get_vertices(list1)
    overlap = get_overlap(verts0, verts1)
    return min([verts0[vert] + verts1[vert] for vert in overlap])


with open("input.txt", "r") as f:
    text = list(csv.reader(f))
    path0 = text[0]
    path1 = text[1]

print(manhattan_wires(path0, path1))
print(minimal_combined_steps(path0, path1))

# assert (
#     manhattan_wires(
#         ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
#         ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
#     )
#     == 159
# )


# assert (
#     minimal_combined_steps(
#         ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
#         ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
#     )
#     == 610
# )
