import PySimpleGUI as sg
import Matches

sg.change_look_and_feel('Reddit')

column_schedule = [[sg.Radio('Half-season', 'season', key='_HALFSEASON_')],
                   [sg.Radio('Full-season', 'season', key='_FULLSEASON_')],
                   [sg.Button('Create matches', key='_CREATEMATCHES_')],
                   [sg.Button('Shuffle', key='_SHUFFLE_')],
                   [sg.Button('Play season!', key='_PLAYSEASON_')]]

layout = [[sg.Text('Input players\t\tSchedule')],
          [sg.Multiline(size=(22, 20), key='_CONTESTANTSIN_'),
           sg.Multiline(size=(22, 20), disabled=True, key='_CONTESTANTSOUT_'), sg.Column(column_schedule)],
          [sg.Text('Red - Black\n 0 - 0', font='Consolas 48', size=(16, 3), key='_SCORE_')],
          [sg.Button('Red won'), sg.Button('Draw'), sg.Button('Black won')],
          [sg.Button('Finish', key='_FINISH_'), sg.Button('Undo')],
          [sg.Multiline(size=(22, 20), disabled=True, key='_RANKINGS_')],
          [sg.Button('Exit')]]

window = sg.Window('CrokinoleChampion', layout)
matches = []

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

    elif event == '_SHUFFLE_':
        # Shuffle the matches
        output_text, matches = Matches.shuffle_matches(matches)
        # Update the multiline text output with the matches
        window['_CONTESTANTSOUT_'].Update(output_text)

    elif event == '_PLAYSEASON_':
        # Get first match
        output_text_score, match, matches = Matches.initialise_match(matches)
        # Update the score text
        window['_SCORE_'].Update(output_text_score)

        # Get the initial rankings
        initial_rankings = Matches.initialise_rankings(values['_CONTESTANTSIN_'])
        # Update the multiline text output with the rankings
        window['_RANKINGS_'].Update(initial_rankings)

    elif event == '_FINISH_':
        # Remove last match
        output_text, matches = Matches.remove_last_match(matches)
        # Update the multiline text output with the matches
        window['_CONTESTANTSOUT_'].Update(output_text)

        # Get next match
        output_text_score, match, matches = Matches.initialise_match(matches)
        # Update the score text
        window['_SCORE_'].Update(output_text_score)

window.Close()
