from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 10

def check_congruence(p1, p2, p3):
    if p1 == p2 and p2 == p3:
        return True
    return False

def check_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    determinant = Decimal(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return determinant == 0

def find_middle_point(p1, p2, p3):
    sorted_points = sorted([(p1, 'A'), (p2, 'B'), (p3, 'C')])
    return sorted_points[1][1]

def get_coordinates(label):
    while True:
        try:
            x, y = map(Decimal, input(f"Zadejte souřadnice bodu {label} (x y): ").split())
            return x, y
        except InvalidOperation:
            print("ERROR VOLE: Neplatný input, vložte pouze číselné hodnoty.")

def main():
    try:
        x1, y1 = get_coordinates('A')
        x2, y2 = get_coordinates('B')
        x3, y3 = get_coordinates('C')
    except KeyboardInterrupt:
        print("Program uknočen.")
        return

    points = [(x1, y1), (x2, y2), (x3, y3)]

    if points[0] == points[1] and points[1] == points[2]:
        print("Všechny 3 body se překrývají.")
    elif points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
        overlapping_points = [label for label, point in zip(['A', 'B', 'C'], points) if points.count(point) > 1]
        print(f"Bod {overlapping_points[0]} a bod {overlapping_points[1]} se překrývají.")
    elif check_collinear(points[0], points[1], points[2]):
        print("Žádné z bodů se nepřekrývají a leží na stejné přímce.")
        middle_point = find_middle_point(points[0], points[1], points[2])
        print(f"Prostředním bodem je {middle_point}.")
    else:
        print("Žádné z bodů se nepřekrývají a neleží na stejné přímce.")

if __name__ == "__main__":
    main()
