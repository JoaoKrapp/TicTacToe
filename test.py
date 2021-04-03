'''
lugares = {1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "}

TIC_TAC_TOE = f"\n\
     {lugares.get(1)} | {lugares.get(2)} | {lugares.get(3)} \n\
    -----------\n\
     {lugares.get(4)} | {lugares.get(5)} | {lugares.get(6)} \n\
    -----------\n\
     {lugares.get(7)} | {lugares.get(8)} | {lugares.get(9)} ".center(100)
     
def impar(numero):
    if (numero%2) == 0:
        return False
    else:
        return True

def won(TIC_TAC_TOE):
    pass
print(TIC_TAC_TOE)

for i in range(1, 10):
    if impar(i):
        player = "X"
    else:
        player = "O"

    
    answer = int(input("Which place do you want to pick? "))
    if answer == 1:
        lugares[1] = player
    elif answer == 2:
        lugares[2] = player
    elif answer == 3:
        lugares[3] = player
    elif answer == 4:
        lugares[4] = player
    elif answer == 5:
        lugares[5] = player
    elif answer == 6:
        lugares[6] = player
    elif answer == 7:
        lugares[7] = player
    elif answer == 8:
        lugares[8] = player
    elif answer == 9:
        lugares[9] = player
    else:
        print("Not a valid command")
        

    TIC_TAC_TOE = f"\n\
     {lugares.get(1)} | {lugares.get(2)} | {lugares.get(3)} \n\
    -----------\n\
     {lugares.get(4)} | {lugares.get(5)} | {lugares.get(6)} \n\
    -----------\n\
     {lugares.get(7)} | {lugares.get(8)} | {lugares.get(9)} ".center(100)


    print(TIC_TAC_TOE)
    

array = [[0]]
TIC_TAC_TOE = f"\n\
 {array[0][0]} | {array[0][0]} | {array[0][0]} \n\
-----------\n\
 {array[0][0]} | {array[0][0]} | {array[0][0]} \n\
-----------\n\
 {array[0][0]} | {array[0][0]} | {array[0][0]} ".center(100)

print(TIC_TAC_TOE)
'''

answer = int(input("Teste: "))
if answer == None:
    print("WOW")