import pygame
from pygame.locals import *
from sys import exit

from Objects.Balon import Balon
from Objects.Arquero import Arquero
from Objects.Porteria import Porteria

from Services.EscenarioJuego import EscenarioJuego
from Services.InterfazJuego import InterfazJuego

pygame.init()

# Largura e altura da janela do jogo
dimensionesVentana = { "anchura": 950, "altura": 650 }
Ventana = pygame.display.set_mode((dimensionesVentana["anchura"], dimensionesVentana["altura"]))
tituloVentana = pygame.display.set_caption("Videojuego de Fútbol")

# Dados dos objetos do jogo
datosArqueiro = { "pontoX": 200, "pontoY": (dimensionesVentana["altura"]-180)-130, "anchura": 100, "altura": 180 }
datosBalon = { "pontoX": dimensionesVentana["anchura"]/2, "pontoY": 590, "radioCirculo": 30 }
datosPorteria = { "pontoX": (dimensionesVentana["anchura"]-800)/2, "pontoY": 140, "anchura": 800, "altura": dimensionesVentana["altura"]-270}

# Objetos do jogo
arquero = Arquero(datosPorteria["pontoX"], datosArqueiro["pontoY"], datosArqueiro["anchura"], datosArqueiro["altura"])
balonFutbol = Balon(datosBalon["pontoX"], datosBalon["pontoY"], datosBalon["radioCirculo"])
porteriaArquero = Porteria(datosPorteria["pontoX"], datosPorteria["pontoY"], datosPorteria["anchura"], datosPorteria["altura"])

relogio = pygame.time.Clock()
velocidadFotogramas = 150

tipoInterfaz = "juego"
reiniciaJuego = False

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

        if event.type == MOUSEBUTTONDOWN: # Verifica o evento de click do mouse
            posi = event.pos # Retorna a possição do Mouse
            balonFutbol.pontoX = posi[0]
            balonFutbol.pontoY = posi[1]


    # Paginação de jogo
    if tipoInterfaz != "juego":
        EscenarioJuego(Ventana, dimensionesVentana["anchura"], dimensionesVentana["altura"])
            
        porteriaArquero.iniciarPorteria(Ventana)
        balonFutbol.iniciarBalon(Ventana)
        arquero.iniciarArquero(Ventana)

        arquero.defensaPorteria(1, datosPorteria["pontoX"], datosPorteria["pontoX"]+datosPorteria["anchura"])
    else:
        InterfazJuego(tipoInterfaz)

    pygame.display.flip()