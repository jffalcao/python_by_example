from random import randint

dice_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
total_score = 0

for roll in range(100):
    number_rolled = randint(1,6)
    dice_dict[number_rolled] += 1
    total_score += number_rolled

print('\nTotals: \n' + '=' * 7)
print(dice_dict)

print('\nTotal Score: \n' + '=' * 12)
print(total_score)