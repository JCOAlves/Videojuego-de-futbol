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
datosArqueiro = { "pontoX": 200, "pontoY": (dimensionesVentana["altura"]-300)-130, "anchura": 180, "altura": 300 }
datosBalon = { "pontoX": int(dimensionesVentana["anchura"]/2)-35, "pontoY": 590-35, "radioCirculo": 35 }
datosPorteria = { "pontoX": int((dimensionesVentana["anchura"]-800)/2), "pontoY": 140, "anchura": 800, "altura": dimensionesVentana["altura"]-270}

# Objetos do jogo
arquero = Arquero(datosPorteria["pontoX"], datosArqueiro["pontoY"], datosArqueiro["anchura"], datosArqueiro["altura"])
balonFutbol = Balon(datosBalon["pontoX"], datosBalon["pontoY"], datosBalon["radioCirculo"])
porteriaArquero = Porteria(datosPorteria["pontoX"], datosPorteria["pontoY"], datosPorteria["anchura"], datosPorteria["altura"])

# Velocidade de atualização de frames do jogo
relogio = pygame.time.Clock()
velocidadFotogramas = 320
velocidadeArquero = 2

tipoInterfaz = "juego"
balonMoviento = False
pontuacao = 0
reiniciaJuego = False
posiGol = ()
fuente = pygame.font.SysFont("arial", 40, True, False)

#Loop infinito principal para atualização do jogo
print("Videojuego de Fútbol iniciado")
print(f"Pontuação: {pontuacao}")
while True:
    relogio.tick(velocidadFotogramas) #Função para controlar o número de frames por segundo 
    Ventana.fill((255,255,255))
    mensaje = f"Pontuação: {pontuacao}"
    textoFormato = fuente.render(mensaje, False, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Videojuego finalizado.\n")
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN and arquero.direccionMovimento != "Paro": # Verifica o evento de click do mouse
            posiGol = event.pos # Retorna a possição do Mouse
            balonMoviento = True
            balonFutbol.iniciarChute(posiGol) 

    # Paginação de jogo
    if tipoInterfaz == "juego":
        EscenarioJuego(Ventana, dimensionesVentana["anchura"], dimensionesVentana["altura"])
        Ventana.blit(textoFormato, (40, 40)) 
            
        porteriaArquero.iniciarPorteria(Ventana)
        arquero.iniciarArquero(Ventana)
        arquero.defensaPorteria(velocidadeArquero, datosPorteria["pontoX"], datosPorteria["pontoX"]+datosPorteria["anchura"])
        
        # Atualiza a posição da bola usando a nova lógica de parábola
        balonFutbol.disparo()
        balonFutbol.iniciarBalon(Ventana)

        # Verifica se o goleiro colidiu com a bola
        if arquero.colisionArquero(balonFutbol) and balonFutbol.pontoY < 450:
            balonMoviento = False
            arquero.direccionMovimento = "Paro"
            balonFutbol.emTrajeto = False

        if balonMoviento and posiGol and not balonFutbol.emTrajeto:
            pontuacao = porteriaArquero.colisionPorteria(balonFutbol, pontuacao)
            if pontuacao % 10 == 0:
                velocidadeArquero += 0.5
            balonMoviento = False
            balonFutbol.pontoX = datosBalon["pontoX"]
            balonFutbol.rect.x = datosBalon["pontoX"]
            balonFutbol.pontoY = datosBalon["pontoY"]
            balonFutbol.rect.y = datosBalon["pontoY"]

        # Vefifica se o goleiro parou com a captura da bola para dar "Game Over"
        if arquero.direccionMovimento == "Paro":
            mensajeFim = fuente.render("Fim de juego", False, (255,0,0))
            Ventana.blit(mensajeFim, (300, 325))
    
    else:
        InterfazJuego(tipoInterfaz)

    pygame.display.flip()