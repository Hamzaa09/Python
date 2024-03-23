import random

print("\n1.SNAKE , 2.WATER , 3.GUN\n")
count_p=0
count_c=0

while True:
    player = int(input("Enter Your Choice "))

    computer = random.randint(1,3)

    if (player == 1 and computer == 2 ):
        print("You Wonn..!")
        count_p += 1
    elif (player == 1 and computer == 3 ):
        print("Computer Wonn :(")
        count_c += 1
    elif (player == 2 and computer == 3 ):
        print("You Wonn..!")
        count_p += 1

    elif (player == 2 and computer == 1 ):
        print("Computer Wonn :(")
        count_c += 1
    elif (player == 3 and computer == 1 ):
        print("You Wonn..!")
        count_p += 1
    elif (player == 3 and computer == 2 ):
        print("Computer Wonn :(")
        count_c += 1
    else:
        print("Draww...")

    print(f"YOur Score = {count_p}\t\tComputer's Score = {count_c}")
    player1 = input("\nWant To Continue..?\n 'y' or 'n'")
    if (player1=='n'):
        break