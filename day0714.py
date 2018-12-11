print("------------Freator---------------")
print("This is a easy game to guess the number.")
#learn how to use 'if-else'
temp = input("guess the number in my mind:")
guess = int(temp)
if guess == 8:
    print("RIGHT!")
    print("But no prize!")
else:
    print("WRONG!")
print("Game Over!")
