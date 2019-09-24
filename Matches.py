import itertools as it
from random import shuffle


def create_match_schedule(input_text, half_season, full_season):
    """
    Creates matches from player names and returns a match schedule
    :param input_text: A multi-line string containing player names
    :param half_season: Boolean if half season was chosen
    :param full_season: Boolean if full season was chosen
    :return: A multi-line string containing all matches, a list (matches) of tuples (players)
    """
    # If an option was chosen
    if half_season or full_season:
        player_list = input_text.split('\n')
        # delete last empty line
        del player_list[-1]

        # Get all possible combinations of names (matches)
        matches = create_all_matches(player_list, full_season)

        output_text = matches2str(matches)

        return output_text, matches
    else:
        return


def shuffle_matches(matches):
    """
    Shuffle the given matches
    :param matches: matches to shuffle in the form of a list (matches) of tuples (players)
    :return: multi-line string containing matches, a list (matches) of tuples (players)
    """
    shuffle(matches)
    output_text = matches2str(matches)

    return output_text, matches


def initialise_match(matches):
    """
    Initialise match and convert to output_text
    :param matches:
    :return: multi-line string containing match, a tuple (match), a list (matches) of tuples (players)
    """
    match = matches[0]
    match_formatted_as_matches = [match]

    output_text = matches2str(match_formatted_as_matches)
    output_text = f'Red - Black\n{output_text}0 - 0'

    return output_text, match, matches


def create_all_matches(player_list, full_season):
    """
    Create all combinations of names (matches) either for a half or full season
    :param player_list: A List of player names
    :param full_season: A boolean if a full season should be computed
    :return: A list (matches) of tuples (players)
    """
    matches = list(it.combinations(player_list, 2))

    # If the user chose A full season
    if full_season:
        # Reverse the names in all existing matches such that (tom, bob) becomes (bob, tom)
        new_matches = []
        for match in matches:
            new_match = (match[1], match[0])
            new_matches.append(new_match)
        # And add them to the list of matches
        matches.extend(new_matches)
        print(matches)

    return matches


def matches2str(matches):
    """
    Get matches into a multi-line string
    :param matches: matches to convert
    :return: multi-line string containing matches
    """
    output_text = ''
    for match in matches:
        output_text += f"{match[0]} - {match[1]}\n"

    return output_text
