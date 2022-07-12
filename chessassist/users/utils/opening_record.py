from chessassist.users.utils.make_game_objects_list import make_game_object_list

def opening_record(game_objects_list):
    
    opening_dict = {}
    for game in game_objects_list:
        if game.opening not in opening_dict:
            if game.win == 'win':
                opening_dict[game.opening] = [1, 0, 0]
            elif game.win == 'draw':
                opening_dict[game.opening] = [0, 1, 0]
            else:
                opening_dict[game.opening] = [0, 0, 1]
        else:
            if game.win == 'win':
                opening_dict[game.opening][0] += 1
            elif game.win == 'draw':
                opening_dict[game.opening][1] += 1
            else:
                opening_dict[game.opening][2] += 1

    return opening_dict
