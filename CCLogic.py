import itertools as it


def create_matches(input_text, half_season, full_season):
    # If an option was chosen
    if half_season or full_season:
        player_list = input_text.split('\n')
        # delete last empty line
        del player_list[-1]

        matches = create_all_combinations(player_list, full_season)

        output_text = ''

        for match in matches:
            output_text += (f"{match[0]} - {match[1]}\n")

        return output_text
    else:
        return


def create_all_combinations(player_list, full_season):
    matches = list(it.combinations(player_list, 2))

    if full_season:
        print("Full season!")

    return matches
