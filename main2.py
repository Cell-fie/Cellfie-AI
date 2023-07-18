import PySimpleGUI as sg

layout = [[sg.Text("Hello")], [sg.Button("Ok")]]

window = sg.Window("Demo", layout, margins=(100,50))

while True:
    event, values = window.read()
    if event == "Ok" or event == sg.WIN_CLOSED:
        break
window.close()