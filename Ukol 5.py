import os
import math

def parse_input(line):
    try:
        coords, name = line.strip().split(":")
        x, y = map(float, coords.split(","))
        return (x, y, name.strip())
    except ValueError:
        return None

def calculate_distance(plane1, plane2):
    x1, y1, _ = plane1
    x2, y2, _ = plane2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def compare_outputs(expected_output, actual_output):
    with open(expected_output, 'r') as f:
        expected_lines = [set(line.strip().split(' - ')) for line in f]
    with open(actual_output, 'r') as f:
        actual_lines = [set(line.strip().split(' - ')) for line in f]

    # Sort the lines in both files
    expected_lines.sort()
    actual_lines.sort()

    # Compare the sorted lines
    if expected_lines != actual_lines:
        return False, "Mismatch found"

    return True, None

def write_output(output_file, min_distance, closest_pairs):
    with open(output_file, 'w') as f:
        f.write("Plane coordinates:\n")
        f.write(f"Minimum airplane distance: {min_distance:.6f}\n")
        f.write(f"Pairs found: {len(closest_pairs)}\n")
        for pair in closest_pairs:
            f.write(f"{pair[0]} - {pair[1]}\n")

def main():
    print("Vítejte v programu pro obsluhu řídící věže!")
    print("Tento program projde input soubory, vypočítá je a srovná výsledek s output soubory.")
    print("Každý input soubor musí mít korespondující output soubor, jinak ho program nebude brát vpotaz.")
    print("Názvy input souborů by měli mít formát: 0000_in.txt, 0001_in.txt, atd.")
    print("Korsepondující názvy output souborů by měli mít formát: 0000_out.txt, 0001_out.txt, atd.")
    print("Správně formátované input a output soubory pro referenci můžete nalézt na: https://drive.google.com/file/d/1ClRR77iyfDx9Pm5ob9pMjhxGeZiChXG3/view")
    print("Jdeme na to...\n")

    directory = input(r"Zadejte lokaci složky s input a output soubory (např. C:\Users\pepa\Downloads\Uloha5\CZE): ")

    if not os.path.isdir(directory):
        print("Neplatná lokace.")
        return

    for filename in os.listdir(directory):
        if filename.endswith("_in.txt"):
            input_file = os.path.join(directory, filename)
            expected_output_file = os.path.join(directory, filename.replace("_in.txt", "_out.txt"))
            actual_output_file = os.path.join(directory, filename.replace("_in.txt", "_program_out.txt"))
            if not os.path.exists(expected_output_file):
                continue

            # Process input file
            airplanes = []
            with open(input_file, 'r') as f:
                for line in f:
                    plane = parse_input(line)
                    if plane:
                        airplanes.append(plane)
                    else:
                        print(f"Neplatný input formát v souboru: {input_file}")
                        break
                else:
                    if len(airplanes) < 2:
                        print(f"Neplatný input formát v souboru: {input_file}")
                        continue

                    # Calculate closest pairs
                    min_distance = float('inf')
                    closest_pairs = []
                    for i in range(len(airplanes)):
                        for j in range(i+1, len(airplanes)):
                            distance = calculate_distance(airplanes[i], airplanes[j])
                            if distance < min_distance:
                                min_distance = distance
                                closest_pairs = [(airplanes[i][2], airplanes[j][2])]
                            elif distance == min_distance:
                                closest_pairs.append((airplanes[i][2], airplanes[j][2]))

                    # Write actual output to file
                    write_output(actual_output_file, min_distance, closest_pairs)

                    # Compare with expected output
                    success, error = compare_outputs(expected_output_file, actual_output_file)
                    if success:
                        print(f"Test úspěšný: {input_file}")
                    else:
                        print(f"Test neúspěšný: {input_file}")
                        print(f"ERROR VOLE: {error}")

if __name__ == "__main__":
    main()
