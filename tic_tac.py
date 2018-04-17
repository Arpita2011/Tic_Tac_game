"""
Created on Sun Feb 25 19:01:09 2018

@author: Arpita
"""

#To check winner on the horizontal line
def same_line(list1):
    for i in range(len(list1)):
        j = 0
        if list1[i][j]==list1[i][j+1]==list1[i][j+2]:
            #print 'won by',list1[i][j]
            return list1[i][j]
            #break

#To check winner on the diagonal line
def diagonal_match(list1):
    i = 0 
    j = 0
    if list1[i][j]==list1[i+1][j+1]==list1[i+2][j+2]:
        return list1[i][j]
    if list1[i][-1]==list1[i+1][-2]==list1[i+2][-3]:
        return list1[i][-1]
    
#To check winner on the vertical line
def vertical_match(list1):
    for i in range(len(list1)):
        j=0
        if list1[j][i]==list1[j+1][i]==list1[j+2][i]:
            return list1[j][i]

#To print the gameboard
def print_game(game,a):
    for i in range(a):
        print '   |   '.join(str(x) for x in game[i])
        print'-----'*a

    
#game=[["1","2","3"],['3','4','5'],['1','0','2']]

a = input('Enter the size of board')       

#a = 3
print ' ---'*a  
game = [["","",""],["","",""],["","",""]]
print_game(game, a)
   
ans = 'y'
count = len(game)*a
#print count
check = []
while ans == 'y':
    if count==0:
        break
    #print ans
    spot = raw_input("Enter where to put you mark in row, column format")
    #count = count-1
    l = spot.split(',') 
    row = int(l[0])-1
    col = int(l[1])-1
    l = [row,col]

#To check if row,column pair already filled    
    if l not in check:
        check.append(l)
    else: 
        print 'Already exists! Try again'
        print_game(game,a)
        continue

    if count%2 != 0:
        print 'Player1'
        game[row][col]='X'
        count = count-1 
        print_game(game,a)
        #print count
    else:
        print 'Player2'
        game[row][col]='0'
        count = count -1 
        print_game(game,a)
        #print count
        
list1 = game
m = vertical_match(list1)
#print 'Final', m 
k = diagonal_match(list1) 
#print 'Final', k
z = same_line(list1)
#print 'Final', z

# To check the winner 
if m!=None:
    print 'Game won by',m 
elif k!= None:
    print 'Game won by',k 
elif z!=None:
    print 'Game won by',z
else:
    print 'Game was not won by anyone'    








