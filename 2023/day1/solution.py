input_path = "./input.txt"

cases = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

with open(input_path, 'r') as file:
    content = file.read()

    lines = open(input_path).read().splitlines()

def find_first_and_last_numbers():
    total_sum = 0
    for line in lines:
        numbers = []

        for key in cases.keys():
            index = 0
            while index != -1:
                index = line.lower().find(key, index)
                if index != -1:
                    numbers.append((index, cases[key]))
                    index += 1

        # Sort the numbers based on their positions
        numbers.sort(key=lambda x: x[0])

        first_number = numbers[0][1] if numbers else None
        last_number = numbers[-1][1] if numbers else None

        # Combine and convert to integers
        if first_number is not None and last_number is not None:
            combined_number = int(str(first_number) + str(last_number))

            # Debugging Line to check combined numbers
            # print(f"Line: {line}, Combined Number: {combined_number}")

            total_sum += combined_number
        else:
            print(f"Error: Could not find both first and last numbers for line - {line}")

    return total_sum

total_sum = find_first_and_last_numbers()

print(f"Total Sum: {total_sum}")


