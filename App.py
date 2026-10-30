import pygame
from pygame.locals import *
from sys import exit

from Objects.Balon import Balon
from Objects.Arquero import Arquero

pygame.init()

# Largura e altura da janela do jogo
dimensionesVentana = { "anchura": 950, "altura": 650 }
Ventana = pygame.display.set_mode((dimensionesVentana["anchura"], dimensionesVentana["altura"]))
tituloVentana = pygame.display.set_caption("Videojuego de Fútbol")

posionesObjetos = { "Arquero": [200,200], "Balon": [100,100] }
arquero = Arquero(posionesObjetos["Arquero"][0], posionesObjetos["Arquero"][1], 30, 60)
balonFutbol = Balon(posionesObjetos["Balon"][0], posionesObjetos["Balon"][1], 30)

relogio = pygame.time.Clock()
velocidadFotogramas = 20

#Loop infinito principal para atualização do jogo
print("Videojuego de Fútbol iniciado")
while True:
    relogio.tick(velocidadFotogramas) #Função para controlar o número de frames por segundo 
    Ventana.fill((255,255,255)) 
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Videojuego finalizado.\n")
            pygame.quit()
            exit()

    
    balonFutbol.iniciarBalon(pygame, Ventana)
    arquero.iniciarArquero(pygame, Ventana)

    balonFutbol.pontoX += 1
    if balonFutbol.pontoX > 800:
        balonFutbol.pontoX = 0



    pygame.display.update()