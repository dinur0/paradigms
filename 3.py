
def show_table(arr):
    for i in arr:
        print('|'.join(i))

def check_of_win(arr):
    if arr[0][0] == arr[0][1] == arr[0][2] or arr[1][0] == arr[1][1] == arr[1][2] or arr[2][0] == arr[2][1] == arr[2][2] or arr[0][0] == arr[1][0] == arr[2][0] or arr[0][1] == arr[1][1] == arr[2][1] or arr[0][2] == arr[1][2] == arr[2][2] or arr[0][0] == arr[1][1] == arr[2][2] or arr[0][2] == arr[1][1] == arr[0][2]:
        return True
    else:
        return False

def choose(arr,player):
    a = input(f"В какую ячейку пишет {player} ? \n")
    match a:
        case '1':
            if arr[0][0] in "XO":
                print("Место занято")
            else:
                arr[0][0] = str(player)
        case '2':
            if arr[0][1] in "XO":
                print("Место занято")
            else:
                arr[0][1] = str(player)
        case '3':
            if arr[0][2] in "XO":
                print("Место занято")
            else:
                arr[0][2] = str(player)
        case '4':
            if arr[1][0] in "XO":
                print("Место занято")
            else:
                arr[1][0] = str(player)
        case '5':
            if arr[1][1] in "XO":
                print("Место занято")
            else:
                arr[1][1] = str(player)
        case '6':
            if arr[1][2] in "XO":
                print("Место занято")
            else:
                arr[1][2] = str(player)
        case '7':
            if arr[2][0] in "XO":
                print("Место занято")
            else:
                arr[2][0] = str(player)
        case '8':
            if arr[2][1] in "XO":
                print("Место занято")
            else:
                arr[2][1] = str(player)
        case '9':
            if arr[2][2] in "XO":
                print("Место занято")
            else:
                arr[2][2] = str(player)


    show_table(arr)


array = [['1','2','3'],['4','5','6'],['7','8','9']]
show_table(array)
for i in range (2):
    choose(array,"X")
    choose(array,"O")
count = 4
while not check_of_win(array):
    if count % 2 == 0:
        choose(array,"X")
        if check_of_win(array):
            print("\n!!!Х - победил!!!")
            break
    else:
        choose(array,"O")
        if check_of_win(array):
            print("\n!!!О - победил!!!")
            break
    count += 1
    if count > 9:
        print("Ничья")
        break













