from statistics import mode
import msvcrt,os


list_Awards = []
list_Candidates = []
list_voting = []



def menu():
    os.system('cls')
    print("\n--- Wellcome to the voting Application ---")
    print("\n1. Setup \n2. Voting Section\n3. View Candidates\n4. Tutorial\n5. Exit")
    inp = input()

    match inp:
        case '1':
            setup()
        case '2':
            voting()        
        case '3':
            view()     
        case '4':
            Tutorial()     
        case '5':
            exit()     
        case _:
            print("Invalid Input")


def setup():
    os.system('cls')
    print("\n-- Setup Section -- \n")
    noa = int(input('\nEnter no Awards/Titles you want to enter: '))
    list_Awards.clear()
    list_Candidates.clear()
    for i in range(noa):
        award_name = input(f'\nEnter {i+1} Award/Title: ')
        list_Awards.append(award_name)
        noc = int(input('\nEnter no of candidates: '))
        for j in range(noc):
            candidate_name = input(f'\nEnter {j+1} Candidate Name: ')
            list_Candidates.append(candidate_name)

        list_Candidates.append('0')

    exit_menu()


def voting():
    os.system('cls')
    print("\n-- Voting Section -- \n")
    if (len(list_Awards)>0 and len(list_Candidates)>0):
        no = int(input("How many voters are there..? "))

        j=0
        for awards in list_Awards:
            print(f"\n-- '{awards}' --\n")    
            for i in range(len(list_Candidates)):
                if j<len(list_Candidates):
                    if (list_Candidates[j] != '0'):
                        print (f"{i+1}. {list_Candidates[j]} ")
                        j+=1
                    else:
                        j+=1
                        break

            for i in range(no):
                voting_inp = input(f"\nPerson'{i+1}' Please Enter Your Vote (Person's Name): " )
                list_voting.append(voting_inp.upper())

            winner =  mode(list_voting)
            print(f'\n"{winner}" Congratulations You Have Won The Title "{awards}"..!')
            print("\nPress Any Key to continue...") 
            msvcrt.getch()
            list_voting.clear()
            os.system('cls')
    else:
        print("No Record Found")

    exit_menu()

def view():
    os.system('cls')
    print("\n-- Viewing Section -- \n")
    j=0
    if (len(list_Awards)>0 and len(list_Candidates)>0):
        for awards in list_Awards:
            print(f"\n-- '{awards}' --\n")    
            for i in range(len(list_Candidates)):
                if j<len(list_Candidates):
                    if (list_Candidates[j] != '0'):
                        print (f"{i+1}. {list_Candidates[j]} ")
                        j+=1
                    else:
                        j+=1
                        break
    else:
        print("No Record Found")

    exit_menu()

def Tutorial():
    os.system('cls')
    print('''-- Voting Application Tutorial --

1. Setup:

    > Choose option 1 in the main menu to set up the awards and candidates.
    > Enter the number of awards/titles you want to add.
    > For each award, provide the award name and the number of candidates.
    > Enter the name of each candidate for the respective award.

2. Voting Section:

    > Choose option 2 in the main menu to start the voting process.
    > If awards and candidates are set up, enter the number of voters.
    > For each award, the candidates will be displayed.
    > Each voter will enter their vote by selecting the candidate number.
    > After all votes are entered, the winner for each award will be announced.

3. View Candidates:

    > Choose option 3 in the main menu to view the list of awards and candidates.
    > The awards and corresponding candidates will be displayed.

4. Tutorial:

    > Choose option 4 in the main menu to view the tutorial (you're already here!).

5. Exit:

    > Choose option 5 to exit the application.
''')
    exit_menu()


def exit_menu():
    while True:
        ch = int(input('\nPress 1 to Return To main menu\nPress 0 To Exit'))           
        if (ch == 1):
            menu()
            break
        elif (ch == 0 ): 
            exit()
            break
        else: 
            print('Invalid Input')
            continue



menu()
