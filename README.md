¡Bienvenido a **Hundir la Flota**, una implementación del clásico juego de "Batalla Naval" desarrollada en Python! 

## CARACTERÍSTICAS 📋

- 🗺️ **Tablero interactivo** generado en consola.  
- 🤖 Posibilidad de jugar contra la computadora.  
- 🚢 **Colocación manual** de los barcos.  
- 🏆 Sistema de seguimiento de puntuación.  
- 🎨 Tablero en formato visual para mayor claridad.
## FUNCIONAMIENTO
Recordemos que el juego constará de dos jugadores (en este caso tú y el PC). 
- ⚓ Configura tus barcos en el tablero accediendo a *utils*.
- 💣  Atacar las coordenadas del enemigo.
- 🎯 Tener buena puntería y hundir la flota enemiga.
## CÓDIGO
El código consiste en definir una serie de funciones que nos van a permitir jugar:
- Crear tablero (tango el del jugador como el del PC)
- Crear barcos de forma aleatoria para el PC
- Colocar barcos
  - De forma aleatoria para el PC
  - Manualmente para el jugador
- Disparar, que buscará la coincidencia de las coordenadas introducidas con los barcos enemigos

🛠️ Para crear el juego se ha hecho uso de funciones predefinidas para aplicarlas a la dinámica del juego y la librería de Numpy.
## JUEGO
Por apantalla nos aparecerá quien queremos que empiece, si empezamos nosotros a disparar tendremos que introducir las coordenadas para intentar das a la flota enemiga. En caso contrario comienza el PC con la misma dinámica.
- 💧 Si fallamos nos restará una vida y pasaremos el turno al PC.
- 💣 Si acertamos continuaremos dando nuevas coordenadas

El intercambio de turnos continuará hasta que:
  - 🏆 Haya un ganador(la otra flota esté hundida)
  - 💀 Uno de los jugadores se quede sin vidas


  
