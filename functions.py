''' Functions
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope 
'''

print("====DEFINE(parametr) vs CALL(argument) =====")
# build in function > print() type ()
# Function -reusable block of code!
# Instead of block {} in JAvA, Python uses indentation!

# DEFINE - build - parametr


def greet(a):
    print(f"how do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


# Call -execute - argument
result1 = greet('Sanchez')
print("result1:", result1)

result2 = greeting("Sam")
print("result2:", result2)


print("====Keyword & default arguments =====")
# DEFINE


def give_greet(name, age=22):
    print("give_great is executed")
    return f"hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("john")
print("result4:", result4)
