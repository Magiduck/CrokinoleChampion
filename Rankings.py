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

    red, black, score_list = _get_players_and_score(score_text)

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


def update_rankings(rankings_text, score_text):
    """
    Update the rankings based on the score
    :param rankings_text: multiline string to update
    :param score_text: multiline string to get score from
    :return: new updated rankings_text
    """
    rankings_list = rankings_text.split('\n')
    red, black, score_list = _get_players_and_score(score_text)

    if score_list[0] > score_list[1]:
        _update_rankings_list(rankings_list, red)
    elif score_list[0] < score_list[1]:
        _update_rankings_list(rankings_list, black)

    output_text = ''
    for ranking in rankings_list:
        output_text += f'{ranking}\n'

    return output_text


def _get_players_and_score(score_text):
    """
    Get the players and the score from the score_text
    :param score_text: multiline string
    :return: red player name, black player name, score list
    """
    # Red player
    red = score_text.split('\n')[1].split(' - ')[0]
    # Black player
    black = score_text.split('\n')[1].split(' - ')[1]
    # Get scores red - black
    score_list = score_text.split('\n')[2].split(' - ')
    # Convert to int
    score_list = list(map(int, score_list))

    return red, black, score_list


def _update_rankings_list(rankings_list, winner):
    """
    Update the rankings list with new score
    :param rankings_list: list of rankings
    :param winner: player to update score to
    """
    counter = 0
    for ranking in rankings_list:
        if winner in ranking:
            player = ranking.split('\t')[0]
            score = int(ranking.split('\t')[1])
            ranking = f'{player}\t{score + 1}'
            rankings_list[counter] = ranking
        counter += 1
