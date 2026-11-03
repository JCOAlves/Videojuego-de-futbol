import pygame

# Classe Balón (Bola)
class Balon(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, radioCirculo):
        self.pontoX = pontoX
        self.pontoY = pontoY
        self.radioCirculo = radioCirculo

    def iniciarBalon(self, ventana):
        pygame.draw.circle(ventana, (255,0,0), (self.pontoX, self.pontoY), self.radioCirculo)

    def disparo(pontoX, pontoY, posicion):
        match posicion:
            case "izquierda":
                return
            case "derecha":
                return
            case "centro":
                return