import PySimpleGUI as sg

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_')],
          [sg.Input(key='_IN_')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window.Element('_OUTPUT_').Update(values['_IN_'])

window.Close()
