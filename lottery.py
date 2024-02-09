import random

#Create empty List of integers:lottery_numbers
lottery_numbers = []

while len(lottery_numbers) < 6:
    #Generate a random num between 1 and 50
    num = random.randint(1, 50)

    #Does this number already exist?
    if num not in lottery_numbers:
        