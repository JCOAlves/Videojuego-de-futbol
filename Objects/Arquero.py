import pygame

# Classe Arquero (Goleiro)
class Arquero(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, anchura, altura):
        self.pontoX = pontoX
        self.pontoY = pontoY
        self.anchura = anchura
        self.altura = altura
        self.direccionMovimento = "derecha"

    def iniciarArquero(self, ventana):
        pygame.draw.rect(ventana, (255,250,0), (self.pontoX, self.pontoY, self.anchura, self.altura))

    def defensaPorteria(self, movimiento, min, max):
        match self.direccionMovimento:
            case "derecha":
                self.pontoX += movimiento
            case "izquierda":
                self.pontoX -= movimiento
        
        if self.pontoX > (max-self.anchura):
            self.direccionMovimento = "izquierda"

        elif self.pontoX < min:
            self.direccionMovimento = "derecha"
        