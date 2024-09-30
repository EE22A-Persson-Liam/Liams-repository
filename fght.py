import random

playera = input("What is player a name? ")
playerb = input("What is player b name? ")

playerahp = 100
playerbhp = 100

while(playerahp >0 and playerbhp > 0):
    damage = random.randint(14,27)
    playerbhp  -= damage
    print(playera, "hits player b" , damage)
    if playerbhp <= 0:
        print(playerb, "0 hp left")
        break

    damage = random.randint(14,20) 
    playerahp -= damage    
    print(playerb, "hits player a" , damage)
    if playerahp <= 0:
        print(playera, "0 hp left")
        break
    

if playerahp > 0:
    print(playera," wins")
else:
    print(playerb," wins")








