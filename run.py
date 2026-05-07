# Dunder __builtins__, __init__
message = "PYTHON: everything is object!"
print(message)

result = type(message)
print("result, result")

''' In Python, there are bultin tools:
(1) Types > in float str list dict 
(2) Functions > print() lens() input() type () str() int()
(3) CONSTANTS > Try False None
'''
print(dir(__builtins__))
