import random 

point1 = 0
point2 = 0
count = 0

red = "\033[31m"
blue = "\033[34m"
reset = "\033[0m"
bold = "\033[1m"
underline = "\033[4m"

print('\033[2J')

print(f"""{red}{underline}{bold}Rules-{reset}\n
      \t{red}# stone vs paper --> paper wins\n
      \t# stone vs scissor --> scissor wins\n
      \t# paper vs sciccer --> scissor wins\033[0m\n
      \n
      \tTotal three games, the player with maximum points wins{reset}""")

print(f"{blue}{underline}{bold}Choose:\n{reset} {blue}1 - stone\n 2 - paper\n 3 - scissor\n{reset}")

while count < 3:
    count += 1
    computer = random.randint(1,3)  
    choose = int(input(f"{red}Your turn > {reset}"))
    

    ratio =  point1, ":", point2

    if choose == computer:
        print("It's a draw\n", point1, ":", point2)
    
    elif choose == 1 and computer == 2:
        point2 += 1
        print("stone vs paper\n paper wins!\n", point1, ":", point2)
        
    
    elif choose == 1 and computer == 3:
        point1 += 1
        print("stone vs scissor\n stone win!\n", point1, ":", point2)
    
    elif choose == 2 and computer == 1:
        point1 += 1
        print("paper vs stone\n paper win!\n", point1, ":", point2)
    
    elif choose == 2 and computer == 3:
        point2 += 1
        print("paper vs scissor\n scissor wins!\n", point1, ":", point2)
    
    elif choose == 3 and computer == 2:
        point1 += 1
        print("scissor vs paper\n scissor wins!\n", point1, ":", point2)

    elif choose == 3 and computer == 1:
        point2 += 1 
        print("scissor vs stone\n stone wins!\n", point1, ":", point2)
    
if point1 > point2:
    print("Congratulations! You won with the score ", point1, ":", point2)

elif point2 > point1:
    print("You lose! Try Again.\n score ", point1, ":", point2)


    