""" Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
"""


import turtle
print("==== Python Packages & COre Package =====")
''' Python Pakcages/Modules: Core, File and External '''
# Core Package> https://docs.python.org/3/library


# Core package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)
# turtle.done()


my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with
with open("material/nessage.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")
