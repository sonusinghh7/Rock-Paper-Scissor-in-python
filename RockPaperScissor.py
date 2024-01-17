
print("Play Rock Paper and Scissor with bot")
name=input("Please enter your name: ")
print('-----------------------------------------------')
print(f"Hello {name.upper()}, let's play a game.")
print("You go first")
print('-----------------------------------------------')

def game():
    import random
    list=['rock', 'paper','scissor']
    word=random.choice(list) 
    userInput=str(input('Enter what you want. Rock, Paper, or scissor: '))
    user=userInput.lower() 
    word=random.choice(list)
    
    if user in list:
       print("You choose: ", user)
       print("Bot choose: ",word)
       
       if word==user:
              print("ohh no! Game Tie")
              
       elif word=='rock' and user=='paper':
              print("yeah! you won")       
       elif word=='rock' and user=='scissor':
              print("ohh shit! you lost")
              
       elif word=='paper' and user== 'rock':
              print("ohh shit! you lost")
       elif word=='paper' and user=='scissor':
              print("yeah! you won")
              
       elif word=='scissor' and user=='rock':
              print("yeah! you won")
       elif word=='scissor' and user=='paper':
              print("ohh shit! you lost")
       else:
              pass
    else :
      print("please enter the valid input")    
      
game()
restart=input("Press (R) to restart the game: ")  
r=restart.lower() 

while r=='r':
    game()
    
    restart=input("Press (R) to restart the game: ")
    r=restart.lower()
else:
    print(f"You press '{restart}' so you exit the game")
    print("Thankyou, please visit again...")
    quit()
# made with ❤️ by Sonu Singh



