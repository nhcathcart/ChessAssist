def get_your_blunders(game_objects_list):
    your_blunders_list = []
    for game in game_objects_list:
        moves = game.moves
        analysis = game.analysis
        if game.color == 'white':
            for i in range(0, len(analysis), 2):
                blunder = None
                if len(analysis[i].keys()) == 4:
                    if analysis[i]['judgment']['name'] == 'Blunder':
                        blunder = i

                if blunder != None:
                    move_list = moves.split()
                    pre_blunder_position = ''
                    for i in range(blunder):
                        pre_blunder_position += move_list[i] + ' '
                    your_blunders_list.append(pre_blunder_position)

        if game.color == 'black':
            for i in range(1, len(analysis), 2):
                blunder = None
                if len(analysis[i].keys()) == 4:
                    if analysis[i]['judgment']['name'] == 'Blunder':
                        blunder = i

                if blunder != None:
                    move_list = moves.split()
                    pre_blunder_position = ''
                    for i in range(blunder):
                        pre_blunder_position += move_list[i] + ' '
                    your_blunders_list.append(pre_blunder_position)

    return your_blunders_list

def get_their_blunders(game_objects_list):
    their_blunders_list = []
    for game in game_objects_list:
        moves = game.moves
        analysis = game.analysis
        if game.color == 'white':
            for i in range(1, len(analysis), 2):
                blunder = None
                if len(analysis[i].keys()) == 4:
                    if analysis[i]['judgment']['name'] == 'Blunder':
                        blunder = i

                if blunder != None:
                    move_list = moves.split()
                    pre_blunder_position = ''
                    for i in range(blunder + 1):
                        pre_blunder_position += move_list[i] + ' '
                    their_blunders_list.append(pre_blunder_position)
        if game.color == 'black':
            for i in range(0, len(analysis), 2):
                blunder = None
                if len(analysis[i].keys()) == 4:
                    if analysis[i]['judgment']['name'] == 'Blunder':
                        blunder = i

                if blunder != None:
                    move_list = moves.split()
                    pre_blunder_position = ''
                    for i in range(blunder + 1):
                        pre_blunder_position += move_list[i] + ' '
                    their_blunders_list.append(pre_blunder_position)
                    
    return their_blunders_list

