print("======numbers=====")
# in JAVA, variable is name storage loaction!
# in Python, variables is named reference!


count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")


result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("======string=====")
# METHODS: upper() loewr() title() find() replace()

course = "AI Python Fullstack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

result = course.upper()
print(f"the result (3): {result}")

result = course.replace("Fullstack", "Masterclass")
print(f"the result (4): {result}")

print("======boolean=====")
# functions > type() input() bool() int() str()
y = input("Givr your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")


# TRUTHY vs FALSY value
# TRUTHY: True 100 -100 "MIT"
# FALSY: False 0 "" None

test_falsy = "" or False or None or 0
print("test_falsy:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
