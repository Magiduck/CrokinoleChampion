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
    """
    Update the score based on who won
    :param score_text: the text of the current score
    :param who_won: a String of who won this round
    :return: output_text for the score
    """
    # Red player
    red = score_text.split('\n')[1].split(' - ')[0]
    # Black player
    black = score_text.split('\n')[1].split(' - ')[1]
    # Get scores red - black
    score_list = score_text.split('\n')[2].split(' - ')
    # Convert to int
    score_list = list(map(int, score_list))

    # Add scores based on Crokinole rules
    if who_won == 'RED':
        score_list[0] = score_list[0] + 2
    elif who_won == 'DRAW':
        score_list[0] = score_list[0] + 1
        score_list[1] = score_list[1] + 1
    elif who_won == 'BLACK':
        score_list[1] = score_list[1] + 2

    # Format the text to original layout
    output_text = f'Red - Black\n{red} - {black}\n{score_list[0]} - {score_list[1]}'

    return output_text
