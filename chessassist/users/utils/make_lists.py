from chessassist.users.utils.make_game_objects_list import make_game_object_list
from chessassist.users.utils.missed_checkmates import make_missed_mate_position_list
from chessassist.users.utils.opening_record import opening_record
from chessassist.users.utils.missed_check_caps import get_missed_check_capture_seqs
from chessassist.users.utils.blunders import get_your_blunders, get_their_blunders

def make_lists(username):
    
    game_objects_list = make_game_object_list(username)

    missed_mates_postions_list = make_missed_mate_position_list(game_objects_list)
    opening_record_list = opening_record(game_objects_list)
    check_caps_list = get_missed_check_capture_seqs(game_objects_list)
    your_blunders = get_your_blunders(game_objects_list)
    their_blunders = get_their_blunders(game_objects_list)

    return missed_mates_postions_list, opening_record_list, check_caps_list, your_blunders, their_blunders