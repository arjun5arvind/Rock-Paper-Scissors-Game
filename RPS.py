import random as rand
user_wins=0
cpu_wins=0
ties=0


def RPS_game():
    plays={1:'rock',2:'paper',3:'scissors'}

    print("Welcome to a game of rock paper and scissors!!!\n\n")
    user_ch=int(input("YOUR TURN \nTime to choose\nOptions are :\n1 : rock\n2 : paper\n3 : scissors\nEnter choice:"))

    print("User choice =",plays[user_ch],'\n')



    cpu_ch=int(rand.randint(1,3))
    print("CPU choice=",plays.get(cpu_ch),'\n')

    if user_ch==cpu_ch:
        print("Tie")
        return 3
    match user_ch:
        case 1: 
            if cpu_ch==3:
                print("Rock VS Scissors\nUser wins")
                return 1
            elif cpu_ch==2:
                print("Rock VS Paper\nCPU wins")
                return 2
        case 2:
            if cpu_ch==1:
                print("Paper VS Rock\nUser wins")
                return 1
            elif cpu_ch==3:
                print("Paper VS Scissors\nCPU wins")
                return 2
        case 3:
            if cpu_ch==2:
                print("Scissors VS Paper\nUser wins")
                return 1
            elif cpu_ch==1:
                print("Scissors VS Rock\nCPU wins")
                return 2
    
while True:
    win=RPS_game()
    if win==1:
        user_wins+=1
    elif win==2:
        cpu_wins+=1
    elif win==3:
        ties+=1
    print("\nNumber of user wins =",user_wins)
    print("\nNumber of cpu wins =",cpu_wins) 
    print("\nNumber of ties =",ties)         