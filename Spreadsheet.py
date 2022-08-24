import PySimpleGUI as sg
import csv

headings = ['Name','Address','Phone Number','City']
header = [
    sg.Text('Name', pad=(0, 0), size=(15, 1), justification='c'),
    sg.Text('Address', pad=(0, 0), size=(31, 1), justification='c'),
    sg.Text('Phone Number', pad=(0, 0), size=(31, 1), justification='c'),
    sg.Text('City', pad=(0, 0), size=(15, 1), justification='c'),
]

layout = [header]

for row in range(0,15):
    current_row = [
        sg.Input(size=(15, 1),pad=(0, 0), key=(row, 0)),
        sg.Input(size=(31, 1),pad=(0, 0), key=(row, 1)),
        sg.Input(size=(31, 1),pad=(0, 0), key=(row, 2)),
        sg.Input(size=(15, 1),pad=(0, 0), key=(row, 3)),
    ]
    layout.append(current_row)
    
buttow_row = [sg.Button("Submit"), sg.Button("Generate CSV"), sg.Button("Clear")]
layout.append(buttow_row)

window = sg.Window('Spreadsheet', layout, font='Courier 12')

def generate_csv(headings, values):
    file = open('contacts.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    writer.writerow(headings)


    for row in range(15):
        current_row = []
        for colum in range(4):
            current_row.append(values[row, colum])
        writer.writerow(current_row)

    file.close()

def clear_all(wubdow):
    for row in range(15):
        for colum in range (4):
            window[(row, colum)].update('')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    elif event == 'Submit':
        print(values[0, 0])
    elif event == 'Generate CSV':
        generate_csv(headings, values)
    elif event == 'Clear':
        clear_all(window)