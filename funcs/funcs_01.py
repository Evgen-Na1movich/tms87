def hello(name: str) -> str:
    return f'Hello, {name}!'


list_names = ['Evgen', 'Helen', 'Maria', 'Valeria', 'Illidan']

for i in list_names:
    print(hello(i))
