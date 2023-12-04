from collections import defaultdict

file_path = "input.txt"
file = open(file_path).read().strip()

part1 = 0
part2 = 0

for line in file.split('\n'):
    is_possible = True
    game_id, line = line.split(':')
    cube_count = defaultdict(int)
    
    for event in line.split(';'):
        for balls in event.split(','):
            count, color = balls.strip().split()
            count = int(count)
            cube_count[color] = max(cube_count[color], count)
            
            # Check if the number of cubes exceeds predefined limits for part 1
            if int(count) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                is_possible = False
    
    score = 1
    for count in cube_count.values():
        score *= count
    
    part2 += score
    
    if is_possible:
        part1 += int(game_id.split()[-1])

print("Part 1:", part1)
print("Part 2:", part2)
