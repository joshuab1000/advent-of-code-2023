input = open("Day 2\input.txt", "r")

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

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
# Determine which games would've been possible with 12 red, 13 green, 14 blue
for id in all_games:
    sets = all_games[id]
    valid_game = True
    for set in sets:
        if (set['red'] > RED_MAX) or (set['green'] > GREEN_MAX) or (set['blue'] > BLUE_MAX):
            valid_game = False
    # Sum up the IDs of all valid games
    if valid_game == True:
        sum += id
print(sum)