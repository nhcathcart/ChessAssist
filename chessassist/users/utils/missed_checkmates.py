
def make_missed_mate_position_list(game_object_list):
    
    missed_mate_position_list = []
    for game in game_object_list:
        analysis = game.analysis
        moves_list = (game.moves).split()
        missed_mate = None
        if game.color == 'white':    
            for i in range(0, len(analysis), 2):
                if len(analysis[i].keys()) == 4:
                    if analysis[i]['judgment']['comment'][0:11] == 'Lost forced':
                        missed_mate = i 
            missed_mate_position = ''
            if missed_mate != None:
                for i in range(missed_mate):
                    missed_mate_position += moves_list[i] + ' '
            if missed_mate_position != '':
                missed_mate_position_list.append(missed_mate_position)
        else:
            for i in range(1, len(analysis), 2):
                if len(analysis[i].keys()) == 4:
                    if analysis[i]['judgment']['comment'][0:11] == 'Lost forced':
                        missed_mate = i 
            missed_mate_position = ''
            if missed_mate != None:
                for i in range(missed_mate):
                    missed_mate_position += moves_list[i] + ' '
            if missed_mate_position != '':
                missed_mate_position_list.append(missed_mate_position)
    
    return missed_mate_position_list