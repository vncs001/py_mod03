#! python3
import math


def distance_formula(t1: tuple, t2: tuple) -> float:
    dis: float
    dis = math.sqrt(
        (t1[0] - t2[0])**2 +
        (t1[1] - t2[1])**2 +
        (t1[2] - t2[2])**2)
    return round(dis, 4)


def get_player_pos() -> tuple:
    while True:
        value = input("Enter new coordinates as "
                      "floats in format 'x,y,z': ")
        coordinates = value.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        try:
            result = []
            for coordinate in coordinates:
                result.append(float(coordinate))

            return tuple(result)

        except ValueError as e:
            print(f"Error on parameter '{coordinate}': {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    center: tuple = (0.0, 0.0, 0.0)

    print("Get a first set of coordinates")
    first_pos: tuple = get_player_pos()
    print(f"Got a first tuple: {first_pos}")

    print(f"It includes: X={first_pos[0]}, "
          f"Y={first_pos[1]}, "
          f"Z={first_pos[2]}")
    dc: float = distance_formula(center, first_pos)
    print(f"Distance to center: {dc}\n")

    print("Get a second set of coordinates")
    second_pos: tuple = get_player_pos()
    dc: float = distance_formula(second_pos, first_pos)
    print(f"Distance between the 2 sets of coordinates: {dc}")
