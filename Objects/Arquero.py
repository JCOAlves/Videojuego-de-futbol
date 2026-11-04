import pygame

# Classe Arquero (Goleiro)
class Arquero(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, anchura, altura):
        super().__init__()

        self.pontoX = pontoX
        self.pontoY = pontoY
        self.anchura = anchura
        self.altura = altura
        self.direccionMovimento = "derecha"

        self.imagem = pygame.Surface((self.anchura, self.altura), pygame.SRCALPHA)

        pygame.draw.rect(self.imagem, (255,250,0), (0, 0, self.anchura, self.altura))

        self.rect = self.imagem.get_rect()
        self.rect.x = self.pontoX
        self.rect.y = self.pontoY
    
    def iniciarArquero(self, ventana):
        ventana.blit(self.imagem, self.rect)

    def defensaPorteria(self, movimiento, min, max):
        match self.direccionMovimento:
            case "derecha":
                self.pontoX += movimiento
                self.rect.x = self.pontoX
            case "izquierda":
                self.pontoX -= movimiento
                self.rect.x = self.pontoX
        
        if self.pontoX > (max-self.anchura):
            self.direccionMovimento = "izquierda"

        elif self.pontoX < min:
            self.direccionMovimento = "derecha"

    def colisionArquero(self, bolan):
        if self.rect.colliderect(bolan.rect): 
            return True
        else:
            return False
        