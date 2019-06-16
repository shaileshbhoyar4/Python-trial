#initializing game
print 'Welcome to tic tac toe game '
board=[]
board=['-','-','-','-','-','-','-','-','-',]
player_name=[]
step_Number=[]
player_name=[None,None]
game_running = True
player1_turn = True
game_won = False
F=8
def print_board():
    i=0
    print '\n\n'
    while i<=7:
        print board[i]+'|'+board[i+1]+'|'+board[i+2]
        i+=3

def get_player_name():
    i=0
    global player_name
    while i<=1:
        player_name[i] = raw_input( '\n\nPlayers %d please Enter your name\t'%(i+1))
        i+=1

def start_game():
    global player1_turn
    p=0
    while game_running:
        if player1_turn:
            get_input(0)
        else:
            get_input(1)
        p+=1
        won_or_tie(p)


def get_input(m):
    global F
    global step_Number
    global player1_turn
    d = input('\n%r its Your Turn \n Enter your position between 1 to 9\t'%player_name[m])
    w=int(d)
    F=m
    #check that w is a part of step number or not
    if w-1 not in step_Number:
        step_Number.append(w - 1)

        try:
            e = int(d)
            if m==0:
                board[e-1] = "X"
            else:
                board[e-1] = "O"
            print_board()
        except IndexError:
            print 'Please enter A Digit in Between 1-9'
        player1_turn=swich(player1_turn)
    else:
        print '\tTHIS NUMBER IS ALREADY CHOOSEN\n\n\tPLEASE CHOOSE ANOTHER NUMBER'

def swich(j):
    if j:
        return (False)
    else:
        return (True)

def won_or_tie(p):
    global game_running
    if check_won():
        print '\n\n\n\t\tCONGRATULATIONS\n\n\n\t\t%r YOU WON\n\n'%player_name[F]
        game_running=False
    elif p==9:
        print '\n\n\n\t\tITS A TIE\n\n'
        game_running = False
    else:
        pass

def check_won():
    global game_won
    if game_won==False:
        #print 'Checking horizontal win'
        horizontal_win()
        if game_won==False:
         #   print 'Checking Verticle win'
            verticle_win()
            if game_won == False:
          #      print 'Checking Digonal win'
                digonal_win()
            else:
                pass
        else:
            pass
    else:
        pass
    return game_won
def horizontal_win():
    global game_won
    i=0
    while i<8:
        if board[i] == board[i + 1] == board[i + 2]!='-':
            game_won = True
        else:
            pass
        i += 3
        #print game_won

def verticle_win():
    global game_won
    i = 0
    while i<3:
        if board[i] == board[i + 3] == board[i + 6]!='-':
            game_won = True
        else:
            pass
        i += 1

        #print game_won

def digonal_win():
    global game_won
    if board[0] == board[4] == board[8]!='-':
        game_won = True
    elif board[2] == board[4] == board[6]!='-':
        game_won = True
    else:
        pass

    #print game_won


print_board()
get_player_name()
start_game()
exit(0)