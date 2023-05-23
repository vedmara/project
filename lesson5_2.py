with open('todo.txt', 'r') as text_file:
    contents = text_file.read()
print(contents)

tex = input('What do you need to do today? ')
with open("todo.txt", "w") as text_file:
    text_file.write(tex)
