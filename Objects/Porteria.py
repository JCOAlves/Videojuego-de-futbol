import pygame

class Porteria(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, anchura, altura):
        super().__init__()

        self.pontoX = pontoX
        self.pontoY = pontoY
        self.anchura = anchura
        self.altura = altura

        # Cria a superfície do desenho (Imagem do Sprite)
        self.imagem = pygame.Surface((self.anchura, self.altura), pygame.SRCALPHA)

        # Desenha na própria imagem (posição local: 0, 0)
        pygame.draw.rect(self.imagem, (211,211,211), (0, 0, self.anchura, self.altura))
        pygame.draw.rect(self.imagem, (137,137,137), (0, 0, self.anchura, self.altura), width=10)

        # Define a caixa de colisão (Rect) na posição global do jogo
        self.rect = self.imagem.get_rect()
        self.rect.x = self.pontoX
        self.rect.y = self.pontoY
    
    def iniciarPorteria(self, ventana):
        ventana.blit(self.imagem, self.rect)

    def colisionPorteria(self, porteria, bolan):
        if porteria.rect.collidedict(bolan.rect): # ERRO
            print("Bola no gol!")