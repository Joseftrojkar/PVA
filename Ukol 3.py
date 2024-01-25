def is_palindrome(s):
    return s == s[::-1]

def find_next_palindrome(number, base):
    while True:
        number += 1
        converted_number = format(number, f'0{base}b') if base == 2 else str(number)
        
        if is_palindrome(converted_number):
            return number

def main():
    try:
        number = int(input("Zadejte číslo: "))
        base = int(input("Zadejte číselnou soustavu. 2 pro binární soustavu, 10 pro decimální: "))
        
        if number < 0 or base < 2:
            print("Prosím zadjte pozitivní číslo se základem vyšším než 2.")
            return

        next_palindrome = find_next_palindrome(number, base)
        
        print(f"Nejbližší vyšší palindromické číslo v soustavě: {base} je: {next_palindrome}")

    except ValueError:
        print("Neplatný input. Prosím zadávejte pouze čísla.")

if __name__ == "__main__":
    main()
