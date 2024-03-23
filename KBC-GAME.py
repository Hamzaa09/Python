print("***** WEllcOme To KBC *****\n")

Questions=["1.How many continents are there on Earth?\nA.4\t\t\tB.5\nC.9\t\t\tD.7\n","2.How much is half of 2 + 2?\nA.1\t\t\tB.2\nC.3\t\t\tD.4\n","3.What is the capital city of Yemen\nA.Sanna\t\t\tB.Ta'izz\nC.Hajjah\t\tD.Al-Hudaydah\n","4.FBG, GBF, HBI, IBH, ____? Fill in the blank\nA.HBL\t\t\tB.HBK\nC.JBI\t\t\tD.JBK\n","5.At the end of a meeting 4 peoples handshaked, How Many Handshakes Will be There??\nA.6\t\t\tB.4\nC.16\t\t\tD.12\n"]
Answers = ['d','c','a','d','a']
price = ["1 Lakh" , "10 lakh" , "50 Lakh" , "1 Caror" , "7 caror"]

balance=0 
wrong =0

for i in range(5):
    while True:
        x = input(Questions[i])
        if(x == Answers[i]):
            x='f'
        match x:  
            case 'f':
                balance = price[i] 
                if (i == 4):
                    print("\n7 Caror...................................!", end = "")

                print(f"\nCongratulations Ap {balance} JEEt Chuke HAin")
                break
            case 'a'|'b'|'c'|'d':
                print(f"\nGAlat JAwab\n'{Answers[i].upper()}' is The Right Option\n")
                wrong=1
                break
        if(x != 'a' or 'b' or 'c' or 'd' ):
            print("Invalid Input")
            continue         
    if (wrong == 1):
        break
print("\nYour BAlance = ",balance)
print("Thanks For Playing :)")

