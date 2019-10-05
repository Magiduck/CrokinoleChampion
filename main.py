import PySimpleGUI as sg
import Matches
import Rankings
import Playoffs

sg.change_look_and_feel('Reddit')

column_schedule = [[sg.Radio('Half-season', 'season', key='_HALFSEASON_')],
                   [sg.Radio('Full-season', 'season', key='_FULLSEASON_')],
                   [sg.Button('Create matches', key='_CREATEMATCHES_')],
                   [sg.Button('Shuffle', key='_SHUFFLE_')],
                   [sg.Button('Play season!', key='_PLAYSEASON_')]]

layout = [[sg.Text('Input players\t\t\t\t  Schedule              ', key='_MENUTEXT_')],
          [sg.Multiline(size=(22, 10), font='Consolas 18', key='_CONTESTANTSIN_'),
           sg.Multiline(size=(22, 10), font='Consolas 18', disabled=True, key='_CONTESTANTSOUT_'), sg.Column(column_schedule)],
          [sg.Text('Red - Black\n 0 - 0', font='Consolas 48', size=(16, 3), key='_SCORE_')],
          [sg.Button('Red won', key='_RED_'), sg.Button('Draw', key='_DRAW_'), sg.Button('Black won', key='_BLACK_')],
          [sg.Button('Finish', key='_FINISH_'), sg.Button('Undo', key='_UNDO_')],
          [sg.Text('Rankings:')],
          [sg.Multiline(size=(22, 10), disabled=True, font='Consolas 18', key='_RANKINGS_')],
          [sg.Button('Exit')]]

window = sg.Window('CrokinoleChampion', layout)
matches = []
prev_score_text = ''
score_text = ''
rankings_text = ''

win2_active = False
matches_created = False
season_active = False

while True:  # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    # If the user has clicked on 'create matches'
    if event == '_CREATEMATCHES_':
        if values['_HALFSEASON_'] or values['_FULLSEASON_']:
            matches_created = True
            # Get the matches
            output_text, matches = Matches.create_match_schedule(values['_CONTESTANTSIN_'], values['_HALFSEASON_'], values['_FULLSEASON_'])
            # Update the multiline text output with the matches
            window['_CONTESTANTSOUT_'].Update(output_text)
            # Update the menu with the amount of matches
            window['_MENUTEXT_'].Update(f'Input players\t\t\t\t  Schedule ({len(matches)} matches)')

    elif event == '_SHUFFLE_' and matches_created:
        # Shuffle the matches
        output_text, matches = Matches.shuffle_matches(matches)
        # Update the multiline text output with the matches
        window['_CONTESTANTSOUT_'].Update(output_text)

    elif event == '_PLAYSEASON_' and matches_created:
        season_active = True
        # Get first match
        score_text, match, matches = Matches.initialise_match(matches)
        # Update the score text
        window['_SCORE_'].Update(score_text)

        # Get the initial rankings
        initial_rankings = Rankings.initialise_rankings(values['_CONTESTANTSIN_'])
        rankings_text = initial_rankings
        # Update the multiline text output with the rankings
        window['_RANKINGS_'].Update(initial_rankings)

    elif event == '_RED_' and season_active:
        # To be able to undo
        prev_score_text = score_text

        # Update score text (add 2 to red player)
        score_text = Rankings.update_score(score_text, 'RED')
        window['_SCORE_'].Update(score_text)

    elif event == '_DRAW_' and season_active:
        # To be able to undo
        prev_score_text = score_text

        # Update score text (add 1 to both players)
        score_text = Rankings.update_score(score_text, 'DRAW')
        window['_SCORE_'].Update(score_text)

    elif event == '_BLACK_' and season_active:
        # To be able to undo
        prev_score_text = score_text

        # Update score text (add 2 to black player)
        score_text = Rankings.update_score(score_text, 'BLACK')
        window['_SCORE_'].Update(score_text)

    elif event == '_FINISH_' and season_active:
        rankings_text = Rankings.update_rankings(rankings_text, score_text)
        # Update the multiline text output with the rankings
        window['_RANKINGS_'].Update(rankings_text)

        # If it is not the last match
        if len(matches) != 1:
            # Remove last match
            output_text, matches = Matches.remove_last_match(matches)
            # Update the multiline text output with the matches
            window['_CONTESTANTSOUT_'].Update(output_text)

            # Get next match
            score_text, match, matches = Matches.initialise_match(matches)
            # Update the score text
            window['_SCORE_'].Update(score_text)

        elif len(matches) == 1 and not win2_active:
            win2_active = True
            window.Hide()
            layout2 = [[sg.Text('Rankings\t\t\t\t'), sg.Text('Input the four Finalists in order')],
                       [sg.Multiline(rankings_text, size=(22, 10), disabled=True, font='Consolas 18', key='_RANKINGS2_'),
                        sg.Multiline(size=(22, 10), font='Consolas 18', key='_CONTESTANTSIN2_'),
                        sg.Button('Start playoffs', key='_PLAYOFFS_')],
                       [sg.Text('Red - Black\n 0 - 0', font='Consolas 48', size=(16, 3), key='_SCORE2_')],
                       [sg.Button('Red won', key='_RED2_'), sg.Button('Draw', key='_DRAW2_'),
                        sg.Button('Black won', key='_BLACK2_')],
                       [sg.Button('Finish', key='_FINISH2_'), sg.Button('Undo', key='_UNDO2_')],
                       [sg.Button('Exit')]]

            win2 = sg.Window('Playoffs', layout2)

            matches_playoffs = []
            prev_score_text_playoffs = ''
            score_text_playoffs = ''
            rankings_text_playoffs = ''
            match_counter = 0
            winner1 = ''
            winner2 = ''

            playoffs_active = False

            while True:
                event2, values2 = win2.Read()
                if event2 in (None, 'Exit'):
                    win2.Close()
                    win2_active = False
                    window.UnHide()
                    break

                if event2 == '_PLAYOFFS_':
                    playoffs_active = True
                    # Get the matches
                    matches_playoffs = Playoffs.create_playoffs(values2['_CONTESTANTSIN2_'])
                    # Update score for first match
                    score_text_playoffs, match_playoffs, matches_playoffs = Matches.initialise_match(matches_playoffs)

                    # Update the score text
                    win2['_SCORE2_'].Update(score_text_playoffs)

                elif event2 == '_RED2_' and playoffs_active:
                    # To be able to undo
                    prev_score_text_playoffs = score_text_playoffs

                    # Update score text (add 2 to red player)
                    score_text_playoffs = Rankings.update_score(score_text_playoffs, 'RED')
                    win2['_SCORE2_'].Update(score_text_playoffs)

                elif event2 == '_DRAW2_' and playoffs_active:
                    # To be able to undo
                    prev_score_text_playoffs = score_text_playoffs

                    # Update score text (add 1 to both players)
                    score_text_playoffs = Rankings.update_score(score_text_playoffs, 'DRAW')
                    win2['_SCORE2_'].Update(score_text_playoffs)

                elif event2 == '_BLACK2_' and playoffs_active:
                    # To be able to undo
                    prev_score_text_playoffs = score_text_playoffs

                    # Update score text (add 2 to black player)
                    score_text_playoffs = Rankings.update_score(score_text_playoffs, 'BLACK')
                    win2['_SCORE2_'].Update(score_text_playoffs)

                elif event2 == '_FINISH2_' and playoffs_active:
                    if match_counter == 0:
                        match_counter += 1
                        winner1 = Playoffs.determine_winner(score_text_playoffs)

                        # Remove last match
                        matches_playoffs.pop(0)
                        # Update score for first match
                        score_text_playoffs, match_playoffs, matches_playoffs = Matches.initialise_match(
                            matches_playoffs)

                    elif match_counter == 1:
                        match_counter += 1
                        winner2 = Playoffs.determine_winner(score_text_playoffs)

                        matches_playoffs.clear()
                        matches_playoffs = [(winner1, winner2)]
                        score_text_playoffs, matches_playoffs, matches_playoffs = Matches.initialise_match(
                            matches_playoffs)

                    elif match_counter == 2:
                        match_counter += 1
                        champion = Playoffs.determine_winner(score_text_playoffs)
                        sg.Popup(f'Your winner is {champion}!', font='Consolas 48')

                    # Update the score text
                    win2['_SCORE2_'].Update(score_text_playoffs)

                elif event2 == '_UNDO2_' and playoffs_active:
                    print('test')
                    score_text_playoffs = prev_score_text_playoffs
                    win2['_SCORE2_'].Update(score_text_playoffs)

    elif event == '_UNDO_' and season_active:
        score_text = prev_score_text
        window['_SCORE_'].Update(score_text)

window.Close()
