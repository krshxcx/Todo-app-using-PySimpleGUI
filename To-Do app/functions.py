#function.py ani save chey root folder lo

def read_todos(filepath):
    with open(filepath,'r') as file:
        Todos = file.readlines()
    return Todos

def write_todos(filepath,Todos):
    with open(filepath,'w') as file:
         file.writelines(Todos)