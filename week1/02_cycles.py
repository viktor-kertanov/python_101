"""
В этом мы модуле, мы познакомимся 
1)с условными операторами;
2) логическими конструкциями; 
3) с функциями;
4) циклами.
"""


# Разберём самый простой цикл
for i in range(0, 13):
    print(i)

for a in range(15):
    print(a**2)

for cube in range(16):
    print(cube**3)

print('---------------------------------')

for kristina in range(65, 77, 2):
    print(f"Happy number: {kristina}")

print('--'*30)

colors = [
    'red',
    'green',
    'blue',
    'yves_klein_bleu',
]

print(f"Our colors are: {colors}")

for fav_color in colors:
    print(f"My favourite color is: {fav_color}")

idxs = [0, 1, 2, 3, 4, 5, 6, 7]
for my_idx in idxs:
    print(f"My current idx: {my_idx}. В квадрате {my_idx**2}")

slice_idxs = idxs[2:5]
print(slice_idxs)

slice_w_step = idxs[1:7:2]
print(slice_w_step)

reverse_idxs = idxs[::-1]
print(reverse_idxs)

for element in reverse_idxs:
    print(element)
print('--'*30)
for bang in range(100):
    ostatok = bang % 4
    if bang % 4 == 0:
        print("BANG!")
    else:
        print("---")

print('---'*15)
for bang in range(100):
    ostatok = bang % 4
    if bang % 4 == 0 and bang % 3 == 0:
        print("BANG! HI-HAT!")
    elif bang % 4 == 0:
        print("BANG")
    elif bang % 3 == 0:
        print("HI-HAT!")
    else:
        print("---")

print("Hello World!")