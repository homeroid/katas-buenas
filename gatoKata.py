#necesite ayuda para corregir lo del template
template = " 0 │ 1 │ 2 \n───┼───┼───\n 3 │ 4 │ 5 \n───┼───┼───\n 6 │ 7 │ 8 "
count = 0
ganador = ""
def GetTablero():
    global template
    return template
    raise NotImplementedError

def JuegoContinua():
    global template
    global ganador

    data = template.replace(" ","").replace("{","").replace("}","").replace("│","").replace("┼","").replace("─","").replace("\n","")
    datawonum = data.replace("X","").replace("O","")

    if  datawonum == "":
        ganador = "Tie"
        return False
    elif (data[0]+data[1]+data[2]) == "XXX" or (data[3]+data[4]+data[5]) == "XXX" or (data[6]+data[7]+data[8]) == "XXX" or (data[0]+data[3]+data[6]) == "XXX" or (data[1]+data[4]+data[7]) == "XXX" or (data[2]+data[5]+data[8]) == "XXX" or (data[0]+data[4]+data[8]) == "XXX" or (data[2]+data[4]+data[6]) == "XXX":
        ganador = "X"
        return False
    elif (data[0]+data[1]+data[2]) == "OOO" or (data[3]+data[4]+data[5]) == "OOO" or (data[6]+data[7]+data[8]) == "OOO" or (data[0]+data[3]+data[6]) == "OOO" or (data[1]+data[4]+data[7]) == "OOO" or (data[2]+data[5]+data[8]) == "OOO" or (data[0]+data[4]+data[8]) == "OOO" or (data[2]+data[4]+data[6]) == "OOO":
        ganador = "O"
        return False
    else:
        return True
    #debe decir alguien ha ganado y no que continue

    raise NotImplementedError

def IntentarTirada(casilla):
    global count
    global ganador
    global template

    if int(casilla) > 9 or int(casilla) < 1:
        return "La tirada debe de estar entre 1 y 9"
    elif template.find(str(casilla)) == -1:
        return "La casilla ya esta ocupada"
    else:
        if count % 2 == 0:
            template = template.replace(str(casilla),"X")
            turn += 1
            JuegoContinua()
            if ganador == "X":
                return "Felicidades X as ganado. weeee"
        elif count % 2 == 1:
            template = template.replace(str(casilla),"O")
            turn += 1
            JuegoContinua()
            if ganador == "O":
                return "Felicidades O as ganado. weeee"
        if count == 9:
            return "Juego empatado. :("
        return "..."

    """
        Esta funcion recibe el intento del jugador por ocupar una casilla
        y regresa una cadena segun los siguientes criterios:
        Si esta fuera de rango: "La tirada debe de estar entre 1 y 9"
        Si la casilla esta ocupada: "La casilla ya esta ocupada"
        Si x a ganado: "Felicidades X as ganado. weeee"
        Si o a ganado: "Felicidades O as ganado. weeee"
        Si el juego a quedado empatado: "Juego empatado. :("
        Ninguna de las anteriores: "" (cadena vacia)
    """
    raise NotImplementedError

def IniciaJuego():
    global template
    global count
    global ganador
    template = " 1 │ 2 │ 3 \n───┼───┼───\n 4 │ 5 │ 6 \n───┼───┼───\n 7 │ 8 │ 9 "
    turn = 0
    ganador = ""

    """
        Esta function se puede utilizar para re iniciar variables.
        Si no se usa se puede dejar vacia
    """
    return None

if __name__ == '__main__':
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        msg = ""
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)