''' Functions
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope 
'''

print("====DEFINE vs CALL =====")
# build in function > print() type ()
# Function -reusable block of code!
# Instead of block {} in JAvA, Python uses indentation!

# DEFINE - build


def greet(a):
    print(f"how do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


# Call -execute
result1 = greet('Sanchez')
print("result1:", result1)

result2 = greeting("Sam")
print("result2:", result2)
