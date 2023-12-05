from collections import defaultdict

input_path = "./input.txt"

with open(input_path, 'r') as file:
    data = file.read().strip()

lines = data.split('\n')
grid = [[cell for cell in line] for line in lines]
num_rows = len(grid)
num_columns = len(grid[0])

part1_sum = 0
part2_sum = 0
numbers_dict = defaultdict(list)

for current_row in range(num_rows):
    adjacent_gears = set()
    current_number = 0
    has_part = False

    for current_column in range(num_columns + 1):
        if current_column < num_columns and grid[current_row][current_column].isdigit():
            current_number = current_number * 10 + int(grid[current_row][current_column])

            for relative_row in [-1, 0, 1]:
                for relative_column in [-1, 0, 1]:
                    neighbor_row = current_row + relative_row
                    neighbor_column = current_column + relative_column

                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_column < num_columns:
                        neighbor_cell = grid[neighbor_row][neighbor_column]

                        if not neighbor_cell.isdigit() and neighbor_cell != '.':
                            has_part = True
                        if neighbor_cell == '*':
                            adjacent_gears.add((neighbor_row, neighbor_column))
        elif current_number > 0:
            for gear_position in adjacent_gears:
                numbers_dict[gear_position].append(current_number)

            if has_part:
                part1_sum += current_number

            current_number = 0
            has_part = False
            adjacent_gears = set()

for gear_position, values in numbers_dict.items():
    if len(values) == 2:
        part2_sum += values[0] * values[1]

print(f"Part 1: {part1_sum}")
print(f"Part 2: {part2_sum}")