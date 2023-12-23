# r,g or b cubes

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
# However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; 
# similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. 
# If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

# data structure for input

import os

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'inputs/day_2_Cube_Conundrum.txt')

# lets transform 
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# to [id,(R,G,B),(R,G,B),(R,G,B)] = [1,(4,0,3),(1,2.6),(0,2,0)]
# bag_content = (R,G,B)


# defines the bag content provided to chek against i.e. 12 red cubes, 13 green cubes, and 14 blue cubes
bag_content = (12,13,14)

# logic to calculate sum
# return id if valid, else 0
def possiblity(game,bag_content):
    # game is in format [game_id,(RGB),(RGB),(RGB)]
    # need to get [game_id,Rmax,Gmax,Bmax]
    rmax,gmax,bmax = 0,0,0
    for item in game[1:]:
        if item[0] > rmax:
            rmax = item[0]
        if item[1] > gmax:
            gmax = item[1]
        if item[2] > bmax:
            bmax = item[2]

    is_valid = (rmax <= bag_content[0] and gmax <= bag_content[1] and bmax <= bag_content[2])
    if is_valid:
        return int(game[0])
    else:
        return 0 


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


id_sum = 0
# Open the file in read mode ('r')
with open(input_path, 'r') as file:
    for row in file:
        id_sum += possiblity(extract_game(row),bag_content)


    print(f'final : {id_sum}') 
