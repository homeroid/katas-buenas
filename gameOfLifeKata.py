def NextOfspring(u):
    global height
    global width
    if u[0] != '.' and u[0] != '*':
        height = u[0]
        height = int(height)
        width = u[1]
        width = int(width)
    else:
        u = str(height) + str(width) + u[2:len(u)]
    """
        Esta funcion recibe un universo y regresa la siguiente generacion segun las reglas
        Nota: La funcion recibe la cadena el el formato establecido y lo regresa en el mismo formato
    """
    #check for live cells
    ued = []
    for x in range(0,height):
        ued.append(u[(width*x)+2:(width*(x+1))+2])
    alive = []
    for x in range(0,height):
        for y in range(0,width):
            if ued[x][y] == '*':
                alive.append([x, y])
    #print ('The alive cells are:', alive)
    #calculate number of adjacent cells (sendhelp)
    count = 0
    celladjacents = {}
    for cell in alive:
        count += 1
        alivecount = -1
        if cell[0]-1 < 0:
            minx = 0
        else:
            minx = cell[0]-1
        if cell[1]-1 < 0:
            miny = 0
        else:
            miny = cell[1]-1

        for x in range(minx,cell[0]+2):
            for y in range(miny,cell[1]+2):
                try:
                    if ued[x][y] == '*':
                        alivecount += 1
                except Exception:
                    pass
        celladjacents[count] = alivecount
    # print (celladjacents)
    #determine whethet each cell will die
    udie = ''
    c = 0
    for letter in u:
        #what this does: udie is a string containing all the cells that would remain
        #alive after the turn, thus udie == uremain
        if letter == '*':
            if celladjacents[c+1] < 2 or celladjacents[c+1] > 3:
                udie += 'x'
            else:
                udie += '*'
            c += 1
        else:
            udie += letter
    #copy paste of code, changed variables for dead cells now
    ued = []
    for x in range(0,height):
        ued.append(u[(width*x)+2:(width*(x+1))+2])
    dead = []
    for x in range(0,height):
        for y in range(0,width):
            if ued[x][y] == '.':
                dead.append([x, y])
    #print ('The dead cells are:', dead)
    #calculate number of adjacent cells
    count = 0
    celladjacents = {}
    for cell in dead:
        count += 1
        alivecount = 0
        if cell[0]-1 < 0:
            minx = 0
        else:
            minx = cell[0]-1
        if cell[1]-1 < 0:
            miny = 0
        else:
            miny = cell[1]-1

        for x in range(minx,cell[0]+2):
            for y in range(miny,cell[1]+2):
                try:
                    if ued[x][y] == '*':
                        alivecount += 1
                except Exception:
                    pass
        celladjacents[count] = alivecount
    #print (celladjacents)
    #determine whether each dead cell will live
    ulive = ''
    c = 0
    for letter in u:
        if letter == '.':
            if celladjacents[c+1] == 3:
                ulive += '*'
            else:
                ulive += '.'
                #now, ulive holds all the cells that will come to life next turn
            c += 1
        else:
            ulive += letter
    #end copy paste, let's hope it works!! it probably wont.
    #mix udie and ulive
    uend = ''
    it = 0
    for letter in u:
        if udie[it] == 'x':
            uend += '.'
        elif ulive[it] == '*' or udie[it] == '*':
            uend += '*'
        else:
            uend += '.'
        it += 1
    return uend
    # return udie
    # return ulive
    # 99....*.*....**...*.....*....**....*......**...*......*.***.***....****..*..*..*..*
    # 48............*......**...........

"""
99....*.*..
..**...*.
....*....
**....*..
....**...
*......*.
***.***..
..****..*
..*..*..*
"""



def GetUniverse(u):
    global height
    global width
    if u[0] != '.' and u[0] != '*':
        height = u[0]
        height = int(height)
        width = u[1]
        width = int(width)
    else:
        u = str(height) + str(width) + u[2:len(u)]
    """
        Esta funcion debe de regresar el universo en el formato establecido
        pero regresa el universo sin el renglon de las dimensiones y con los saltos
        de linea correspondie
    """
    uni = ''
    for x in range(0,height):
        uni += u[(width*x)+2:(width*(x+1))+2]
        uni += '\n'
    return uni

    raise NotImplementedError

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
    