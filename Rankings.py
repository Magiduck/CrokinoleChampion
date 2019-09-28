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