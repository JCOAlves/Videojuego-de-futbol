import pygame

# Classe Balón (Bola)
class Balon(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, radioCirculo):
        super().__init__()

        self.pontoX = pontoX
        self.pontoY = pontoY
        self.radioCirculo = radioCirculo

        self.imagem = pygame.Surface((self.radioCirculo*2, self.radioCirculo*2), pygame.SRCALPHA)

        pygame.draw.circle(self.imagem, (255,0,0), (self.radioCirculo, self.radioCirculo), self.radioCirculo)

        self.rect = self.imagem.get_rect()
        self.rect.x = self.pontoX
        self.rect.y = self.pontoY

    def iniciarBalon(self, ventana):
        ventana.blit(self.imagem, self.rect)

    def disparo(self, coordsGol, balonMoviento):
        if balonMoviento:
            if self.pontoX > coordsGol[0]:
                self.pontoX -= 1
            elif self.pontoX < coordsGol[0]:
                self.pontoX += 1

            if self.pontoY < coordsGol[1]:
                self.pontoY += 1
            elif self.pontoY > coordsGol[1]:
                self.pontoY -= 1

            self.rect.x = self.pontoX
            self.rect.y = self.pontoY
            