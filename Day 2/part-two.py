input = open("Day 2\input.txt", "r")

all_games = {}

# Parse out each game and put them in a big dictionary

# Example format:
# {1: 
# [{'blue': '3','red': '4'},
# {'red': '1', 'green': '2', 'blue': '6'},
# {'green': '2'}]
# }

for line in input:
    game = line.split(': ')
    game_id = int((game[0].split(' '))[1])
    game_sets = game[1].split('; ')
    all_sets = []
    for set in game_sets:
        cube_pairs = set.split(', ')
        curr_set = {}
        present_colors = []
        for pair in cube_pairs:
            pair = pair.split(' ')
            color = pair[1].strip('\n')
            curr_set[color] = int(pair[0])
            present_colors.append(color)
        # If any colors aren't included, add them to set with value 0
        if 'red' not in present_colors:
            curr_set['red'] = 0
        if 'green' not in present_colors:
            curr_set['green'] = 0
        if 'blue' not in present_colors:
            curr_set['blue'] = 0
        all_sets.append(curr_set)
    all_games[game_id] = all_sets

sum = 0
# Find the least number of each color you'd need to play each game
for id in all_games:
    sets = all_games[id]
    valid_game = True
    red_max = 0
    green_max = 0
    blue_max = 0
    for set in sets:
        if (set['red'] > red_max):
            red_max = set['red']
        if (set['green'] > green_max):
            green_max = set['green']
        if (set['blue'] > blue_max):
            blue_max = set['blue']
    # Multiply all the maxes to get the "power"
    power = red_max * green_max * blue_max
    # Sum all the powers
    sum += power
print(sum)