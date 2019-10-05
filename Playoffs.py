import Rankings


def create_playoffs(input_text):
    player_list = input_text.split('\n')
    # delete last empty line
    del player_list[-1]

    player1 = player_list[0]
    player2 = player_list[1]
    player3 = player_list[2]
    player4 = player_list[3]

    matches = [(player1, player4), (player2, player3)]

    return matches


def determine_winner(input_text):
    red, black, score_list = Rankings.get_players_and_score(input_text)

    if score_list[0] > score_list[1]:
        return red
    elif score_list[0] < score_list[1]:
        return black
