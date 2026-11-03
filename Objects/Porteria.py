import pygame

class Porteria(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, anchura, altura):
        self.pontoX = pontoX
        self.pontoY = pontoY
        self.anchura = anchura
        self.altura = altura

    def iniciarPorteria(self, ventana):
        pygame.draw.rect(ventana, (211,211,211), (self.pontoX, self.pontoY, self.anchura, self.altura))
        pygame.draw.rect(ventana, (137,137,137), (self.pontoX, self.pontoY, self.anchura, self.altura), width=10)