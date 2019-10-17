for x in range(21):
    print(x)

upper_value = (int(input("What number do you want as the maximum?")))

for a in range(upper_value):
    print(a)

lower_value = (int(input("What number do you want as the minimum?")))

for b in range(lower_value, upper_value):
    print(b)

if upper_value < lower_value:
    print("That doesn't make any sense!")
    for c in range(lower_value, upper_value, -1):
        print(c)
