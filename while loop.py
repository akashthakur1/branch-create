quit = input('Type "enter" to quit:')

while quit != "enter":
    quit = input('Type "enter" to quit:')

user1 = input("what's your name?")
user2 = input("And your name")

user1_answer = input("%s, do you want to choose rock, paper or scissors?" %user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" %user2)

print(user1_answer, user2_answer)

def compare(u1, u2):
    if u1 == u2:
        return(" it is tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
           return (" rock wins")
        else:
          return("paper wins")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return ("scissors wins")
        else:
            return ("rock wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            return ("paper wins")
        else:
            return ("scissor wins")
    else:
        return ("invalid input ! you have not enter rock , paper or scissors, try again")

print(compare(user1_answer, user2_answer))



