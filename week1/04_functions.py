from week1.our_functions import give_me_any_power, give_me_squared_number
from random import random, randint
import turtle

for i in range(10):
    # print(i)
    print(f"Квадрат числа {i} = {i**2}")

my_var = give_me_squared_number(9)
my_other_var = give_me_any_power(9,9)

print(f"my_var = {my_var}")
print(f"my_other_var = {my_other_var}")

give_me_any_power(9,9)
give_me_any_power(11,2)
give_me_any_power(3,9)
give_me_any_power(9,9)
give_me_any_power(9,9)
