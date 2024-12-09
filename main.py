from utils import* 
import emoji
import numpy as np
coordenadas_falladas =[]
vidas_yo = 8
vidas_pc = 8

def jugar():
   
    jugador = input("quien es el primer jugador: ")#si lo pongo dentro de while hace bucle
    '''Como es un array no puedo poner while emoji.. in x_tablero, ya que asi solo busca en la primera fila
        Por eso especifico: que mientras que encuentre algun barco en algun tablero (mirando fila a fila) el juego sigue'''
    
    juego = proceso_juego(jugador,mi_tablero,maquina_tablero)
    print(juego)
        

if __name__ == "__main__":
    jugar()