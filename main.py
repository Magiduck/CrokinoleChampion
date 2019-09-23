import PySimpleGUI as sg
import CCLogic

sg.change_look_and_feel('Reddit')

layout = [[sg.Multiline(size=(20, 20), key='_CONTESTANTSIN_'),
           sg.Multiline(size=(20, 20), disabled=True, key='_CONTESTANTSOUT_')],
          [sg.Radio('Half-season', 'season', key='_HALFSEASON_'), sg.Radio('Full-season', 'season', key='_FULLSEASON_'), sg.Button('Create matches', key='_CREATEMATCHES_')],
          [sg.Button('Shuffle', key='_SHUFFLE_')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('CrokinoleChampion', layout)


while True:  # Event Loop
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    # If the user has clicked on 'create matches'
    if event == '_CREATEMATCHES_':
        # Get the matches
        matches = CCLogic.create_match_schedule(values['_CONTESTANTSIN_'], values['_HALFSEASON_'], values['_FULLSEASON_'])
        # Update the multiline text output with the matches
        window['_CONTESTANTSOUT_'].Update(matches)



window.Close()
