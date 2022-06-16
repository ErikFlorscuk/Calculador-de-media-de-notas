import PySimpleGUI as sg

#layout

sg.theme('Reddit')

layout = [

    [sg.Text('Digite nota 1:'), sg.Input(key='nota1')],
    [sg.Text('Digite nota 2:'), sg.Input(key='nota2')], 
    [sg.Text('Digite nota 3:'), sg.Input(key='nota3')],
    [sg.Button('CALCULAR'), sg.Text('', key='mensagem')] 

]

# Janela

window = sg.Window('Calculadora de média', layout = layout)

# Ler eventos

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:  

        break 

    elif event == 'CALCULAR':

        nota1 = float
        nota2 = float
        nota3 = float

        soma = nota1 + nota2 + nota3  



