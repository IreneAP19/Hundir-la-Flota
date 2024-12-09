import emoji
import numpy as np
import random

#<FUNCION CREAR TABLERO>

#return np.full((filsd,columnas), "_") = que hacer la de zeros
def crear_tablero(filas=10,columnas=10):
    tablero= np.zeros((filas,columnas), dtype = str)#hago una tupla para que sea bidimensional
    #hago un array de zeros e indico que sea de tipo string para que al sustituir un 0=int por un "_"=str no me de problemas
    tablero[:]="_"#sustituyo todos los elementos del tablero(0) por "_"

    return tablero

#<FUNCION COLOCAR BARCOS>

def colocar_barcos(barco,tablero):
    '''cada barco va atener uno/varios valor/es en columna y en fila
       lo que queremos es sustituir dichos valores en el tablero de juego
       Para ello vamos a crear un bucle for(hay una medida determinada en cada uno pero varia segun el barco)
        
            para cada valor de columna y de fila que encuentres en la variable barco:
                coge el tablero y en la posicion (fila,columna) cambia"_" por un barquito
                devuelveme el nuevo tablero'''
    for fila,columna in barco:
        tablero[fila,columna] = emoji.emojize(':ship:') #no me va a dar fallo pq estamos trabajando con str
    return tablero #devuelveme el tablero con los cambios
    
#barco sera una lista de posiciones y el tablero va a ir variando entre el mio y el del pc

#<FUNCION CREAR BARCO>
def crear_barco(eslora): #eslora=len(barco)
    #esta lista de barcos es la que voy a llamar en colocar barcos
    barcos = []#inicializo una lista para guardar todas las posiciones de los barcos
        
    ocupado = set() #conjunto de casillas ya ocupadas, las almacenamos para evitar que una posicion pise a otra
    for medida in eslora:
        while True:#mientras que exista la posicion   
            barco_actual =[]#aqui almacenamos las posiciones de cada barco de forma individual
               #Le pido que me de dos valores iniciales para cada eslora
            i= np.random.randint(0,9)
            j = np.random.randint(0,9)
            #tambien tengo que considerar que la direccion puede ser aleatoria
            orientacion = random.choice(["vertical","horizontal"])  #me da de forma aleatoria la orientacion
            
            

        #estudio de casos segun la orinetacion y contemplando la dimension del tablero y longitud de cada eslora
            if orientacion == "vertical" and (i+ medida <=9):
                barco_actual= [(i+n, j) for n in range(medida)]#n=0,...,num eslora. Por eso no ponemos el primer valor en barco antes del if
                
            elif orientacion == "vertical" and  (i- medida>=0):
                barco_actual = [(i-n, j) for n in range(medida)]
                
        
        
            elif orientacion == "horizontal" and (j + medida <=9):
                barco_actual= [(i, j+ n) for n in range(medida)]
                
            elif orientacion == "horizontal" and  (j- medida >=0):
                barco_actual = [(i, j-n) for n in range(medida)]
            
            #comprobamos que la posicion del barco no esta ocupada, si no hacemos un break y volvemos al bucle
            if all(pos not in ocupado for pos in barco_actual):
                barcos.append(barco_actual)
                ocupado.update(barco_actual)#pon esa posicion como ocupada para que no se pisen
                break# haz el bucle con una nueva medida de eslora
            
            
    return barcos#mi lista de posiciones de cada barco
            
#<FUNCION DISPARAR>
def disparar(casilla,tablero):
    for fila,columna in casilla:
        if tablero[fila,columna] == "_":
            
            tablero[fila,columna] = emoji.emojize(':droplet:')
            return "Agua"
            
    
        else:
            tablero[fila,columna] = emoji.emojize(':bomb:')
            return "Tocado"
         #elif tablero[fila,columna] == emoji.emojize(':bomb:')
            #return "Ya le habias dado aqui"
            #break
        
    return tablero
#si vuelvo a dispara a una coordenada donde hay una bomba ahora me lo saca como agua. Hay que poner una condicion donde diga que ya le has dado, dispara otra vez

#<CREAMOS EL TABLERO DEL PC>

maquina_tablero = crear_tablero()
esloras = (2, 2, 2, 3, 3, 4)
#crear_barco me devuelve la lista de barcos, cada barco con sus coordenadas
barcos = crear_barco(esloras)#se me crea una lista con todas las posiciones, con una sublista de las posiciones de los barcos individualmente

lista_barcos_pc=[]
for indice, barco in enumerate(barcos):#[[-,-,-],[-,-],...]-->lista de barcos -->barcos --> coordenadas individuales(indice)
    lista_barcos_pc.append(barco)#añademe los barcos uno a uno b1,b2,b3... a la lista de barcos_pc

    #metemos los barcos en su tablero
    for i in lista_barcos_pc:#para cada uno de los barcos_pc, coloca en maquina_tablero las posiciones de cada barquito
        maquina_tablero = colocar_barcos(i,maquina_tablero)#i son los barquitos b1,b2...
        #colocar_barco coge las coordenadas de cada b1,b2,b3 de la lista y las coloca en el tablero indicado

#<TABLERO DEL JUGADOR>

mi_tablero = crear_tablero()

b1 = ((0,1),(1,1))
b2 = ((3,8),(4,8))
b3 = ((2,2),(3,2))
b4 = ((0,7), (0,4),(0,5),(0,6))
b5= ((6,7),(5,7),(4,7))
b6 = ((8,2),(8,3),(8,4))
#hago una lista de los 6 barcos
barquitos=[b1,b2,b3,b4,b5,b6]
for i in barquitos:#para cada uno de los barcos, en mi tablero(de jugador) colocame en mi_tablero las posiciones de cada barquito
    mi_tablero = colocar_barcos(i,mi_tablero)#i son los barcos


#<FUNCION DE TURNOS>

def proceso_juego(jugador,mi_tablero,maquina_tablero):

    vidas_yo = 8
    vidas_pc = 8
    coordenadas_falladas =[]
    while any(emoji.emojize(':ship:') in fila for fila in mi_tablero) and any(emoji.emojize(':ship:') in fila for fila in maquina_tablero) and vidas_yo!=0 and vidas_pc!=0:
        
        if jugador == "yo":
            '''pido al jugador las coordenadas de donde quiere disparar
                disparo al tablero de la maquina y saco el resultado y el tablero actualizado con el que estoy jugando el turno
                si acierto el tiro sigo jugando
                pongo la condicion de que si en cada barco de la lista las casillas son bombas (en el tablero de juego) entonces lo he hundido

                si no acierto pierdo una vida y el turno
                '''
            #1-llamo a la maquina del pc
            print("Jugamos con el tablero de la maquina")
            print(f"Tablero del pc: \n{maquina_tablero}")
            print(f"Has fallado estas coordenadas: {coordenadas_falladas}")
    #HAGO UN TRY SOLO EN JUGADOR POR SI ME EQUIVOCO METIENDO LAS COORDENADAS

            try:
                
                val1 = int(input("Dime una coordenada"))
                val2 = int(input("Dime la segunda coordenada"))
                print("A disparar")
                disparo = disparar([(val1,val2)],maquina_tablero)
                print(disparo)
                print(maquina_tablero)#nos saca el tablero con el disparo

                if disparo == "Tocado":
                    print("Disparas de nuevo")
                    for i in barquitos:
                        if all(mi_tablero[fila:columna] == emoji.emojize(':bomb:') for fila,columna in i):
                            print("Hundido")
                    
                else:
                    vidas_yo = vidas_yo - 1
                    print(f"Has fallado JUGADOR, te quedan {vidas_yo} vidas")
                    coordenadas_falladas.append([(val1,val2)])
                    jugador = "Maquina"

            except (IndexError, ValueError):
                    print("Coordenada inválida. Intenta de nuevo.")
                
        else :
        #juega en el tablero del usuario
            
            print("Jugamos con mi tablero")
            print(f"Tablero del jugador: \n{mi_tablero}")
        
            print("A disparar")
            disparo = disparar([(np.random.randint(0,9),np.random.randint(0,9))], mi_tablero)#las casillas de disparos sn random y dispara a mi tablero
            print(disparo)
            print(mi_tablero)#tablero actualizado

            if disparo == "Tocado":
                print("Disparas de nuevo")
                for i in lista_barcos_pc:#i son los barcos de la lista de los barcos_pc que hemos hecho antes de froma aleatoria
                    if all(maquina_tablero[fila:columna] == emoji.emojize(':bomb:') for fila,columna in i):#si en todas las casilla en en tablero de la maquina correspondientes a los barcos del pc(individualmente) son bombas, lo has hundido
                        print("Hundido")
                

            else:
                vidas_pc = vidas_pc - 1
                print(f"Has fallado PC, te quedan {vidas_pc} vidas")

                jugador= "yo"
    '''si no hay mas barcos a los que disparar o nos quedamos sin vidas, gana el contrincante'''
    if not any(emoji.emojize(':ship:') in fila for fila in mi_tablero) or vidas_yo == 0:
        print(f"GAME OVER JUGADOR {emoji.emojize(':skull:')}")

    if not any(emoji.emojize(':ship:') in fila for fila in mi_tablero) or vidas_pc ==0:
        print(f"GAME OVER PC {emoji.emojize(':skull:')}")
    return