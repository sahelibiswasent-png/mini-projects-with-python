"""
WORKFLOW OF THIS PROJECT
input user(rock,paper,seissor)
computer choice(ramdomly choos not the specific condition)
result print

case:1
A-Rock
Rock-Rock=tie
Rock-paper=paper win
Rock-scissor=rock win
case-2
B-Paper
paper-paer=tie
paper-rock=paper win
paper-scissor=scissor win
case-3
C-scissor
scissors-scissors=tie
scissors-rock=rock win
scissors-paper=scissors win
"""
import random
list=["rock","stone","scissor"]
user_choice=input("enter your turn = rock,stone,scissor=")
comp_choice=random.choice(list)
print(f"user choice={user_choice}, computer choice={comp_choice}")
if user_choice==comp_choice:
    print("both choose same :=match tie")
elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper covers rock =computer choice win")
    else:
        print("rock smashes scissors =user choice win")
elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissors cut paper,computer win")
    else:
        print("paper covers rock,you win")
elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissors cuts paer,you win")            
    else:
        print("rock smashes scissor,computer win")      