# fewest number of cubes of each color that could have been in the bag to make the game possible?

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# # Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
# The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. 
# Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?


import os

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'inputs/day_2_Cube_Conundrum.txt')




def power(game):
    # game is in format [game_id,(RGB),(RGB),(RGB)]
    # find the min 
    rmax,gmax,bmax = 0,0,0
    for item in game[1:]:
        if item[0] > rmax:
            rmax = item[0]
        if item[1] > gmax:
            gmax = item[1]
        if item[2] > bmax:
            bmax = item[2]
    power = int(rmax*gmax*bmax)
    return power

def extract_game(row):
    row = row.strip()
    game = []
    game_id = row.split(':')[0].split(' ')[1]
    game.append(game_id)
    picks = row.split(':')[1].split(';')
    for pick in picks:
        red,green,blue = 0,0,0
        for item in pick.strip().split(','):
            if 'red' in item:
                red= int(item.strip().split(' ')[0])
            if 'blue' in item:
                blue = int(item.strip().split(' ')[0])
            if 'green' in item:
                green = int(item.strip().split(' ')[0])
        
        game.append((red,green,blue))
    return game


power_sum = 0
# Open the file in read mode ('r')
with open(input_path, 'r') as file:
    for row in file:
        power_sum += power(extract_game(row))


    print(f'final : {power_sum}') 
