def initialise_rankings(input_text):
    """
    Initialises the rankings with each player and a score of 0
    :param input_text: A multi-line string containing player names
    :return: A multi-line string containing all rankings
    """
    player_list = input_text.split('\n')
    # delete last empty line
    del player_list[-1]

    output_text = ''
    for player in player_list:
        output_text += f'{player}\t0\n'

    return output_text


def update_score(score_text, who_won):
    red = score_text.split('\n')[1].split(' - ')[0]
    black = score_text.split('\n')[1].split(' - ')[1]
    score_list = score_text.split('\n')[2].split(' - ')
    score_list = list(map(int, score_list))

    if who_won == 'RED':
        score_list[0] = score_list[0] + 2
    elif who_won == 'DRAW':
        score_list[0] = score_list[0] + 1
        score_list[1] = score_list[1] + 1
    elif who_won == 'BLACK':
        score_list[1] = score_list[1] + 2

    output_text = f'Red - Black\n{red} - {black}\n{score_list[0]} - {score_list[1]}'

    return output_text
