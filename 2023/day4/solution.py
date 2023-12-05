from collections import defaultdict

input_file_path = "./input.txt"
with open(input_file_path, 'r') as file:
    data = file.read().strip()

lines = data.split('\n')

total_points = 0
occurrences = defaultdict(int)

for i, line in enumerate(lines):
    occurrences[i] += 1

    first_part, last_part = line.split('|')
    card_id, card_numbers_str = first_part.split(':')

    winning_numbers = [int(num) for num in card_numbers_str.split()]
    card_numbers = [int(num) for num in last_part.split()]

    matching_numbers = set(winning_numbers) & set(card_numbers)
    val = len(matching_numbers)
    #Debugging Lines
    # print(f"Winning Numbers: {winning_numbers}")
    # print(f"Card Numbers:    {card_numbers}")

    if val > 0:
        total_points += 2**(val - 1)

    for j in range(val):
        occurrences[i + 1 + j] += occurrences[i]


print(f"Part 1: {total_points}")
print(f"Part 2: {sum(occurrences.values())}")
