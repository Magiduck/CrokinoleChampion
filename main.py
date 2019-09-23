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
    if event == '_CREATEMATCHES_':
        matches = CCLogic.create_matches(values['_CONTESTANTSIN_'], values['_HALFSEASON_'], values['_FULLSEASON_'])
        # change the "output" element to be the value of "input" element
        window['_CONTESTANTSOUT_'].Update(matches)



window.Close()
