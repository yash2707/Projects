import random

def play():
    user = input("What will be your choice?--> 'r' for rock, 's' for scissors and 'p' for paper \n ")
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer:
        return 'Sigh! It\'s a tie!!'

    if is_win(user,computer):
        return 'Yay, you won :)'

    return 'You lost :('
def is_win(player,opponent):
    # rule is r>s , s>p , p>r
    if (player == 'r' and opponent== 's') or ( player == 's' and opponent== 'p') \
            or ( player =='p' and opponent == 'r'):
        return True

print(play())
