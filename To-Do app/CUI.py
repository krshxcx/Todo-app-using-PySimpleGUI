import functions as fct

while True:
    user_choice = input('enter :')
    user_choice = user_choice.strip()
    
    if user_choice.startswith('add'):
        todo = user_choice[4:]
        Todos = fct.read_todos('Todos.txt')
        Todos.append(todo+'\n')
        fct.write_todos('Todos.txt',Todos)
        
    elif user_choice.startswith('show'):
            Todos = fct.read_todos('Todos.txt')
            
            new_todos = []
            for items in Todos:
                new_items = items.strip('\n')
                new_todos.append(new_items)
            
            for index,items in enumerate(new_todos):
                row = f'{index+1}.{items}'
                print(row)
        
    elif user_choice.startswith('edit'):
        number = user_choice[4:]
        number = int(number)
        Todos = fct.read_todos('Todos.txt')
        
        new = input('enter a new todo:') +'\n'
        
        Todos[number-1] = new
        
        fct.write_todos('Todos.txt',Todos)
    
    elif user_choice.startswith('done'):
        number1 = user_choice[5:]
        number1 = int(number1)    
        Todos = fct.read_todos('Todos.txt') 
        Todos.pop(number1-1)   
        fct.write_todos('Todos.txt',Todos)
    
    elif user_choice.startswith('exit'):
        break
    
    else :
        print('wrong choice try again')


