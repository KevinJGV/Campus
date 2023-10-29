import colorama


def game_sheet():
    sheet = ["7","8","9",
             "4","5","6",
             "1","2","3"]

def valid_selec(msj):
    try: 
        while True:
            op = input(msj)
            if op in ("1","2","3"):
                return op
            elif op == "":
                print("Selecciona una opción.")
            elif op.isalnum():
                print("Seleccione las opciones mostradas.") 
    except Exception as e:
        print('Ocurrió un error',e)
        input()

def player_1(msj):
    try:
        while True:
            player = input(msj)
            player = player.strip()
            if len(player) == 0:
                print("Ingrese un Nickname para el " + colorama.Fore.RED + colorama.Style.BRIGHT + "Jugador 1" + colorama.Fore.RESET + colorama.Style.RESET_ALL, ".")
            else:
                print("Nickname definido: " + colorama.Fore.RED + colorama.Style.BRIGHT +  player + colorama.Fore.RESET + colorama.Style.RESET_ALL + ".")
                input()
                return player
    except Exception as e:
        print('Ocurrió un error',e)
        input()

def player_2(msj):
    try:
        while True:
            player = input(msj)
            player = player.strip()
            if len(player) == 0:
                print("Ingrese un Nickname para el " + colorama.Fore.BLUE + colorama.Style.BRIGHT + "Jugador 2" + colorama.Fore.RESET + colorama.Style.RESET_ALL, ".")
            else:
                print("Nickname definido: " + colorama.Fore.BLUE + colorama.Style.BRIGHT +  player + colorama.Fore.RESET + colorama.Style.RESET_ALL + ".")
                input()
                return player
    except Exception as e:
        print('Ocurrió un error',e)
        input()


                
def start_game():
    # try:
        print("\n>>> INICIAR JUEGO.\nEn éste juego PvP debera definir el alias para el Player 1 quien sera asignado con la ficha \"X\"\nasí mismo se definira el alias de Player 2 (\"O\").", "\n\nDefina Jugador 1 -------------------------------")
        player_X = player_1(colorama.Fore.RED + colorama.Style.BRIGHT + "Jugador 1" + colorama.Fore.RESET + colorama.Style.RESET_ALL + ", asigne su Nick => ")
        player_O = player_2(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Jugador 2" + colorama.Fore.RESET + colorama.Style.RESET_ALL + ", asigne su Nick => ")
        
def bienvenida():
    print("✮" * 20, "TIC TAC TOE".center(35), "✮" * 20, "\n=======", "Menú principal".center(35), "=======", "\n1 - INICIAR PARTIDA\n2 - TABLA CLASIFICATORIA\n3 - SALIR DEL JUEGO")
    selec = valid_selec(">>> ")
    if selec == "1":
        start_game()
    
    
    

# def select_menu_option(op):
    
# def input_players():
bienvenida()
