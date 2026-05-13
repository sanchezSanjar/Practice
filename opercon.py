''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("==== Operators ======")
# + - > >= < <= == is * /   // % += -= **

a = 19
b = 5

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("="*5)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)

e = c


print("c==d", c == d)  # only value
print(id(c), id(d))


print("c is d", c is d)
print("c is e", c is e)


print("==== Condition ======")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("==== Logical Operators ======")


age = 21

# person = None
# if age > 16:
#     person = "adult"
# else:
#     person = "minor"


# Ternary
person = "adult" if age > 18 else "minor"
print("person:", person)


print("-----")


is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, do you want to be students!")
elif is_admin:
    print("Please go to this office!")
elif is_guest or is_parent:
    print("waiting room is over there!")
else:
    print("Other cases")
