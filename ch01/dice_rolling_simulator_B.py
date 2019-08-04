from random import randint

counter = 1
while True:
    random_number = randint(1,6)
    print("Roll: ", counter, "Value: ", random_number)
    if random_number == 1:
        break
    counter += 1