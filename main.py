import PySimpleGUI as sg
import Matches
import Rankings

sg.change_look_and_feel('Reddit')

column_schedule = [[sg.Radio('Half-season', 'season', key='_HALFSEASON_')],
                   [sg.Radio('Full-season', 'season', key='_FULLSEASON_')],
                   [sg.Button('Create matches', key='_CREATEMATCHES_')],
                   [sg.Button('Shuffle', key='_SHUFFLE_')],
                   [sg.Button('Play season!', key='_PLAYSEASON_')]]

layout = [[sg.Text('Input players\t\tSchedule              ', key='_MENUTEXT_')],
          [sg.Multiline(size=(22, 20), key='_CONTESTANTSIN_'),
           sg.Multiline(size=(22, 20), disabled=True, key='_CONTESTANTSOUT_'), sg.Column(column_schedule)],
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

while True:  # Event Loop
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break

    # If the user has clicked on 'create matches'
    if event == '_CREATEMATCHES_':
        # Get the matches
        output_text, matches = Matches.create_match_schedule(values['_CONTESTANTSIN_'], values['_HALFSEASON_'], values['_FULLSEASON_'])
        # Update the multiline text output with the matches
        window['_CONTESTANTSOUT_'].Update(output_text)
        # Update the menu with the amount of matches
        window['_MENUTEXT_'].Update(f'Input players\t\tSchedule ({len(matches)} matches)')

    elif event == '_SHUFFLE_':
        # Shuffle the matches
        output_text, matches = Matches.shuffle_matches(matches)
        # Update the multiline text output with the matches
        window['_CONTESTANTSOUT_'].Update(output_text)

    elif event == '_PLAYSEASON_':
        # Get first match
        score_text, match, matches = Matches.initialise_match(matches)
        # Update the score text
        window['_SCORE_'].Update(score_text)

        # Get the initial rankings
        initial_rankings = Rankings.initialise_rankings(values['_CONTESTANTSIN_'])
        rankings_text = initial_rankings
        # Update the multiline text output with the rankings
        window['_RANKINGS_'].Update(initial_rankings)

    elif event == '_RED_':
        # To be able to undo
        prev_score_text = score_text

        # Update score text (add 2 to red player)
        score_text = Rankings.update_score(score_text, 'RED')
        window['_SCORE_'].Update(score_text)

    elif event == '_DRAW_':
        # To be able to undo
        prev_score_text = score_text

        # Update score text (add 1 to both players)
        score_text = Rankings.update_score(score_text, 'DRAW')
        window['_SCORE_'].Update(score_text)

    elif event == '_BLACK_':
        # To be able to undo
        prev_score_text = score_text

        # Update score text (add 2 to black player)
        score_text = Rankings.update_score(score_text, 'BLACK')
        window['_SCORE_'].Update(score_text)

    elif event == '_FINISH_':
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

    elif event == '_UNDO_':
        score_text = prev_score_text
        window['_SCORE_'].Update(score_text)

window.Close()
