import PySimpleGUI as sg
import functions as fct
import time

sg.theme("Topanga")

label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip='Enter a todo',key='Todo')
button1 = sg.Button('Add')

listbox = sg.Listbox(values=fct.read_todos('Todos.txt'),key="Todos",enable_events=True,size=[40,10])
button2 = sg.Button('Edit')
button3 = sg.Button('Complete')
button4 = sg.Button('Exit')



window = sg.Window("Shona's Todo ",layout=[[label],[input_box,button1],[listbox,button2,button3],
                                           [button4]],
                   font=('Helvetica',20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    

    match event:
        case "Add":
            Todos = fct.read_todos('Todos.txt')
            new_todo = values['Todo'] + '\n'
            Todos.append(new_todo)
            fct.write_todos('Todos.txt ',Todos)
            window["Todos"].update(values=Todos)
            
        case 'Edit':
            try :
                Todos_to_edit = values['Todos'][0]
                new_todo = values['Todo']
                
                Todos = fct.read_todos('Todos.txt')
                
                index = Todos.index(Todos_to_edit)
                Todos[index] = new_todo
                            
                fct.write_todos('Todos.txt',Todos)
                window["Todos"].update(values=Todos)
            except IndexError:
                sg.popup("select an item")
                continue
            
        case 'Complete':
            try:
                Todos_to_complete = values['Todos'][0]
                Todos = fct.read_todos("Todos.txt")
                Todos.remove(Todos_to_complete)
                fct.write_todos('Todos.txt',Todos)
                window["Todos"].update(values=Todos)
                window['Todo'].update(value=Todos)
            except IndexError:
                sg.popup("select an item")
                continue
        case 'Exit':
            break
            
        case "Todos" :
            window["Todo"].update(value=values["Todos"][0])
            
            
        case sg.WIN_CLOSED :
            break
window.close()