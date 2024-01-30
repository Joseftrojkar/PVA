def find_interval_sums(sequence):
    intervals = []
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence) + 1):
            if j - i >= 2:
                interval = sequence[i:j]
                interval_sum = sum(interval)
                intervals.append((i, j - 1, interval_sum))
    return intervals

def find_same_sum_pairs(intervals):
    count = 0
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][2] == intervals[j][2]:
                count += 1
    return count

def main():
    while True:
        try:
            raw_input = input("Zadejte řadu čísel rozdělené mezerou: ")
            if not raw_input.strip():
                raise ValueError("ERROR VOLE: Prázdný vstup. Prosím zadejte vstup s nějakým obsahem.")
            
            sequence = list(map(int, raw_input.split()))

            if len(sequence) > 2000:
                raise ValueError("ERROR VOLE: Řada je delší než 2000 jednotek. Prosím zadejte řadu kratší než 2000.")

            intervals = find_interval_sums(sequence)
            same_sum_pairs_count = find_same_sum_pairs(intervals)

            print("Počet dvojic intervalů se stejným součtem:", same_sum_pairs_count)
            break

        except ValueError as e:
            if "obsahem" in str(e):
                print(e)
            else:
                print("ERROR VOLE: Zadávejte prosím pouze čísla. Zadejte vstup znovu.")

if __name__ == "__main__":
    main()
