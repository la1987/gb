a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print("15 * 3", ", "  "15 / 3", ", " "15 // 2", ", " "15 ** 2")
print(type(a))
print(type(b))
print(type(c))
print(type(d))

expression_list = ["(15 * 3)", "(15 / 3)", "(15 // 2)", "(15 ** 2)"]
for x in expression_list:
    print(f"{x} is {type(eval(x))}")
