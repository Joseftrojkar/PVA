import math
import itertools

def check_combinations(x, y, z, side):
    conditions = [
        x < 20,
        y < 20,
        z < 20,
        x > side - 20,
        y > side - 20,
        z > side - 20
    ]

    for i in range(2, 4):
        for combo in itertools.combinations(conditions, i):
            if all(combo):
                return False

    return True

def validate_point(x, y, z, side):
    if x < 0 or y < 0 or z < 0 or x > side or y > side or z > side or (x or y or z != side or 0):
        print(f"ERROR VOLE: Bod ({x}, {y}, {z}) není na stěně krychle.")
        return False

    if not check_combinations(x, y, z, side):
        print(f"ERROR VOLE: Některé z bodů ({x}, {y}, {z}) jsou blíže než 20 jednotek od hrany krychle.")
        return False

    return True

def get_input_point(point_name):
    while True:
        try:
            point_input = input(f"Zadejte souřadnice {point_name} bodu (x y z): ")
            if not point_input:
                print(f"ERROR VOLE: Neplatné souřadnice {point_name} bodu.")
                continue

            point = list(map(int, point_input.split()))

            if len(point) != 3:
                print(f"ERROR VOLE: Neplatné souřadnice {point_name} bodu. Zadejte všechny tři souřadnice (x y z).")
                continue

            if validate_point(*point, side):
                return point

        except ValueError:
            print(f"ERROR VOLE: Neplatné souřadnice {point_name} bodu.")

while True:
    try:
        side = int(input("Zadejte délku strany místnosti: "))
        if side <= 0:
            print("ERROR VOLE: Délka strany musí být kladné číslo.")
            continue
        break
    except ValueError:
        print("ERROR VOLE: Zadejte prosím platné číslo.")

point1 = get_input_point('prvního')
point2 = get_input_point('druhého')

distances = [abs(a - b) for a, b in zip(point1, point2)]

def distance_to_edge(point, side):
    return [point[0], point[1], side - point[0], side - point[1]]

if side in distances:
    point1 = [i for i in point1 if (i != 0) and (i != side)]
    point2 = [i for i in point2 if (i != 0) and (i != side)]
    point1_to_edges = distance_to_edge(point1, side)
    point2_to_edges = distance_to_edge(point2, side)

    distances_pipes = []
    distances_hose = []

    for i in range(4):
        point1_to_edge = point1_to_edges[i]
        point2_to_edge = point2_to_edges[i]

        dist_between_points = [abs(a - b) for a, b in zip(point1, point2)]

        if i % 2 == 0:
            distances_pipes.append(point1_to_edge + point2_to_edge + side + dist_between_points[1])
            distances_hose.append(((point1_to_edge + point2_to_edge + side)**2 + dist_between_points[1]**2)**0.5)
        else:
            distances_pipes.append(point1_to_edge + point2_to_edge + side + dist_between_points[0])
            distances_hose.append(((point1_to_edge + point2_to_edge + side)**2 + dist_between_points[0]**2)**0.5)

    pipe_length = min(distances_pipes)
    hose_length = min(distances_hose)

else:
    pipe_length = sum(distances)

    axis = [i for i in range(3) if (point1[i] not in [0, side]) and (point2[i] not in [0, side])][0]
    remain = [distances[i] for i in range(3) if i != axis]

    hose_length = (sum(remain)**2 + distances[axis]**2)**0.5

print(f"Délka potrubí je: {pipe_length}")
print(f"Délka hadice je: {hose_length}")
