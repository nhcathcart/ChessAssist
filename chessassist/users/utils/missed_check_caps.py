def get_missed_check_capture_seqs(game_object_list):    
    missed_check_capture_positions = []
    for game in game_object_list:
        moves_list = (game.moves).split()
        analysis = game.analysis
        missed_check_capture = None
        if game.color == 'white':    
                for i in range(0, len(analysis), 2):
                    missed_check_capture = None
                    if len(analysis[i].keys()) == 4:
                        if analysis[i]['judgment']['name'] == 'Blunder':
                            variation_list = analysis[i]['variation'].split()
                            if len(variation_list) >= 3:
                                if variation_list[0][-1] == '+' and variation_list[2][1] == 'x':
                                    missed_check_capture = i

                    missed_check_capture_position = ''
                    if missed_check_capture != None:
                        for i in range(missed_check_capture):
                            missed_check_capture_position += moves_list[i] + ' '
                    if missed_check_capture_position != '':
                        missed_check_capture_positions.append(missed_check_capture_position)
                        
        else:
            for i in range(1, len(analysis), 2):
                    missed_check_capture = None
                    if len(analysis[i].keys()) == 4:
                        if analysis[i]['judgment']['name'] == 'Blunder':
                            variation_list = analysis[i]['variation'].split()
                            if len(variation_list) >= 3:
                                if variation_list[0][-1] == '+' and variation_list[2][1] == 'x':
                                    missed_check_capture = i

                    missed_check_capture_position = ''
                    if missed_check_capture != None:
                        for i in range(missed_check_capture):
                            missed_check_capture_position += moves_list[i] + ' '
                    if missed_check_capture_position != '':
                        missed_check_capture_positions.append(missed_check_capture_position)
                        

    return missed_check_capture_positions